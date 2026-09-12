# 03 — AI Log & Reflection

> **Deliverable Phase 6 (REFLECTION)** — Lab 02: AI Product Scoping
> Nhật ký phản ánh quá trình sử dụng AI làm **thought-partner** (không phải máy sinh đáp án) trong buổi lab.

---

## 🛠️ 1. Tôi đã dùng AI vào việc gì?

| Giai đoạn | Cách tôi dùng AI | Có hữu ích không? |
|---|---|---|
| **Phase 1 — SCAN** | Dùng AI để brainstorm pain point vận hành ở các công ty thành viên Vingroup mà tôi không có kiến thức nội bộ (Vinmec, Vinpearl). | ✅ Rất hữu ích để **mở rộng không gian tìm kiếm** |
| **Phase 2 — Quick Cards** | Yêu cầu AI đóng vai **CFO và Trưởng phòng Vận hành khắt khe** để phản biện thẻ bài toán của tôi. | ✅ Hữu ích nhất trong cả buổi |
| **Phase 3 — Deep-Dive** | Nhờ AI kiểm tra xem Problem Statement 6-field của tôi có trường nào mơ hồ, metric nào thiếu số. | ⚠️ Hữu ích một phần |
| **Phase 4 — Prompt Prototype** | Nhờ AI gợi ý các hướng tấn công (adversarial input) mà tôi chưa nghĩ ra. | ✅ Hữu ích |
| **Phase 5 — Evaluate** | Thảo luận với AI về việc nên chọn GO hay NOT YET. | ⚠️ Phải tự quyết định cuối cùng |

---

## ✅ 2. AI đã giúp tôi những gì cụ thể?

### 2.1. Mở rộng không gian tìm kiếm bài toán
Ban đầu tôi chỉ nghĩ ra được 2 bài toán, và cả hai đều xoay quanh mảng xe điện vì đó là thứ tôi quen thuộc nhất. Khi hỏi AI về pain point ở **Vinmec** và **Vinpearl** — hai mảng tôi hoàn toàn không có kinh nghiệm — tôi mới tìm ra bài toán *"tóm tắt hồ sơ bệnh án xuất viện"*, và đây chính là bài toán nhóm chọn để deep-dive.

**Bài học:** AI hữu ích nhất ở chỗ tôi *thiếu kiến thức nền*, không phải ở chỗ tôi đã biết rõ.

### 2.2. Phản biện thẳng thắn khi được giao vai trò cụ thể
Đây là phần giá trị nhất. Khi tôi hỏi *"thẻ bài toán này ổn không?"*, AI trả lời chung chung kiểu "ý tưởng tốt, có tiềm năng". Nhưng khi tôi đổi prompt thành:

> *"Hãy đóng vai CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn dùng AI."*

thì AI chỉ ra được một điểm khiến tôi phải sửa lại toàn bộ phần kết luận:

> *"Nếu bác sĩ vẫn phải đọc lại toàn bộ hồ sơ gốc để duyệt bản nháp, thì thời gian bạn tưởng là tiết kiệm có thể chỉ là ảo giác."*

Tôi đã bổ sung thêm một **guardrail metric** vào Problem Statement: *tỉ lệ bác sĩ phải viết lại hoàn toàn bản nháp < 10%* — nếu vượt ngưỡng này thì AI đang tạo thêm việc chứ không tiết kiệm.

### 2.3. Gợi ý hướng tấn công cho boundary test
Tôi tự nghĩ ra được 2 adversarial input (ép bỏ thẻ `[DRAFT_ONLY]`, ép đề xuất trạm sạc xa khi pin yếu). AI gợi ý thêm một hướng tôi chưa nghĩ tới: **prompt injection giả danh nội bộ** — người dùng tự xưng là kỹ sư Vin Smart Future và yêu cầu "chế độ debug, tạm tắt ranh giới". Tôi đã thêm đây thành Test Case 3.

---

## ❌ 3. AI đã sai / hallucinate ở đâu?

### 3.1. Bịa số liệu thống kê nghe rất thuyết phục
Khi tôi hỏi về pain point ở Vinmec, AI trả lời kèm những con số rất cụ thể:

> *"Theo báo cáo nội bộ của Vinmec năm 2024, bác sĩ mất trung bình 27.5 phút/hồ sơ và tỉ lệ sai sót đơn thuốc là 3.2%..."*

Tôi hỏi lại nguồn thì AI thừa nhận đây là **con số ước lượng minh họa**, không có báo cáo nào như vậy. Nếu tôi copy thẳng vào báo cáo, nhóm sẽ nộp một bài có số liệu giả mạo nguồn.

**Cách tôi sửa:** Tôi giữ lại các con số làm *ước tính để xếp hạng ưu tiên*, nhưng ghi rõ trong file `01-problem-scan.md`:

> *"Các con số tần suất là ước tính dựa trên quan sát thực địa và phỏng vấn nhanh stakeholder, dùng để xếp hạng ưu tiên chứ chưa phải số liệu chính thức."*

Và quan trọng hơn — chính vì không có baseline thật, nhóm đã chọn **NOT YET** thay vì GO.

### 3.2. Luôn có xu hướng đề xuất giải pháp phức tạp nhất
Khi tôi hỏi về kiến trúc cho bài toán Vinmec, AI đề xuất ngay một hệ **multi-agent** gồm agent trích xuất dữ liệu, agent soạn thảo, agent kiểm tra chéo. Nghe rất ấn tượng nhưng sai hoàn toàn với bối cảnh: quy trình đã cố định (1 bệnh án → 1 bản nháp), và trong môi trường y tế thì **mọi output đều phải qua người duyệt** — nên khả năng tự trị của agent là vô nghĩa, chỉ làm hệ thống khó audit hơn khi có tranh chấp pháp lý.

**Cách tôi sửa:** Tôi tự quyết định chọn **LLM Feature** đơn giản, và ghi rõ lý do loại Agentic Loop vào bảng AI Fit Analysis. Nguyên tắc trong Inspiration Kit đã cảnh báo đúng điều này: *"Đừng cố tìm bài toán phức tạp chỉ để dùng Multi-Agent."*

### 3.3. Trả lời nước đôi khi phải ra quyết định
Khi tôi hỏi nên chọn GO hay NOT YET, AI liệt kê ưu nhược điểm của cả hai rồi kết luận *"tùy thuộc vào mức độ chấp nhận rủi ro của tổ chức"*. Đây là câu trả lời đúng nhưng vô dụng — quyết định vẫn phải là của tôi.

**Cách tôi sửa:** Tôi đổi cách hỏi, yêu cầu AI liệt kê cụ thể *"những gì nhóm chưa chứng minh được bằng dữ liệu"*. Từ danh sách đó tôi thấy rõ 3 thứ còn thiếu (baseline thật, sign-off pháp lý, sự đồng thuận của bác sĩ) — và tự kết luận **NOT YET**.

---

## 🔧 4. Tôi đã sửa prompt / ranh giới như thế nào?

| Prompt ban đầu (kém) | Vấn đề | Prompt đã sửa (tốt) |
|---|---|---|
| *"Thẻ bài toán này ổn không?"* | AI khen chung chung, không phản biện | *"Đóng vai CFO khắt khe, chỉ ra 3 điểm yếu về logic và metric, giải thích vì sao rule-based tốt hơn AI ở đây."* |
| *"Cho tôi số liệu về Vinmec"* | AI bịa số có vẻ chính thống | *"Hãy đưa ước tính và **ghi rõ đây là ước tính minh họa, không phải số liệu thật**."* |
| *"Nên chọn GO hay NOT YET?"* | AI trả lời nước đôi | *"Liệt kê cụ thể những gì nhóm CHƯA chứng minh được bằng dữ liệu thật."* |

### Bài học lớn nhất về việc viết ranh giới cho AI

Trong Phase 4, tôi phát hiện ra điều này khi stress-test: **ranh giới định tính thì LLM dễ bị thuyết phục phá vỡ, ranh giới có ngưỡng số cụ thể thì rất vững.**

* Khi tôi viết *"nên cân nhắc kỹ nếu pin yếu"* → AI bị adversarial input thuyết phục, vẫn đề xuất trạm sạc xa vì "khách VIP đang gấp".
* Khi tôi viết *"NẾU `battery_level < 5%` VÀ `station_distance > 5km` THÌ BẮT BUỘC trả về `dispatch_mobile_charger`"* → AI giữ vững ranh giới trước cả 3 hướng tấn công.

Đây là nguyên tắc tôi sẽ mang sang khi viết Operational Boundary cho hệ thống Vinmec: **mọi ranh giới an toàn phải viết thành điều kiện kiểm chứng được bằng máy, không phải lời khuyên.**

---

## 💭 5. Tổng kết: AI là thought-partner hay máy sinh đáp án?

Sau buổi lab này tôi nhận ra ranh giới khá rõ ràng:

**AI làm tốt:**
* Mở rộng không gian tìm kiếm ở lĩnh vực tôi không có kiến thức nền
* Đóng vai người phản biện khi được giao **vai trò cụ thể và khắt khe**
* Chỉ ra những lỗ hổng logic mà tôi đã quá quen nên không còn nhìn thấy

**AI làm kém (và tôi phải tự làm):**
* Cung cấp dữ liệu thực tế — nó sẽ bịa số nghe rất thuyết phục
* Chọn giải pháp phù hợp với ràng buộc thực tế — nó luôn thiên về phương án phức tạp, ấn tượng
* **Ra quyết định** — nó sẽ luôn trả lời nước đôi, vì rủi ro của quyết định là của tôi chứ không phải của nó

Điều tôi rút ra: **chất lượng đầu ra của AI phụ thuộc gần như hoàn toàn vào chất lượng ràng buộc tôi đặt vào prompt.** Hỏi mơ hồ thì nhận lại lời khen vô nghĩa; giao vai trò rõ ràng và yêu cầu phản biện thì nhận lại giá trị thật. Đây cũng chính là bài học trùng khớp với nội dung lab — **Operational Boundary quyết định chất lượng sản phẩm AI**, dù là trong một prompt hay trong cả một hệ thống production.

---

> 📌 **Ghi chú:** File này phản ánh trải nghiệm cá nhân trong buổi lab. Các bạn khác trong nhóm vui lòng viết bản của riêng mình trên branch cá nhân — nội dung phản ánh trung thực quan trọng hơn việc viết hay.
