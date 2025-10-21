from addres import Address
from mailing import Mailing

my_mailing = Mailing(
    # Заполняем поле to_address - создаем объект Address для адреса назначения
    to_address = Address(
        index = "123456",           # индекс
        city = "Москва",            # город
        street = "Ленина",          # улица
        home = "10",                # дом
        flat = "25"                 # квартира
    ),
    
    # Заполняем поле from_address - создаем объект Address для адреса отправителя
    from_address = Address(
        index = "654321",           # индекс
        city = "Санкт-Петербург",   # город
        street = "Пушкина",         # улица
        home = "5",                 # дом
        flat = "10"                 # квартира
    ),
    
    # Заполняем поле cost - стоимость (число)
    cost = 150,
    
    # Заполняем поле track - трек-номер (строка)
    track = "TRACK123456"
)
    # Заполняем поле cost - стоимость (число)
cost = 150,
    
    # Заполняем поле track - трек-номер (строка)
track = "TRACK123456"


print(f"Отправление {my_mailing.track} из:{my_mailing.from_address.index},{my_mailing.from_address.city},{my_mailing.from_address.street},{my_mailing.from_address.home},{my_mailing.from_address.home},{my_mailing.from_address.flat} в {my_mailing.to_address.city},{my_mailing.to_address.street},{my_mailing.to_address.home} - {my_mailing.to_address.flat}.Стоимость {my_mailing.cost} ")

