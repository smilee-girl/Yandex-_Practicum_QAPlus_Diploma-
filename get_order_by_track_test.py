import data
import sender_stand_request


# Функция для получения данных о заказе по его трек-номеру

def test_get_order_info_by_track():
    track_number = sender_stand_request.get_order_info_by_track()
    assert track_number.status_code == 200
