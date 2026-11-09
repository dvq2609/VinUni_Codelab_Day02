# Phase 1 — SCAN: Cơ hội ứng dụng AI tại Vinpearl

**Sinh viên:** Phạm Quang Tuấn  
**Nhánh cá nhân:** `phamquangtuan`  
**Ngày nghiên cứu:** 09/11/2026

## Cách thực hiện

Phần SCAN sử dụng bốn lenses trong worksheet để tìm các điểm nghẽn vận hành tại Vinpearl:

1. **Lặp lại (Repetitive):** tác vụ được thực hiện nhiều lần mỗi ngày.
2. **Tốn thời gian (Time-consuming):** tác vụ cần nhân viên đọc, kiểm tra hoặc tổng hợp nhiều thông tin.
3. **AI có thể tốt hơn (AI-upgrade):** tác vụ cần hiểu ngôn ngữ tự nhiên hoặc cá nhân hóa phản hồi.
4. **Pain từ người khác (Stakeholder Pain):** điểm nghẽn khiến khách hàng hoặc nhân viên gặp khó khăn.

Các vấn đề bên dưới là **giả thuyết nghiên cứu**, được xây dựng từ quy trình và chính sách công khai của Vinpearl. Cần phỏng vấn người vận hành và lấy dữ liệu mẫu trước khi kết luận doanh nghiệp đang xử lý thủ công hoặc xác lập metric chính thức.

## Danh sách bài toán của tôi

|   # | Subsidiary (VinFast/Xanh SM...) | Lens                                  | Mô tả ngắn bài toán                                                                                                                                            |
| --: | ------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Vinpearl                        | Lặp lại (Repetitive)                  | Phân loại yêu cầu gửi đến CSKH và chuyển đúng bộ phận phụ trách như đặt phòng, thanh toán, hoàn tiền, VinWonders hoặc dịch vụ tại khách sạn.                   |
|   2 | Vinpearl                        | Tốn thời gian (Time-consuming)        | Trích xuất thông tin từ yêu cầu đặt phòng khách đoàn/sự kiện gồm số phòng, ngày lưu trú, gói phòng, tiệc, vận chuyển và dịch vụ bổ sung để nhân viên kiểm tra. |
|   3 | Vinpearl                        | AI có thể tốt hơn (AI-upgrade)        | Đọc ghi chú đặt phòng để nhận diện yêu cầu đặc biệt như phòng tầng cao, phòng liền kề hoặc trang trí phòng và tạo checklist cho nhân viên xác nhận.            |
|   4 | Vinpearl                        | Pain từ người khác (Stakeholder Pain) | Hỗ trợ khách tra cứu tiến độ hoàn tiền, giải thích các bước còn thiếu và chuyển trường hợp quá hạn cho nhân viên phụ trách.                                    |
|   5 | Vinpearl                        | Tốn thời gian (Time-consuming)        | Kiểm tra trước thông tin check-in trực tuyến, phát hiện dữ liệu còn thiếu hoặc không khớp và hướng dẫn khách bổ sung trước khi đến khách sạn.                  |

## Ghi chú nghiên cứu cho từng bài toán

### 1. Phân loại và điều hướng yêu cầu CSKH

**Actor:** Nhân viên Trung tâm Chăm sóc Khách hàng và nhân viên các bộ phận liên quan.

**Quy trình giả định cần kiểm chứng:**

1. Khách gửi câu hỏi hoặc yêu cầu qua kênh hỗ trợ.
2. Nhân viên đọc nội dung và xác định loại yêu cầu.
3. Nhân viên kiểm tra thông tin ban đầu.
4. Yêu cầu được chuyển đến bộ phận liên quan.
5. CSKH tổng hợp kết quả và phản hồi khách.

**Bottleneck giả định:** Nội dung khách gửi là văn bản tự do, có thể chứa nhiều vấn đề trong cùng một yêu cầu. Việc phân loại sai làm phát sinh thêm handoff và kéo dài thời gian phản hồi.

**Cơ hội AI:** LLM tóm tắt nội dung, nhận diện ý định và đề xuất nhãn; rule-based router dùng nhãn, cơ sở lưu trú và loại dịch vụ để chuyển ticket. Trường hợp không chắc chắn phải chuyển nhân viên kiểm tra.

**Bằng chứng công khai:** FAQ Vinpearl cho biết CSKH tiếp nhận thông tin, kiểm tra với các bộ phận liên quan và phản hồi trong vòng 48 giờ làm việc.

**Nguồn:** [Câu hỏi thường gặp — Vinpearl](https://vinpearl.com/vi/faqs)

**Dữ liệu cần thu thập:** Số ticket/ngày, danh mục ticket hiện có, số lần chuyển bộ phận, thời gian phản hồi và tỷ lệ phân loại sai.

### 2. Trích xuất yêu cầu đặt phòng khách đoàn và sự kiện

**Actor:** Nhân viên kinh doanh đoàn, nhân viên đặt phòng và nhân viên tổ chức sự kiện.

**Quy trình giả định cần kiểm chứng:**

1. Khách hoặc đối tác gửi yêu cầu đặt dịch vụ.
2. Nhân viên đọc nội dung và xác định quy mô đoàn.
3. Nhân viên trích xuất ngày, số phòng, loại phòng và gói dịch vụ.
4. Các yêu cầu tiệc, sự kiện, golf hoặc vận chuyển được chuyển đến bộ phận tương ứng.
5. Nhân viên kiểm tra khả năng cung cấp và soạn xác nhận/báo giá.

**Bottleneck giả định:** Một yêu cầu đoàn có thể chứa nhiều loại dịch vụ và nhiều điều kiện, khiến nhân viên phải nhập lại dữ liệu vào biểu mẫu hoặc hệ thống nội bộ.

**Cơ hội AI:** LLM chuyển nội dung email hoặc tài liệu thành dữ liệu có cấu trúc. Rule engine kiểm tra trường bắt buộc, xác định khách lẻ/khách đoàn và cảnh báo thông tin còn thiếu. Nhân viên vẫn phải kiểm tra quỹ phòng và phê duyệt báo giá.

**Bằng chứng công khai:** Điều khoản Vinpearl định nghĩa khách đoàn là yêu cầu từ 10 phòng/đêm hoặc 5 biệt thự/đêm trở lên và có thể bao gồm lưu trú, tiệc, sự kiện, golf cùng các dịch vụ khác.

**Nguồn:** [Điều khoản chung về đặt dịch vụ — Vinpearl](https://booking.vinpearl.com/vi/dieu-khoan/dieu-khoan-chung)

**Dữ liệu cần thu thập:** Số yêu cầu đoàn/tháng, số trường dữ liệu cần nhập, thời gian chuẩn bị báo giá, tỷ lệ email thiếu thông tin và số lần phải hỏi lại khách.

### 3. Trích xuất yêu cầu đặc biệt trong đặt phòng

**Actor:** Nhân viên đặt phòng, lễ tân, bộ phận buồng phòng và khách lưu trú.

**Quy trình giả định cần kiểm chứng:**

1. Khách ghi chú hoặc gọi CSKH về yêu cầu đặc biệt.
2. Nhân viên đọc và chuẩn hóa yêu cầu.
3. Nhân viên xác định bộ phận cần phối hợp.
4. Bộ phận vận hành kiểm tra khả năng đáp ứng.
5. Nhân viên phản hồi hoặc ghi chú vào booking.

**Bottleneck giả định:** Yêu cầu được diễn đạt theo nhiều cách và có thể bị bỏ sót khi chuyển giữa CSKH, đặt phòng, lễ tân và buồng phòng.

**Cơ hội AI:** LLM nhận diện loại yêu cầu, thời điểm, đối tượng và chi tiết còn thiếu; hệ thống tạo checklist cho nhân viên. AI không được tự cam kết với khách vì khả năng đáp ứng phụ thuộc tình trạng thực tế.

**Bằng chứng công khai:** Vinpearl nêu các yêu cầu như phòng tầng cao, phòng liền kề và trang trí phòng chỉ được cung cấp tùy khả năng sẵn có của khách sạn tại thời điểm nhận phòng.

**Nguồn:** [Câu hỏi thường gặp — Vinpearl](https://vinpearl.com/vi/faqs)

**Dữ liệu cần thu thập:** Số booking có yêu cầu đặc biệt, tỷ lệ yêu cầu bị bỏ sót, thời gian xác nhận và các loại yêu cầu phổ biến.

### 4. Hỗ trợ tra cứu tiến độ hoàn tiền

**Actor:** Khách hàng, nhân viên CSKH, kế toán và bộ phận thanh toán.

**Quy trình giả định cần kiểm chứng:**

1. Khách gửi yêu cầu hoàn tiền.
2. Nhân viên kiểm tra booking, chính sách và chứng từ.
3. Hồ sơ được chuyển đến bộ phận phê duyệt/thanh toán.
4. Khách liên hệ lại để hỏi trạng thái.
5. CSKH kiểm tra nhiều hệ thống hoặc hỏi bộ phận liên quan rồi phản hồi.

**Bottleneck giả định:** Khách không biết hồ sơ đang ở bước nào hoặc còn thiếu thông tin gì, dẫn đến các câu hỏi trạng thái lặp lại và tăng tải cho CSKH.

**Cơ hội AI:** Trợ lý truy xuất trạng thái đã được hệ thống xác nhận, giải thích bước tiếp theo bằng ngôn ngữ dễ hiểu và tạo ticket escalation khi vượt SLA. AI không được tự phê duyệt hoàn tiền hoặc hứa ngày nhận tiền.

**Bằng chứng công khai:** FAQ Vinpearl công bố thời gian hoàn tiền trung bình khoảng 30–45 ngày kể từ khi nhận yêu cầu của khách hàng.

**Nguồn:** [Câu hỏi thường gặp — Vinpearl](https://vinpearl.com/vi/faqs)

**Dữ liệu cần thu thập:** Số yêu cầu hỏi trạng thái, thời gian xử lý theo từng loại thanh toán, nguyên nhân chậm, tỷ lệ hồ sơ thiếu và số trường hợp vượt 45 ngày.

### 5. Kiểm tra trước thông tin check-in trực tuyến

**Actor:** Khách lưu trú, lễ tân và nhân viên hỗ trợ khách hàng.

**Quy trình giả định cần kiểm chứng:**

1. Khách mở chức năng check-in trực tuyến.
2. Khách nhập hoặc chọn mã hành trình, mã đặt phòng và ngày check-in.
3. Hệ thống đối chiếu booking.
4. Khách bổ sung thông tin lưu trú theo yêu cầu.
5. Lễ tân kiểm tra lại khi khách đến khách sạn.

**Bottleneck giả định:** Khách có thể nhập sai mã, thiếu thông tin hoặc không hiểu nguyên nhân check-in thất bại; lễ tân vẫn phải rà soát dữ liệu không đầy đủ khi khách đến.

**Cơ hội AI:** Trợ lý giải thích lỗi theo ngữ cảnh, hướng dẫn khách bổ sung đúng trường và tạo bản tóm tắt các mục cần lễ tân kiểm tra. Việc đối chiếu mã đặt phòng và điều kiện check-in phải dùng rule/API xác định, không giao cho LLM suy đoán.

**Bằng chứng công khai:** Vinpearl cung cấp check-in trực tuyến trên MyVinpearl; khách không đặt phòng qua ứng dụng phải nhập mã hành trình, mã đặt phòng và ngày check-in. Tính năng chỉ mở trong vòng 24 giờ trước ngày nhận phòng.

**Nguồn:** [Hướng dẫn check-in trực tuyến — Vinpearl](https://vinpearl.com/vi/check-in-truc-tuyen-du-lich-an-toan-tiet-kiem-thoi-gian)

**Dữ liệu cần thu thập:** Tỷ lệ khách dùng check-in online, tỷ lệ thất bại, lỗi phổ biến, thời gian lễ tân kiểm tra và thời gian chờ trung bình tại quầy.

## Đánh giá ban đầu

| Bài toán                       | Giá trị tiềm năng | Khả năng làm prototype | Rủi ro khi AI sai | Nhận định                                               |
| ------------------------------ | ----------------- | ---------------------- | ----------------- | ------------------------------------------------------- |
| Phân loại yêu cầu CSKH         | Cao               | Rất cao                | Trung bình        | Phù hợp mô hình hybrid: LLM phân loại, rule định tuyến  |
| Yêu cầu khách đoàn/sự kiện     | Cao               | Cao                    | Cao               | Có giá trị nhưng cần nhiều dữ liệu và tích hợp hệ thống |
| Yêu cầu đặc biệt trong booking | Trung bình–cao    | Rất cao                | Trung bình        | Scope rõ, phù hợp làm Quick Card                        |
| Tra cứu hoàn tiền              | Cao               | Cao                    | Cao               | Phải có dữ liệu trạng thái đáng tin cậy và HITL         |
| Kiểm tra trước check-in        | Cao               | Cao                    | Trung bình        | Rule/API xử lý logic; AI chỉ giải thích và hỗ trợ       |

## Kết luận Phase 1

Ba bài toán phù hợp nhất để đưa sang Phase 2 — QUICK-ASSESS là:

1. **Phân loại và điều hướng yêu cầu CSKH:** tần suất tiềm năng cao, đầu vào là ngôn ngữ tự nhiên và có thể đo bằng độ chính xác phân loại, số lần chuyển sai và thời gian phản hồi.
2. **Trích xuất yêu cầu đặc biệt trong đặt phòng:** phạm vi hẹp, dễ tạo dữ liệu thử nghiệm và có ranh giới vận hành rõ ràng.
3. **Kiểm tra trước thông tin check-in trực tuyến:** tác động trực tiếp đến trải nghiệm khách; có thể kết hợp rule/API với AI hỗ trợ giải thích.

Các metric số sẽ được đặt ở Phase 2 dưới dạng **mục tiêu thử nghiệm**, sau đó cần xác nhận lại bằng baseline từ dữ liệu vận hành thực tế.

---

# Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn **#1, #3 và #5** từ bảng SCAN Vinpearl. Đây là ba card khảo sát cá nhân; phần nhóm chọn Xanh SM từ Phase 3 trong báo cáo. Workflow và thời gian sau là giả định cần xác minh, metric là mục tiêu thử nghiệm.

## Quick Problem Card #1 — Phân loại và điều hướng yêu cầu CSKH

| Trường theo worksheet | Nội dung |
|---|---|
| Bài toán (1 câu) | Đọc, phân loại và chuyển yêu cầu bằng ngôn ngữ tự nhiên đến đúng bộ phận Vinpearl. |
| Công ty thành viên | Vinpearl |
| Actor | Nhân viên CSKH, bộ phận nhận ticket và khách hàng. |
| Workflow thủ công (5 bước) | Nhận yêu cầu → đọc và xác định ý định → tra bộ phận phụ trách → tóm tắt/chuyển ticket → kiểm tra và chuyển lại nếu sai. |
| Bước tốn thời gian/lỗi nhất | Bước 2–4, giả định 5 phút/ticket. |
| AI hỗ trợ ở đâu? | Bước 2–4: tóm tắt, đề xuất nhãn; rule router chọn bộ phận, nhân viên kiểm tra khi không chắc chắn. |
| Metric có số | Pilot ≥100 ticket; giảm thời gian từ 5 xuống dưới 2 phút/ticket nếu baseline được xác nhận; macro-F1 ≥0,85; recall ticket khẩn cấp ≥95%. |
| Quick Architecture | [ ] No AI · [ ] Rule · [x] LLM Feature · [ ] Agent; rule hỗ trợ định tuyến. |
| Operational Boundary | Chỉ tạo đề xuất; không tự đóng ticket, hứa SLA hoặc gửi phản hồi cuối cùng. |

**Phản biện:** Chưa chứng minh phân loại là bottleneck; accuracy chung có thể che lỗi ở nhóm hiếm; form có category và rule router có thể đủ. Cần baseline và đối chứng rule-only trước khi đầu tư.

## Quick Problem Card #3 — Yêu cầu đặc biệt trong booking

| Trường theo worksheet | Nội dung |
|---|---|
| Bài toán (1 câu) | Trích xuất yêu cầu đặc biệt trong ghi chú booking và tạo checklist cho nhân viên xác nhận. |
| Công ty thành viên | Vinpearl |
| Actor | Nhân viên đặt phòng, lễ tân, buồng phòng và khách lưu trú. |
| Workflow thủ công (5 bước) | Khách ghi chú/gọi CSKH → nhân viên đọc → chuẩn hóa yêu cầu → chuyển bộ phận kiểm tra → ghi vào booking và phản hồi. |
| Bước tốn thời gian/lỗi nhất | Bước 2–4, giả định 7 phút/booking có yêu cầu. |
| AI hỗ trợ ở đâu? | Bước 2–3: trích xuất loại yêu cầu, ngày áp dụng và dữ kiện thiếu; rule tạo checklist cho người duyệt. |
| Metric có số | Pilot ≥100 ghi chú; recall ≥95%, precision ≥90%; giảm thời gian tạo checklist ≥50% so với baseline thực đo; 0 cam kết tự động về khả năng đáp ứng. |
| Quick Architecture | [ ] No AI · [ ] Rule · [x] LLM Feature · [ ] Agent; kết hợp form/rule cho yêu cầu phổ biến. |
| Operational Boundary | Không tự xác nhận còn phòng hoặc cung cấp dịch vụ; nhân viên xác minh khả năng đáp ứng trước khi phản hồi. |

**Phản biện:** Chưa biết volume và tỷ lệ bỏ sót; tiết kiệm thời gian chưa đồng nghĩa giảm khiếu nại; checkbox/dropdown có thể tốt hơn LLM. Chỉ dùng LLM cho ghi chú tự do, đa ý hoặc đa ngôn ngữ.

## Quick Problem Card #5 — Kiểm tra trước thông tin check-in trực tuyến

| Trường theo worksheet | Nội dung |
|---|---|
| Bài toán (1 câu) | Phát hiện dữ liệu check-in thiếu hoặc không khớp và hướng dẫn khách sửa trước khi đến quầy. |
| Công ty thành viên | Vinpearl |
| Actor | Khách gặp lỗi và lễ tân phải rà soát/nhập lại dữ liệu. |
| Workflow hiện tại (5 bước, có bước hệ thống) | Khách nhập mã/ngày → hệ thống đối chiếu booking → khách bổ sung thông tin → hệ thống/nhân viên phát hiện lỗi → khách sửa và lễ tân xác minh. |
| Bước tốn thời gian/lỗi nhất | Bước 3–5, giả định 8 phút/trường hợp lỗi. |
| AI hỗ trợ ở đâu? | Bước 4–5: LLM chỉ diễn giải mã lỗi đã được rule/API xác định; template tĩnh là phương án đối chứng. |
| Metric có số | Pilot ≥100 phiên lỗi; ≥80% khách hoàn thành bước tiếp theo; giảm lượt cần CSKH ≥30%; 100% kết luận trạng thái booking lấy từ rule/API. |
| Quick Architecture | [ ] No AI · [x] Rule / State-Machine · [ ] LLM · [ ] Agent; LLM giải thích là tùy chọn nếu có lợi ích tăng thêm. |
| Operational Boundary | Không suy đoán trạng thái booking, không thay đổi thông tin hoặc xác nhận check-in thay nhân viên. |

**Phản biện:** Bài toán validation có logic xác định; mức “hiểu hướng dẫn” cần đo bằng hành vi hoàn tất; template theo mã lỗi thường rẻ và ổn định hơn LLM. Chỉ bổ sung AI nếu A/B test chứng minh cải thiện.

