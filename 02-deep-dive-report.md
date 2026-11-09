# 02 — Deep-Dive Report: Đối soát phiên sạc và hóa đơn VinFast

> **Trạng thái:** Chủ đề đã được nhóm lựa chọn để phân tích sâu. Các quy mô, thời gian và chi phí trong báo cáo là **giả định ban đầu do nhóm cung cấp**, chưa được xác minh với đơn vị vận hành. Workflow hiện tại dưới đây là giả thuyết cần walkthrough với nhân viên đối soát/kế toán. Không xem các con số là baseline hay kết quả đạt được.

## 1. Chủ đề và phạm vi

**Bài toán:** Hỗ trợ đối soát bản ghi phiên sạc với dữ liệu thanh toán/hóa đơn đối tác, tự động ghép các trường hợp khớp theo quy tắc và đưa sai lệch hoặc dữ liệu thiếu vào hàng đợi để nhân viên kiểm tra.

**Phạm vi pilot đề xuất:** Một đối tác hoặc một nhóm trạm, trong một kỳ đối soát giới hạn. Đối chiếu các trường có sẵn như mã phiên, mã trạm/điểm sạc, thời gian, sản lượng điện, đơn giá, số tiền và trạng thái thanh toán. Chưa tự động điều chỉnh hóa đơn, sổ kế toán hoặc thanh toán.

## 2. Giả định quy mô và ước lượng tác động

| Giả định | Giá trị | Ghi chú |
|---|---:|---|
| Trạm sạc hoạt động | 2.000 | Cần xác minh phạm vi và thời điểm thống kê |
| Phiên sạc trung bình mỗi trạm mỗi ngày | 100 | Giả định |
| Tổng phiên sạc/ngày | 200.000 | 2.000 × 100 |
| Giá trị trung bình mỗi phiên | 50.000 VNĐ | Giá trị giao dịch giả định; không đồng nghĩa doanh thu ghi nhận |
| Tỷ lệ đưa vào hàng đợi rà soát | 2% | 4.000 phiên/ngày; không có nghĩa 2% chắc chắn sai |
| Thời gian rà soát thủ công | 3–5 phút/phiên | Cần đo bằng mẫu công việc thực tế |
| Chi phí lao động quy đổi | 45.000 VNĐ/giờ | Theo giả định 8 triệu VNĐ/tháng; cần xác minh cách tính giờ công |
| Ngày vận hành trong tháng | 30 | Giả định |

Theo các giả định trên, hàng đợi 4.000 phiên cần khoảng **200–333 giờ công/ngày** nếu rà soát hoàn toàn thủ công. Nếu hệ thống xử lý đúng 80% hàng đợi và nhân viên không cần kiểm lại các trường hợp đó, thời gian lao động quy đổi giảm khoảng **160–267 giờ/ngày**, tương đương **4.800–8.000 giờ/tháng** hoặc **216–360 triệu VNĐ/tháng** theo đơn giá giờ giả định. Đây là giá trị thời gian công quy đổi, **không khẳng định khoản tiết kiệm tiền mặt**; chưa tính chi phí xây dựng/vận hành, kiểm soát chất lượng, ngoại lệ và khả năng phải kiểm tra lại.

Giá trị giao dịch tổng hợp theo giả định là khoảng **10 tỷ VNĐ/ngày** (200.000 × 50.000 VNĐ). Đây chỉ là tổng giá trị phiên ước tính, không phải doanh thu hay số tiền thất thoát đã xác minh.

## 3. Current-State Workflow (giả thuyết cần xác minh)

Workflow dự kiến để mang đi walkthrough với nhân viên đối soát/kế toán:

1. Nhận dữ liệu phiên sạc từ hệ thống vận hành và hóa đơn/bảng kê từ đối tác qua các kênh hiện có.
2. Tập hợp, chuẩn hóa định dạng và ghép kỳ đối soát; kiểm tra file thiếu, bản ghi trùng hoặc trường bắt buộc bị khuyết.
3. So sánh mã phiên, trạm, thời gian, sản lượng, đơn giá, số tiền và trạng thái thanh toán theo quy tắc nghiệp vụ.
4. Phân loại các bản ghi khớp, lệch, thiếu hoặc trùng; nhân viên mở nguồn liên quan và điều tra từng ngoại lệ.
5. Ghi nhận kết quả xử lý, chuyển trường hợp cần trao đổi cho đối tác/người phụ trách, sau đó hoàn tất đối soát và lưu vết.

**Nút thắt giả thuyết:** chuẩn hóa dữ liệu không đồng nhất, tìm bản ghi tương ứng giữa hai nguồn, và điều tra các ngoại lệ. Theo giả định nhóm đưa ra, 4.000 giao dịch/ngày vào hàng đợi rà soát × 3–5 phút = 200–333 giờ công/ngày. Cần kiểm chứng xem “2% cần kiểm tra” là tỷ lệ mismatch, tỷ lệ không tự khớp, hay ngưỡng lấy mẫu; đồng thời xác minh khối lượng thực tế, thời gian xử lý và cách xử lý ngoại lệ.

**Handoff cần thể hiện/xác minh:** hệ thống vận hành → đội đối soát; đối tác → đội đối soát; nhân viên đối soát → kế toán/người có thẩm quyền; nhân viên → đối tác khi cần làm rõ sai lệch.

Sơ đồ current-state được cung cấp riêng tại [`04-workflow-diagram.png`](04-workflow-diagram.png).

## 4. Problem Statement (6 fields)

| Trường | Nội dung |
|---|---|
| **1. Actor / Operator** | Giả thuyết: nhân viên đối soát giao dịch/kế toán hoặc vận hành tài chính phụ trách đối chiếu dữ liệu phiên sạc với bảng kê/hóa đơn đối tác. Cần xác nhận chức danh và nhóm chịu trách nhiệm. |
| **2. Current Workflow** | Nhận dữ liệu từ hệ thống phiên sạc và đối tác, chuẩn hóa/ghép dữ liệu, đối chiếu các trường theo quy tắc, điều tra sai lệch hoặc bản ghi thiếu/trùng, ghi nhận và chuyển cấp/trao đổi khi cần. Luồng và công cụ cụ thể cần walkthrough. |
| **3. Bottleneck** | Giả thuyết: xử lý thủ công các bản ghi không tự khớp, nhất là khi định dạng/khóa giao dịch khác nhau hoặc thiếu trường. Ước lượng ban đầu là 4.000 lượt rà soát/ngày × 3–5 phút; các giả định này chưa phải số đo. |
| **4. Business Impact** | Theo giả định, rà soát toàn bộ hàng đợi cần 200–333 giờ công/ngày. Tự động xử lý chính xác 80% có thể giải phóng 160–267 giờ/ngày, tương đương 216–360 triệu VNĐ/tháng theo chi phí lao động quy đổi. Chưa xác minh ảnh hưởng tới SLA, sai thanh toán hay thất thoát. |
| **5. Success Metrics** | Pilot đề xuất: (a) giảm ít nhất 80% số lượt kiểm tra thủ công trong phạm vi pilot mà không tăng sai sót; (b) precision của nhóm “tự khớp” ≥99,5% trên tập kiểm tra độc lập đã được nhân viên xác nhận; (c) 100% mismatch/thiếu dữ liệu được đưa vào hàng đợi và lưu lý do; (d) đo tỷ lệ bỏ sót sai lệch, false positive và thời gian xử lý trung vị so với baseline. Đây là ngưỡng mục tiêu cần nhóm/đơn vị xác nhận, không phải kết quả đã đạt. |
| **6. Operational Boundary** | Hệ thống được phép chuẩn hóa dữ liệu, so khớp theo quy tắc đã phê duyệt, gắn nhãn trạng thái và tạo hàng đợi/lý do sai lệch. **Không được** tự sửa dữ liệu nguồn, xác nhận thanh toán, điều chỉnh hóa đơn/sổ sách, hoặc loại bỏ ngoại lệ. Mọi sai lệch tài chính, thiếu dữ liệu, trùng lặp không rõ nguyên nhân và trường hợp độ tin cậy thấp phải do nhân viên có thẩm quyền xem xét. Lưu nguồn đối chiếu và audit trail; nếu dữ liệu/API lỗi thì dừng tự động khớp và chuyển sang quy trình thủ công. |

## 5. AI Fit: Rule vs LLM vs Agent

| Cách tiếp cận | Vai trò phù hợp | Đánh giá |
|---|---|---|
| **Rule / State Machine** | Chuẩn hóa định dạng; ghép theo mã phiên; so sánh thời gian, sản lượng, đơn giá, tiền và trạng thái; áp dụng dung sai được phê duyệt; phát hiện bản ghi thiếu/trùng. | **Thành phần chính nên dùng.** Kết quả có thể giải thích, kiểm toán và kiểm thử rõ ràng. Khóa ghép và dung sai phải do nghiệp vụ xác nhận. |
| **LLM Feature** | Đọc tài liệu phi cấu trúc nếu có; tóm tắt lý do mismatch từ dữ liệu đã lọc; soạn ghi chú/yêu cầu làm rõ cho nhân viên. | Chỉ là phần bổ trợ tùy chọn. Không dùng LLM làm trọng tài số học hoặc quyết định khớp tài chính. Nội dung tạo ra phải được kiểm tra và gắn với dữ liệu nguồn. |
| **Agentic Loop** | Tự gọi nhiều hệ thống và tự xử lý ngoại lệ. | Chưa phù hợp cho pilot: hành động tài chính có rủi ro, workflow và quyền truy cập chưa xác minh; không có lý do để trao quyền tự quyết cho agent. |

**Kết luận AI fit:** Bắt đầu bằng pipeline đối soát dựa trên rule. Thêm LLM chỉ nếu có tài liệu phi cấu trúc hoặc nhu cầu giải thích thực tế đã xác nhận. Đây là bài toán tự động hóa và quản trị dữ liệu trước hết; không cần buộc dùng LLM/Agent để được gọi là giải pháp AI.

## 6. Future-State Flow, HITL và fallback

1. Nhận hai bộ dữ liệu trong phạm vi pilot; kiểm tra quyền truy cập, schema, kỳ dữ liệu và tính toàn vẹn.
2. Chuẩn hóa trường theo quy tắc đã thống nhất; ghi nhận bản gốc và phiên bản dữ liệu.
3. **Rule engine** ghép chính xác theo khóa nghiệp vụ; áp dụng dung sai chỉ khi kế toán/đơn vị sở hữu quy trình phê duyệt.
4. Đánh dấu kết quả thành `matched`, `mismatch`, `missing`, `duplicate` hoặc `needs_review`; kèm trường nguồn và lý do so khớp/lệch.
5. **HITL:** nhân viên rà soát tất cả ngoại lệ và mẫu kiểm soát của nhóm tự khớp; quyết định cách xử lý và phê duyệt mọi điều chỉnh ngoài hệ thống đối soát.
6. Lưu kết quả, quyết định của người duyệt và audit trail; tổng hợp metric pilot.

**Fallback:** nếu một nguồn dữ liệu thiếu/sai schema, khóa ghép mơ hồ, dịch vụ lỗi hoặc quy tắc chưa bao phủ trường hợp, không tự khớp trường hợp đó. Dừng batch hoặc cách ly bản ghi liên quan, báo lỗi có thể truy vết và chuyển nhân viên xử lý thủ công. Không để LLM tự điền dữ liệu thiếu.

## 7. Readiness và quyết định

| Câu hỏi readiness | Trạng thái hiện tại | Điều kiện cần xác minh |
|---|---|---|
| Có dữ liệu mẫu/log sạch để thử không? | Chưa xác nhận | Xin mẫu đã ẩn danh của cả hai nguồn; xác nhận quyền sử dụng, đủ kỳ và có nhãn kết quả do chuyên viên xác nhận. |
| Rủi ro khi sai có kiểm soát được không? | Có thể kiểm soát ở pilot nếu chỉ tạo gợi ý và giữ HITL | Kiểm tra quyền truy cập, audit trail, xử lý bản ghi thiếu/trùng, quy trình rollback và người chịu trách nhiệm phê duyệt. |
| Stakeholder sẵn sàng thay đổi quy trình không? | Chưa xác nhận | Walkthrough với đối soát/kế toán và đối tác; thống nhất queue, SLA, quy tắc và cách ghi nhận kết quả. |
| Baseline và giả định khối lượng đã đo chưa? | Chưa | Đo số phiên thực, tỷ lệ auto-match hiện hữu, tỷ lệ ngoại lệ, phút xử lý, tỷ lệ sửa lại và chi phí thực tế. |

### Quyết định: **GO cho prototype mô phỏng; chưa GO cho pilot vận hành thật**

Nhóm có thể bắt đầu prototype giới hạn bằng dữ liệu mẫu/tổng hợp để minh họa bước chuẩn hóa, so khớp theo rule, phân loại ngoại lệ và tạo hàng đợi rà soát. GO ở đây chỉ áp dụng cho thử nghiệm kỹ thuật offline; không có nghĩa các giả định đã được xác nhận hoặc hệ thống được phép xử lý giao dịch thật. Chưa đủ bằng chứng để chạy pilot trên dữ liệu vận hành vì chưa có dữ liệu đối soát mẫu được duyệt, workflow được người vận hành xác nhận, baseline thời gian/ngoại lệ, hay khóa ghép và dung sai đã thống nhất. Trước khi mở rộng sang pilot thật, cần hoàn tất các xác minh tại mục 8 và giữ nhân viên duyệt mọi ngoại lệ; prototype không được tự điều chỉnh hóa đơn hay sổ sách.

## 8. Việc cần nhóm xác minh trước khi chốt báo cáo

- Xác nhận số trạm, số phiên mỗi trạm/ngày và giá trị trung bình/phiên bằng nguồn dữ liệu và thời kỳ cụ thể.
- Làm rõ tỷ lệ 2% là mismatch thực tế, bản ghi không tự ghép được, hay giả định lập kế hoạch.
- Walkthrough với nhân viên để xác nhận hệ thống nguồn, định dạng, bước thao tác, handoff, thời gian và quy trình kết thúc đối soát.
- Xác nhận khóa giao dịch, dung sai thời gian/sản lượng/giá, xử lý phí/thuế, bản ghi trùng và hoàn tiền.
- Định nghĩa tập kiểm thử được chuyên viên gán nhãn, baseline, metric và người phê duyệt.
