# 📝 Báo Cáo Nhật Ký Tương Tác AI (AI Log & Reflection)

> **Họ và tên Kỹ sư:** Đồng Văn Quyến Quyến  
> **Vai trò:** AI Product Engineer — **Vin Smart Future (Vingroup)**  
> **Dự án thực hiện:** Hệ thống Lên lịch sạc pin thông minh tránh trùng giờ cao điểm (Xanh SM & V-GREEN)  
> **Hệ thống AI đồng hành:** Antigravity (Gemini 2.5 Flash / Claude)

---

## 1. 🤖 AI đã giúp gì trong quá trình làm việc? (What AI helped with)

Trong suốt quá trình scoping và deep-dive bài toán, AI đóng vai trò như một **Thought-Partner (Cộng sự tư duy phản biện)** và **Co-pilot kỹ thuật**:

1. **Phân tích bối cảnh & Phân rã bài toán (Deconstruction):**
   * Giúp áp dụng **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Pain point) để rà soát toàn bộ các công ty thành viên Vingroup (Xanh SM, VinFast, Vinhomes, Vinmec), từ đó chọn lọc ra bài toán có ROI cao nhất tại Xanh SM.
   * Chuyển hóa các quan sát thực địa thô sơ thành quy trình 5 bước mạch lạc (Current-State Workflow), nhận diện sắc bén 2 điểm nghẽn chính: **Bước 3 (Dò trạm sạc thủ công: 10 phút)** và **Bước 4 (Dồn cục xếp hàng chờ sạc: 45–60 phút)**.
2. **Trực quan hóa quy trình sang mã nguồn đồ họa:**
   * Tự động sinh mã **ASCII diagram** chuẩn layout và đặc biệt là sinh mã **Mermaid flowchart** tương thích 100% với Draw.io, gắn các class màu sắc nổi bật để làm nổi bật các điểm nghẽn (🔴 Bottlenecks) cho tài liệu báo cáo.
3. **Định lượng hóa các chỉ số kinh doanh (Business Metrics):**
   * Giúp xây dựng công thức tính toán thiệt hại thực tế: Quy đổi từ "20% – 25% xe hụt nguồn cung trong khung 17h–19h" thành con số tổn thất tài chính cụ thể **~840 triệu VNĐ/ngày** dựa trên số cuốc giờ cao điểm và hệ số nhân giá (surge pricing).
4. **Hỗ trợ đánh giá khả thi & Checklist đầu tư (Phase 5):**
   * Đóng vai trò phản biện từ góc nhìn của CFO và Giám đốc Vận hành, đối chiếu AI Readiness Checklist (dữ liệu IoT xe, API trạm sạc V-GREEN) và tính toán thời gian hoàn vốn (Payback Period < 2 ngày).

---

## 2. ⚠️ AI trả lời sai / Ảo giác (Hallucination) ở đâu? (Where AI failed / hallucinated)

Dù rất thông minh, AI đã bộc lộ những điểm mù và lỗi nghiêm trọng cần sự can thiệp của con người:

1. **Lỗi "Neo ngữ cảnh" & Copy nhầm bài toán cũ (Context Leakage / Hallucination):**
   * *Hiện tượng:* Khi được yêu cầu viết phần `3.2 Problem Statement`, AI đã tự động "bê nguyên" dữ liệu từ file ví dụ [02-deliverable-example.md](02-deliverable-example.md) (vốn là bài toán *Xử lý sự cố hết pin thực địa của Điều phối viên Dispatcher*).
   * *Sai lệch cụ thể:* AI ghi nhận: *"Mỗi ngày có ~80 sự cố pin thực địa tại Hà Nội"*, *"Giảm thời gian xử lý từ 15 phút xuống 3 phút"*, *"AI tự động draft tin nhắn SMS"*. Đây là hallucination nguy hiểm vì các chỉ số này hoàn toàn lạc đề so với bài toán *Lên lịch sạc pin tránh giờ cao điểm*.
2. **Ảo tưởng về mức độ tự chủ của AI (Over-automation / Agent Bias):**
   * *Hiện tượng:* Ban đầu AI đề xuất xây dựng một "Autonomous Agent" có toàn quyền tự động ngắt kết nối app nhận khách của tài xế, tự động đặt lịch sạc và cưỡng chế xe di chuyển về trạm sạc.
   * *Sai sót thực tế:* AI không hiểu bản chất vận hành: Tài xế Xanh SM là đối tác vận hành có quyền tự chủ, việc hệ thống tự ý khóa app nhận khách sẽ gây bức xúc nghiêm trọng, vi phạm hợp đồng và làm đứt gãy luồng điều xe.
3. **Bỏ quên rủi ro an toàn vật lý xe điện (Physical Safety Blindspot):**
   * *Hiện tượng:* AI đề xuất thuật toán "gợi ý cuốc xe tiện đường về trạm sạc" nhưng không đưa ra ràng buộc mức pin sàn.
   * *Hậu quả nếu áp dụng:* Nếu xe chỉ còn 10–12% pin mà AI vẫn gán một cuốc xe 15km trong giờ tan tầm kẹt xe, pin điều hòa và động cơ sẽ cạn kiệt, dẫn đến xe chết máy giữa đường, gây ùn tắc giao thông nghiêm trọng.

---

## 3. 🛠️ Tôi đã sửa Prompt, thiết lập Ranh giới (Boundary) ra sao để đạt kết quả chuẩn? (How I adjusted Prompts & Guardrails)

Để đưa AI về đúng quỹ đạo và đảm bảo tiêu chuẩn khắt khe của Vin Smart Future, tôi đã thực hiện các điều chỉnh sau:

### 3.1. Kỹ thuật Prompting & Grounding lại ngữ cảnh:
* **Chặn Context Leakage:** Ra chỉ thị tường minh: *"Chỉ sử dụng dữ liệu từ Problem Card #2 trong 01-problem-scan.md; tuyệt đối không lấy dữ liệu sự cố cứu hộ pin của file ví dụ. Mọi metric phải gắn liền với: Tỷ lệ xe sạc giờ cao điểm (25% -> 8%), doanh thu thất thoát (~840 triệu/ngày), và thời gian xếp hàng tại trạm (45-60 phút -> 10 phút)"*.
* **Yêu cầu đối chiếu thực tế:** Bắt buộc AI phân tích vai trò thực tế của cả 3 bên: Tài xế Xanh SM — Trung tâm Điều vận — Mạng lưới trạm sạc V-GREEN.

### 3.2. Thiết lập Ranh giới Vận hành Bắt buộc (Operational Boundaries & Guardrails):
Tôi đã trực tiếp can thiệp và ép AI phải đưa 4 ranh giới an toàn vào bản thiết kế:
1. **Ranh giới CẤM 1 (Bảo vệ quyền tự chủ của tài xế):** CẤM tuyệt đối việc AI tự động tắt app hoặc ngắt quyền nhận cuốc. Hệ thống chỉ được đưa ra "Đề xuất thông minh" kèm ưu đãi (voucher giảm giá sạc, điểm thưởng), quyền nhận slot sạc 100% do tài xế bấm xác nhận (**Bắt buộc Human-in-the-loop - HITL**).
2. **Ranh giới CẤM 2 (An toàn năng lượng xe điện):** CẤM gán bất kỳ cuốc xe nào có lộ trình > 10km hoặc đi qua điểm đen ùn tắc cho các xe có mức pin dưới **15%**.
3. **Ranh giới CẤM 3 (Tương thích phần cứng):** CẤM điều hướng xe đến các trạm sạc không tương thích chuẩn cổng sạc / công suất của xe (VF5/VFe34/VF8) hoặc trạm đang có báo lỗi mất điện từ V-GREEN.

### 3.3. Tái định hình kiến trúc AI Fit (Architecture Re-alignment):
* Thay vì để AI tùy tiện chọn mô hình LLM phức tạp, tôi đã định hướng lại giải pháp theo mô hình Hybrid tối ưu chi phí và độ tin cậy:
  * **Predictive ML (XGBoost/LightGBM):** Dự báo nhu cầu khách theo cụm giờ/vị trí.
  * **Optimization Algorithm (Operations Research / Linear Programming):** Giải bài toán phân bổ slot sạc tối ưu cân bằng tải trạm.
  * **Template / Rule Engine:** Gửi thông báo ưu đãi và điều hướng tài xế (thay vì để LLM tự do sinh văn bản có thể bị hallucinate giá cước).

---

## 4. 🧠 Bài học kinh nghiệm cá nhân (Reflection & Takeaways)

1. **AI là một "Gia tốc kế" (Multiplier), không phải người thay thế tư duy kỹ sư:** AI giúp tôi hoàn thành khối lượng tài liệu và sơ đồ trong 30 phút thay vì mất nửa ngày, nhưng giá trị cốt lõi (logic vận hành xe điện, ranh giới an toàn, sự thấu cảm với tài xế) hoàn toàn phải đến từ sự can thiệp của con người.
2. **Nguy cơ tiềm ẩn của việc "tin tưởng mù quáng":** Nếu không đọc kỹ và phát hiện lỗi copy nhầm bảng Problem Statement, toàn bộ bài báo cáo sẽ biến thành một sản phẩm râu ông nọ cắm cằm bà kia.
3. **Tư duy Guardrail-First trong AI cho Công nghiệp:** Khi làm AI cho các hệ thống vật lý như xe điện và lưới trạm sạc, ranh giới an toàn (Safety Boundary) quan trọng hơn độ thông minh của thuật toán. Một thuật toán tối ưu 99% nhưng để 1% xe chết máy trên cầu vào giờ cao điểm là một thảm họa vận hành.