# 02 — Deep-Dive Report: Smart Maintenance Booking System (VinFast)

> **Dự án:** Hệ thống đề xuất lịch bảo dưỡng xe điện thông minh  
> **Công ty:** VinFast - Vin Smart Future  
> **Ngày phân tích:** 12/09/2026  
> **Team:** AI Product Engineering

---

## 📋 Executive Summary

Dự án này tập trung vào việc tối ưu hóa quy trình đặt lịch bảo dưỡng xe điện VinFast thông qua việc ứng dụng AI (LLM) để tự động hóa việc tra cứu lịch trống, đề xuất khung giờ phù hợp và soạn thảo tin nhắn xác nhận. Mục tiêu giảm thời gian xử lý từ 10 phút xuống dưới 3 phút/cuộc gọi, tăng tỷ lệ conversion đặt lịch từ 65% lên 85%+.

---

## 🏗️ Phase 3 — DEEP-DIVE ANALYSIS

### 3.1. Current-State Workflow Mapping

**Quy trình đặt lịch bảo dưỡng hiện tại (Thủ công 100%)**

```text
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Bước 1           │     │ Bước 2           │     │ Bước 3           │
│ Khách gọi        │     │ Thu thập thông   │     │ Tra cứu lịch     │
│ hotline VinFast  │ ──→ │ tin xe & yêu cầu │ ──→ │ trống xưởng      │
│                  │     │                  │     │                  │
│ Actor: Khách hàng│     │ Actor: CSKH      │     │ Actor: CSKH      │
│ ⏱ 1-2 phút       │     │ ⏱ 2-3 phút       │     │ ⏱ 4-6 phút 🔴    │
│ In: Nhu cầu      │     │ In: Hỏi đáp      │     │ In: Biển số, KM  │
│ Out: Kết nối     │     │ Out: Data record │     │ Out: Slot list   │
└──────────────────┘     └──────────────────┘     └──────────────────┘
                                                            │
                                                            ▼
                         ┌──────────────────┐     ┌──────────────────┐
                         │ Bước 5           │     │ Bước 4           │
                         │ Ghi nhận & xác   │ ◀── │ Tư vấn qua điện  │
                         │ nhận vào CRM     │     │ thoại & chốt     │
                         │                  │     │                  │
                         │ Actor: CSKH      │     │ Actor: CSKH      │
                         │ ⏱ 1-2 phút       │     │ ⏱ 3-5 phút 🔴    │
                         │ In: Thông tin    │     │ In: Slot + khách │
                         │ Out: Booking ID  │     │ Out: Decision    │
                         └──────────────────┘     └──────────────────┘

🔴 = Bottleneck (điểm nghẽn)
🔄 = Handoff point (chuyển giao thông tin)
```

**Chi tiết các Bottleneck:**

1. **Bước 3 - Tra cứu lịch trống (4-6 phút):**
   - Nhân viên phải mở 3-4 tab trình duyệt để kiểm tra lịch của nhiều xưởng dịch vụ gần vị trí khách hàng
   - Phải đối chiếu thủ công loại xe (VF5, VF8, VF9) với năng lực xưởng (không phải xưởng nào cũng nhận tất cả dòng xe)
   - Phải tính toán khoảng cách và thời gian di chuyển phù hợp với khách hàng

2. **Bước 4 - Tư vấn qua điện thoại (3-5 phút):**
   - Phải giải thích qua loa cho khách hàng nghe về vị trí xưởng, khung giờ trống
   - Khách hàng thường yêu cầu so sánh nhiều options → phải lặp lại thông tin nhiều lần
   - Nếu khách chưa quyết định được, cuộc gọi kéo dài hoặc phải gọi lại

**🔄 Handoff Point:** Giữa Bước 2-3 và 4-5, thông tin được chuyển từ hệ thống CRM → Excel tra cứu → Lại về CRM để lưu booking.

**⏱ Tổng thời gian xử lý trung bình: 10-15 phút/cuộc gọi**

---

### 3.2. Problem Statement (6-field Standard)

| Field | Nội dung chi tiết |
|-------|-------------------|
| **1. Actor / Operator** | Nhân viên CSKH hotline VinFast (Bộ phận After-Sales Service), làm việc tại Trung tâm Chăm sóc Khách hàng VinFast Hà Nội và TP.HCM. Mỗi trung tâm có 15-20 nhân viên tổng đài, xử lý trung bình 80-120 cuộc gọi đặt lịch bảo dưỡng/ngày (cao điểm 8-10h sáng và 14-16h chiều). |
| **2. Current Workflow** | Quy trình thủ công 5 bước: (1) Nhận cuộc gọi → (2) Hỏi thông tin xe (biển số, km đã chạy, loại xe) → (3) Tra cứu thủ công lịch trống của 3-5 xưởng dịch vụ gần vị trí khách hàng trên hệ thống quản lý nội bộ (phải mở nhiều tab) → (4) Đọc và giải thích qua điện thoại các slot trống, tư vấn khách chọn → (5) Ghi nhận vào CRM và gửi SMS xác nhận thủ công. |
| **3. Bottleneck** | **Bước 3 & 4 (Tra cứu + Tư vấn)** chiếm 70% thời gian xử lý (7-11 phút/cuộc gọi). Vấn đề cụ thể: (1) Hệ thống quản lý lịch không tích hợp → phải tra từng xưởng, (2) Khách hàng khó hình dung thông tin qua điện thoại → phải giải thích nhiều lần, (3) Không có công cụ so sánh nhanh để đề xuất slot tối ưu nhất. |
| **4. Business Impact** | **Chi phí vận hành:** 2 trung tâm hotline xử lý ~3.000 cuộc gọi/tháng, tốn ~500 giờ nhân công/tháng chỉ cho công việc tra cứu-tư vấn lịch. **Opportunity cost:** 35% khách hàng không chốt được lịch ngay trong cuộc gọi đầu tiên vì "cần suy nghĩ thêm" → tỷ lệ conversion chỉ đạt 65%. **Customer experience:** Thời gian chờ đợi trung bình 4-5 phút vào giờ cao điểm, dẫn đến 15-20% khách hàng up điện thoại trước khi được kết nối. |
| **5. Success Metric** | **Primary KPI:** (1) Giảm thời gian xử lý trung bình từ 10 phút → **dưới 3 phút/cuộc gọi** (70% faster). **Secondary KPI:** (2) Tăng tỷ lệ conversion đặt lịch từ 65% → **≥85%** (20 điểm phần trăm improvement). (3) Giảm tỷ lệ khách hàng gọi lại để đổi lịch từ 25% → **dưới 10%** (do đề xuất chính xác hơn ngay từ đầu). **Quality metric:** Tỷ lệ slot được đề xuất phù hợp với nhu cầu khách (verified qua khảo sát sau cuộc gọi) đạt **≥90%**. |
| **6. Operational Boundary** | **AI được phép:** (1) Truy vấn API lịch trống của tất cả các xưởng dịch vụ VinFast, (2) Đề xuất 3 slot phù hợp nhất dựa trên vị trí khách hàng, loại xe, và thời gian mong muốn, (3) Tự động soạn thảo tin nhắn SMS/Zalo xác nhận draft để CSKH review trước khi gửi. **AI TUYỆT ĐỐI KHÔNG được:** (1) Tự động confirm booking mà không có CSKH xác nhận với khách hàng qua điện thoại (vì có thể hiểu sai nhu cầu), (2) Đề xuất xưởng dịch vụ không có năng lực xử lý loại xe của khách (ví dụ: xưởng nhỏ không nhận VF9), (3) Truy cập hoặc thay đổi thông tin cá nhân khách hàng trong CRM (chỉ đọc data xe). **Human-in-the-loop bắt buộc:** CSKH phải đọc lại 3 slot được AI đề xuất, xác nhận với khách qua điện thoại, và click nút [Confirm] trước khi booking được ghi nhận chính thức. |

---

### 3.3. Future-State Flow & AI Fit Analysis

#### 🎯 AI Fit Matrix — Xác định mức độ tự động hóa

| Tiêu chí | Rule-based | LLM Feature | Agentic Loop |
|----------|------------|-------------|--------------|
| **Structured data** | ✅ Lịch xưởng có cấu trúc | ✅ Text generation cần | ❌ Không cần tự quyết định |
| **Complexity** | ⚠️ Logic phức tạp (nhiều điều kiện) | ✅ Phù hợp | ❌ Overkill |
| **Risk tolerance** | ✅ Low risk | ✅ Medium (có HITL) | ❌ High risk (auto booking) |
| **Human oversight** | N/A | ✅ Cần CSKH confirm | ❌ Không phù hợp |

**→ Quyết định: Chọn LLM Feature với Human-in-the-loop**

#### 🔮 Future-State Workflow (Có AI hỗ trợ)

```text
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Bước 1           │     │ Bước 2           │     │ Bước 3           │
│ Khách gọi        │     │ CSKH nhập thông  │     │ 🔵 AI tự động    │
│ hotline VinFast  │ ──→ │ tin vào assistant│ ──→ │ query lịch trống │
│                  │     │ interface        │     │ 3-5 xưởng phù hợp│
│ Actor: Khách     │     │ Actor: CSKH      │     │ Actor: AI System │
│ ⏱ 1-2 phút       │     │ ⏱ 30 giây       │     │ ⏱ 5 giây        │
└──────────────────┘     └──────────────────┘     └──────────────────┘
                                                            │
                                                            ▼
                         ┌──────────────────┐     ┌──────────────────┐
                         │ Bước 6           │     │ Bước 4           │
                         │ 🔵 AI auto-send  │ ◀── │ 🔵 AI đề xuất    │
                         │ SMS xác nhận     │     │ top 3 slots +    │
                         │                  │     │ draft SMS        │
                         │ Actor: AI System │     │ Actor: AI System │
                         │ ⏱ 2 giây         │     │ ⏱ 3 giây         │
                         └──────────────────┘     └──────────────────┘
                                 ▲                         │
                                 │                         ▼
                         ┌──────────────────┐     ┌──────────────────┐
                         │ Bước 5           │     │ 🟢 HITL          │
                         │ Ghi nhận CRM     │ ◀── │ CSKH đọc đề xuất │
                         │ (auto-log)       │     │ cho khách & xác  │
                         │                  │     │ nhận [Confirm]   │
                         │ Actor: System    │     │ Actor: CSKH      │
                         │ ⏱ 1 giây         │     │ ⏱ 1 phút         │
                         └──────────────────┘     └──────────────────┘

🔵 = AI-powered step
🟢 = Human-in-the-loop (HITL) checkpoint
↩️ = Fallback mechanism
```

**Tổng thời gian mới: ~3 phút/cuộc gọi (giảm 70%)**

#### ↩️ Fallback Mechanism (Kế hoạch dự phòng)

| Tình huống lỗi | Fallback action | Responsible |
|----------------|-----------------|-------------|
| API lịch xưởng timeout/lỗi | CSKH tra cứu thủ công như cũ, log incident để IT khắc phục | CSKH + IT Ops |
| AI đề xuất 0 slot (không tìm thấy lịch trống phù hợp) | AI hiển thị thông báo "Không có lịch trống trong khung giờ này" → CSKH suggest khung giờ khác hoặc ghi nhận vào waitlist | CSKH |
| AI đề xuất sai loại xưởng (không phù hợp với loại xe) | CSKH phát hiện qua giao diện → Reject suggestion → Chọn thủ công từ dropdown list → Report bug cho AI team | CSKH + AI Team |
| Khách hàng yêu cầu điều kiện đặc biệt ngoài khả năng của AI (ví dụ: "Tôi muốn kỹ thuật viên Nam phụ trách") | CSKH ghi nhận special request vào trường Note → Xác nhận booking manual → Escalate đến Service Manager | CSKH + Manager |

---

## 📐 Technical Architecture Design

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                      CSKH Web Interface                     │
│  (Booking Assistant Dashboard - React Frontend)             │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTPS
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               Backend API Gateway (FastAPI)                 │
│  - Authentication & Authorization                           │
│  - Rate limiting & Logging                                  │
└────┬────────────────┬─────────────────────┬─────────────────┘
     │                │                     │
     ▼                ▼                     ▼
┌─────────┐   ┌──────────────┐   ┌──────────────────────┐
│ CRM DB  │   │ LLM Service  │   │ Workshop Schedule DB │
│(Customer│   │ (Gemini 2.5) │   │ (Available slots)    │
│ & Car)  │   │              │   │                      │
└─────────┘   └──────────────┘   └──────────────────────┘
```

### AI Workflow Logic

```python
# Pseudo-code cho AI Booking Assistant
def suggest_booking_slots(customer_info, car_info, preferred_time):
    # Step 1: Validate input
    if not validate_car_model(car_info.model):
        return {"error": "Invalid car model"}
    
    # Step 2: Query available workshops
    nearby_workshops = get_workshops_by_location(
        customer_location=customer_info.address,
        radius_km=15,
        car_model_support=car_info.model
    )
    
    # Step 3: Query available slots
    available_slots = []
    for workshop in nearby_workshops:
        slots = query_workshop_calendar(
            workshop_id=workshop.id,
            date_range=(preferred_time - 2days, preferred_time + 3days),
            service_type="maintenance"
        )
        available_slots.extend(slots)
    
    # Step 4: LLM-powered ranking & SMS generation
    prompt = f"""
    Customer: {customer_info.name}, Location: {customer_info.address}
    Car: {car_info.model}, Current KM: {car_info.current_km}
    Preferred time: {preferred_time}
    
    Available slots: {available_slots}
    
    Please:
    1. Rank top 3 most suitable slots considering distance, time preference, workshop quality
    2. Generate a friendly Vietnamese SMS message (max 160 chars) listing these 3 options
    
    Output JSON format:
    {{
        "recommended_slots": [
            {{"workshop": "...", "time": "...", "distance_km": ..., "reason": "..."}},
            ...
        ],
        "sms_draft": "..."
    }}
    """
    
    llm_response = call_gemini_api(prompt, temperature=0.3)
    
    # Step 5: HITL checkpoint - return to CSKH for confirmation
    return {
        "suggestions": llm_response.recommended_slots,
        "sms_draft": llm_response.sms_draft,
        "requires_human_approval": True
    }
```

---

## 🏁 Phase 5 — EVALUATION & DECISION

### AI Readiness Checklist

| # | Tiêu chí | Trạng thái | Chi tiết |
|---|----------|-----------|----------|
| 1 | **Data availability** | ✅ SẴN SÀNG | Có sẵn database lịch xưởng real-time, thông tin xe khách hàng trong CRM, log lịch sử đặt lịch 12 tháng qua (~10,000 bookings) để training/testing |
| 2 | **API integration** | ✅ SẴN SÀNG | Workshop calendar API đã tồn tại (dùng cho internal tool), chỉ cần expose endpoint mới cho AI service |
| 3 | **Risk mitigation** | ✅ KIỂM SOÁT ĐƯỢC | Rủi ro thấp vì có HITL checkpoint (CSKH phải confirm trước khi booking chính thức). Worst case: AI suggest sai → CSKH reject và làm thủ công như cũ |
| 4 | **Stakeholder buy-in** | ⚠️ CẦN XÁC NHẬN | CSKH team trưởng ủng hộ (giảm workload), nhưng cần training 2-3 ngày để làm quen với giao diện mới. IT Ops lo ngại về system stability → cần pilot test 2 tuần với 20% traffic trước khi full rollout |
| 5 | **Measurement baseline** | ✅ SẴN SÀNG | Đã có baseline metric từ log hệ thống hiện tại: Average handling time = 10.2 phút, Conversion rate = 65%, Reschedule rate = 25% |
| 6 | **Fallback plan** | ✅ SẴN SÀNG | Nếu AI service down, CSKH revert về quy trình thủ công ngay lập tức. Không ảnh hưởng đến khả năng phục vụ khách hàng |

### Cost-Benefit Analysis (Ước tính 6 tháng đầu)

**Investment Cost:**
- Development: 3 AI Engineers × 2 tháng = ~$30,000
- Gemini API cost: ~$500/month (ước tính 3,000 calls × $0.15/call)
- Infrastructure: $200/month (cloud hosting)
- Training CSKH team: $2,000 one-time

**Total 6-month cost: ~$37,000**

**Expected Benefit:**
- Tiết kiệm nhân công: 500 giờ/tháng × 70% = 350 giờ saved × $15/hour = **$5,250/month**
- Tăng conversion: 3,000 calls/month × 20% tăng thêm × $50 service revenue/booking = **$30,000/month**
- Giảm cuộc gọi lại: 750 calls/month × 60% reduction × 5 minutes saved = **$1,000/month value**

**Total 6-month benefit: ~$217,500**

**ROI: 488% (payback trong <1 tháng)**

### Final Decision

**🟢 GO — Bắt đầu phát triển Prototype với phạm vi hẹp**

**Justification (Căn cứ quyết định):**

1. **ROI cực kỳ hấp dẫn:** Với chi phí đầu tư ban đầu ~$37K và lợi nhuận dự kiến $217K trong 6 tháng, dự án có ROI 488% và payback period dưới 1 tháng.

2. **Risk thấp và có thể kiểm soát:** 
   - Human-in-the-loop checkpoint đảm bảo không có booking nào được tạo tự động mà không có sự xác nhận của CSKH
   - Fallback mechanism rõ ràng: nếu AI lỗi, CSKH vẫn làm việc bình thường
   - Pilot test với 20% traffic trước khi full rollout giảm thiểu risk

3. **Technical feasibility cao:**
   - Data sẵn có và chất lượng tốt (10K+ historical bookings)
   - API integration đơn giản (workshop calendar API đã tồn tại)
   - LLM task tương đối straightforward (ranking + text generation)

4. **Clear success metrics:**
   - Có baseline rõ ràng để đo lường impact (handling time, conversion rate, reschedule rate)
   - Có thể A/B test trong pilot phase để validate

5. **Stakeholder alignment:**
   - CSKH team ủng hộ vì giảm workload và cải thiện KPI
   - Management team quan tâm vì impact trực tiếp lên customer experience và revenue

**Implementation Plan:**
- **Phase 1 (Tháng 1-2):** Development + Internal testing với dummy data
- **Phase 2 (Tuần 1-2 tháng 3):** Pilot test với 20% traffic tại HN hotline center, train CSKH team
- **Phase 3 (Tuần 3-4 tháng 3):** Evaluate pilot results, fix bugs, optimize prompt
- **Phase 4 (Tháng 4):** Full rollout HN + HCM nếu pilot thành công (≥80% positive feedback từ CSKH)

**Success Criteria cho Pilot:**
- Average handling time ≤4 phút (60% improvement, mục tiêu cuối cùng là 3 phút)
- Conversion rate ≥75% (15% improvement)
- CSKH satisfaction score ≥4/5 (khảo sát sau 2 tuần pilot)
- Zero critical incidents (sai sót nghiêm trọng dẫn đến khiếu nại khách hàng)

---

## 📎 Appendix

### Wireframe: CSKH Dashboard Interface (Draft)

```
┌─────────────────────────────────────────────────────────────┐
│  VinFast Booking Assistant                    [CSKH: Nam]  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📞 Cuộc gọi đang kết nối: 0123456789                       │
│                                                             │
│  🚗 Thông tin xe khách hàng:                                │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ Biển số: 30A-12345    ✅ Đã xác thực                   │ │
│  │ Chủ xe: Nguyễn Văn A                                   │ │
│  │ Loại xe: VinFast VF8                                   │ │
│  │ Km hiện tại: 15,200 km                                 │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  📅 Khung thời gian mong muốn: [________] [Tìm kiếm]       │
│                                                             │
│  🤖 AI đề xuất 3 lịch phù hợp nhất:                         │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ 🥇 #1: Xưởng Cầu Giấy - Thứ 6, 15/09, 9:00-11:00      │ │
│  │      📍 3.2km từ vị trí khách | ⭐ 4.8/5 rating        │ │
│  │      Lý do: Gần nhất, khung giờ sáng phù hợp          │ │
│  │      [✅ Chọn]  [❌ Bỏ qua]                             │ │
│  ├───────────────────────────────────────────────────────┤ │
│  │ 🥈 #2: Xưởng Long Biên - Thứ 7, 16/09, 14:00-16:00    │ │
│  │      📍 5.8km | ⭐ 4.9/5 | Ưu tiên nếu khách muốn cuối│ │
│  │      tuần                                              │ │
│  │      [  Chọn]  [❌ Bỏ qua]                             │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  📱 Tin nhắn xác nhận (Draft):                              │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ "Kính chào anh A, VinFast xác nhận lịch bảo dưỡng VF8│ │
│  │  30A-12345: Thứ 6, 15/09, 9h tại xưởng Cầu Giấy       │ │
│  │  (3.2km từ nhà anh). Hotline: 1900xxx. Trân trọng!"   │ │
│  │                                            [✏️ Sửa]     │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│                   [🟢 XÁC NHẬN & GỬI SMS]                   │
│                   [⚪ HỦY VÀ LÀM THỦ CÔNG]                  │
└─────────────────────────────────────────────────────────────┘
```

---

*Hoàn thành Deep-Dive Report. Xem tiếp: Phase 4 — Prompt Prototype (code implementation) và Phase 6 — Reflection (file `03-ai-log.md`)*
