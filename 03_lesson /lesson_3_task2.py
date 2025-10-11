from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 7", "+79456789012"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+79567890123"))


for dota in catalog:
    print(f"{dota.brand}, {dota.model},{dota.number}")
