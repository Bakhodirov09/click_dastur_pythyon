import os
if not os.path.exists("../tayyorlov/history.txt"):
    file = open("../tayyorlov/history.txt", "x")
def karta_tekshirish(cards: dict, karta: str, phones: dict, codes: list, kommunals: dict):
    try:
        if karta in cards.keys():
            password = int(input("Karta Parolini Kiriting: "))
            if password == cards[karta]["password"]:
                date = input("Karta Amal Qilish Muddatini Kiriting: ")
                if date == cards[karta]["date"]:
                    name = cards[karta]["name"]
                    number = cards[karta]["number"]
                    date = cards[karta]["date"]
                    money = cards[karta]["money"]
                    turi = cards[karta]["turi"]
                    number = '*********' + number[8:]
                    karta_malumot = f"Karta Raqam: {number} \t |Turi: {turi} \t | Ism: {name} \t |Amal Qilish Muddati: {date} \t | Kartada {money} So'm Pul Mavjud"
                    print(karta_malumot)
                    while True:
                        res1 = payment_card(cards, karta, phones, codes, kommunals)
                        print(res1)
                else:
                    return f"Siz Kiritgan {date} Notogri"
            else:
                return f"Parol Notog'ri!"
        else:
            return "Bunday Karta Mavjud Emas!"
    except ValueError:
        return "Siz Notog'ri Ma'lumot Kiritdingiz!"


def payment_card(cards: dict, karta: str, phones: dict, codes: list, kommunals: dict):
    try:
        while True:
            print("1.Kartadan Kartaga Pul O'tkazma")
            print("2.Telefonlarga To'lov Qilish")
            print("3.Komunal Xizmatlarga To'lov Qilish")
            print("4.To'lovlarni Korish")
            sorash = int(input("Click Xizmatini kiriting(raqamda!): "))
            if sorash == 1:
                karta_sorash = input("Pul O'tkazmoqchi Bo'lgan Karta Raqam Kiriting: ")
                if karta_sorash in cards.keys():
                    egasi = cards[karta_sorash]["name"]
                    turi = cards[karta_sorash]["turi"]
                    print(f"Karta: {karta_sorash} \t | Turi: {turi} \t | Ism: {egasi}")
                    pul_miqdor = int(input("Qancha Pul To'lamoqchisiz?: "))
                    res = pul_miqdor / 100
                    pul_miqdor += res
                    if cards[karta]["money"] >= pul_miqdor:
                        cards[karta]["money"] -= pul_miqdor
                        cards[karta_sorash]["money"] += pul_miqdor
                        ress = f"Operatsiya Muvaffaqqiyatli Amalga Oshirildi! Sizda {cards[karta]['money']} so'm Qoldi!"
                        with open("../tayyorlov/history.txt", "a") as appeneder:
                            appeneder.write(f"Karta: {cards[karta]['number']} dan {karta_sorash} Ga {pul_miqdor} So'm Pul Jo'natildi! \n")
                        return ress
                    else:
                        return f"Sizda Yetarli Mablag' Mavjud Emas!"
                else:
                    return "Bunday Karta Topilmadi!"
            if sorash == 2:
                res = payment_phone(phones, codes, karta, cards)
                print(res)
            elif sorash == 3:
                res = payment_kommunal(kommunals, cards, karta)
                print(res)
            elif sorash == 4:
                res = show_history()
                print(res)
    except ValueError:
        text = "Siz Notog'ri Xizmat Kiritdingiz!"
        return text

def payment_phone(phones: dict, codes: list, karta: str, cards: dict):
    number = input("To'lamoqchi Bo'lgan Raqamingizni Kiiriting: ")
    if number[0:4] != "+998":
        print("Siz O'zbekiston Kodini Kiritmadingiz!")
    if len(number) > 13 or len(number) < 13 :
        print("Siz Noto'gri Raqam Kiritdingiz! Raqam Uzunligi 13 Xonalik Bo'lsin!")
    if number[4:6] not in codes:
        print("Siz Notog'ri Kompaniya Kodini Kiritdingiz!")
    if number not in phones.keys():
        return "Bunday Raqam Mavjud Emas!"
    if number in phones.keys() and number[0:4] == "+998" and len(number) == 13 and number[4:6] in codes and number in phones.keys():
        ismm = phones[number]["name"]
        raqam = phones[number]["number"]
        operator = phones[number]["kompaniya"]
        print(f"Ism: {ismm} \nRaqam: {raqam} \nOperator: {operator}")
        pul_miqdor = int(input("Qancha Pul To'lamoqchisiz?: "))
        ress = pul_miqdor / 100
        pul_miqdor += ress
        if cards[karta]["money"] >= pul_miqdor:
            phones[number]["money"] += pul_miqdor
            cards[karta]["money"] -= pul_miqdor
            print("Operatsiya Muvaffaqqiyatli Amalga Oshirildi!")
            res = f"Sizda {cards[karta]['money']} So'm Pul Qoldi!"
            with open("../tayyorlov/history.txt", "a") as appender:
                appender.write(f"Karta: {cards[karta]['number']} dan | {raqam} ga | {pul_miqdor} So'm Jonatildi! \n")
            return res
        else:
            res = f"Sizda Yetarli Mablag' Mavjud Emas!"
            return res

def payment_kommunal(kommunals: dict, cards: dict, karta: str):
    uy_kommunal = input("Id Raqam: ")
    if uy_kommunal in kommunals.keys():
        narx = kommunals[uy_kommunal]["oylik tolov"]
        uy = kommunals[uy_kommunal]["xonadon"]
        qarz = kommunals[uy_kommunal]["qarz"]
        print(f"Xonadon: {uy} \t | Qarzdorlik: {qarz} \t | Oylik To'lov: {narx}")
        tolov = int(input("To'lov Puli: "))
        foiz = tolov / 100
        tolov += foiz
        if tolov >= narx:
            cards[karta]["money"] -= tolov
            kommunals[uy_kommunal]["money"] += tolov
            return f"Operatsiya Muvaffaqqiyatli Amalga Oshirildi! Sizda: {cards[karta]['money']} so'm Pul Qoldi!"
        else:
            text = f"Tolov Puli {kommunals[uy_kommunal]['money']} so'm"
            with open("../tayyorlov/history.txt", "a") as appender:
                appender.write(f"Karta: {cards[karta]['number']} dan | {uy_kommunal} ga | {tolov} So'm Pul To'landi! \n")
            return text
    else:
        text = "Bunday Id Raqam Topilmadi!"
        return text

def show_history():
    with open("../tayyorlov/history.txt", "r") as reader:
        res = reader.readlines()
        return res
