import copy

import pytest

from prompt_prototype import plan_charge, sample_data
from prompt_prototype import call_with_retry
from google.genai.errors import APIError


def test_retry_transient_error_then_success(monkeypatch):
    waits = []
    monkeypatch.setattr('prompt_prototype.time.sleep', waits.append)
    calls = []
    def operation():
        calls.append(1)
        if len(calls) < 3:
            raise APIError(503, {'error': {'message': 'Unavailable'}})
        return 'valid response'
    assert call_with_retry(operation) == 'valid response'
    assert waits == [10, 20]


@pytest.mark.parametrize('code,expected_calls', [(400, 1), (503, 3)])
def test_retry_stops_and_preserves_failure(monkeypatch, code, expected_calls):
    monkeypatch.setattr('prompt_prototype.time.sleep', lambda _: None)
    calls = []
    def operation():
        calls.append(1)
        raise APIError(code, {'error': {'message': 'Failure'}})
    with pytest.raises(APIError):
        call_with_retry(operation, max_attempts=3)
    assert len(calls) == expected_calls


def test_selects_off_peak_feasible_slot():
    assert plan_charge(sample_data())["slot_id"] == "16:00-A"


@pytest.mark.parametrize("field,value", [("compatible", False), ("available_ports", 0),
    ("within_shift", False), ("trip_conflict", True), ("energy_to_slot", 30)])
def test_rejects_each_infeasible_candidate(field, value):
    data = copy.deepcopy(sample_data())
    for slot in data["slots"]:
        slot[field] = value
    assert plan_charge(data)["action"] == "human_review"


@pytest.mark.parametrize("change", [{"soc": 2}, {"soc": float('nan')},
    {"age_minutes": 6}, {"slots": []}, {"reserve": -1}])
def test_fails_closed_on_unsafe_or_invalid_inputs(change):
    assert plan_charge(sample_data(**change))["action"] == "human_review"


def test_missing_input_fails_closed():
    assert plan_charge({})["action"] == "human_review"
