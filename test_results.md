# Test Results - TravelBuddy Agent

## Test 1 - Direct Answer (Khong can tool)

**User**

```text
Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
```

**Console log**

```text
[Agent] Tra loi truc tiep ngay tu dau, khong can goi tool.
TravelBuddy: Xin chào! Rất vui được hỗ trợ bạn. Bạn đang có ý tưởng nào về điểm đến chưa? Hoặc bạn có sở thích cụ thể nào về loại hình du lịch (biển, núi, văn hóa, ẩm thực) không? Nếu bạn có ngân sách hay thời gian cụ thể, mình cũng có thể giúp đề xuất những điểm đến phù hợp hơn!
```

**Danh gia**

- Dat ky vong: agent chao hoi, hoi them nhu cau, khong goi tool.

## Test 2 - Single Tool Call

**User**

```text
Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
```

**Console log**

```text
[Tool] search_flights -> {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}
[Agent] Khong goi them tool, dang tao cau tra loi cuoi cung.
TravelBuddy: Dưới đây là các chuyến bay từ Hà Nội đến Đà Nẵng:

1. VietJet Air | 08:30 - 09:50 | Hạng vé: Economy | Giá: 890.000₫
2. Bamboo Airways | 11:00 - 12:20 | Hạng vé: Economy | Giá: 1.200.000₫
3. Vietnam Airlines | 06:00 - 07:20 | Hạng vé: Economy | Giá: 1.450.000₫
4. Vietnam Airlines | 14:00 - 15:20 | Hạng vé: Business | Giá: 2.800.000₫

Gợi ý tiết kiệm nhất: Chuyến bay của VietJet Air lúc 08:30 với giá 890.000₫.
```

**Danh gia**

- Dat ky vong: agent goi `search_flights` va liet ke 4 chuyen bay.

## Test 3 - Multi-Step Tool Chaining

**User**

```text
Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
```

**Console log**

```text
[Tool] search_flights -> {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}
[Tool] search_hotels -> {'city': 'Phú Quốc', 'max_price_per_night': 1950000}
[Tool] calculate_budget -> {'total_budget': 5000000, 'expenses': '1.100.000₫ (vé máy bay) + 2.000.000₫ (2 đêm khách sạn)'}
[Tool] calculate_budget -> {'total_budget': 5000000, 'expenses': 'vé máy bay:1100000, khách sạn:2000000'}
[Agent] Khong goi them tool, dang tao cau tra loi cuoi cung.
TravelBuddy: Dưới đây là chuyến đi của bạn từ Hà Nội đến Phú Quốc trong 2 đêm:

Chuyến bay:
- Hãng bay: VietJet Air
- Giờ bay: 16:00 - 18:15
- Hạng vé: Economy
- Giá vé: 1.100.000₫

Khách sạn:
- Tên: Sol by Meliá
- Số sao: 4 sao
- Khu vực: Bãi Trường
- Giá mỗi đêm: 1.500.000₫
- Rating: 4.2

Tổng chi phí ước tính:
- Tổng vé máy bay: 1.100.000₫
- Tổng tiền khách sạn: 3.000.000₫ (1.500.000₫ x 2 đêm)
- Ngân sách ban đầu: 5.000.000₫
- Số tiền còn lại: 1.900.000₫

Gợi ý thêm:
- Bạn vẫn còn 1.900.000₫ để chi tiêu cho các hoạt động khác như ăn uống, tham quan hay mua sắm trong chuyến đi.
- Nếu bạn muốn ở khách sạn khác hoặc có thêm yêu cầu nào, hãy cho mình biết nhé!
```

**Danh gia**

- Dat muc tieu chinh: agent da tu chain `search_flights` -> `search_hotels` -> `calculate_budget` va tong hop thanh goi y hoan chinh.
- Luu y nho: model thu goi `calculate_budget` mot lan voi dinh dang expenses sai, sau do tu sua va goi lai dung dinh dang.

## Test 4 - Missing Info / Clarification

**User**

```text
Tôi muốn đặt khách sạn
```

**Console log**

```text
[Agent] Tra loi truc tiep ngay tu dau, khong can goi tool.
TravelBuddy: Chắc chắn rồi! Bạn có thể cho tôi biết thành phố mà bạn muốn đặt khách sạn, số đêm lưu trú và ngân sách của bạn không?
```

**Danh gia**

- Dat ky vong: agent hoi lai thanh pho, so dem, ngan sach va khong goi tool.

## Test 5 - Guardrail / Refusal

**User**

```text
Giải giúp tôi bài tập lập trình Python về linked list
```

**Console log**

```text
[Agent] Tra loi truc tiep ngay tu dau, khong can goi tool.
TravelBuddy: Xin lỗi, nhưng mình chỉ hỗ trợ về các yêu cầu liên quan đến du lịch, đặt vé, khách sạn, và lịch trình mà thôi. Bạn có cần trợ giúp về kế hoạch chuyến đi nào không?
```

**Danh gia**

- Dat ky vong: agent tu choi lich su va giu dung pham vi tro ly du lich.
