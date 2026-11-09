# 01 — Problem Scan & Quick Problem Cards

> **Trạng thái:** Bản cá nhân để thảo luận; các vấn đề dưới đây là giả thuyết lấy từ `03-inspiration-kit.md`, chưa được xác nhận với đơn vị vận hành. Workflow mô tả là luồng dự kiến để kiểm chứng. Các con số trong mục tiêu là **ngưỡng thử nghiệm đề xuất**, không phải baseline hay kết quả đo. Cần thay bằng dữ liệu/ý kiến đã xác minh trước khi xem là kết luận.
>
> **Sinh viên:** Bùi Ngọc Hùng
> **MSSV:** 2A202603770
> **Vai trò:** Thành viên nhóm
> **Branch:** `2a202603770`

## Phase 1 — SCAN

Dùng bốn lenses trong worksheet để lập danh sách cơ hội ban đầu. Mỗi dòng cần được xác minh với người thực hiện quy trình hoặc nguồn dữ liệu phù hợp.

| # | Subsidiary | Lens | Vấn đề/bottleneck giả thuyết cần xác minh |
|---:|---|---|---|
| 1 | Vinhomes | Repetitive | Phản ánh của cư dân (ví dụ: mất nước, hỏng đèn, tiếng ồn) có thể cần được phân loại và chuyển đến đúng ban quản lý/tòa nhà. Cần xác minh kênh tiếp nhận, quy tắc routing và tỷ lệ chuyển sai hiện tại. |
| 2 | Vinpearl | Stakeholder Pain | Review của khách có thể chứa phàn nàn khẩn cấp như phòng chưa sạch hoặc trải nghiệm dịch vụ không tốt; quản lý cần phát hiện và chuyển xử lý. Cần xác minh nguồn review được phép dùng, thời gian phát hiện hiện nay và quy trình escalation. |
| 3 | VinFast | Repetitive | Đối chiếu dữ liệu phiên sạc từ đối tác với hóa đơn có thể gồm nhiều bản ghi lặp lại và ngoại lệ cần kiểm tra thủ công. Cần xác minh hệ thống nguồn, khối lượng, quy tắc đối soát và tỷ lệ mismatch. |
| 4 | Vinmec | Time-consuming | Soạn bản nháp tóm tắt xuất viện từ hồ sơ bệnh án có thể tốn thời gian của nhân viên y tế. Đây là quy trình nhạy cảm: cần xác minh người dùng, dữ liệu được phép xử lý và yêu cầu bác sĩ kiểm duyệt; AI không chẩn đoán hay tự phê duyệt nội dung. |
| 5 | Xanh SM | Stakeholder Pain | Lý do hủy chuyến trong cuộc gọi/ghi chú có thể khó tổng hợp thành nhóm nguyên nhân để đội vận hành nhận diện vấn đề lặp lại. Cần xác minh khả năng truy cập bản ghi, đồng thuận/quyền riêng tư, taxonomy và cách đo độ chính xác. |

## Phase 2 — QUICK-ASSESS

Ba cards dưới đây là lựa chọn ban đầu để mang ra thảo luận. Việc chọn này **không phải quyết định của nhóm**. Mục tiêu định lượng là đề xuất để thiết kế pilot sau khi có baseline; không khẳng định hiện trạng hoặc kết quả đạt được.

### Quick Problem Card #1 — Phân loại phản ánh cư dân Vinhomes

- **Bài toán (1 câu):** Hỗ trợ phân loại phản ánh cư dân theo chủ đề và đề xuất đơn vị tiếp nhận để nhân viên rà soát, xử lý.
- **Công ty thành viên:** Vinhomes.
- **Ai đang đau (Actor):** Giả thuyết: nhân viên tiếp nhận/ban quản lý cần sàng lọc phản ánh; cư dân bị ảnh hưởng nếu yêu cầu chuyển sai hoặc chậm. Cần xác nhận vai trò thực tế.
- **Workflow hiện tại (giả thuyết, cần walkthrough với nhân viên):**
  1. Cư dân gửi phản ánh qua kênh được chỉ định.
  2. Nhân viên đọc nội dung và xác định chủ đề, mức độ ưu tiên.
  3. Nhân viên tra quy tắc hoặc tìm đơn vị phụ trách.
  4. Nhân viên chuyển yêu cầu và theo dõi trạng thái.
- **Bottleneck cần đo:** Bước đọc, phân loại và chọn nơi chuyển tiếp; chưa có thời gian xử lý hay tỷ lệ chuyển sai đã xác minh.
- **AI có thể hỗ trợ:** Đề xuất nhãn/chủ đề và queue nhận xử lý từ nội dung đã được phép sử dụng; trường hợp mơ hồ hoặc nhạy cảm chuyển cho người xử lý. Không tự kết luận tranh chấp, phí hay trách nhiệm pháp lý.
- **Metric đề xuất cho pilot:** Đạt **≥90% precision** trên nhãn/queue tự động đề xuất ở tập kiểm thử do nhân viên gán nhãn; đồng thời theo dõi tỷ lệ chuyển sai và thời gian xử lý trung vị so với baseline. Mốc 90% là ngưỡng mục tiêu cần nhóm xác nhận, không phải kết quả hiện tại.
- **Quick Architecture:** **LLM Feature** để phân loại ngôn ngữ tự do, kết hợp **Rule** cho taxonomy/điều kiện routing cố định; nhân viên duyệt các trường hợp thấp tự tin.
- **Thông tin cần hỏi nhóm/đơn vị:** Có taxonomy và lịch sử phản ánh đã ẩn danh không? Ai chịu trách nhiệm duyệt? Quy tắc ưu tiên/đơn vị nhận đã được ghi nhận ở đâu?

### Quick Problem Card #2 — Phát hiện review cần escalation tại Vinpearl

- **Bài toán (1 câu):** Tóm tắt và gắn cờ review có dấu hiệu cần quản lý khách sạn xem xét, để nhân viên quyết định có escalation hay không.
- **Công ty thành viên:** Vinpearl.
- **Ai đang đau (Actor):** Giả thuyết: nhân viên chăm sóc khách hàng hoặc quản lý khách sạn theo dõi phản hồi; khách bị ảnh hưởng nếu phản ánh khẩn cấp không được nhìn thấy kịp thời. Cần xác minh quy trình và nguồn review.
- **Workflow hiện tại (giả thuyết, cần xác minh):**
  1. Review xuất hiện trên một kênh được phép theo dõi.
  2. Nhân viên đọc review và xác định cơ sở/chủ đề.
  3. Nhân viên đánh giá mức độ cần xử lý và chuyển quản lý liên quan.
  4. Nhân viên/manager phản hồi hoặc ghi nhận hướng xử lý.
- **Bottleneck cần đo:** Khâu theo dõi nhiều review và nhận diện sớm nội dung cần escalation; chưa có baseline về số lượng, thời gian hay bỏ sót.
- **AI có thể hỗ trợ:** Tóm tắt, gắn nhãn chủ đề và đề xuất mức ưu tiên; nhân viên xác minh nội dung và quyết định escalation. Không tự đăng phản hồi công khai hoặc cam kết bồi thường.
- **Metric đề xuất cho pilot:** **≥90% recall** đối với nhóm review được nhân viên đánh dấu cần escalation trong tập kiểm thử đã gán nhãn; theo dõi thêm precision để kiểm soát cảnh báo sai. Mốc 90% là mục tiêu pilot đề xuất, không phải kết quả đo.
- **Quick Architecture:** **LLM Feature** để tóm tắt/nhận diện chủ đề; **Rule** cho từ khóa hoặc tiêu chí escalation đã được quản lý phê duyệt; người phụ trách quyết định hành động.
- **Thông tin cần hỏi nhóm/đơn vị:** Kênh nào được phép thu thập? Có SLA/escalation policy và dữ liệu nhãn không? Ai duyệt nội dung trước khi phản hồi khách?

### Quick Problem Card #3 — Đối chiếu hóa đơn sạc VinFast

- **Bài toán (1 câu):** Hỗ trợ đối chiếu bản ghi phiên sạc với hóa đơn đối tác và đưa các trường hợp lệch sang hàng đợi kiểm tra.
- **Công ty thành viên:** VinFast.
- **Ai đang đau (Actor):** Giả thuyết: nhân viên phụ trách đối soát/tài chính; cần xác nhận đơn vị và trách nhiệm cụ thể.
- **Workflow hiện tại (giả thuyết, cần walkthrough):**
  1. Nhận dữ liệu phiên sạc và hóa đơn từ các nguồn liên quan.
  2. Chuẩn hóa mã giao dịch, thời gian, địa điểm và số tiền.
  3. So khớp các trường theo quy tắc nghiệp vụ.
  4. Điều tra mismatch/thiếu dữ liệu và ghi nhận kết quả.
- **Bottleneck cần đo:** Chuẩn hóa và điều tra ngoại lệ; số lượng bản ghi, phút xử lý và tỷ lệ mismatch chưa được cung cấp.
- **AI có thể hỗ trợ:** Chỉ trích xuất trường từ tài liệu không đồng nhất hoặc tóm tắt lý do mismatch cho nhân viên. So khớp số tiền/mã giao dịch nên dùng **Rule-based**; AI không tự xác nhận thanh toán hay sửa sổ sách.
- **Metric đề xuất cho pilot:** Đạt **≥95% precision** khi trích xuất các trường cần thiết trên một tập mẫu được kiểm tra thủ công; báo cáo riêng tỷ lệ mismatch được phát hiện và tỷ lệ false positive. Mốc 95% là mục tiêu thử nghiệm cần xác nhận theo mức rủi ro.
- **Quick Architecture:** **Rule / State-Machine** cho so khớp chính xác; **LLM Feature** chỉ khi cần đọc tài liệu phi cấu trúc. Chưa có lý do để dùng Agent tự trị.
- **Thông tin cần hỏi nhóm/đơn vị:** Có bộ dữ liệu đối chiếu được phép dùng không? Khóa đối soát và dung sai đã thống nhất chưa? Ai phê duyệt điều chỉnh tài chính?

## Ghi chú lựa chọn và bước tiếp theo

Nhóm đã chọn **VinFast — đối soát phiên sạc và hóa đơn** làm chủ đề Deep-Dive; đây là Quick Problem Card #3. Hai thẻ còn lại là shortlist cá nhân, không phải lựa chọn Deep-Dive của nhóm. Các số liệu và workflow vẫn là giả thuyết cho tới khi được xác minh. Báo cáo Deep-Dive đề xuất **GO cho prototype mô phỏng offline**, nhưng chưa GO cho pilot trên dữ liệu vận hành thật trước khi xác nhận dữ liệu, quy trình, baseline, khóa ghép và dung sai.
