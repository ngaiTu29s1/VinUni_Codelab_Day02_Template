# 01-problem-scan.md — Scan & Quick-Assess (Vin Smart Future)

> **Học viên thực hiện:** Tuấn Tú (Trưởng nhóm)  
> **Đơn vị:** Vin Smart Future — AI Product Engineering  
> **Dự án:** Tối ưu hóa vận hành thông minh cho hệ sinh thái Vingroup  

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (4 Lenses)

Dưới đây là danh sách quét các cơ hội ứng dụng AI trong hoạt động vận hành của các công ty thành viên Vingroup sử dụng 4 thấu kính (4 Lenses).

| # | Subsidiary | Lens | Mô tả bài toán vận hành & Pain Point |
|---|------------|------|--------------------------------------|
| 1 | **Xanh SM** | Lặp lại | So khớp và phân bổ lại cuốc xe khi hành khách yêu cầu đổi lộ trình hoặc điểm đến giữa chừng. |
| 2 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế về sự cố hết pin/lỗi trạm sạc thực địa (mất 15–20 phút/lượt). |
| 3 | **VinFast** | Lặp lại | Đối chiếu hóa đơn sạc điện và kiểm toán số liệu điện năng tiêu thụ tại các trạm sạc đối tác hằng tuần. |
| 4 | **Vinhomes** | AI-upgrade | Hệ thống phân loại, gắn tag và định tuyến tự động phản ánh/khiếu nại của cư dân trên App Vinhomes Resident (hiện mất 12–24h xử lý thủ công). |
| 5 | **Vinmec** | Pain từ người khác | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ xuất viện và nhập mã ICD-10 (mất 20–30 phút/bệnh nhân, gây quá tải giờ cao điểm). |
| 6 | **Vinpearl** | Tốn thời gian | Tóm tắt đánh giá đa ngôn ngữ của du khách quốc tế trên OTA để phân loại phàn nàn về dịch vụ phòng/buồng phòng theo ca trực. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn top 3 bài toán tiềm năng nhất từ danh sách SCAN:
1. **Card #1:** Xanh SM — Xử lý sự cố sạc pin & cạn pin thực địa của tài xế.
2. **Card #2:** Vinhomes — Tự động phân loại và định tuyến khiếu nại cư dân trên App Resident.
3. **Card #3:** Vinmec — Trợ lý AI tóm tắt hồ sơ xuất viện & đề xuất mã ICD-10 lâm sàng.

---

## 🎴 Thẻ bài toán 1: Xanh SM — Xử lý sự cố pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo sự cố cạn pin/hỏng trụ sạc     │
│ giữa đường cần điều phối cứu hộ hoặc trạm sạc khả dụng gấp. │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (stress, mất khách), Dispatcher (quá tải)│
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi hotline điều vận báo nguy cấp pin           │
│   ──> 2. Dispatcher tra cứu GPS xe trên bản đồ nội bộ       │
│   ──> 3. Mở portal VinFast lọc trạm sạc còn trụ trống phù hợp│
│   ──> 4. Soạn SMS/in-app message chỉ đường chi tiết gửi xe  │
│   ──> 5. Gọi đội xe cứu hộ nếu pin < 5% không đi tiếp được   │
│                                                             │
│ Bước nào tốn nhất? Bước 3 & 4 (⏱ 10–12 phút/lượt)           │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (Auto-pull vị trí -> Lọc trạm trống -> Draft tin chỉ dẫn)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/xe.   │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Drafting + Boundary)   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎴 Thẻ bài toán 2: Vinhomes — Smart Resident Ticket Routing

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Cư dân gửi phản ánh bằng văn bản tự do, ban quản lý│
│ phải đọc và chuyển tiếp thủ công đến các bộ phận kỹ thuật.   │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Cư dân (chờ lâu), Nhân viên CSKH BQL (quá tải) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Nhận yêu cầu cư dân trên ứng dụng Vinhomes Resident    │
│   ──> 2. Nhân viên đọc nội dung, trích xuất mã căn hộ & lỗi │
│   ──> 3. Gán nhãn thủ công (Điện nước, Thang máy, An ninh)  │
│   ──> 4. Chuyển tiếp ticket đến đội kỹ thuật phụ trách tòa  │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 15 phút/ticket)            │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Trích xuất thực thể, phân loại lỗi và gán tag tự động)     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Thời gian định tuyến ticket giảm từ 4 giờ ──> dưới 30 giây; │
│ Độ chính xác gán nhãn đạt >= 95%.                           │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Classification & NER)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎴 Thẻ bài toán 3: Vinmec — Hỗ trợ tóm tắt hồ sơ bệnh án xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Bác sĩ điều trị mất thời gian tổng hợp diễn biến  │
│ bệnh án từ nhiều khoa phòng để viết giấy ra viện.           │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau? Bác sĩ điều trị, Điều dưỡng trưởng              │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Mở phần mềm HIS tra cứu lịch sử xét nghiệm và phẫu thuật│
│   ──> 2. Đọc và tổng hợp các ghi chú lâm sàng của từng ngày │
│   ──> 3. Gõ bản tóm tắt quá trình điều trị & chỉ định thuốc │
│   ──> 4. Tra cứu mã ICD-10 phù hợp để lưu hồ sơ bảo hiểm    │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 25 phút/hồ sơ)             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Tổng hợp ghi chú lâm sàng thành bản nháp tóm tắt xuất viện) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian soạn tóm tắt từ 25 phút ──> 5 phút/hồ sơ.    │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Summarization + HITL)   │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn của nhóm

* **Bài toán được chọn để làm Deep-Dive:** **Card #1 — Xanh SM Xử lý sự cố pin thực địa**.
* **Lý do lựa chọn:**
  * **Tính cấp bách vận hành:** Xe điện Xanh SM chạy liên tục ngoài đường, nếu cạn pin giữa đường sẽ gây tắc nghẽn giao thông, hỏng pin và mất doanh thu tức thì.
  * **Dữ liệu & API sẵn có:** Đã có hệ thống telemetry GPS xe và API trạng thái trụ sạc VinFast.
  * **Ranh giới an toàn rõ ràng:** Có thể áp dụng quy tắc cứng (pin < 5% cấm đi trạm xa, bắt buộc điều xe cứu hộ) và cơ chế Human-in-the-loop (bắt buộc gắn thẻ `[DRAFT_ONLY]` để điều phối viên duyệt trước khi gửi).
