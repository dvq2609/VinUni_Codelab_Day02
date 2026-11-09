## 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Công**, AI Engineer tại **Vin Smart Future**. Nhóm chúng tôi được giao nhiệm vụ phối hợp với Khối Vận Hành của **Xanh SM (GSM)** để tìm kiếm các cơ hội tối ưu hóa bằng trí tuệ nhân tạo. 

Thông qua khảo sát thực địa tại Trung tâm Điều vận Xanh SM Hà Nội, tôi nhận thấy các điều phối viên (Dispatchers) đang gặp một áp lực cực kỳ lớn vào giờ cao điểm, dẫn đến việc rò rỉ hiệu suất điều xe và tăng tỉ lệ khách hàng hủy chuyến. Bài toán tôi mang vào buổi Lab hôm nay đến từ chính quan sát thực tế này.

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Dùng **4 Lenses** quét qua vận hành của các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinmec** | Lặp lại + Tốn thời gian | chuyển hội thoại thành hồ sơ bệnh án có cấu trúc để bác sĩ kiểm tra và xác nhận. |
| 2 | **Vinmec** | AI-upgrade + Lặp lại + Tốn thời gian | tự động tiếp nhận, xác nhận, nhắc lịch và tìm lịch thay thế, giảm tải tổng đài và hạn chế bệnh nhân bỏ lịch |
| 3 | **Vinmec** | Lặp lại + Tốn thời gian | Khi kiểm tra thẻ bảo hiểm AI tự động đọc, đối chiếu hồ sơ và phát hiện thông tin thiếu hoặc không khớp trước khi gửi yêu cầu bảo lãnh. |
| 4 | **Vinmec** | Lặp lại + Stakeholder Pain | Nhân viên xét nghiệm phải tìm đúng bác sĩ phụ trách, gọi điện thông báo kết quả xét nghiệm nguy cấp và theo dõi xác nhận tiếp nhận. AI kết hợp workflow automation để định tuyến thông báo, theo dõi phản hồi và tự động escalation khi chưa có xác nhận. |
| 5 | **Vinmec** | Pain từ người khác + Tốn thời gian | Nhân viên phải phối hợp bác sĩ, điều dưỡng, nhà thuốc, thu ngân và bộ phận bảo hiểm để hoàn tất thủ tục xuất viện. |
---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn top 3 từ danh sách SCAN: **#1 (Chuyển hội thoại thành hồ sơ bệnh án), #2 (Tự động xử lý tiếp nhận lịch khám), #3 (Quá trình kiểm tra bảo hiểm).**

## Thẻ bài toán tiêu biểu: Card #1 — Chuyển hội thoại thành hồ sơ bệnh án

```text
┌──────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #01                                       │
│                                                              │
│ Bài toán (1 câu):                                            │
│ Bác sĩ mất nhiều thời gian nhập liệu và hoàn thiện bệnh án   │
│ sau mỗi lượt khám, làm giảm thời gian dành cho bệnh nhân.    │
│                                                              │
│ Công ty thành viên:                                          │
│ [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes                       │
│ [x] Vinmec   [ ] Khác                                        │
│                                                              │
│ Ai đang đau (Actor)?                                         │
│ - Bác sĩ khám ngoại trú                                      │
│ - Điều dưỡng / thư ký y khoa                                 │
│ - Bộ phận quản lý hồ sơ bệnh án                              │
│                                                              │
│ Workflow thủ công hiện tại (5 bước):                         │
│ 1. Bác sĩ trao đổi và khám bệnh nhân                         │
│       ↓                                                      │
│ 2. Ghi chú triệu chứng, tiền sử và kết quả khám              │
│       ↓                                                      │
│ 3. Nhập chẩn đoán và hướng điều trị vào EMR                  │
│       ↓                                                      │
│ 4. Hoàn thiện các trường thông tin của bệnh án              │
│       ↓                                                      │
│ 5. Kiểm tra và xác nhận lưu hồ sơ                            │
│                                                              │
│ Bước nào tốn thời gian/lỗi nhất?                             │
│ Nhập liệu và hoàn thiện bệnh án (bước 3–4).                  │
│ ⏱ Giả định khảo sát ban đầu: 5–10 phút/lượt khám.            │
│                                                              │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                        │
│ - Speech-to-Text chuyển hội thoại thành văn bản.             │
│ - LLM tóm tắt và phân loại thông tin y khoa.                 │
│ - Tạo bản nháp bệnh án theo cấu trúc EMR.                    │
│ - Bác sĩ kiểm tra và xác nhận trước khi lưu.                 │
│                                                              │
│ Đo thành công bằng gì (Metric có số)?                        │
│ - Giảm 30% thời gian hoàn thiện bệnh án/lượt khám.           │
│ - Độ chính xác các trường dữ liệu trích xuất ≥ 95%.          │
│ - 100% bệnh án do AI tạo phải được bác sĩ xác nhận.          │
│ - Tỷ lệ phải chỉnh sửa nội dung không tăng so với baseline.  │
│                                                              │
│ Quick Architecture:                                          │
│ [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent                      │
│ Hybrid: Speech-to-Text + LLM + Rule Validation.              │
└──────────────────────────────────────────────────────────────┘

---