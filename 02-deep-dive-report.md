# 02-deep-dive-report.md — Deep-Dive Report & Evaluation

> **Dự án:** Vin Smart Future — Xanh SM Intelligent Battery Dispatcher Co-Pilot  
> **Người thực hiện:** Tuấn Tú (Trưởng nhóm)  
> **Đơn vị phối hợp:** Khối Vận Hành Xanh SM (GSM) & Vin Smart Future  

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Quy trình tiếp nhận và xử lý sự cố pin xe điện thực địa hiện tại của Điều phối viên Xanh SM:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Tiếp nhận    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn văn bản │
│ cuộc gọi/app │ ──> │ vị GPS xe    │ ──> │ sạc VinFast  │ ──> │ chỉ đường    │
│              │ 🔄  │ trên bản đồ  │ 🔄  │ còn trụ trống│     │ gửi tài xế   │
│ Dispatcher   │     │ Dispatcher   │     │ Dispatcher   │     │ Dispatcher   │
│ ⏱ 2 phút     │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Điều xe cứu  │
                                                               │ hộ (nếu cần) │
                                                               │ Dispatcher   │
                                                               │ ⏱ 1 phút     │
                                                               └──────────────┘

* Ký hiệu:
  🔴 Bottleneck (Điểm nghẽn gây trễ nải nhất: Bước 3 và Bước 4)
  🔄 Handoff (Điểm chuyển giao thông tin qua các màn hình và hệ thống)
* Tổng thời gian xử lý thủ công: ~15 phút/xe.
```

---

## 3.2. Problem Statement (6-Field Standard)

| Field | Chi tiết nội dung |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM Hà Nội / TP.HCM. |
| **2. Current Workflow** | Khi nhận phản ánh xe sắp hết pin hoặc sự cố trạm sạc, điều phối viên tra cứu toạ độ GPS của xe trên portal nội bộ, chuyển sang hệ thống quản lý trạm sạc VinFast để tìm trụ sạc tương thích còn trống, tự gõ tin nhắn hướng dẫn đường đi qua app tài xế, và gọi đội xe sạc di động nếu pin dưới 5%. Quy trình 5 bước thủ công mất trung bình 15 phút. |
| **3. Bottleneck** | **Bước 3 & Bước 4:** Tốn 10 phút để rà soát loại đầu sạc (CCS2, công suất KW phù hợp dòng xe VF5/VFe34/VF8/VF9) và gõ tin nhắn hướng dẫn đường đi bằng tiếng Việt chuẩn mực, thân thiện. |
| **4. Business Impact** | Mỗi ngày xảy ra ~80 sự cố pin tại Hà Nội (số liệu chuẩn từ tài liệu phân tích mẫu của môn học 02-deliverable-example.md). Với 15 phút/lượt xử lý thủ công, toàn đội điều vận tiêu tốn 80 × 15 = 1.200 phút/ngày (~20 giờ làm việc/ngày). Khi ứng dụng AI rút ngắn xuống dưới 3 phút/lượt, tổng thời gian xử lý chỉ còn 80 × 3 = 240 phút/ngày (4 giờ/ngày), giúp **tiết kiệm thực tế 16 giờ làm việc mỗi ngày** (giảm 80% thời gian lãng phí, tương đương giải phóng công sức của 2 nhân sự full-time). |
| **5. Success Metric** | **1. Hiệu suất:** Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút/lượt (theo chuẩn SLA của 02-deliverable-example.md).<br>**2. Độ chính xác:** Tỉ lệ điều phối đúng trạm sạc có trụ khả dụng và đúng chuẩn kết nối đạt >= 98%.<br>**3. An toàn:** 100% trường hợp pin dưới 5% được cảnh báo và kích hoạt điều xe cứu hộ kịp thời, không có xe bị sập nguồn giữa đường. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Truy vấn API vị trí xe, API trạm sạc khả dụng, tự động soạn thảo tin nhắn hướng dẫn dạng nháp (Draft).<br>**AI TUYỆT ĐỐI CẤM:** Không được tự động gửi tin nhắn cho tài xế khi chưa có điều phối viên nhấn xác nhận (Bắt buộc phải có tag `[DRAFT_ONLY]` ở đầu để áp dụng Human-in-the-loop); Không được đề xuất trạm sạc cách xa quá 5km khi pin xe báo dưới 5% (phải chuyển sang lệnh `dispatch_mobile_charger`). |

---

## 3.3. Future-State Flow & AI Fit

### 🧭 Đánh giá AI Fit (AI-Fit Matrix)
* **Giải pháp lựa chọn: LLM Feature tích hợp Rule-based Guardrail.**
  * *Vì sao không dùng Full Agentic Loop?* Điều phối xe điện và xử lý sự cố liên quan đến an toàn giao thông và tài sản lớn. Một hành động tự trị sai lầm của Agent (gửi xe đến trạm hỏng hoặc trạm xa) có thể làm xe chết máy giữa cầu/đường cao tốc.
  * *Vì sao không dùng Rule thuần túy?* Rule thuần túy không thể tạo tin nhắn hướng dẫn linh hoạt theo ngữ cảnh giao thông, thời tiết, dòng xe và sắc thái giao tiếp thân thiện với tài xế.
  * *Kết hợp tối ưu:* Rule-based router để chặn ngưỡng pin cứng (< 5%), kết hợp Gemini 3.7 Flash để soạn thảo hướng dẫn thông minh có ranh giới `[DRAFT_ONLY]`.

### 🔄 Luồng quy trình tương lai (Future-State Flow):

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận tín hiệu│     │ 🔵 Auto-pull │     │ 🔵 AI Draft  │     │ 🟢 Dispatcher│
│ pin yếu      │ ──> │ vị trí GPS & │ ──> │ tin nhắn kèm │ ──> │ Review & Gửi │
│ từ xe/tài xế │     │ trạm sạc gần │     │ [DRAFT_ONLY] │     │ (1 Click)    │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
                                           ↩️ Fallback Plan:
                        Nếu AI gặp lỗi API hoặc vi phạm ranh giới an toàn,
                        hệ thống fallback về giao diện nhập tay truyền thống
                        cho Dispatcher xử lý ngay lập tức.
```

---

# 🏁 Phase 5 — EVALUATE: Quyết định triển khai

### AI Readiness Checklist:
1. **[x] Dữ liệu mẫu & API:** Đã có hệ thống Telematics của VinFast và API Dashboard trụ sạc GSM.
2. **[x] Kiểm soát rủi ro an toàn:** Áp dụng mô hình Human-in-the-loop (Bắt buộc `[DRAFT_ONLY]`) và chặn cứng pin < 5% bằng lệnh `dispatch_mobile_charger`. Có Fallback rõ ràng.
3. **[x] Stakeholders sẵn sàng:** Đội ngũ Dispatcher Xanh SM rất mong muốn giảm tải công việc thủ công giờ cao điểm.

### 🎯 Quyết định cuối cùng: **GO (Tiến hành xây dựng Prototype)**

**Lý giải quyết định (Technical & Business Justification):**
* **ROI cao:** Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút/lượt, tiết kiệm 16 giờ làm việc mỗi ngày cho team điều vận (tương đương 112 giờ làm việc/tuần), đồng thời giảm thời gian chết của xe điện ngoài đường để đón khách.
* **Độ phức tạp kỹ thuật vừa phải:** Sử dụng Gemini 3.7 Flash với System Prompt nghiêm ngặt cho thời gian phản hồi cực nhanh (< 2s) và chi phí token thấp.
* **Rủi ro vận hành bằng 0:** Nhờ cơ chế `[DRAFT_ONLY]`, AI không bao giờ trực tiếp gửi tin mà chỉ đóng vai trò Trợ lý (Co-pilot), quyền quyết định cuối cùng vẫn thuộc về Dispatcher.
