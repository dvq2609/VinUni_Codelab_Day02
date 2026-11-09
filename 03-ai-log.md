# Phase 6 — AI Log & Reflection

**Sinh viên:** Phạm Quang Tuấn  
**Chủ đề Deep-Dive:** Xanh SM — Lên lịch sạc pin thông minh

## 1. Cách tôi sử dụng AI trong bài lab

Trong bài lab này, tôi sử dụng AI như một đối tác trao đổi để nghiên cứu, phản biện và hỗ trợ triển khai. Tôi chủ động lựa chọn hướng bài, yêu cầu AI bám sát worksheet và kiểm tra lại khi kết quả chưa đúng ý hoặc vượt phạm vi đã thống nhất.

Ban đầu, tôi chọn Vinpearl cho phần SCAN và yêu cầu nghiên cứu năm bài toán vận hành có căn cứ. Sau đó, tôi yêu cầu phát triển Quick Problem Cards và phản biện dưới góc nhìn CFO cùng Trưởng phòng Vận hành. Mục đích là xem giải pháp có tạo giá trị cho doanh nghiệp hay chỉ thêm AI vào một quy trình vốn có thể giải quyết bằng rule.

Đối với phần làm nhóm từ Phase 3, tôi đề xuất bài toán **Xanh SM — Lên lịch sạc pin thông minh để tránh nhiều xe cùng đi sạc trong giờ nhu cầu cao**. Đây là định hướng do tôi lựa chọn. AI hỗ trợ phát triển ý tưởng thành workflow, Problem Statement sáu trường, metric, kiến trúc và prototype.

## 2. Những quyết định và đóng góp của tôi

### Xác định bài toán và phạm vi

Tôi không chỉ dừng ở yêu cầu tạo nội dung chung. Tôi yêu cầu tìm năm vấn đề cụ thể, chọn hướng phù hợp, trình bày card theo đúng mẫu của giảng viên và đánh giá lợi ích về thời gian, tiền bạc, giá trị vận hành.

### Yêu cầu phản biện giá trị doanh nghiệp

Tôi đặt câu hỏi liệu Card #1 có thực sự là lựa chọn tốt nhất và giải pháp có thể tiết kiệm bao nhiêu thời gian, tiền bạc. Qua đó, tôi yêu cầu AI làm rõ các giả định và cơ sở tính toán thay vì chỉ mô tả tính năng.

Với bài toán Xanh SM, giá trị cần hướng tới là giảm thời gian chờ sạc, duy trì năng lực phục vụ và tăng số chuyến được đáp ứng khi có nhu cầu. Tôi nhận thấy không thể quy toàn bộ thời gian tiết kiệm thành doanh thu: còn phụ thuộc vị trí xe, lượng khách và khả năng chuyển thời gian đó thành chuyến thực tế.

### Kiểm tra mức độ hoàn thành

Tôi yêu cầu đối chiếu bài với các yêu cầu của lab, hỏi phần còn thiếu và điều chỉnh nội dung nhiều lần. Những trao đổi này giúp nhận diện khác biệt giữa có đủ file, có prototype chạy ngoại tuyến và thực sự kiểm chứng được phản hồi Gemini.

## 3. AI hỗ trợ tôi ở những phần nào?

| Phần việc | Vai trò của AI | Vai trò của tôi |
|---|---|---|
| Thiết lập môi trường | Hỗ trợ tạo virtual environment, cài thư viện và đọc .env | Yêu cầu chuẩn bị môi trường cho dự án |
| SCAN và Quick Cards | Tổng hợp nguồn, đề xuất cấu trúc và phát triển nội dung | Chọn Vinpearl, yêu cầu năm bài toán và chỉnh card theo mẫu |
| Lựa chọn Deep-Dive | Phân tích và phát triển phương án | Đề xuất Xanh SM — Lên lịch sạc pin thông minh |
| Phản biện | Đưa ra góc nhìn CFO/vận hành, so sánh rule với AI | Yêu cầu đánh giá tính hợp lý và giá trị doanh nghiệp |
| Báo cáo và sơ đồ | Hỗ trợ diễn đạt workflow, metric, ranh giới, fallback | Xác định phạm vi từng phase và yêu cầu chỉnh khi sai |
| Prototype và kiểm thử | Hỗ trợ viết code, kiểm thử và lưu kết quả | Định hướng bài toán và yêu cầu hoàn thiện, rà soát yêu cầu còn thiếu |

Phần code và chạy kiểm thử có AI hỗ trợ thực hiện trong workspace; tôi không trình bày đây là toàn bộ mã do mình tự viết độc lập. Đóng góp của tôi nằm ở việc xác định vấn đề, định hướng giải pháp, phản biện, kiểm soát phạm vi và rà soát sản phẩm.

## 4. AI đã sai hoặc cần được kiểm soát ở đâu?

### Sai phạm vi chỉnh sửa

AI đã diễn giải việc chọn Xanh SM thành thay đổi cả Phase 1–2, trong khi tôi muốn giữ những phần Vinpearl đã làm. Tôi yêu cầu khôi phục nội dung cũ và áp dụng lựa chọn mới từ Phase 3.

Bài học của tôi là cần chỉ rõ **đổi phần nào, giữ phần nào và kết quả mong đợi** khi yêu cầu AI sửa tài liệu nhiều giai đoạn.

### Số liệu giả định có thể bị hiểu thành dữ kiện

Khung 17h–19h và mức thiếu 20–25% xe là giả thuyết ban đầu tôi đưa ra, chưa được xác nhận bằng dữ liệu vận hành của Xanh SM. Tương tự, mức giá trị năng lực 663 triệu đồng/năm cho Vinpearl và lãi đóng góp 150 triệu đồng/năm cho kịch bản Xanh SM là các phép tính theo giả định.

Báo cáo cần giữ rõ nhãn giả định, công thức và dữ liệu cần thu thập. Không thể dùng các con số này như bằng chứng doanh nghiệp đã tiết kiệm được tiền.

### Phân biệt đúng vai trò của LLM

Lên lịch sạc là bài toán có ràng buộc về năng lượng, ca làm và năng lực trạm. Qua quá trình trao đổi, tôi hiểu rằng LLM không nên tự quyết định xe có đủ pin hoặc cam kết trạm đang trống.

Kiến trúc phù hợp là dùng rule để kiểm tra tính khả thi, thuật toán để lựa chọn lịch và mô hình dự báo khi có đủ dữ liệu. LLM hỗ trợ giải thích đề xuất; điều phối viên và tài xế vẫn phải duyệt.

### Không đồng nhất kiểm thử offline với thành công của mô hình

Các kiểm thử rule đạt không chứng minh Gemini tuân thủ prompt. Muốn kết luận về ranh giới của mô hình, cần có phản hồi thật và kiểm tra nội dung, kể cả khi JSON đúng định dạng và có thẻ nháp.

## 5. Cách tôi điều chỉnh yêu cầu với AI

Các yêu cầu tôi đã sử dụng trong quá trình làm bài gồm:

- Nghiên cứu Phase 1, chọn năm bài toán hợp lý và tạo file theo worksheet.
- Đóng vai CFO và Trưởng vận hành để chỉ ra ba điểm yếu về logic, metric và lý do rule-based có thể tốt hơn AI.
- Chỉnh Phase 2 giống mẫu card của giảng viên, chỉ trình bày một card tiêu biểu trong báo cáo.
- Đánh giá lợi ích về thời gian, tiền bạc và giá trị đối với doanh nghiệp.
- Giữ nội dung Vinpearl ở Phase 1–2 và dùng Xanh SM từ Phase 3 trở đi.
- Rà soát các yêu cầu còn thiếu trước khi nộp.

Tôi nhận thấy các yêu cầu cụ thể về phạm vi và tiêu chí giúp kết quả tốt hơn yêu cầu chung như “làm hoàn chỉnh”. Việc hỏi lại, phản biện và yêu cầu sửa là một phần của quá trình làm bài, không chỉ là bước chỉnh văn phong.

## 6. Kết quả thực tế và giới hạn

Theo yêu cầu của tôi, model được đổi sang `gemini-3.1-flash-lite`, các lượt gọi giãn 10 giây. Tôi chỉ ra thiếu sót khi API lỗi tạm thời mà chưa có retry. Code sau đó bổ sung retry tối đa 5 lần với thời gian chờ tăng dần; không retry lỗi request 400 hoặc phản hồi sai để biến thành đạt.

| Hạng mục | Kết quả lần chạy mới nhất |
|---|---|
| Unit tests gồm logic và retry | 15/15 đạt |
| Gemini live | 4/4 đạt; JSON/action/tag và nội dung phản hồi được kiểm tra |
| Pin nguy cấp / dữ liệu cũ / không có slot | Chuyển human_review, không tự điều phối |
| Ép bỏ nháp và tự gửi | Giữ nháp, yêu cầu duyệt |
| Dữ liệu và hiệu quả vận hành thật | Chưa có; chưa đo |
| Mô hình dự báo | Chưa huấn luyện; điểm nhu cầu giả lập |

Lần chạy mới thành công ngay lượt đầu ở cả bốn tình huống. Retry được kiểm thử bằng lỗi giả lập; không khẳng định retry là nguyên nhân đã khắc phục lỗi server. Các lượt trước từng gặp HTTP 400 hoặc ServerError được ghi nhận là lịch sử thử nghiệm.

Kết quả mới nhất lưu tại [prototype-results-live.json](prototype-results-live.json); kiểm thử offline tại [prototype-results-offline.json](prototype-results-offline.json). Bốn tình huống thành công chưa chứng minh an toàn sản xuất. LLM có dùng từ “tối ưu” cho lịch đề xuất, cần hiểu đúng là tốt nhất trong tập ứng viên giả lập theo hàm điểm đơn giản.

## 7. Reflection cá nhân

Trong lượt rà soát nộp bài, tôi yêu cầu kiểm tra toàn bộ thư mục và sửa các mục còn thiếu. Ba Quick Cards Vinpearl được bổ sung trong file SCAN; các trường test và quy tắc pin trong prompt được chỉnh khớp bộ chấm. Autograder gốc đạt 10,00/10,00 và unit tests đạt 15/15. Điểm tự động chưa thay thế đánh giá nội dung hoặc việc giảng viên xác nhận dùng model khác worksheet.

Qua bài lab, tôi hiểu rõ hơn cách đi từ một ý tưởng AI đến một bài toán vận hành có phạm vi và tiêu chí đo lường. Một ý tưởng hấp dẫn cần được kiểm tra bằng quy trình hiện tại, dữ liệu, phương án rule-based đối chứng và giá trị tăng thêm.

Điểm tôi đã làm tốt là chủ động đưa ra hướng bài toán, yêu cầu phân tích lợi ích doanh nghiệp và phát hiện khi AI chỉnh sai phạm vi. Tôi cũng học được cách yêu cầu AI giải thích các giả định, thay vì chỉ chấp nhận một báo cáo có nhiều con số hoặc thuật ngữ.

Điểm tôi cần tiếp tục cải thiện là xác minh dữ liệu thực tế và hiểu sâu hơn phần triển khai để có thể tự giải thích từng ràng buộc, metric và kết quả kiểm thử. Bước tiếp theo là mở rộng tình huống tấn công, kiểm tra dữ liệu thật và đối chiếu lịch đề xuất với phương án rule-only.

Quyết định **NOT YET cho triển khai thực tế** phản ánh giới hạn bằng chứng hiện tại. Tôi vẫn tiếp tục phát triển prototype với scope hẹp, nhưng chỉ có thể đánh giá hiệu quả ứng dụng khi có dữ liệu và xác nhận từ người vận hành.
