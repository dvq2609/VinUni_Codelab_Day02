## 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Quyến**, AI Engineer tại **Vin Smart Future**. Nhóm chúng tôi được giao nhiệm vụ phối hợp với Khối Vận Hành của **Xanh SM (GSM) ** để tìm kiếm các cơ hội tối ưu hóa bằng trí tuệ nhân tạo. 

Thông qua khảo sát thực địa tại Trung tâm Điều vận Xanh SM Hà Nội, tôi nhận thấy các điều phối viên (Dispatchers) đang gặp một áp lực cực kỳ lớn vào giờ cao điểm, dẫn đến việc rò rỉ hiệu suất điều xe và tăng tỉ lệ khách hàng hủy chuyến. Bài toán tôi mang vào buổi Lab hôm nay đến từ chính quan sát thực tế này.


# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Xanh SM |Repetitive  |Kiểm duyệt ảnh điểm danh ca làm việc (Check-in QC): Mỗi đầu ca, hàng chục nghìn tài xế chụp ảnh đồng phục, nội thất và ngoại thất xe gửi lên hệ thống. Nhân viên QC phải duyệt thủ công từng ảnh để đảm bảo chuẩn 5 sao (mất ~1–2 phút/xe, dễ bỏ sót lỗi bẩn xe hoặc sai đồng phục vào giờ giao ca cao điểm).  |
| 2 | Xanh SM |AI-upgrade  |Lên lịch sạc pin thông minh tránh trùng giờ cao điểm khách đặt xe: Hiện tại tài xế tự quyết định lúc nào đi sạc, dẫn đến tình trạng nhiều xe cùng hết pin và đổ dồn về trạm sạc vào khung giờ tan tầm (17h–19h), vừa gây ùn tắc trạm sạc VinFast vừa làm hụt 20–25% lượng xe phục vụ khách giờ cao điểm.  |
| 3 | Xanh SM |AI-upgrade  |Chatbot đặt xe & điều chỉnh chuyến cho khách doanh nghiệp/khách quốc tế: Khách nước ngoài hoặc trợ lý đặt xe đoàn thường nhắn yêu cầu phức tạp (cần cốp rộng đựng 4 vali, có ghế trẻ em, đón nhiều điểm). Chatbot rule-based hiện tại trả lời rập khuôn, buộc khách phải gọi tổng đài chờ 5–10 phút.  |
| 4 | Xanh SM |Stakeholder Pain | Gợi ý "Điểm đón thực tế" tại các khu đô thị lớn: tài xế và khách hàng thường xuyên phàn nàn vì định vị GPS thường bị lệch, mất định vị, Tài xế phải gọi điện hỏi khách "Anh đứng ở sảnh nào, cổng mấy?" mất 5–7 phút vòng vèo tìm nhau, tăng tỉ lệ hủy chuyến |
| 5 | Xanh SM |Stakeholder Pain | Trợ lý chẩn đoán nhanh mã lỗi xe điện (EV) trên taplo cho tài xế: Nhiều tài xế mới chuyển từ xe xăng sang xe điện (VF5, VFe34) bị hoang mang khi taplo hiện đèn cảnh báo lạ. Họ phải gọi lên hotline kỹ thuật chờ 10–15 phút để hỏi xem xe có chạy tiếp được không hay phải dừng khẩn cấp. |

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Top 3 từ danh sách scan:  **#2 (Lên lịch sạc pin thông minh), #4 (Gợi ý "Điểm đón thực tế" tại các khu đô thị lớn), #5 (Trợ lý chẩn đoán nhanh mã lỗi xe điện (EV) trên taplo ).**


┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                      │
│                                                             │
│ Bài toán: Lên lịch sạc pin thông minh tránh trùng giờ cao   │
│ điểm khách đặt xe.                                          │
│ Công ty thành viên: [x] Xanh SM (GSM) & V-GREEN   │
│                                                             │
│ Ai đang đau?                                                │
│ - Tài xế: Xếp hàng chờ sạc lâu, mất cuốc giờ cao điểm       │
│ - Khách hàng: Khó đặt xe, giá surge tăng                    │
│ - Vận hành: Hụt 20–25% xe sẵn sàng đón khách (17h–19h)      │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế tự theo dõi % pin trên taplo theo thói quen     │
│   → 2. Xe báo pin yếu (<20%) ngẫu nhiên gần giờ tan tầm     │
│   → 3. Tài xế tắt app nhận cuốc, tự tìm trạm sạc gần nhất   │
│   → 4. Dồn cục tại trạm sạc VinFast, chờ 30–60 phút đến lượt│
│   → 5. Bỏ lỡ toàn bộ khung giờ nhu cầu khách cao nhất       │
│                                                             │
│ Bước nào tốn nhất? Bước 3-4 (⏱ 45–60 phút chờ sạc & mất cuốc)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-3              │
│ (Dự báo nhu cầu cuốc xe + Theo dõi mức pin IoT real-time    │
│  → Đề xuất slot sạc lệch giờ cao điểm kèm incentive/thưởng) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ - Giảm tỷ lệ xe sạc dồn giờ cao điểm từ 25% ──> dưới 8%.   │
│ - Thu hồi ~840 triệu VNĐ doanh thu thất thoát/ngày.         │
│                                                             │
│ Quick Architecture:                                         │
│ [x] Predictive Model (Dự báo nhu cầu đặt xe theo cụm giờ)   │
│ [x] Optimization Algorithm (Phân bổ slot sạc thông minh)    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #4                                       │
│                                                             │
│ Bài toán: Gợi ý "Điểm đón thực tế" (Smart Pickup Points)    │
│ tại các khu đô thị lớn, chung cư cao tầng.                 │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau?                                                │
│ - Tài xế: Mất công chạy vòng vo, dễ bị phạt dừng đỗ         │
│ - Khách hàng: Chờ lâu, bực bội vì phải giải thích vị trí    │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Khách ghim vị trí theo GPS trôi/mặc định trong app     │
│   → 2. Tài xế đến tọa độ ghim nhưng vướng rào chắn/cửa sau  │
│   → 3. Tài xế gọi điện hỏi "Anh/chị đứng ở sảnh nào, cổng mấy?"│
│   → 4. Hai bên mất 5–7 phút miêu tả vị trí và tìm nhau      │
│   → 5. Khách hoặc tài xế bức xúc ấn hủy cuốc                │
│                                                             │
│ Bước nào tốn nhất? Bước 3-4 (⏱ 5–7 phút gọi điện & tìm điểm) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-2              │
│ (Clustering điểm đón lịch sử + Nhận diện sảnh/cổng đón hợp  │
│  lệ gần nhất → Snap ghim khách vào điểm đón thực tế)        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ - Giảm thời gian tiếp cận đón khách từ 6 phút ──> dưới 2 phút│
│ - Giảm tỷ lệ hủy cuốc do sai lệch điểm đón từ 5% ──> dưới 1%│
│                                                             │
│ Quick Architecture:                                         │
│ [x] Spatial Clustering / Geospatial AI (Tọa độ sảnh đón)    │
│ [x] LLM / Rule Feature (Gợi ý text rõ ràng: Sảnh A, Cổng 2) │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                      │
│                                                             │
│ Bài toán: Trợ lý chẩn đoán nhanh mã lỗi xe điện (EV) trên   │
│ màn hình taplo cho tài xế.                                  │
│ Công ty thành viên: [x] Xanh SM & VinFast                   │
│                                                             │
│ Ai đang đau?                                                │
│ - Tài xế: Hoang mang khi thấy đèn báo lạ, sợ hỏng xe/cháy nổ│
│ - Tổng đài kỹ thuật: Quá tải các cuộc gọi giải thích mã lỗi │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Xe báo đèn cảnh báo/mã lỗi lạ (ví dụ: con rùa vàng)    │
│   → 2. Tài xế tấp xe vào lề, gọi hotline hỗ trợ kỹ thuật    │
│   → 3. Chờ máy và miêu tả lỗi bằng lời nói dân dã, mơ hồ    │
│   → 4. Kỹ thuật viên tra sổ tay hướng dẫn hoặc hỏi chéo     │
│   → 5. Kỹ thuật viên kết luận: Đi tiếp hay gọi xe cứu hộ    │
│                                                             │
│ Bước nào tốn nhất? Bước 2-4 (⏱ 10–15 phút chờ máy & giải thích)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4              │
│ (Tài xế chụp ảnh taplo → Vision AI đọc mã/icon → RAG tra    │
│  cẩm nang kỹ thuật VinFast → Trả hướng xử lý ngay lập tức) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ - Thời gian chẩn đoán lỗi giảm từ 15 phút ──> dưới 30 giây. │
│ - Giảm 70% lượng cuộc gọi kỹ thuật cơ bản về hotline.       │
│                                                             │
│ Quick Architecture:                                         │
│ [x] Multimodal Vision Model (OCR + Nhận diện biểu tượng)    │
│ [x] RAG (Truy xuất cẩm nang vận hành xe điện VinFast)       │
└─────────────────────────────────────────────────────────────┘
