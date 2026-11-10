
🏗️ Phase 3 — DEEP-DIVE
## 3.1. Current-State Workflow
Quy trình Lên lịch sạc pin thông minh tránh trùng giờ cao điểm khách đặt xe:

**Quy trình quản lý và sạc pin thủ công hiện tại của tài xế Xanh SM:**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Theo dõi pin │     │ Xe báo pin   │     │ Tắt app nhận │     │ Di chuyển &  │
│ theo cảm tính│ ──→ │ yếu (<20%)   │ ──→ │ khách, tự tìm│ ──→ │ xếp hàng chờ │
│ & thói quen  │     │ ngẫu nhiên   │     │ trạm sạc gần │     │ sạc tại trạm │
│ Ai: Tài xế   │     │ Ai: Xe/Tài xế│     │ Ai: Tài xế   │     │ Ai: Tài xế   │
│ ⏱ Rải rác    │     │ ⏱ 1 phút     │     │ ⏱ 10 phút 🔴 │     │ ⏱ 45-60 ph 🔴│
│ In: Taplo %  │     │ In: Báo động │     │ In: App      │     │ In: Trạm sạc │
│ Out: Ước tính│     │ Out: Quyết định│   │ Out: Tọa độ  │     │ Out: Trụ sạc │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Cắm sạc & bỏ │
                                                               │ lỡ toàn bộ   │
                                                               │ giờ cao điểm │
                                                               │ Ai: Tài xế   │
                                                               │ ⏱ 45 phút    │
                                                               |              │
                                                               └──────────────┘
```

🔴 = Bottlenecks (Điểm nghẽn gây lãng phí thời gian và tổn thất doanh thu lớn nhất)  
⏱ **Tổng thời gian lãng phí/xe ngừng hoạt động (Downtime):** **100 – 115 phút/xe** (rơi trúng khung giờ cao điểm 17h00 – 19h30).

---

## 3.2. Problem Statement (6-field) 


| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Tài xế Xanh SM thuộc Trung tâm Điều vận Xanh SM. |
| **2. Current Workflow** | Nhìn pin taplo  ──> 2. Xe báo pin yếu bất ngờ ──> 3. Tắt app, tự mở map tìm trạm ──> 4. Xếp hàng chờ sạc tại trạm đông đúc ──> 5. Cắm sạc và lỡ toàn bộ khung giờ cao điểm khách đặt xe. |
| **3. Bottleneck** | Bước 3 & 4 (mất 100 – 115 phút/xe): tài xế phải tìm, chờ đợi xếp hàng để đến lượt sạc và đợi xe sạc đầy làm bỏ lỡ khoảng thời gian cao điểm |
| **4. Business Impact** | Khoảng **20% – 25%** tổng đội xe tại Hà Nội và TP.HCM bị vô hiệu hóa trong khung giờ vàng 17h00 – 19h00 do phải đi sạc hoặc xếp hàng chờ sạc. Mỗi xe mất từ 2 – 3 cuốc xe surge pricing (trung bình 70.000 – 100.000 VNĐ/cuốc). Với quy mô hàng nghìn xe của Xanh SM, ước tính gây thất thoát từ **600 – 840 triệu VNĐ/ngày** doanh thu tiềm năng |
| **5. Success Metric** | 1. **Giảm tỷ lệ xe sạc dồn giờ cao điểm:** Hạ từ **25% xuống dưới 8%** lượng xe sạc trong khung 17h00 – 19h00 (Supply Availability) 2. **Giảm thời gian chờ tại trạm sạc:** Rút ngắn thời gian xếp hàng từ **45–60 phút xuống dưới 10 phút** nhờ đặt trước slot sạc thông minh (Efficiency) 3. **Thu hồi doanh thu:** Thu hồi ước tính **~840 triệu VNĐ doanh thu/ngày** thất thoát trong giờ cao điểm (Revenue Impact) 4. **Tỷ lệ tuân thủ lịch sạc khuyến nghị (Driver Compliance Rate):** Đạt trên **85%** tài xế đồng ý sạc lệch đỉnh (Adoption). |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Dự báo nhu cầu đặt xe theo cụm giờ/khu vực; Đọc % pin và định vị xe qua Telemetry IoT; Phân tích tải trạm sạc V-GREEN; Đề xuất slot sạc lệch đỉnh (14h30–16h00 hoặc sau 19h30) kèm ưu đãi/voucher giảm giá sạc; Gợi ý ghép cuốc tiện đường về trạm sạc đã đặt slot. **CẤM:**• Không được tự ý ngắt app nhận khách hoặc ép buộc tài xế offline nếu tài xế chưa bấm xác nhận (Bắt buộc HITL).• Không được điều phối xe có pin dưới 15% nhận cuốc dài (>10km) gây nguy cơ chết máy cạn pin giữa đường.• Không được điều hướng tài xế đến trạm sạc không tương thích chuẩn sạc dòng xe hoặc trạm đang báo lỗi kỹ thuật/mất điện từ hệ thống V-GREEN. |

---


# 🏁 Phase 5 — EVALUATE: Đánh giá khả thi & Quyết định đầu tư

### 1. 📋 AI Readiness Checklist (Kiểm tra độ sẵn sàng của dự án):
* [x] **1. Dữ liệu mẫu & Logs sạch để huấn luyện/kiểm thử:**
  * **Telemetry IoT xe điện VinFast:** Luồng dữ liệu real-time từ ECU xe (% pin SoC, tốc độ tiêu thụ năng lượng kWh/km, GPS).
  * **Log lịch sử đặt xe Xanh SM:** Kho dữ liệu chuyến đi theo không gian & thời gian, hệ số nhân giá theo cụm giờ/khu vực.
  * **Dữ liệu mạng lưới trạm sạc V-GREEN:** API trạng thái trụ sạc real-time (số trụ trống, công suất, hàng chờ).
* [x] **2. Rủi ro khi AI sai sót nằm trong tầm kiểm soát (HITL & Fallback):**
  * **Cơ chế HITL (Human-In-The-Loop):** AI chỉ đóng vai trò đề xuất slot sạc thông minh. Tài xế toàn quyền xác nhận hoặc từ chối trên app.
  * **Cơ chế Fallback (Dự phòng):** Nếu module AI ngắt kết nối, hệ thống tự động fallback về rule-based phân bổ theo khoảng cách địa lý đơn thuần hoặc tài xế tự tìm trạm như cũ.
* [x] **3. Mức độ sẵn sàng thay đổi của các bên liên quan (Stakeholder Buy-in):**
  * **Khối Vận hành Xanh SM:** Rất cấp thiết vì giải quyết tình trạng thiếu hụt 20–25% xe giờ cao điểm.
  * **V-GREEN:** Giảm quá tải cục bộ tại các trạm sạc lớn, bảo vệ tuổi thọ lưới điện.
  * **Tài xế:** Hưởng ứng cao do được đảm bảo có trụ sạc trống ngay khi đến, giảm 80% thời gian chờ đợi và có ưu đãi voucher sạc.

### 2. 🏛️ Quyết định của Ban Giám Đốc Vin Smart Future:
> **Quyết định: [x] GO (Bắt đầu xây dựng MVP Prototype)**  
> *(Triển khai thử nghiệm có kiểm soát tại cụm Cầu Giấy – Nam Từ Liêm, Hà Nội trước khi nhân rộng).*

### 3. 💡 Justification (Lý giải quyết định dựa trên Bằng chứng Kỹ thuật & Chi phí):
* **ROI vượt trội:** Chi phí MVP ước tính ~400 triệu VNĐ (1 đội AI/Backend trong 6 tuần). Thu hồi được ~600 – 840 triệu VNĐ/ngày từ việc giải phóng nguồn cung giờ cao điểm. Thời gian hoàn vốn dưới 2 ngày.
* **Độ khả thi kỹ thuật cao:** Sử dụng kết hợp **Predictive Machine Learning** (dự báo nhu cầu đặt xe) và **Operations Research / Optimization Algorithm** (phân bổ slot sạc) – mô hình đã được chứng minh hiệu quả trong ngành gọi xe công nghệ.
* **Ranh giới an toàn tuyệt đối:** Không can thiệp điều khiển phần cứng của xe; cấm gán cuốc xa cho xe dưới 15% pin; 100% tôn trọng quyết định của tài xế.
