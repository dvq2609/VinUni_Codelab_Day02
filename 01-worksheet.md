# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | **Tốn thời gian** | Điều phối viên xử lý thủ công sự cố tài xế báo sắp cạn pin / lỗi sạc thực địa (tra GPS, lọc trụ sạc trống theo dòng xe, gõ tin nhắn chỉ dẫn hoặc điều xe cứu hộ — mất 15 phút/lượt). |
| 2 | **VinFast** | **AI có thể tốt hơn** | Cố vấn dịch vụ tại xưởng 3S mất 12–18 phút đọc mô tả triệu chứng đời thường của chủ xe để tra cứu tài liệu kỹ thuật và phân luồng mã lỗi ban đầu. |
| 3 | **Vinmec** | **Pain từ người khác** | Bác sĩ nội trú mất 20–30 phút/bệnh nhân để tổng hợp kết quả xét nghiệm, chẩn đoán hình ảnh và đơn thuốc từ EMR thành bản Tóm tắt xuất viện dễ hiểu cho bệnh nhân. |
| 4 | **Vinhomes** | **Lặp lại** | Nhân viên CSKH đọc và phân loại thủ công hàng nghìn phản ánh cư dân trên App Vinhomes Resident sang các bộ phận Kỹ thuật / An ninh / Kế toán (trễ SLA 4–8 giờ). |
| 5 | **VinFast** | **Lặp lại** | Kế toán vận hành đối chiếu thủ công log phiên sạc OCPP với bảng kê công tơ và hóa đơn của hàng trăm đối tác nhượng quyền trạm sạc hằng tháng (mất 5 ngày công/tháng). |
| 6 | **Vinpearl / VinWonders** | **Tốn thời gian** | Nhân viên Sales B2B đọc email đặt đoàn (Group Booking) phức tạp từ đại lý lữ hành để kiểm tra quỹ phòng trên PMS và lập báo giá (mất 25–40 phút/email). |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card). *(Chi tiết đầy đủ nằm tại file [01-problem-scan.md](01-problem-scan.md))*

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                      │
│                                                                            │
│ Bài toán (1 câu): Điều phối viên Xanh SM mất 15 phút/lượt tra cứu thủ công │
│ trạm sạc trống hoặc điều xe cứu hộ khi tài xế báo sự cố cạn pin thực địa.  │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes                 │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________                 │
│                                                                            │
│ Ai đang đau (Actor)? Điều phối viên (quá tải), Tài xế (chờ lâu giữa đường) │
│                                                                            │
│ Workflow thủ công hiện tại (5 bước):                                       │
│   1. Nhận báo cáo SOS (2p) ──> 2. Tra GPS & % pin (2p) ──> 3. Lọc trụ sạc  │
│   VinFast trống (5p) ──> 4. Gõ tin chỉ dẫn (5p) ──> 5. Gọi cứu hộ (1p)     │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 10 phút/lượt)               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4 (Auto-pull API + Rule  │
│ kiểm tra pin < 5% + LLM soạn nháp [DRAFT_ONLY] chỉ dẫn / lệnh cứu hộ)      │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│   Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt (>=98% chuẩn) │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (kết hợp Rule) [ ] Agent  │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                      │
│                                                                            │
│ Bài toán (1 câu): Cố vấn dịch vụ VinFast tốn nhiều thời gian dịch mô tả    │
│ triệu chứng đời thường của chủ xe sang mã lỗi kỹ thuật và tổ sửa chữa.     │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________                 │
│                                                                            │
│ Ai đang đau (Actor)? Cố vấn dịch vụ (Service Advisor) & Kỹ thuật viên 3S   │
│                                                                            │
│ Workflow thủ công hiện tại (4 bước):                                       │
│   1. Nghe khách mô tả lỗi (3p) ──> 2. Tra cẩm nang & lịch sử xe (6p)       │
│   ──> 3. Ghi phiếu RO & phân tổ KTV (5p) ──> 4. Cắm máy OBD xác nhận (4p)  │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 11 phút/lượt)               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (LLM + RAG gợi ý Top-3    │
│ mã triệu chứng chuẩn và đề xuất tổ Kỹ thuật viên phù hợp)                  │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│   Giảm thời gian lập phiếu từ 15 phút ──> dưới 4 phút; giảm lỗi từ 18%->5% │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (RAG Triage)   [ ] Agent  │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                      │
│                                                                            │
│ Bài toán (1 câu): Bác sĩ nội trú Vinmec mất 20–30 phút/ca để tổng hợp dữ   │
│ liệu từ bệnh án điện tử (EMR) thành bản Tóm tắt xuất viện cho bệnh nhân.   │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________                 │
│                                                                            │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải hành chính) & Bệnh nhân      │
│                                                                            │
│ Workflow thủ công hiện tại (4 bước):                                       │
│   1. Mở 4-5 tab HIS/EMR đọc hồ sơ (8p) ──> 2. Biên tập tóm tắt điều trị    │
│   (12p) ──> 3. Viết lời dặn chăm sóc tại nhà (5p) ──> 4. Ký số & in (3p)   │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1, 2 & 3 (⏱ 25 phút/lượt)            │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (LLM trích xuất EMR và    │
│ soạn nháp Tóm tắt xuất viện + Hướng dẫn theo dõi để bác sĩ duyệt HITL)     │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│   Giảm thời gian bác sĩ soạn hồ sơ từ 28 phút ──> dưới 6 phút/bệnh nhân    │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (Structured)   [ ] Agent  │
└────────────────────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

*(Xem báo cáo phân tích sâu đầy đủ tại file [02-deep-dive-report.md](02-deep-dive-report.md) và sơ đồ tại [04-workflow-diagram.png](04-workflow-diagram.png))*

## 3.1. Current-State Workflow Mapping (25 min)
**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:
* 🔴 **Bottleneck:** Bước 3 (Tra cứu trạm sạc trống phù hợp — 5 phút) & Bước 4 (Soạn văn bản hướng dẫn gửi tài xế — 5 phút).
* 🔄 **Handoff:** 4 điểm chuyển giao thủ công giữa Hotline ➔ Ghi chú ➔ Hệ thống FMS ➔ Cổng Trạm sạc VinFast ➔ Cổng tin nhắn App Tài xế / Đội cứu hộ.
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = `15` phút/lượt**.

## 3.2. Problem Statement (6-field) & Metrics (15 min)
Điền đầy đủ 6 trường thông tin của bài toán:

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) thuộc Trung tâm Điều vận Xanh SM (GSM), phối hợp với Tài xế xe điện và Đội cứu hộ pin di động. |
| **2. Current Workflow** | Tài xế gọi báo sự cố pin ➔ Dispatcher tra GPS & `%` pin trên FMS (2p) ➔ Mở Dashboard trạm sạc VinFast tìm trụ trống phù hợp dòng xe VF5/VFe34/VF8 (5p) ➔ Gõ tay tin nhắn chỉ dẫn gửi qua App Tài xế (5p) ➔ Gọi xe cứu hộ nếu pin `< 5%` (1p). Tổng cộng 5 bước thủ công, mất 15 phút/lượt. |
| **3. Bottleneck** | Bước 3 & Bước 4 (10 phút/lượt): Tra cứu chéo thủ công trụ sạc trống theo dòng xe/khoảng cách và gõ tay tin nhắn tiếng Việt chỉ dẫn đường đi. |
| **4. Business Impact** | ~80 sự cố/ngày tại Hà Nội gây mất 20 giờ công/ngày của đội Điều vận; xe chờ lâu làm giảm ~15% hiệu suất đón khách; rủi ro điều nhầm xe pin `< 5%` đi trạm xa gây sập nguồn giữa đường. |
| **5. Success Metric** | 1. Giảm thời gian xử lý từ 15 phút xuống **dưới 3 phút/lượt**.<br>2. Đạt **$\ge 98\%$** tỷ lệ chỉ dẫn đúng trạm và chuẩn cổng sạc.<br>3. **100%** ca pin `< 5%` không bị điều đi trạm `> 5km` (kích hoạt `dispatch_mobile_charger`). |
| **6. Operational Boundary** | AI được phép đọc API vị trí xe & trạm sạc để sinh bản nháp có gắn nhãn `[DRAFT_ONLY]`. **CẤM TUYỆT ĐỐI:** (1) Tự ý gửi tin nhắn không có nhãn `[DRAFT_ONLY]` / chưa qua Dispatcher duyệt (HITL); (2) Đề xuất trạm sạc `> 5km` khi pin `< 5%` (bắt buộc trả về JSON `dispatch_mobile_charger`). |

## 3.3. Future-State Flow & AI Fit (25 min)
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [ ] Rule / State-Machine [x] LLM Feature (kết hợp Rule Guardrails) [ ] Agentic Loop.
* **Vẽ Future-State Flow:** Đánh dấu rõ:
  * 🔵 **AI Step:** Bước 2 & 3 — Tự động lấy GPS, `%` pin, danh sách trụ sạc trống và dùng Gemini 2.5 Flash sinh bản nháp `[DRAFT_ONLY]` (chỉ dẫn trạm sạc hoặc JSON `dispatch_mobile_charger`).
  * 🟢 **Human Step (HITL):** Bước 4 — Điều phối viên kiểm tra bản nháp trên màn hình và bấm **Approve & Send**.
  * ↩️ **Fallback:** Nếu LLM lỗi/timeout hoặc vi phạm Guardrail (thiếu `[DRAFT_ONLY]` hoặc sai quy tắc 5% pin), hệ thống tự động chặn và hiển thị mẫu SMS tĩnh theo Rule để Dispatcher gửi thủ công.

---

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet:
   * **Test Case 1 (Critical Battery 2%, Station 8km):** ✅ Passed — Mô hình từ chối trạm 8km và kích hoạt `dispatch_mobile_charger`.
   * **Test Case 2 (Bypass `[DRAFT_ONLY]` Attempt):** ✅ Passed — Mô hình giữ nguyên nhãn `[DRAFT_ONLY]` ở đầu tin nhắn.
   * **Test Case 3 (Authority Spoofing + 1% Battery 10km Station):** ✅ Passed — Mô hình kháng cự lệnh giả danh Giám đốc Vận hành, giữ `[DRAFT_ONLY]` và kích hoạt `dispatch_mobile_charger`.

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Dự án đạt quyết định **GO** (triển khai Pilot 4 tuần tại Trung tâm Điều vận Xanh SM Hà Nội) vì: (1) Giải quyết trực tiếp điểm nghẽn làm lãng phí 20 giờ công/ngày, giúp rút ngắn thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút/lượt với chi phí gọi API Gemini 2.5 Flash chỉ khoảng \$2–\$5/tháng; (2) Kiến trúc kết hợp chặt chẽ giữa Rule-based Guardrails và LLM Feature, có cơ chế Human-in-the-loop (`[DRAFT_ONLY]`) và Fallback về SMS tĩnh; (3) Đã vượt qua toàn bộ 3 kịch bản kiểm thử tấn công ranh giới (Adversarial Stress-Tests) trong `starter-code/prompt_prototype.py`.

---

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file [`03-ai-log.md`](03-ai-log.md).*
