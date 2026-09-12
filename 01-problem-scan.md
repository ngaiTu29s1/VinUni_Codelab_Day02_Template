# 01 — Problem Scan: Vin Smart Future AI Product Scoping

> **Tác giả:** AI Product Engineer - Vin Smart Future  
> **Ngày thực hiện:** 12/09/2026  
> **Mục tiêu:** Quét và đánh giá các cơ hội tối ưu hóa bằng AI tại các công ty thành viên Vingroup

---

## 🔍 Phase 1 — SCAN: Quét Cơ Hội (Individual Work)

Sử dụng **4 Lenses** để tìm kiếm các bài toán thực tế có tiềm năng ứng dụng AI tại các công ty thành viên Vingroup.

### 📝 Danh sách 5+ Bài toán Tiềm năng

| # | Công ty | Lens | Mô tả ngắn bài toán |
|---|---------|------|---------------------|
| 1 | **VinFast** | Tốn thời gian | Nhân viên tổng đài phải tự tra cứu lịch trống của xưởng bảo dưỡng và thủ công đề xuất khung giờ phù hợp qua điện thoại (mất 8-12 phút/cuộc gọi). |
| 2 | **Xanh SM** | Lặp lại | Điều phối viên phải thủ công tái phân bổ cuốc xe khi khách hàng yêu cầu thay đổi điểm đón/điểm đến giữa chừng (xảy ra 200+ lần/ngày tại TP.HCM). |
| 3 | **Vinhomes** | AI-upgrade | Hệ thống CSKH hiện tại chỉ có bot đơn giản trả lời rập khuôn, không hiểu ngữ cảnh phức tạp của cư dân về vấn đề phí quản lý, tiện ích chung. |
| 4 | **Vinmec** | Tốn thời gian | Y tá phải gọi điện xác nhận lịch tái khám với bệnh nhân, giải thích hướng dẫn chuẩn bị xét nghiệm bằng giọng nói (mất 15-20 phút cho 10 bệnh nhân/ngày). |
| 5 | **VinFast** | Pain từ người khác | Kỹ thuật viên phàn nàn về việc mô tả lỗi xe từ khách hàng thường mơ hồ (ví dụ: "xe có tiếng lạ"), khiến việc chuẩn bị phụ tùng và công cụ trước khi bảo dưỡng không chính xác. |
| 6 | **Xanh SM** | Tốn thời gian | Phân tích và tóm tắt lý do khách hàng hủy chuyến từ ghi âm cuộc gọi và ghi chú tài xế để tìm pattern cải thiện dịch vụ (hiện tại làm thủ công hằng tuần, mất 6-8 giờ). |
| 7 | **Vinpearl** | Lặp lại | Nhân viên lễ tân phải tra cứu thủ công các yêu cầu đặc biệt của khách (phòng tầng cao, giường đôi, gần thang máy) từ email/ghi chú và cập nhật vào hệ thống đặt phòng. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn **top 3 bài toán** có tác động lớn nhất để phân tích sơ bộ.

---

### 📋 QUICK PROBLEM CARD #1

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Hệ thống tự động đề xuất lịch bảo dưỡng xe điện  │
│ thông minh cho khách hàng VinFast qua tổng đài hotline     │
│                                                             │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau (Actor)?                                         │
│ - Nhân viên tổng đài CSKH VinFast (quá tải giờ cao điểm)   │
│ - Khách hàng (chờ đợi lâu, đặt lịch không thuận tiện)      │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Khách gọi hotline yêu cầu đặt lịch bảo dưỡng          │
│   → 2. Nhân viên hỏi thông tin xe (biển số, km đã đi)      │
│   → 3. Tra cứu thủ công lịch trống của 3-5 xưởng gần nhất  │
│   → 4. Tư vấn khung giờ phù hợp qua điện thoại             │
│   → 5. Ghi nhận thông tin đặt lịch vào hệ thống CRM        │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 3-4 (⏱ 8-12 phút/cuộc gọi)                             │
│ - Phải mở 3-4 tab để tra lịch nhiều xưởng                  │
│ - Phải giải thích qua điện thoại cho khách hàng hiểu       │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Bước 2-4: Tự động nhận diện thông tin xe → Tra cứu lịch    │
│ trống tự động → Draft tin nhắn đề xuất 3 khung giờ phù hợp │
│ gửi qua SMS/App để khách chọn                               │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ 1. Giảm thời gian xử lý từ 10 phút → dưới 3 phút/cuộc gọi  │
│ 2. Tăng tỷ lệ đặt lịch thành công từ 65% → 85%+            │
│ 3. Giảm 40% cuộc gọi lặp lại do đặt lịch không phù hợp     │
│                                                             │
│ Quick Architecture:                                          │
│ [x] LLM Feature (Tự động đề xuất lịch + soạn tin nhắn)     │
└─────────────────────────────────────────────────────────────┘
```

---

### 📋 QUICK PROBLEM CARD #2

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Phân loại và chẩn đoán sơ bộ mô tả lỗi xe        │
│ bằng tiếng Việt từ khách hàng VinFast                       │
│                                                             │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau (Actor)?                                         │
│ - Kỹ thuật viên xưởng dịch vụ (nhận thông tin mơ hồ)       │
│ - Nhân viên CSKH (không chuyên môn kỹ thuật để hỏi đúng)   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Khách hàng mô tả lỗi xe qua hotline (tiếng Việt)      │
│   → 2. CSKH ghi chép thủ công vào phiếu tiếp nhận          │
│   → 3. Kỹ thuật viên đọc phiếu và đoán vấn đề              │
│   → 4. Chuẩn bị công cụ/phụ tùng dựa trên kinh nghiệm      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 2-3 (⏱ 10-15 phút + 30% sai sót chuẩn bị)             │
│ - Mô tả khách hàng mơ hồ: "xe kêu lạ", "đèn nháy đỏ"       │
│ - Kỹ thuật viên phải gọi lại để hỏi thêm                   │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Bước 1-2: AI chatbot hỏi thêm chi tiết có cấu trúc         │
│ (âm thanh khi nào? đèn màu gì?) → Phân loại mã lỗi sơ bộ   │
│ (phanh, pin, hệ thống điện, động cơ) → Gợi ý checklist     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ 1. Giảm tỷ lệ chuẩn bị sai phụ tùng từ 30% → dưới 10%      │
│ 2. Tăng độ chính xác phân loại lỗi lên 80%+                │
│ 3. Giảm 50% cuộc gọi lại để làm rõ thông tin               │
│                                                             │
│ Quick Architecture:                                          │
│ [x] LLM Feature (Conversational diagnosis với hỏi đáp)     │
└─────────────────────────────────────────────────────────────┘
```

---

### 📋 QUICK PROBLEM CARD #3

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Tự động phân tích lý do hủy chuyến của khách     │
│ hàng Xanh SM để tìm pattern cải thiện dịch vụ              │
│                                                             │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)?                                         │
│ - Analyst team Xanh SM (làm thủ công mất nhiều thời gian)  │
│ - Manager vận hành (thiếu insight kịp thời để cải tiến)    │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Thu thập file ghi âm cuộc gọi hủy chuyến hằng tuần    │
│   → 2. Nghe thủ công 200-300 cuộc gọi (6-8 giờ)            │
│   → 3. Phân loại lý do vào 10 categories (Excel manual)    │
│   → 4. Tạo báo cáo insight gửi Manager                      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 2-3 (⏱ 6-8 giờ/tuần, chỉ sample 20% data)             │
│ - Không thể phân tích toàn bộ cuộc gọi do mất thời gian    │
│ - Phân loại không nhất quán giữa các analysts              │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Bước 2-3: Speech-to-text → LLM phân loại lý do hủy         │
│ (tài xế chậm, giá cao, app lỗi, thay đổi kế hoạch...)      │
│ → Tự động tạo dashboard insight theo tuần                   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ 1. Tăng % data được phân tích từ 20% → 100%                │
│ 2. Giảm thời gian từ 8 giờ/tuần → 30 phút tự động          │
│ 3. Độ chính xác phân loại đạt 85%+ (so với human label)    │
│                                                             │
│ Quick Architecture:                                          │
│ [x] LLM Feature (Speech-to-text + classification)           │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Lựa chọn bài toán cho Deep-Dive

**Bài toán được chọn:** **Card #1 — Hệ thống đề xuất lịch bảo dưỡng xe điện VinFast**

### Lý do lựa chọn:
1. **Tác động trực tiếp đến trải nghiệm khách hàng:** Đây là điểm chạm quan trọng trong customer journey của VinFast, ảnh hưởng đến sự hài lòng và loyalty.
2. **ROI rõ ràng:** Giảm thời gian xử lý = tăng năng suất tổng đài + giảm chi phí nhân sự, đồng thời tăng conversion rate đặt lịch.
3. **Khả thi kỹ thuật cao:** Có sẵn data (lịch xưởng, thông tin xe), workflow rõ ràng, risk thấp (vì vẫn có human-in-the-loop).
4. **Metric đo lường chính xác:** Có thể A/B test trước/sau triển khai để đo impact.

### Lý do loại bỏ các thẻ khác:
* **Card #2 (Chẩn đoán lỗi xe):** Rủi ro cao hơn vì chẩn đoán sai có thể ảnh hưởng an toàn. Cần nhiều data training hơn và domain expertise sâu từ kỹ sư cơ khí.
* **Card #3 (Phân tích hủy chuyến Xanh SM):** Đây là back-office analytics task, không ảnh hưởng trực tiếp real-time operations như Card #1. Impact gián tiếp và khó đo trong ngắn hạn.

---

## 📊 Tóm tắt Phase 1-2

| Tiêu chí | Kết quả |
|----------|---------|
| **Số bài toán quét được** | 7 problems từ 5 công ty thành viên |
| **Top 3 cards hoàn thành** | ✅ Card #1 (VinFast), Card #2 (VinFast), Card #3 (Xanh SM) |
| **Bài toán chọn Deep-Dive** | Card #1 — Smart Maintenance Booking System |
| **Lý do chính** | High impact + High feasibility + Clear metrics |

---

*Tiếp theo: Phase 3 — Deep-Dive Analysis (xem file `02-deep-dive-report.md`)*
