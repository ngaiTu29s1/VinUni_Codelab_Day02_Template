# 01 — Problem Scan & Quick Cards (Vin Smart Future)

> **Deliverable Phase 1 (SCAN) + Phase 2 (QUICK-ASSESS)** — Lab 02: AI Product Scoping
> **Vai trò:** AI Product Engineer tại **Vin Smart Future** (đơn vị công nghệ hợp nhất của Vingroup).

---

## 🏛️ Bối cảnh khảo sát

Nhóm được giao nhiệm vụ quét qua hoạt động vận hành của các công ty thành viên Vingroup để tìm các bottleneck có thể tối ưu bằng AI. Quá trình scan được thực hiện qua **4 Lenses** (Lặp lại / Tốn thời gian / AI-upgrade / Pain từ người khác), tập trung vào các quy trình **thủ công, tần suất cao, và có dữ liệu ngôn ngữ tự nhiên** — nơi LLM có lợi thế rõ rệt so với rule-based code.

---

# 🔍 Phase 1 — SCAN: Bảng quét cơ hội

| # | Subsidiary | Lens | Mô tả ngắn bài toán | Tần suất ước tính |
|---|------------|------|---------------------|-------------------|
| 1 | **Vinmec** | Tốn thời gian | Bác sĩ mất 20-30 phút/bệnh nhân để tự viết tóm tắt hồ sơ bệnh án khi xuất viện (Discharge Summary) từ ghi chú điều trị rời rạc trên EMR. | ~150 ca/ngày toàn hệ thống |
| 2 | **VinFast** | Lặp lại | Kỹ sư bảo trì rà soát thủ công log pin (nhiệt độ, chu kỳ sạc, điện áp cell) trên Excel để phát hiện xe có nguy cơ hỏng pin trước khi khách hàng báo lỗi. | ~200 xe/tuần |
| 3 | **Vinhomes** | AI-upgrade | Tổng đài CSKH cư dân phản hồi rập khuôn và chậm (trung bình 12 giờ) cho các yêu cầu lặp lại về phí quản lý, sự cố tiện ích, đặt lịch bảo trì căn hộ. | ~500 ticket/ngày |
| 4 | **Vinpearl** | Pain từ người khác | Nhân viên lễ tân phàn nàn vì phải tra cứu thủ công qua nhiều hệ thống rời rạc (đặt phòng, vé công viên, nhà hàng) khi khách yêu cầu đổi lịch trình combo. | ~80 yêu cầu/ngày/resort |
| 5 | **Xanh SM** | AI-upgrade | Tài xế phàn nàn chatbot hỗ trợ hiện tại trả lời rập khuôn khi báo cáo sự cố xe, không phân biệt được mức độ khẩn cấp (hết pin / tai nạn / hỏng máy). | ~300 báo cáo/ngày |
| 6 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công sự cố hết pin thực địa: tra cứu GPS, tìm trạm sạc trống, soạn tin chỉ đường (15 phút/lượt). | ~80 sự cố/ngày (HN) |

> **Ghi chú phương pháp:** Các con số tần suất là ước tính dựa trên quan sát thực địa và phỏng vấn nhanh stakeholder, dùng để **xếp hạng ưu tiên** chứ chưa phải số liệu chính thức. Baseline chính xác cần được đo lại trong giai đoạn pilot.

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Nhóm chọn **top 3** từ bảng SCAN dựa trên 3 tiêu chí: (1) tần suất cao, (2) metric đo được rõ ràng, (3) dữ liệu đầu vào đã có sẵn dạng số hóa.

## 🃏 Card #1 — Vinmec: Tóm tắt hồ sơ bệnh án xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Bác sĩ Vinmec mất quá nhiều thời gian     │
│ viết tóm tắt hồ sơ bệnh án khi bệnh nhân xuất viện.         │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị nội trú (quá tải cuối  │
│ ca trực), Trưởng khoa (tắc ở khâu duyệt), Bệnh nhân (chờ).  │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tổng hợp ghi chú điều trị hàng ngày trên EMR           │
│   ──> 2. Đọc lại toàn bộ kết quả cận lâm sàng (CLS)         │
│   ──> 3. Tự viết tóm tắt chẩn đoán & quá trình điều trị     │
│   ──> 4. Viết hướng dẫn dùng thuốc & lịch tái khám          │
│   ──> 5. Trưởng khoa duyệt & ký hồ sơ ra viện               │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 20 phút/lượt)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3-4            │
│ (Tổng hợp dữ liệu EMR ──> Draft tóm tắt ──> Bác sĩ duyệt)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian soạn hồ sơ xuất viện: 40 phút ──> dưới 10    │
│ phút/bệnh nhân; độ chính xác thuốc & chẩn đoán ≥ 98%.       │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

**Vì sao là LLM chứ không phải Rule?** Đầu vào là văn bản y khoa tự do (ghi chú bác sĩ viết tay số hóa, diễn đạt không chuẩn hóa giữa các khoa). Rule-based không thể tổng hợp diễn ngôn; nhưng output vẫn phải bị chặn bởi Operational Boundary nghiêm ngặt vì đây là văn bản y tế có giá trị pháp lý.

---

## 🃏 Card #2 — VinFast: Dự đoán sớm lỗi pin từ log xe

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Kỹ sư VinFast rà soát thủ công log pin để │
│ phát hiện xe có nguy cơ hỏng pin trước khi khách báo lỗi.   │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Kỹ sư bảo trì đội Battery Health,      │
│ Khách hàng (chỉ biết lỗi khi xe đã hỏng giữa đường).        │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tải log pin theo VIN từ hệ thống telemetry             │
│   ──> 2. Lọc thủ công các chỉ số bất thường trên Excel      │
│   ──> 3. Đối chiếu ngưỡng cảnh báo kỹ thuật                 │
│   ──> 4. Gọi khách đặt lịch kiểm tra nếu nghi ngờ           │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ 25 phút/xe)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│ (Phân tích pattern log ──> Chấm điểm rủi ro tự động)        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Phát hiện sớm ≥ 90% ca lỗi pin tiềm ẩn trước khi khách báo  │
│ lỗi; giảm thời gian rà soát từ 25 phút ──> dưới 2 phút/xe.  │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

**Vì sao là Rule chứ không phải LLM?** Đầu vào là **dữ liệu số có cấu trúc** (điện áp, nhiệt độ, chu kỳ sạc) với ngưỡng kỹ thuật đã được định nghĩa sẵn bởi phòng R&D. Một pipeline rule-based + mô hình thống kê rẻ hơn, nhanh hơn, và **giải thích được** — điều bắt buộc khi ra quyết định triệu hồi kỹ thuật. Dùng LLM ở đây là over-engineering.

---

## 🃏 Card #3 — Vinhomes: Phân loại & draft phản hồi cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tổng đài CSKH Vinhomes phản hồi rập khuôn,│
│ chậm cho các yêu cầu lặp lại của cư dân.                    │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Cư dân (chờ 12 giờ), Nhân viên CSKH    │
│ tuyến 1 (xử lý lặp lại), Ban quản lý tòa nhà (nhận sai vé). │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi yêu cầu qua App Vinhomes Resident           │
│   ──> 2. NV đọc & phân loại thủ công vào đúng nhóm nghiệp vụ│
│   ──> 3. Tra cứu quy định/FAQ nội bộ                        │
│   ──> 4. Soạn phản hồi gửi cư dân                           │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 15 phút/lượt)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3-4            │
│ (Phân loại ticket ──> Draft trả lời dựa trên FAQ nội bộ)    │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian phản hồi trung bình: 12 giờ ──> dưới 1 giờ;  │
│ độ chính xác định tuyến ticket ≥ 92%.                       │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

**Rủi ro đã nhận diện:** Phản hồi sai về phí quản lý hoặc tranh chấp căn hộ có thể dẫn tới khiếu nại pháp lý. Cần rule-based router chặn trước các chủ đề nhạy cảm (phí, hợp đồng, tranh chấp) và chuyển thẳng cho người xử lý.

---

# 🗳️ Quyết định lựa chọn bài toán cho Deep-Dive

Nhóm quyết định chọn **Card #1 — Vinmec: Tóm tắt hồ sơ bệnh án xuất viện** để thực hiện Phase 3 (Deep-Dive).

### Lý do chọn Card #1:
* **Tần suất cao và ổn định:** Mọi bệnh nhân nội trú đều phải có hồ sơ xuất viện — tác động lan tỏa toàn hệ thống Vinmec, không phụ thuộc mùa vụ.
* **Metric rõ ràng, đo được ngay:** Thời gian soạn hồ sơ và % khớp thông tin thuốc/chẩn đoán đều có thể đo trên hồ sơ thực tế đã ẩn danh.
* **Bài toán thuần ngôn ngữ:** Đây đúng là thế mạnh của LLM (tổng hợp văn bản y khoa rời rạc), không thể thay thế bằng rule-based.
* **Rủi ro kiểm soát được:** Quy trình vốn đã có sẵn bước Trưởng khoa duyệt & ký — HITL là bước *có sẵn trong quy trình*, không phải thứ phải thêm vào.

### Lý do loại các thẻ còn lại:
* **Card #2 (VinFast Pin):** Bài toán dữ liệu số có cấu trúc với ngưỡng kỹ thuật đã định nghĩa sẵn — **rule-based + mô hình thống kê giải quyết tốt hơn và rẻ hơn LLM**. Đưa LLM vào đây là dùng sai công cụ.
* **Card #3 (Vinhomes CSKH):** Rủi ro pháp lý cao (phí quản lý, tranh chấp căn hộ) nhưng **không có bước duyệt bắt buộc sẵn trong quy trình** như Vinmec. Cần xây rule-based router chặn chủ đề nhạy cảm trước khi nghĩ đến LLM.

---

## 🤖 Phản biện đã nhận từ AI (Stress-test thẻ bài toán)

Nhóm đã dán Card #1 vào LLM với vai trò "CFO và Trưởng phòng Vận hành khắt khe". Ba điểm yếu bị chỉ ra và cách nhóm đã xử lý:

| # | Phản biện | Cách nhóm điều chỉnh |
|---|-----------|----------------------|
| 1 | *"Metric 'giảm 40 xuống 10 phút' là con số bạn tự nghĩ ra, chưa có baseline đo thực tế."* | Chuyển quyết định cuối từ GO sang **NOT YET**, thêm yêu cầu pilot đo baseline trên 20-30 hồ sơ thật trước khi cam kết con số. |
| 2 | *"Nếu bác sĩ vẫn phải đọc lại toàn bộ để duyệt, thời gian tiết kiệm có thể chỉ là ảo giác."* | Bổ sung metric chất lượng ≥ 98% khớp thông tin — nếu độ chính xác thấp, thời gian review sẽ ăn hết phần tiết kiệm, và đó chính là tín hiệu để dừng dự án. |
| 3 | *"Template rule-based điền sẵn theo mã ICD có thể giải quyết 60% ca đơn giản mà không cần LLM."* | Nhóm ghi nhận là hợp lý: đề xuất **scope hẹp giai đoạn 1 chỉ áp dụng cho các ca nội trú phức tạp**, còn ca đơn giản vẫn dùng template — tránh trả tiền LLM cho việc rule làm được. |
