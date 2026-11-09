# 📝 Báo Cáo Nhật Ký Tương Tác AI (AI Log & Reflection)

> **Họ và tên Kỹ sư:** Nguyễn Thành Công 
> **Vai trò:** AI Product Engineer — **Vin Smart Future (Vingroup)**  
> **Dự án thực hiện:** Các bài toán được lựa chọn: AI Medical Documentation – Tự động hóa ghi chép bệnh án.

Appointment & Contact Center Automation – Tự động hóa đặt lịch và chăm sóc bệnh nhân.

Insurance Claim & Guarantee Processing – Tự động hóa xử lý hồ sơ bảo hiểm.

> **Hệ thống AI đồng hành:** ChatGPT (GPT-6)

---

1. 🤖 AI đã giúp gì trong quá trình làm việc? (What AI helped with)

Trong quá trình tìm kiếm và đánh giá các bài toán AI cho Vinmec, AI đóng vai trò như một Thought Partner (Cộng sự tư duy phản biện), Business Analyst và AI Solution Architect, hỗ trợ tôi thực hiện các công việc sau:

1.1. Phân tích bối cảnh và tìm kiếm pain point (Problem Discovery)

Áp dụng 4 Lenses (Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain) để rà soát các quy trình vận hành tiềm năng tại Vinmec.

Đề xuất và phân tích 5 bài toán: Appointment Automation, Medical Documentation, Insurance Processing, Critical Lab Notification và Discharge Coordination.

Nhận diện các điểm nghẽn trong quy trình khám ngoại trú, ghi chép bệnh án, xử lý bảo hiểm và phối hợp giữa các bộ phận.

Đối chiếu với quy trình công khai của Vinmec để tránh chỉ đưa ra những ý tưởng AI chung chung, thiếu bối cảnh doanh nghiệp.

1.2. Phân rã quy trình và xây dựng Quick Problem Cards

AI hỗ trợ chuyển các ý tưởng ban đầu thành 3 Quick Problem Cards có cấu trúc rõ ràng, bao gồm Actor, Current Workflow, Bottleneck, AI Intervention và Success Metrics.

Cụ thể:

Medical Documentation: Xác định bước nhập liệu và hoàn thiện bệnh án là điểm tiêu tốn thời gian của bác sĩ.

Contact Center: Xác định quy trình gọi điện xác nhận, nhắc lịch và xử lý yêu cầu đổi lịch là nhóm tác vụ lặp lại.

Insurance Processing: Xác định các bước đọc chứng từ, đối chiếu quyền lợi và bổ sung hồ sơ là các điểm có thể ứng dụng Document AI.

1.3. Đóng vai CFO/COO để phản biện tính khả thi

AI được yêu cầu đóng vai trò CFO và Trưởng phòng Vận hành nhằm tìm ra 3 điểm yếu chính trong cách lựa chọn bài toán AI:

Business Logic: Không phải công việc thủ công nào cũng là vấn đề kinh doanh đáng đầu tư.

Metric & ROI: Giảm thời gian xử lý không đồng nghĩa với việc doanh nghiệp tiết kiệm được tiền.

Technology Selection: Không nên mặc định sử dụng LLM hoặc Agent khi Rule-based Automation đã giải quyết tốt nghiệp vụ.

Qua đó, tôi nhận ra cần đánh giá bài toán theo giá trị kinh doanh thay vì chỉ đánh giá mức độ phù hợp về mặt công nghệ.

1.4. Định lượng hóa đóng góp kinh doanh (Business Case & ROI)

AI hỗ trợ xây dựng mô hình tài chính dự kiến cho cả 3 dự án, bao gồm CAPEX, OPEX, lợi ích tài chính, ROI và thời gian hoàn vốn trong 3 năm.

Dự án

Lợi ích ròng dự kiến/năm ổn định

ROI 3 năm

AI Medical Documentation

337 triệu VNĐ

6,9%

Contact Center Automation

306,8 triệu VNĐ

12,7%

Insurance Processing

164,96 triệu VNĐ

-4,6%

Các mô hình sử dụng giả định về quy mô triển khai, thời gian xử lý, tỷ lệ tự động hóa, chi phí nhân công và contribution margin. AI cũng giúp phân biệt công suất lao động được giải phóng với khoản tiết kiệm tiền mặt thực tế, tránh tính toàn bộ thời gian tiết kiệm thành doanh thu.

Kết quả phân tích giúp xác định Contact Center Automation là phương án có ROI dự kiến tốt nhất trong kịch bản cơ sở, Medical Documentation có giá trị chiến lược cao, còn Insurance Processing cần xác minh thêm khả năng thu hồi thất thoát claim.

2. ⚠️ AI trả lời sai / Ảo giác (Hallucination) ở đâu? (Where AI failed / hallucinated)

Trong quá trình làm việc, rủi ro lớn nhất không phải là AI tạo ra một thông tin hoàn toàn vô lý, mà là đưa ra những con số và kết luận có vẻ rất thuyết phục nhưng chưa được xác thực bằng dữ liệu vận hành thực tế của Vinmec.

2.1. Đưa ra số liệu giả định với độ chính xác có vẻ quá cao (False Precision)

Hiện tượng: Khi xây dựng business case, AI đưa ra các con số như 20.000 yêu cầu đặt lịch/tháng, 35% tỷ lệ tự động xử lý, 8% tỷ lệ no-show, 80.000 VNĐ chi phí nhân công/giờ và 250.000 VNĐ contribution margin/lượt khám.

Sai lệch: Đây là các giả định phục vụ mô hình tính toán, không phải dữ liệu nội bộ được Vinmec xác nhận. Tuy nhiên, khi trình bày dưới dạng bảng tài chính và công thức ROI, chúng dễ tạo cảm giác như kết quả thống kê thực tế.

Rủi ro: Nếu sử dụng trực tiếp để xin phê duyệt ngân sách, doanh nghiệp có thể đánh giá sai lợi ích đầu tư và thời gian hoàn vốn.

2.2. Áp dụng Benchmark quốc tế chưa đủ điều kiện (Benchmark Transfer Error)

Hiện tượng: AI sử dụng nghiên cứu về AI Medical Scribe tại các trung tâm y tế ở Mỹ, với benchmark tiết kiệm 16 phút ghi chép trên mỗi 8 giờ khám và tăng khoảng 0,49 lượt khám/bác sĩ/tuần.

Sai lệch tiềm ẩn: Chưa có bằng chứng cho thấy Vinmec có cùng quy trình khám, hệ thống EMR, khối lượng công việc hoặc mức độ trưởng thành công nghệ như các cơ sở trong nghiên cứu.

Rủi ro: Nếu áp dụng trực tiếp benchmark quốc tế cho Vinmec mà không hiệu chỉnh, dự báo năng suất và ROI có thể bị sai lệch đáng kể.

2.3. Đánh giá quá cao khả năng tạo ra giá trị tài chính (ROI Overestimation)

Hiện tượng: AI quy đổi thời gian tiết kiệm thành tiền thông qua một tỷ lệ 40% công suất lao động có thể chuyển thành tiết kiệm thực tế.

Sai lệch: Tỷ lệ 40% là giả định mô hình, chưa được chứng minh bằng kế hoạch giảm OT, tránh tuyển dụng hoặc tăng năng suất thực tế.

Rủi ro: Doanh nghiệp có thể nhầm lẫn giữa việc giải phóng 1.000 giờ công với việc thực sự tiết kiệm được chi phí tương ứng.

Một ví dụ khác là bài toán Insurance Processing: AI giả định có thể bảo toàn 0,25% tổng giá trị hồ sơ claim nhờ hạn chế thiếu hoặc sai chứng từ. Khoản lợi ích 240 triệu VNĐ/năm này chưa có dữ liệu audit chứng minh.

2.4. Nguy cơ tính trùng lợi ích giữa các chỉ số (Double Counting)

Hiện tượng: Ở bài toán Medical Documentation, AI vừa xác định thời gian nhập liệu được tiết kiệm, vừa dự báo số lượt khám tăng thêm.

Rủi ro: Nếu đồng thời quy đổi toàn bộ giờ công tiết kiệm thành tiền và ghi nhận toàn bộ lượt khám tăng thêm thành doanh thu, có thể tính trùng cùng một phần công suất bác sĩ.

Cách xử lý: Trong mô hình cuối cùng, thời gian tiết kiệm được báo cáo như công suất giải phóng, còn lợi ích tài chính được tính qua số lượt khám tăng thêm. Không cộng cả hai thành hai khoản lợi ích tiền tệ độc lập.

3. 🛠️ Tôi đã sửa Prompt, thiết lập Ranh giới (Boundary) ra sao để đạt kết quả chuẩn? (How I adjusted Prompts & Guardrails)

Sau khi nhận diện các điểm yếu, tôi thay đổi cách sử dụng AI theo hướng yêu cầu minh bạch dữ liệu, phản biện tài chính và lựa chọn công nghệ có căn cứ.

3.1. Kỹ thuật Prompting & Grounding lại ngữ cảnh

Tôi yêu cầu AI tuân thủ các nguyên tắc:

Phân loại nguồn dữ liệu: Mọi con số phải được ghi rõ là dữ liệu chính thức của Vinmec, Benchmark quốc tế, Giả định mô hình hay Target của PoC.

Không tự tạo dữ liệu nội bộ: Không được khẳng định số lượng cuộc gọi, thời gian xử lý hay tỷ lệ lỗi của Vinmec khi chưa có nguồn xác nhận.

Yêu cầu công khai công thức: Mỗi kết quả tài chính phải có công thức, đơn vị tính, giả định đầu vào và cách diễn giải.

Kiểm tra tính nhất quán: Không được cộng trùng giờ công tiết kiệm, doanh thu tăng thêm và các khoản lợi ích có cùng nguồn gốc.

3.2. Thiết lập ranh giới kinh doanh và vận hành (Business Guardrails)

Tôi đưa ra các yêu cầu bắt buộc cho 3 dự án:

Medical Documentation – Human-in-the-loop: AI chỉ được tạo bản nháp bệnh án, bác sĩ phải kiểm tra và xác nhận trước khi lưu chính thức. Không để LLM tự đưa ra chẩn đoán hoặc chỉ định điều trị độc lập.

Contact Center – Limited Agent Authority: AI được phép tư vấn thông tin hành chính, kiểm tra lịch trống và hỗ trợ xác nhận theo quyền được cấp. Các trường hợp liên quan đến tư vấn y tế, thông tin không chắc chắn hoặc yêu cầu ngoại lệ phải chuyển nhân viên phụ trách. Không tự ý thay đổi hoặc hủy lịch trái với xác nhận của bệnh nhân.

Insurance Processing – Human Approval: AI chỉ hỗ trợ trích xuất, đọc hiểu và đối chiếu chứng từ. Việc xác định quyền lợi, phê duyệt hoặc từ chối bảo lãnh phải tuân thủ hợp đồng, business rules và thẩm quyền của nhân viên có trách nhiệm.

3.3. Tái định hình kiến trúc AI Fit (Architecture Re-alignment)

Qua quá trình phản biện, tôi không lựa chọn LLM hay Agent một cách mặc định mà định hướng theo kiến trúc Hybrid:

AI Medical Documentation: Speech-to-Text + LLM + Rule Validation + Human Review. LLM hiểu hội thoại và tạo bản nháp, còn Rule Engine kiểm tra cấu trúc và trường dữ liệu bắt buộc.

Appointment Automation: Voice AI + LLM + Booking API + Rule-based Workflow. LLM xử lý hội thoại tự nhiên, còn hệ thống nghiệp vụ quản lý lịch, xác nhận trạng thái và kiểm soát quyền thực thi.

Insurance Processing: OCR/Document AI + LLM + Rule Engine + Human Approval. AI đọc hiểu tài liệu, Rule Engine đối chiếu điều kiện có cấu trúc và nhân viên xử lý các trường hợp ngoại lệ.

Nguyên tắc lựa chọn: Dùng AI cho dữ liệu phi cấu trúc và các tác vụ cần hiểu ngữ cảnh; dùng Rule-based Code cho logic nghiệp vụ xác định, kiểm tra và thực thi có kiểm soát.

4. 🧠 Bài học kinh nghiệm cá nhân (Reflection & Takeaways)

4.1. Tư duy AI-first không đồng nghĩa với việc mọi vấn đề đều cần AI

Trước quá trình phân tích, tôi có xu hướng tập trung vào việc tìm những quy trình có thể ứng dụng LLM hoặc Agent. Tuy nhiên, qua phản biện, tôi nhận ra một vấn đề vận hành có thể được giải quyết tốt hơn bằng SQL, API, Scheduler hoặc Rule Engine.

Năng lực quan trọng của AI Engineer không chỉ là lựa chọn model, mà còn là xác định đúng điểm mà AI tạo ra giá trị vượt trội so với phần mềm truyền thống.

4.2. Business Value quan trọng hơn Model Performance

Một hệ thống AI có độ chính xác cao không mặc định mang lại lợi ích kinh tế.

Qua việc xây dựng business case, tôi hiểu rằng cần đi từ Operational Metric đến Business Metric: giảm thời gian xử lý, giảm lỗi, tăng công suất và cuối cùng là chứng minh tác động đến chi phí hoặc contribution margin.

Đặc biệt, giờ công tiết kiệm chưa chắc là tiền mặt tiết kiệm được. Phải có phương án sử dụng lại công suất hoặc giảm chi phí thực tế thì mới có thể ghi nhận lợi ích tài chính.

4.3. Không được nhầm lẫn giữa Benchmark và dữ liệu doanh nghiệp

Benchmark quốc tế hữu ích để xây dựng giả thuyết và target ban đầu, nhưng không thể thay thế dữ liệu nội bộ.

Muốn đưa ra một business case có sức thuyết phục, tôi cần làm việc với các bộ phận vận hành để lấy baseline, xác định volume, thời gian xử lý, tỷ lệ lỗi và chi phí thực tế trước khi đưa ra cam kết ROI.

4.4. Tư duy Guardrail-first trong môi trường y tế

Vinmec là môi trường có dữ liệu sức khỏe nhạy cảm và các quy trình ảnh hưởng trực tiếp đến bệnh nhân. Do đó, hiệu quả AI phải đi cùng độ tin cậy, bảo mật, khả năng truy vết và cơ chế phê duyệt của con người.

Đặc biệt, không thể đánh đổi an toàn bệnh nhân lấy tỷ lệ tự động hóa cao hơn.

4.5. Kế hoạch hành động tiếp theo

Để chuyển từ đề xuất sang dự án có khả năng triển khai thực tế, tôi xác định các bước tiếp theo:

Data Discovery: Làm việc với Contact Center, đội ngũ bác sĩ và bộ phận bảo hiểm để thu thập dữ liệu vận hành thực tế.

Baseline Measurement: Đo thời gian xử lý, số lượng giao dịch, tỷ lệ sai sót và chi phí của từng quy trình trong ít nhất 4 tuần.

PoC Development: Ưu tiên Contact Center Automation để kiểm chứng khả năng tự động hóa và ROI; đồng thời nghiên cứu Medical Scribe về STT, LLM và tích hợp EMR.

Business Validation: So sánh kết quả trước và sau PoC, tính lại ROI theo dữ liệu thực tế và đánh giá chi phí vận hành dài hạn.

Tổng kết:

Thông qua quá trình tương tác với AI, tôi không chỉ xây dựng được 3 đề xuất AI cho Vinmec mà còn hiểu rõ hơn cách chuyển một pain point vận hành thành một business case có thể đánh giá và ra quyết định đầu tư.

Bài học lớn nhất là: Một dự án AI thành công không được đo bằng việc mô hình thông minh đến đâu, mà bằng giá trị kinh doanh có thể chứng minh được, mức độ an toàn khi vận hành và khả năng giải quyết đúng vấn đề của doanh nghiệp.