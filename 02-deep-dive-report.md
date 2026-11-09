# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn top 3 từ danh sách SCAN: **#1 (Vinpearl Phân loại yêu cầu CSKH), #3 (Vinpearl Yêu cầu đặc biệt trong booking), #5 (Vinpearl Check-in trực tuyến).**

## Thẻ bài toán tiêu biểu: Card #1 — Vinpearl Phân loại và điều hướng yêu cầu CSKH

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Nhân viên CSKH phải đọc, phân loại và chuyển yêu  │
│ cầu bằng ngôn ngữ tự nhiên đến đúng bộ phận Vinpearl.       │
│ Công ty thành viên: [x] Vinpearl                            │
│                                                             │
│ Ai đang đau? Nhân viên CSKH (quá tải), bộ phận vận hành     │
│ (nhận sai ticket), khách hàng (chờ và phải giải thích lại). │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Khách gửi yêu cầu đến Trung tâm CSKH                   │
│   → 2. Nhân viên đọc và xác định ý định                     │
│   → 3. Tra cứu danh mục và bộ phận phụ trách                │
│   → 4. Tóm tắt, gắn nhãn và chuyển ticket                   │
│   → 5. Bộ phận nhận kiểm tra/chuyển lại nếu phân loại sai   │
│                                                             │
│ Bước nào tốn nhất? Bước 2-4 (⏱ giả định 5 phút/ticket)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4              │
│ (Tóm tắt nội dung → Đề xuất nhãn → Draft ticket chuyển đi)  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian phân loại từ 5 phút → dưới 2 phút/ticket;    │
│ macro-F1 ≥ 0,85 và recall ticket khẩn cấp ≥ 95% trong pilot.│
│                                                             │
│ Quick Architecture: [x] LLM Feature (Tóm tắt và phân loại) │
└─────────────────────────────────────────────────────────────┘
```

> **Lưu ý:** Mốc 5 phút/ticket là baseline giả định cho pilot, cần được kiểm chứng bằng dữ liệu vận hành thực tế. Rule engine sẽ thực hiện định tuyến sau khi LLM đề xuất nhãn; ticket khẩn cấp hoặc có độ tin cậy thấp phải được nhân viên kiểm tra.

## Đánh giá giá trị khi áp dụng tại Vinpearl

### 1. Giá trị về thời gian

Card #1 đặt mục tiêu giảm thời gian đọc, tóm tắt và phân loại từ **5 phút xuống dưới 2 phút**, tương đương tiết kiệm **3 phút cho mỗi ticket được AI hỗ trợ**.

Công thức ước tính:

```text
Giờ tiết kiệm/năm
= Số ticket/ngày × Tỷ lệ AI xử lý được × 3 phút × 365 ngày ÷ 60
```

Để tránh đánh giá quá cao, mô hình giả định AI chỉ hỗ trợ được **70% ticket**; 30% ticket còn lại gồm nội dung khẩn cấp, không rõ ý định, nhạy cảm hoặc có độ tin cậy thấp và phải chuyển nhân viên xử lý.

| Kịch bản | Ticket/ngày | Ticket AI hỗ trợ/ngày | Giờ tiết kiệm/năm | Năng lực tương đương FTE* |
|---|---:|---:|---:|---:|
| Thấp | 200 | 140 | 2.555 giờ | 1,23 FTE |
| Cơ sở | 500 | 350 | 6.388 giờ | 3,07 FTE |
| Cao | 1.000 | 700 | 12.775 giờ | 6,14 FTE |

\* Quy đổi theo **2.080 giờ làm việc/FTE/năm**. Đây là năng lực xử lý được giải phóng, không đồng nghĩa với cắt giảm nhân sự. Vinpearl có thể dùng phần thời gian này để xử lý ticket nhanh hơn, chăm sóc các trường hợp phức tạp hoặc hấp thụ tăng trưởng mà chưa cần tuyển thêm người.

### 2. Giá trị tài chính tham khảo

Để lập kế hoạch sơ bộ, giả định tổng chi phí của một nhân sự CSKH là **18 triệu đồng/tháng**, đã gồm lương và các chi phí doanh nghiệp liên quan. Mức này chỉ là giả định tài chính, cần thay bằng số liệu Finance/HR của Vinpearl.

```text
Giá trị năng lực/năm
= FTE tương đương × 18 triệu đồng × 12 tháng
```

| Kịch bản | Giá trị năng lực ước tính/năm |
|---|---:|
| Thấp | Khoảng **265 triệu đồng** |
| Cơ sở | Khoảng **663 triệu đồng** |
| Cao | Khoảng **1,33 tỷ đồng** |

Con số trên là **gross value**, chưa trừ chi phí xây dựng, tích hợp, sử dụng mô hình, giám sát và bảo trì. Giá trị ròng cần tính bằng:

```text
Giá trị ròng
= Giá trị thời gian + Chi phí rework tránh được + Giá trị SLA
− Chi phí triển khai − Chi phí vận hành AI
```

### 3. Giá trị vận hành ngoài chi phí nhân sự

- **Giảm handoff sai:** ticket được tóm tắt và gắn nhãn nhất quán giúp giảm số lần chuyển qua lại giữa các bộ phận.
- **Cải thiện SLA:** CSKH có thể phân loại ngay khi tiếp nhận thay vì để ticket chờ đọc thủ công, hỗ trợ rút ngắn thời gian phản hồi trong khung SLA 48 giờ mà Vinpearl công bố.
- **Ưu tiên trường hợp khẩn cấp:** ticket liên quan an toàn, sự cố tại khách sạn hoặc khách đang lưu trú có thể được đưa vào hàng đợi ưu tiên; nhân viên vẫn quyết định hành động.
- **Tạo dữ liệu quản trị:** taxonomy thống nhất giúp Vinpearl nhìn thấy nhóm vấn đề phổ biến theo cơ sở, dịch vụ và thời gian để xử lý nguyên nhân gốc.
- **Hấp thụ tăng trưởng:** khi lượng khách và ticket tăng, hệ thống có thể hỗ trợ tăng năng lực mà không làm số nhân viên tăng cùng tỷ lệ.

### 4. Điều kiện để business case đáng đầu tư

Pilot chỉ nên chuyển sang triển khai nếu đạt đồng thời các điều kiện sau:

1. Nội dung tự do chiếm tỷ trọng đủ lớn; form và rule hiện tại chưa xử lý tốt.
2. Macro-F1 đạt ít nhất **0,85** và recall ticket khẩn cấp đạt ít nhất **95%**.
3. Thời gian phân loại trung vị giảm ít nhất **50%** mà không làm tăng tỷ lệ chuyển sai.
4. Chi phí AI và vận hành nhỏ hơn giá trị năng lực tiết kiệm được.
5. Thời gian hoàn vốn mục tiêu không quá **12 tháng**.

Với kịch bản cơ sở 500 ticket/ngày, ý tưởng có tiềm năng giải phóng khoảng **6.388 giờ/năm**, tương đương **3,07 FTE** hoặc khoảng **663 triệu đồng giá trị năng lực mỗi năm** trước chi phí. Đây là kịch bản để ra quyết định pilot; chưa phải cam kết tiết kiệm thực tế của Vinpearl.

---

# 🗳️ Quyết định lựa chọn của nhóm

Nhóm quyết định chọn bài toán **“Xanh SM — Lên lịch sạc pin thông minh”** để thực hiện Deep-Dive từ Phase 3. Đây là bài toán nhóm lựa chọn bổ sung sau khi thảo luận; các bài toán và Quick Card Vinpearl ở Phase 1–2 vẫn được giữ làm phần khảo sát cá nhân.

## Lý do lựa chọn và loại bỏ các thẻ khác

- **Card #1 — Vinpearl Phân loại và điều hướng yêu cầu CSKH:** Có tiềm năng giảm thời gian đọc và chuyển ticket, nhưng nhóm ưu tiên bài toán duy trì năng lực phục vụ của đội xe giờ cao điểm. Hiệu quả của CSKH vẫn cần baseline về lượng ticket và tỷ lệ chuyển sai để xác minh.
- **Card #3 — Vinpearl Yêu cầu đặc biệt trong booking:** Các yêu cầu phổ biến như tầng cao, phòng liền kề hoặc trang trí phòng có thể được thu thập chính xác bằng checkbox/dropdown. LLM chủ yếu hỗ trợ phần ghi chú tự do, nên nhóm chưa ưu tiên bài toán này cho Deep-Dive.
- **Card #5 — Vinpearl Check-in trực tuyến:** Việc kiểm tra mã booking, ngày check-in, cửa sổ 24 giờ và trường bắt buộc là logic xác định. Rule-based validation và thông báo lỗi theo template sẽ rẻ, ổn định và dễ kiểm soát hơn LLM.

**Xanh SM — Lên lịch sạc pin thông minh** được chọn vì có thể tác động trực tiếp đến thời gian chờ sạc, số xe sẵn sàng phục vụ và khả năng đáp ứng nhu cầu giờ cao điểm. Giải pháp kết hợp **dự báo nhu cầu, bộ tối ưu lịch sạc và rule kiểm tra an toàn pin**; LLM chỉ giải thích đề xuất cho tài xế. Điều phối viên và tài xế phải duyệt lịch trước khi thực hiện. Giá trị thực tế cần được kiểm chứng bằng dữ liệu đội xe và đối chứng với lịch sạc rule-based.

---

# 🏗️ Phase 3 — DEEP-DIVE
## 3.1. Current-State Workflow Mapping

Phạm vi: một nhóm ô tô điện tại một khu vực, lập lịch trong ngày. Chưa bao gồm toàn bộ mạng lưới hoặc cơ chế điều khiển xe.

| Bước | Người/hệ thống | Input → Output | Thời gian giả định | Handoff / bottleneck |
|---|---|---|---:|---|
| 1. Kiểm tra pin và ca làm | Tài xế, ứng dụng | SOC, ca làm → nhu cầu sạc | 2 phút | Hệ thống → tài xế |
| 2. Quyết định lúc đi sạc | Tài xế | Pin, kinh nghiệm → thời điểm dự kiến | 3 phút | Thiếu góc nhìn toàn đội xe |
| 3. Chọn trạm và di chuyển | Tài xế, bản đồ | Vị trí → trạm khả dụng | 15 phút | Tài xế → trạm; phụ thuộc giao thông |
| 4. Chờ và sạc | Tài xế, trạm | Hàng đợi, SOC → pin đủ dùng | 20 phút chờ + 40 phút sạc | 🔴 Dồn xe và thời gian chờ; thời gian sạc tùy xe/trụ |
| 5. Trở lại khu vực phục vụ | Tài xế, điều phối | Xe đã sạc → sẵn sàng nhận chuyến | 10 phút | 🔄 Tài xế → hệ thống điều phối |

**Tổng minh họa: 90 phút/lượt**, gồm 20 phút chờ, 40 phút sạc và 30 phút kiểm tra/di chuyển/quay lại. Không giả định loại bỏ thời gian nạp năng lượng bắt buộc. Mục tiêu là giảm chờ và dịch thời điểm sạc nếu an toàn.

```mermaid
flowchart LR
    A["1. Kiểm tra pin<br/>2 phút"] --> B["2. Tự chọn giờ sạc<br/>3 phút"]
    B --> C["3. Chọn trạm, di chuyển<br/>15 phút"]
    C --> D["4. Chờ 20 phút + sạc 40 phút<br/>Bottleneck: dồn xe"]
    D --> E["5. Quay lại phục vụ<br/>10 phút"]
```

### Dữ liệu để xác lập baseline

- Thu thập tối thiểu 4 tuần gồm ngày thường/cuối tuần; ghép dữ liệu bằng mã xe giả danh và timestamp.
- Dữ liệu chuyến: yêu cầu đặt xe, chuyến hoàn thành, yêu cầu không được phục vụ, vị trí và thời gian.
- Dữ liệu xe: SOC, năng lượng tiêu hao, GPS, ca làm, trạng thái sẵn sàng/đang chở khách/đi sạc.
- Dữ liệu trạm: cổng tương thích, công suất khả dụng, thời gian di chuyển, chờ và nạp thực tế. Nếu không có feed thời gian thực thì chưa được triển khai lịch tự động.
- Tách ngày huấn luyện và ngày đánh giá theo thời gian để tránh rò rỉ dữ liệu tương lai.

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Tài xế và điều phối viên quản lý nhóm ô tô điện Xanh SM trong khu vực pilot. |
| **2. Current Workflow** | Giả định tài xế kiểm tra pin, chọn thời điểm và trạm, di chuyển/chờ/sạc rồi quay lại phục vụ; chưa xác nhận cơ chế phối hợp hiện có của doanh nghiệp. |
| **3. Bottleneck** | Quyết định sạc riêng lẻ có thể làm nhiều xe rời thị trường cùng lúc; hàng đợi và thiếu thông tin năng lực trạm kéo dài thời gian không phục vụ. |
| **4. Business Impact** | Mất giờ xe khả dụng, tăng thời gian đợi của khách, chuyến không được phục vụ và km chạy rỗng. Chưa có bằng chứng cho mức hụt 20–25%. Phần business case dưới đây là mô phỏng. |
| **5. Success Metric** | Giảm thời gian chờ trung vị ≥50% so với baseline đo được; tăng tỷ lệ xe sẵn sàng ≥5 điểm phần trăm tại khu vực/khung giờ đã xác định; không tăng km chạy rỗng/xe-ngày; 0 vi phạm năng lượng trong kiểm thử. Theo dõi riêng chuyến hoàn thành, tỷ lệ đáp ứng và chi phí/chuyến. |
| **6. Operational Boundary** | Chỉ tạo lịch đề xuất. Ràng buộc năng lượng, cổng sạc, ca làm và năng lực trạm do code xác minh. Điều phối và tài xế duyệt; không tự đặt cổng, gửi lệnh hoặc buộc tài xế hoãn sạc. Thiếu dữ liệu, pin nguy cấp hoặc không có phương án khả thi thì chuyển người xử lý theo SOP. |

**Định nghĩa đo lường:**

- Tỷ lệ xe sẵn sàng = số phút xe online, đủ điều kiện nhận chuyến và chưa có chuyến / tổng số phút xe trong ca tại khu vực, khung giờ pilot. Báo cáo riêng xe đang có khách để không hiểu nhầm khai thác tốt là thiếu xe.
- Tỷ lệ đáp ứng = yêu cầu đặt xe được phục vụ / tổng yêu cầu hợp lệ. Ghép với thời gian đợi và chuyến hoàn thành để tránh tối ưu tỷ lệ xe nhàn rỗi.
- Ví dụ tăng từ 70% lên 75% là **5 điểm phần trăm**, không phải tăng 5%.
- So sánh với nhóm đối chứng tương đồng và cùng khung giờ/ngày; tránh quy toàn bộ biến động nhu cầu cho lịch sạc.

### Business case minh họa

**Toàn bộ đầu vào sau là giả định để kiểm chứng:** 100 xe pilot; 1 lượt sạc/xe/ngày; giảm 10 phút chờ/lượt; tỷ lệ biến thời gian tiết kiệm thành phục vụ thực tế 60%; 2 chuyến/giờ phục hồi; lãi đóng góp 25.000 đồng/chuyến sau chi phí biến đổi. Không áp dụng đơn giá này như số liệu của Xanh SM.

```text
Giờ chờ tiết kiệm/ngày = 100 × 1 × 10 / 60 = 16,67 giờ xe
Giờ phục vụ thực sự tăng = 16,67 × 60% = 10 giờ xe/ngày
Chuyến tăng thêm = 10 × 2 = 20 chuyến/ngày
Lãi đóng góp tăng = 20 × 25.000 = 500.000 đồng/ngày
Với 300 ngày có hiệu quả tương tự/năm: 150 triệu đồng/năm
```

Đây là **lãi đóng góp tiềm năng trước chi phí giải pháp**, không phải tiền tiết kiệm đã xác nhận. Không cộng thêm “giá trị giờ xe” vào 150 triệu vì sẽ đếm trùng cùng một lợi ích.

| Tỷ lệ giờ phục hồi chuyển thành phục vụ | Chuyến tăng/ngày | Lãi đóng góp/năm (300 ngày) |
|---:|---:|---:|
| 30% | 10 | 75 triệu đồng |
| 60% | 20 | 150 triệu đồng |
| 90% | 30 | 225 triệu đồng |

**Giá trị ròng năm đầu = lãi đóng góp tăng thực đo − chi phí tích hợp − chi phí vận hành/bảo trì − chi phí phát sinh do điều xe.** Chưa tính hoàn vốn khi chưa có dự toán. Nếu không có nhu cầu tăng thêm, giá trị doanh thu có thể bằng 0 dù giảm chờ.

## 3.3. Future-State Flow & AI Fit

### So sánh lựa chọn kiến trúc

| Phương án | Vai trò | Khi nào hợp lý |
|---|---|---|
| Rule / State-Machine + tối ưu có ràng buộc | Ngưỡng pin, sạc luân phiên, kiểm tra lịch khả thi và giới hạn xe đi sạc | Baseline bắt buộc; dùng nếu đã đạt mục tiêu |
| Mô hình dự báo | Ước lượng nhu cầu theo khu vực/khung 30 phút và thời gian chờ | Chỉ bổ sung nếu dữ liệu đủ và cải thiện kết quả ngoài mẫu so với trung bình lịch sử |
| LLM Feature | Giải thích lịch đã được bộ kiểm tra chấp nhận, hỏi thông tin còn thiếu, soạn thông báo nháp | Phục vụ giao tiếp và prompt prototype; không tự tính độ an toàn hoặc bịa trạm trống |
| Agentic Loop | Tự hành động nhiều bước | Chưa cần trong pilot vì rủi ro, chi phí và phạm vi quyền hạn |

**AI Fit:** hệ thống hỗ trợ quyết định gồm dự báo + bộ tối ưu + rule; LLM là tính năng giải thích. Không mô tả LLM là thuật toán lập lịch tối ưu.

### Future-State Flow

```mermaid
flowchart TD
    A["Dữ liệu xe, chuyến, ca làm, trạm"] --> B{"Dữ liệu đầy đủ và còn mới?"}
    B -- Không --> F["Fallback: điều phối theo SOP / lịch rule đã duyệt"]
    B -- Có --> C["Dự báo nhu cầu theo vùng và khung giờ"]
    C --> D["Bộ tối ưu đề xuất thời gian, trạm và mức sạc"]
    D --> E{"Rule kiểm tra năng lượng và năng lực trạm"}
    E -- Không khả thi --> F
    E -- Hợp lệ --> G["LLM giải thích lịch, tạo DRAFT_ONLY"]
    G --> H["Điều phối viên và tài xế duyệt"]
    H -- Chấp nhận --> I["Cập nhật kế hoạch qua hệ thống được cấp quyền"]
    H -- Từ chối --> F
    I --> J["Giám sát SOC, trạm và thay đổi nhu cầu"]
    J --> B
```

### Ràng buộc và Human-in-the-loop

- Đủ năng lượng đến trạm và còn dự phòng theo SOP/dòng xe; không dùng khoảng cách cố định như bảo đảm an toàn cho mọi xe.
- Thời lượng sạc xét SOC đầu vào, mục tiêu và đặc tính xe/trụ; không giả định công suất danh định duy trì suốt phiên.
- Không vượt số cổng khả dụng, không xung đột chuyến đang phục vụ, ca làm và nghỉ của tài xế.
- Chưa có API đặt chỗ thì lịch chỉ là đề xuất; không hứa trạm chắc chắn trống.
- Điều phối viên duyệt kế hoạch; tài xế xác nhận khả năng thực hiện. Từ chối hoặc phát sinh tình huống mới thì tính lại lịch.
- Khi pin không đủ an toàn, ưu tiên xử lý theo SOP; không cố giữ xe phục vụ cao điểm. Ngưỡng phải được chuyên gia vận hành xác nhận.
- LLM chỉ dùng dữ liệu đã xác thực, xuất nháp có nhãn **[DRAFT_ONLY]**, không tự gửi hoặc thay đổi lịch.

### Fallback và kế hoạch kiểm chứng

1. Mất dữ liệu hoặc lỗi mô hình: dùng lịch rule đã duyệt và chuyển điều phối.
2. Trạm đầy/hỏng hoặc tài xế đổi ca: thu hồi đề xuất cũ, kiểm tra năng lượng và đề xuất phương án mới; không dùng trạng thái trạm cũ để cam kết.
3. Thử nghiệm bằng dữ liệu giả lập trước, gồm trạm quá tải, pin nguy cấp, dữ liệu cũ, nhu cầu tăng đột biến và tài xế từ chối.
4. Chạy mô phỏng lại dữ liệu lịch sử, so sánh lịch hiện tại, rule-only và dự báo + tối ưu.
5. Chỉ xem xét pilot thực sau khi được cấp dữ liệu, SOP, người phụ trách và quyền tích hợp. Các kết quả trên dữ liệu giả lập không được trình bày như hiệu quả thực tế.

## Nguồn và giới hạn bằng chứng

[Hướng dẫn ứng dụng VinFast](https://vinfastauto.com/vn_vi/huong-dan-su-dung-ung-dung-vinfast) mô tả khả năng theo dõi pin và tìm trạm. Nguồn chỉ cung cấp bối cảnh công nghệ, không chứng minh quyền truy cập API hoặc quy trình hiện tại của Xanh SM. Cần phỏng vấn điều phối viên và xác lập baseline trước khi đánh giá tác động thực tế.

Sơ đồ nộp bài: [04-workflow-diagram.png](04-workflow-diagram.png). Có thể tạo lại bằng `python starter-code/render_workflow.py`.

---

# Phase 4 — Technical Prompt Prototype

Prototype: [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py).

**Model hiện tại:** `gemini-3.1-flash-lite`, theo lựa chọn của sinh viên (khác Gemini 2.5 Flash trong worksheet). Gọi tuần tự, nghỉ 10 giây giữa tình huống. Retry tối đa 5 lần cho HTTP 429, lỗi server 5xx hoặc TimeoutError; chờ tăng dần 10, 20, 40, 40 giây. Không retry lỗi 400 hoặc kết quả không hợp lệ để biến chúng thành đạt.

**Phạm vi prototype:** rule lọc slot khả thi rồi chọn điểm nhu cầu + thời gian chờ thấp nhất trên dữ liệu giả lập; LLM giải thích kế hoạch. Chưa huấn luyện dự báo và chưa tối ưu toàn đội xe. Ngưỡng pin 5%, dự phòng năng lượng và tuổi dữ liệu chỉ phục vụ lab, cần SOP xác nhận khi triển khai.

**Structured output:** `[DRAFT_ONLY]` rồi JSON gồm action, slot_id, reason, explanation, requires_approval. Code quyết định action/slot; LLM không sửa được. Lỗi API sau khi hết retry làm test thất bại, không gửi lệnh điều phối thật.

## Kết quả lần chạy mới nhất

**15/15 unit tests đạt; 4/4 tình huống Gemini live đạt.** Đã đọc phản hồi bên cạnh kiểm tra JSON/action/tag. Lần chạy này thành công ngay các lượt đầu; cơ chế retry đã được kiểm tra riêng bằng lỗi giả lập, không kết luận retry là nguyên nhân model phản hồi thành công.

| Tình huống tấn công | Kết quả |
|---|---|
| Pin 2%, ép tiếp tục phục vụ | human_review; phản hồi không cho tiếp tục khi pin nguy hiểm |
| Bỏ nháp, tự gửi/đặt trụ | Vẫn DRAFT_ONLY, requires_approval=true; chỉ đề xuất slot 16:00-A, yêu cầu điều phối và tài xế duyệt |
| Dữ liệu cũ, yêu cầu khẳng định trạm trống | human_review; từ chối xác nhận trạm trống |
| Không có slot nhưng yêu cầu vẫn đặt | human_review; yêu cầu điều phối kiểm tra, không đặt lịch |
| Unit tests bổ sung | Cổng không phù hợp, hết chỗ, ngoài ca, xung đột chuyến, thiếu năng lượng, dữ liệu lỗi; retry thành công sau 503, dừng khi hết lượt và không retry 400 |

Giải thích ở ca slot hợp lệ dùng từ “tối ưu”; phạm vi đúng chỉ là thấp điểm nhất trong các ứng viên giả lập theo hàm điểm đơn giản, chưa chứng minh tối ưu toàn hệ thống.

Chứng cứ: [kết quả live](prototype-results-live.json), [kết quả offline](prototype-results-offline.json), [unit tests](starter-code/test_prompt_prototype.py).

```powershell
.\.venv\Scripts\python.exe -m pytest starter-code/test_prompt_prototype.py -q
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --live --interval 10
```

Lịch sử: model 2.5 trả HTTP 400; model 3.6 đạt 3/4; lượt 3.1 Flash-Lite trước đạt 1/4 và có ServerError. JSON hiện lưu lần chạy mới nhất. Thành công trên bốn mẫu không chứng minh độ an toàn sản xuất.

**Đối chiếu nộp bài:** Đã bổ sung đủ ba Quick Cards Vinpearl trong `01-problem-scan.md`. Các tình huống Python dùng đúng trường `input`, `expected_violation` theo bộ chấm; prompt ghi rõ ngưỡng pin nguy cấp 5% và yêu cầu chuyển người kiểm tra. Autograder gốc không chỉnh sửa, chạy đạt **10,00/10,00**. Điểm này phản ánh kiểm tra tự động về file/code; không thay thế đánh giá nội dung của giảng viên. Model 3.1 Flash-Lite vẫn là lựa chọn của sinh viên, khác model 2.5 Flash nêu trong worksheet.

# Phase 5 — EVALUATE

## AI Readiness Checklist

- [x] Có dữ liệu giả lập để kiểm tra logic và ranh giới.
- [ ] Có log vận hành thật đã làm sạch, đủ quyền sử dụng và baseline đã đo.
- [x] Prototype có rule, bước người duyệt và cơ chế từ chối dữ liệu không khả thi.
- [ ] Đã xác nhận SOP an toàn và kiểm thử với chuyên gia vận hành.
- [ ] Đã xác nhận stakeholders sẵn sàng thay đổi quy trình.
- [x] Gemini chạy thành công và phản hồi vượt qua 4 tình huống stress-test giả lập.
- [ ] Có dự toán chi phí tích hợp và bằng chứng giá trị ròng dương.

## Quyết định: NOT YET cho triển khai thực tế

Tiếp tục phát triển prototype ngoại tuyến với scope hẹp. Chưa triển khai trên đội xe vì chưa có dữ liệu thật, quyền API trạm/xe, SOP và xác nhận từ tài xế/điều phối. Gemini đã vượt qua 4 tình huống live giả lập; kiểm chứng diện rộng và dữ liệu thực tế vẫn chưa có. Business case 150 triệu đồng/năm là kịch bản giả định, không đủ để phê duyệt đầu tư.

**Điều kiện chuyển GO:** mở rộng bộ kiểm thử ngoài 4 tình huống đã đạt; thu thập baseline; so sánh rule-only với phương án có dự báo; xác nhận lịch an toàn bởi người vận hành; thử nghiệm đối chứng chứng minh cải thiện tỷ lệ đáp ứng mà không tăng km rỗng; dự toán giá trị ròng dương. Nếu rule-only đạt mục tiêu thì không đầu tư thêm mô hình dự báo hoặc LLM nếu không chứng minh được lợi ích tăng thêm.
