from __future__ import annotations

from typing import Dict, List, Tuple

from langchain_core.tools import tool


FLIGHTS_DB: Dict[Tuple[str, str], List[dict]] = {
    ("Hà Nội", "Đà Nẵng"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "06:00",
            "arrival": "07:20",
            "price": 1_450_000,
            "class": "economy",
        },
        {
            "airline": "Vietnam Airlines",
            "departure": "14:00",
            "arrival": "15:20",
            "price": 2_800_000,
            "class": "business",
        },
        {
            "airline": "VietJet Air",
            "departure": "08:30",
            "arrival": "09:50",
            "price": 890_000,
            "class": "economy",
        },
        {
            "airline": "Bamboo Airways",
            "departure": "11:00",
            "arrival": "12:20",
            "price": 1_200_000,
            "class": "economy",
        },
    ],
    ("Hà Nội", "Phú Quốc"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "07:00",
            "arrival": "09:15",
            "price": 2_100_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "10:00",
            "arrival": "12:15",
            "price": 1_350_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "16:00",
            "arrival": "18:15",
            "price": 1_100_000,
            "class": "economy",
        },
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "06:00",
            "arrival": "08:10",
            "price": 1_600_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "07:30",
            "arrival": "09:40",
            "price": 950_000,
            "class": "economy",
        },
        {
            "airline": "Bamboo Airways",
            "departure": "12:00",
            "arrival": "14:10",
            "price": 1_300_000,
            "class": "economy",
        },
        {
            "airline": "Vietnam Airlines",
            "departure": "18:00",
            "arrival": "20:10",
            "price": 3_200_000,
            "class": "business",
        },
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "09:00",
            "arrival": "10:20",
            "price": 1_300_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "13:00",
            "arrival": "14:20",
            "price": 780_000,
            "class": "economy",
        },
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {
            "airline": "Vietnam Airlines",
            "departure": "08:00",
            "arrival": "09:00",
            "price": 1_100_000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "15:00",
            "arrival": "16:00",
            "price": 650_000,
            "class": "economy",
        },
    ],
}


HOTELS_DB: Dict[str, List[dict]] = {
    "Đà Nẵng": [
        {
            "name": "Mường Thanh Luxury",
            "stars": 5,
            "price_per_night": 1_800_000,
            "area": "Mỹ Khê",
            "rating": 4.5,
        },
        {
            "name": "Sala Danang Beach",
            "stars": 4,
            "price_per_night": 1_200_000,
            "area": "Mỹ Khê",
            "rating": 4.3,
        },
        {
            "name": "Fivitel Danang",
            "stars": 3,
            "price_per_night": 650_000,
            "area": "Sơn Trà",
            "rating": 4.1,
        },
        {
            "name": "Memory Hostel",
            "stars": 2,
            "price_per_night": 250_000,
            "area": "Hải Châu",
            "rating": 4.6,
        },
        {
            "name": "Christina's Homestay",
            "stars": 2,
            "price_per_night": 350_000,
            "area": "An Thượng",
            "rating": 4.7,
        },
    ],
    "Phú Quốc": [
        {
            "name": "Vinpearl Resort",
            "stars": 5,
            "price_per_night": 3_500_000,
            "area": "Bãi Dài",
            "rating": 4.4,
        },
        {
            "name": "Sol by Meliá",
            "stars": 4,
            "price_per_night": 1_500_000,
            "area": "Bãi Trường",
            "rating": 4.2,
        },
        {
            "name": "Lahana Resort",
            "stars": 3,
            "price_per_night": 800_000,
            "area": "Dương Đông",
            "rating": 4.0,
        },
        {
            "name": "9Station Hostel",
            "stars": 2,
            "price_per_night": 200_000,
            "area": "Dương Đông",
            "rating": 4.5,
        },
    ],
    "Hồ Chí Minh": [
        {
            "name": "Rex Hotel",
            "stars": 5,
            "price_per_night": 2_800_000,
            "area": "Quận 1",
            "rating": 4.3,
        },
        {
            "name": "Liberty Central",
            "stars": 4,
            "price_per_night": 1_400_000,
            "area": "Quận 1",
            "rating": 4.1,
        },
        {
            "name": "Cochin Zen Hotel",
            "stars": 3,
            "price_per_night": 550_000,
            "area": "Quận 3",
            "rating": 4.4,
        },
        {
            "name": "The Common Room",
            "stars": 2,
            "price_per_night": 180_000,
            "area": "Quận 1",
            "rating": 4.6,
        },
    ],
}


CITY_ALIASES = {
    "Da Nang": "Đà Nẵng",
    "Danang": "Đà Nẵng",
    "Ho Chi Minh": "Hồ Chí Minh",
    "TP.HCM": "Hồ Chí Minh",
    "TP HCM": "Hồ Chí Minh",
    "Sai Gon": "Hồ Chí Minh",
    "Phu Quoc": "Phú Quốc",
    "Ha Noi": "Hà Nội",
}


def format_currency(amount: int) -> str:
    return f"{amount:,}".replace(",", ".") + "₫"


def normalize_city_name(city: str) -> str:
    clean_city = city.strip()
    return CITY_ALIASES.get(clean_city, clean_city)


@tool
def search_flights(origin: str, destination: str) -> str:
    """Tìm kiếm các chuyến bay giữa hai thành phố."""
    normalized_origin = normalize_city_name(origin)
    normalized_destination = normalize_city_name(destination)

    direct_key = (normalized_origin, normalized_destination)
    reverse_key = (normalized_destination, normalized_origin)

    flights = FLIGHTS_DB.get(direct_key)
    route_label = f"{normalized_origin} đến {normalized_destination}"

    if flights is None:
        flights = FLIGHTS_DB.get(reverse_key)
        if flights is None:
            return (
                f"Không tìm thấy chuyến bay từ {normalized_origin} đến "
                f"{normalized_destination}."
            )
        route_label = (
            f"{normalized_origin} đến {normalized_destination} "
            f"(tham khảo dữ liệu chiều ngược lại)"
        )

    sorted_flights = sorted(flights, key=lambda flight: flight["price"])
    lines = [f"Các chuyến bay từ {route_label}:"]
    for index, flight in enumerate(sorted_flights, start=1):
        lines.append(
            (
                f"{index}. {flight['airline']} | {flight['departure']} - "
                f"{flight['arrival']} | {flight['class']} | "
                f"{format_currency(flight['price'])}"
            )
        )

    cheapest = sorted_flights[0]
    lines.append(
        "Gợi ý tiết kiệm nhất: "
        f"{cheapest['airline']} lúc {cheapest['departure']} với giá "
        f"{format_currency(cheapest['price'])}."
    )
    return "\n".join(lines)


@tool
def search_hotels(city: str, max_price_per_night: int = 99_999_999) -> str:
    """Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm."""
    normalized_city = normalize_city_name(city)
    hotels = HOTELS_DB.get(normalized_city)

    if hotels is None:
        return f"Không tìm thấy dữ liệu khách sạn tại {normalized_city}."

    filtered_hotels = [
        hotel
        for hotel in hotels
        if hotel["price_per_night"] <= max_price_per_night
    ]
    filtered_hotels.sort(
        key=lambda hotel: (-hotel["rating"], hotel["price_per_night"])
    )

    if not filtered_hotels:
        return (
            f"Không tìm thấy khách sạn tại {normalized_city} với giá dưới "
            f"{format_currency(max_price_per_night)}/đêm. Hãy thử tăng ngân sách."
        )

    lines = [
        f"Khách sạn phù hợp tại {normalized_city} "
        f"(tối đa {format_currency(max_price_per_night)}/đêm):"
    ]
    for index, hotel in enumerate(filtered_hotels, start=1):
        lines.append(
            (
                f"{index}. {hotel['name']} | {hotel['stars']} sao | "
                f"{hotel['area']} | {format_currency(hotel['price_per_night'])}/đêm | "
                f"rating {hotel['rating']}"
            )
        )

    best_value = filtered_hotels[0]
    lines.append(
        "Ưu tiên nổi bật: "
        f"{best_value['name']} với rating {best_value['rating']} và giá "
        f"{format_currency(best_value['price_per_night'])}/đêm."
    )
    return "\n".join(lines)


def parse_expenses(expenses: str) -> Dict[str, int]:
    parsed: Dict[str, int] = {}
    for raw_item in expenses.split(","):
        item = raw_item.strip()
        if not item:
            continue
        if ":" not in item:
            raise ValueError(
                f"Khoản chi '{item}' không đúng định dạng 'ten_khoan:so_tien'."
            )

        name, amount_text = item.split(":", 1)
        expense_name = name.strip()
        cleaned_amount = amount_text.strip().replace(".", "").replace("_", "")

        if not expense_name:
            raise ValueError("Tên khoản chi không được để trống.")
        if not cleaned_amount.isdigit():
            raise ValueError(
                f"Số tiền của khoản '{expense_name}' phải là số nguyên dương."
            )

        parsed[expense_name] = int(cleaned_amount)

    if not parsed:
        raise ValueError("Danh sách chi phí đang trống.")
    return parsed


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """Tính toán ngân sách còn lại sau khi trừ các khoản chi phí."""
    if total_budget < 0:
        return "Ngân sách tổng phải là số không âm."

    try:
        expense_map = parse_expenses(expenses)
    except ValueError as error:
        return f"Lỗi định dạng expenses: {error}"

    total_expense = sum(expense_map.values())
    remaining_budget = total_budget - total_expense

    lines = ["Bảng chi phí:"]
    for expense_name, amount in expense_map.items():
        pretty_name = expense_name.replace("_", " ").strip().capitalize()
        lines.append(f"- {pretty_name}: {format_currency(amount)}")

    lines.append("")
    lines.append(f"Tổng chi: {format_currency(total_expense)}")
    lines.append(f"Ngân sách: {format_currency(total_budget)}")

    if remaining_budget >= 0:
        lines.append(f"Còn lại: {format_currency(remaining_budget)}")
    else:
        lines.append(f"Còn lại: -{format_currency(abs(remaining_budget))}")
        lines.append(
            f"Vượt ngân sách {format_currency(abs(remaining_budget))}! "
            "Cần điều chỉnh kế hoạch."
        )

    return "\n".join(lines)
