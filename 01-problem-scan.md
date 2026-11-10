# 🔍 Lab 02 — Problem Scan & Quick-Assess (Vin Smart Future)

> **Học viên thực hiện:** Tùng Nguyễn (`2A202603854`) — AI Product Engineer tại **Vin Smart Future**  
> **Phạm vi:** Phase 1 (SCAN — 4 Lenses) & Phase 2 (QUICK-ASSESS — 3 Quick Problem Cards)

---

## 🏛️ 1. Phase 1 — SCAN: Tìm kiếm cơ hội tối ưu vận hành bằng AI (Cá nhân)

Sử dụng **4 Lenses** (*Lặp lại / Repetitive*, *Tốn thời gian / Time-consuming*, *AI có thể tốt hơn / AI-upgrade*, *Pain từ người khác / Stakeholder Pain*) để quét qua các điểm nghẽn vận hành thực tế tại các công ty thành viên thuộc tập đoàn Vingroup:

| # | Subsidiary | Lens | Mô tả ngắn bài toán & Tổn thất ước tính |
|---|------------|------|-----------------------------------------|
| 1 | **Xanh SM (GSM)** | **Tốn thời gian** *(Time-consuming)* | **Điều phối xử lý sự cố pin khẩn cấp & cứu hộ thực địa:** Điều phối viên phải tra cứu thủ công tọa độ GPS của xe gặp sự cố, đối chiếu danh sách trụ sạc VinFast còn trống theo đúng chuẩn cổng sạc (VF5/VFe34/VF8) và gõ tay tin nhắn chỉ dẫn hoặc gọi xe cứu hộ pin di động. Mất trung bình **15 phút/lượt** (~80 ca/ngày tại Hà Nội, lãng phí ~20 giờ công/ngày và gây giảm ~15% hiệu suất đón khách của xe). |
| 2 | **VinFast** | **AI có thể tốt hơn** *(AI-upgrade)* | **Chẩn đoán sơ bộ mã lỗi kỹ thuật từ mô tả tiếng Việt của chủ xe:** Cố vấn dịch vụ (Service Advisor) tại xưởng dịch vụ mất **12–18 phút/xe** để đọc mô tả triệu chứng đời thường của khách hàng (VD: *"xe đi qua gờ giảm tốc kêu lục cục bên phụ, màn hình báo lỗi hình con rùa"*), tra cứu tài liệu kỹ thuật (Service Manual) và ánh xạ sang mã lỗi OBD/DTC ban đầu. Tỷ lệ phân luồng sai kỹ thuật viên chuyên trách còn ở mức ~18%. |
| 3 | **Vinmec** | **Pain từ người khác** *(Stakeholder Pain)* | **Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary):** Bác sĩ nội trú phải tổng hợp thủ công kết quả xét nghiệm, chẩn đoán hình ảnh, đơn thuốc và diễn tiến điều trị từ hệ thống HIS để viết giấy ra viện và hướng dẫn chăm sóc tại nhà bằng ngôn ngữ dễ hiểu cho bệnh nhân. Tốn **20–30 phút/bệnh nhân**, khiến bác sĩ quá tải hành chính và bệnh nhân phải chờ làm thủ tục xuất viện lâu (trung bình 90 phút). |
| 4 | **Vinhomes** | **Lặp lại** *(Repetitive)* | **Phân loại & điều hướng phản ánh cư dân trên App Vinhomes Resident:** Hằng ngày Ban Quản lý tiếp nhận hàng nghìn yêu cầu kèm ảnh/mô tả tự do (mất nước, thẻ thang máy lỗi, đăng ký thi công, khiếu nại tiếng ồn). Nhân viên CSKH phải đọc và phân loại thủ công sang các bộ phận Kỹ thuật / An ninh / Kế toán, gây trễ SLA phản hồi (trung bình **4–8 giờ**) và tỷ lệ chuyển nhầm bộ phận ~14%. |
| 5 | **VinFast** | **Lặp lại** *(Repetitive)* | **Đối soát hóa đơn sạc điện và sản lượng điện với đối tác nhượng quyền trạm sạc:** Kế toán vận hành phải đối chiếu log phiên sạc từ hệ thống quản lý trụ sạc (OCPP) với bảng kê công tơ điện và hóa đơn đầu vào từ hàng trăm đối tác mặt bằng hằng tháng. Quy trình xử lý bảng tính thủ công mất **5 ngày công/tháng**, dễ phát sinh sai lệch số liệu thanh toán. |
| 6 | **Vinpearl / VinWonders** | **Tốn thời gian** *(Time-consuming)* | **Bóc tách yêu cầu đặt phòng & dịch vụ đoàn (Group Booking Email Intake):** Nhân viên Sales B2B phải đọc các email dài từ đại lý lữ hành (OTA/TA) với nhiều yêu cầu thay đổi ngày, hạng phòng, phụ thu trẻ em, vé VinWonders và xe đưa đón để kiểm tra quỹ phòng trên PMS và soạn báo giá. Mất **25–40 phút/email**, làm chậm tốc độ chốt đoàn vào mùa cao điểm. |

---

## 🃏 2. Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Từ danh sách 6 bài toán ở Phase 1, chọn ra **Top 3 bài toán** có tác động vận hành rõ rệt nhất (**#1 Xanh SM**, **#2 VinFast**, **#3 Vinmec**) để đánh giá nhanh qua 3 thẻ bài toán:

### 2.1. Quick Problem Card #1 — Xanh SM: Điều phối xử lý sự cố pin khẩn cấp & cứu hộ thực địa

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                      │
│                                                                            │
│ Bài toán (1 câu): Điều phối viên Xanh SM mất quá nhiều thời gian tra cứu   │
│ thủ công trạm sạc trống hoặc điều xe cứu hộ khi tài xế báo sự cố cạn pin   │
│ giữa đường.                                                                │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes                 │
│                     [ ] Vinmec   [ ] Khác: _______________________________ │
│                                                                            │
│ Ai đang đau (Actor)?                                                       │
│ - Điều phối viên (Dispatcher) tại Trung tâm Điều vận (quá tải giờ cao điểm)│
│ - Tài xế Xanh SM (chờ đợi lâu giữa đường, mất doanh thu cuốc xe)           │
│                                                                            │
│ Workflow thủ công hiện tại (5 bước):                                       │
│   1. Tài xế gọi hotline điều vận báo xe sắp cạn pin / lỗi sạc (2 phút)     │
│   ──> 2. Dispatcher tra cứu thủ công tọa độ GPS & % pin của xe (2 phút)    │
│   ──> 3. Mở Dashboard VinFast lọc trạm sạc gần nhất còn trụ trống phù hợp  │
│          với dòng xe VF5/VFe34/VF8 (5 phút)                                │
│   ──> 4. Gõ tay tin nhắn chỉ dẫn đường đi gửi qua App Tài xế (5 phút)      │
│   ──> 5. Liên hệ đội xe cứu hộ pin di động nếu pin < 5% (1 phút)           │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & Bước 4 (⏱ 10 phút/lượt)          │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                      │
│ - Bước 2–3 (Auto-pull API tọa độ & trạm sạc trống + Rule kiểm tra ngưỡng   │
│   an toàn pin < 5% / khoảng cách > 5km)                                    │
│ - Bước 4 (LLM tự động soạn nháp `[DRAFT_ONLY]` tin nhắn chỉ dẫn tiếng Việt │
│   hoặc lệnh JSON `dispatch_mobile_charger` để Dispatcher duyệt 1-click)    │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│ - Giảm thời gian xử lý trung bình từ 15 phút/lượt ──> dưới 3 phút/lượt.    │
│ - Đạt >= 98% độ chính xác khi đề xuất trụ sạc đúng chuẩn xe & khoảng cách. │
│ - 100% ca pin nguy cấp (< 5%) không bị điều đi trạm xa > 5km.              │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (kết hợp Rule) [ ] Agent  │
└────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.2. Quick Problem Card #2 — VinFast: Trợ lý phân loại mã lỗi kỹ thuật từ mô tả khách hàng tại Xưởng dịch vụ

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                      │
│                                                                            │
│ Bài toán (1 câu): Cố vấn dịch vụ VinFast tốn nhiều thời gian dịch mô tả    │
│ lỗi bằng ngôn ngữ đời thường của chủ xe sang mã lỗi kỹ thuật chuẩn và      │
│ danh mục kiểm tra ban đầu.                                                 │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [ ] Vinmec   [ ] Khác: _______________________________ │
│                                                                            │
│ Ai đang đau (Actor)?                                                       │
│ - Cố vấn dịch vụ (Service Advisor) tại xưởng dịch vụ VinFast (3S)          │
│ - Kỹ thuật viên sửa chữa (nhận phiếu yêu cầu mô tả mơ hồ, thiếu thông tin) │
│                                                                            │
│ Workflow thủ công hiện tại (4 bước):                                       │
│   1. Khách hàng mô tả triệu chứng lỗi bằng lời hoặc tin nhắn (3 phút)      │
│   ──> 2. Cố vấn dịch vụ tra cứu cẩm nang sửa chữa & lịch sử bảo dưỡng xe   │
│          trên hệ thống DMS (6 phút)                                        │
│   ──> 3. Ghi chú thủ công phiếu tiếp nhận (RO) & đoán nhóm bệnh để phân    │
│          công tổ kỹ thuật viên: Điện - Pin / Gầm - Máy / Đồng sơn (5 phút) │
│   ──> 4. Kỹ thuật viên cắm máy chẩn đoán xác nhận lại và báo giá (4 phút)  │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & Bước 3 (⏱ 11 phút/lượt)          │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                      │
│ - Bước 2 & 3: Dùng LLM + RAG trên Cẩm nang Kỹ thuật VinFast để chuẩn hóa   │
│   mô tả tiếng Việt của khách thành Top-3 mã triệu chứng chuẩn, gợi ý câu   │
│   hỏi khai thác thêm và đề xuất tổ Kỹ thuật viên phù hợp.                  │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│ - Giảm thời gian lập phiếu tiếp nhận kỹ thuật từ 15 phút ──> dưới 4 phút.  │
│ - Giảm tỷ lệ phân luồng sai tổ kỹ thuật viên từ 18% ──> dưới 5%.           │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (RAG Triage)   [ ] Agent  │
└────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.3. Quick Problem Card #3 — Vinmec: Trợ lý soạn thảo nháp Hồ sơ Tóm tắt Xuất viện (Discharge Summary Co-pilot)

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                      │
│                                                                            │
│ Bài toán (1 câu): Bác sĩ nội trú Vinmec mất 20–30 phút/ca để tổng hợp dữ   │
│ liệu từ bệnh án điện tử (EMR) thành bản tóm tắt xuất viện và hướng dẫn     │
│ theo dõi tại nhà cho bệnh nhân.                                            │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [x] Vinmec   [ ] Khác: _______________________________ │
│                                                                            │
│ Ai đang đau (Actor)?                                                       │
│ - Bác sĩ điều trị / Điều dưỡng hành chính tại Vinmec                       │
│ - Bệnh nhân & người nhà (chờ đợi hồ sơ xuất viện lâu)                      │
│                                                                            │
│ Workflow thủ công hiện tại (4 bước):                                       │
│   1. Bác sĩ mở 4–5 tab trên hệ thống HIS/EMR (lâm sàng, xét nghiệm, chẩn   │
│      đoán hình ảnh, đơn thuốc ra viện) để đọc lại toàn bộ đợt điều trị     │
│      (8 phút)                                                              │
│   ──> 2. Copy-paste và biên tập thủ công tóm tắt quá trình bệnh lý, phương │
│          pháp điều trị và kết quả (12 phút)                                │
│   ──> 3. Viết lời dặn dò chế độ ăn uống, tái khám và dấu hiệu cảnh báo     │
│          bằng ngôn ngữ dễ hiểu cho bệnh nhân (5 phút)                      │
│   ──> 4. Bác sĩ kiểm tra lại, ký số và in giao cho bệnh nhân (3 phút)      │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1, 2 & 3 (⏱ 25 phút/bệnh nhân)       │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                      │
│ - Bước 2 & 3: LLM trích xuất dữ liệu có cấu trúc từ EMR và tự động sinh    │
│   bản nháp (Draft) Tóm tắt xuất viện + Hướng dẫn chăm sóc tại nhà kèm      │
│   trích dẫn nguồn từ hồ sơ gốc để bác sĩ review và ký duyệt (HITL).        │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)?                                      │
│ - Giảm thời gian bác sĩ soạn hồ sơ xuất viện từ 28 phút ──> dưới 6 phút.   │
│ - 100% bản tóm tắt được bác sĩ điều trị kiểm duyệt (0% tự động phát hành). │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM (Structured)   [ ] Agent  │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 🧠 3. Stress-Test & Lý do lựa chọn bài toán vào Phase 3 (Deep-Dive)

### 3.1. Phản biện từ góc nhìn CFO & Trưởng phòng Vận hành (AI Stress-Test)
Khi đưa cả 3 thẻ bài toán qua bước phản biện khắt khe:
* **Phản biện với Card #1 (Xanh SM):** *"Tại sao không dùng thuật toán tìm kiếm khoảng cách địa lý (Haversine / Routing API) và biểu mẫu SMS tĩnh (Template) thay vì gọi LLM?"*
  * **Giải trình kỹ thuật:** Đúng là việc lọc trạm sạc trống trong bán kính `< 5km` và kiểm tra ngưỡng pin `< 5%` **nên được xử lý bằng Rule/API xác định (Deterministic)** để đảm bảo an toàn tuyệt đối và tiết kiệm chi phí. Tuy nhiên, trong thực tế vận hành Xanh SM, tài xế báo sự cố qua tin nhắn/cuộc gọi với ngữ cảnh rất đa dạng (đang kẹt xe ở cầu Chương Dương, đang chở khách VIP ra sân bay, trụ sạc báo trống trên hệ thống nhưng bị xe xăng đỗ chắn, v.v.). Một **LLM Feature mỏng** kết hợp với **Rule Guardrails** sẽ giúp bóc tách nhanh ngữ cảnh tự do của tài xế và soạn thảo chỉ dẫn linh hoạt, rõ ràng trong vài giây thay vì để Dispatcher gõ tay 5 phút.
* **Phản biện với Card #2 (VinFast):** Cần xây dựng pipeline RAG đồng bộ toàn bộ tài liệu Service Manual của nhiều đời xe và tích hợp sâu với DMS trước khi kiểm chứng được độ chính xác.
* **Phản biện với Card #3 (Vinmec):** Dữ liệu bệnh án điện tử (EMR) chịu sự quản lý cực kỳ nghiêm ngặt về bảo mật dữ liệu y tế cá nhân (HIPAA / Nghị định 13/2023/NĐ-CP), không thể đưa lên môi trường thử nghiệm nhanh trong phạm vi 1 buổi Lab nếu chưa hoàn tất khử định danh (De-identification).

### 3.2. Quyết định lựa chọn
👉 Chọn **Card #1 — Xanh SM: Điều phối xử lý sự cố pin khẩn cấp & cứu hộ thực địa** để thực hiện **Phase 3 (Deep-Dive)** và **Phase 4 (Technical Prompt Prototype)** vì:
1. **Tác động thời gian thực (Real-time Operational ROI):** Giải quyết trực tiếp nút thắt cổ chai làm mất 20 giờ công/ngày của Trung tâm Điều vận và giảm thời gian chết của đội xe điện.
2. **Ranh giới an toàn rõ ràng, dễ kiểm chứng bằng code:** Có các quy tắc an toàn định lượng cụ thể (`[DRAFT_ONLY]` bắt buộc có HITL duyệt, và quy tắc cứng khi pin `< 5%` cấm điều đi trạm `> 5km` mà phải kích hoạt `dispatch_mobile_charger`).
3. **Phù hợp hoàn hảo với nguyên lý "Problem First, AI Second":** Kết hợp chặt chẽ giữa API/Rule-based Guardrails và LLM Feature, không lạm dụng Agent tự trị ở nơi có rủi ro vận hành cao.

