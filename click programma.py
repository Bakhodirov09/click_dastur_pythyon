from utils import karta_tekshirish, payment_card

import random

random_son = random.randint(1000, 9999)

cards = {
    "9860999977774444": {
        "name": "Nurulloh Bahodirov",
        "money": 2000000,
        "date": "10/25",
        "number": "8600999977774444",
        "password": 1232,
        "turi": "Humo"
    },
    "8600994577774444": {
        "name": "Alijon Valijanov",
        "money": 5000000,
        "date": "01/27",
        "number": "8600994577774444",
        "password": 1112,
        "turi": "Uzcard"
    },
    "8600988977774444": {
        "name": "Qahhor Namozov",
        "money": 3000000,
        "date": "11/28",
        "number": "8888988977774444",
        "password": 1212,
        "turi": "Uzcard"
    }
}

phones = {
    "+998959491108": {
        "name": "Baxodirov Nurulloh",
        "money": 0,
        "number": "+998959491108",
        "kompaniya": "Uztelecom"
    },
    "+998946795107": {
        "name": "Ziyavutdinov Shukurulloh",
        "money": 2000,
        "number": "+998946795107",
        "kompaniya": "Ucell"
    },
    "+998903457808": {
        "name": "Ziyavutdinova Zulxumor",
        "money": 0,
        "number": "+998903457808",
        "kompaniya": "Beeline"
    },
    "+998909744131": {
        "name": "Sodiqova Surayyo",
        "money": 10000,
        "number": "+998909744131",
        "kompaniya": "Beeline"
    }
}

kommunals = {
    "84123ziy": {
        "xonadon": "8-Hudud-41-Dom-23-Xonadon",
        "oylik tolov": 2000000,
        "money": 0,
        "qarz": 0
    }
}

kodlar = ["90", "91", "93", "94", "95", "97", "98", "99", "33"]

print("Clickga Ro'yxatdan O'tish Uchun Tel Raqam Kiriting")
count = 1
while True:
    tel_sorash = input("Telefon Raqam Kiriting: ")
    if len(tel_sorash) < 13 or len(tel_sorash) > 13:
        print("Kiritilgan Raqam Uzunligi Minimal 13 Xonalik Bo'lsin!")
    if tel_sorash[0:4] != "+998":
        print("Siz O'zbekiston Raqamini Kiritmadingiz!")
    if tel_sorash[4:6] not in kodlar:
        print("Siz Notog'ri Kompaniya Kodini Kiritdingiz!")
    if len(tel_sorash[6:13]) != 7:
        print("Siz Noto'g'ri Raqam Kiritdingiz!")
    if len(tel_sorash) == 13 and tel_sorash[0:4] == "+998" and tel_sorash[4:6] in kodlar and len(tel_sorash[6:13]) == 7:
        print("Telefon Raqam Tog'ri!")
        print("Clickga Xush Kelibsiz!Biz Telefoningizga Kod Yubordik Shuni Kiriting: ")
        print("\n")
        print("\n")
        print(f"Sizning Kodingiz: {random_son} \nBuni Hech Kimga Aytmang!")
        while True:
            kod = int(input("Kodni Kiriting: "))
            if kod != random_son:
                print(f"Siz Kiritgan {kod} Notogri Kod!")
            else:
                print("Clickga Xush Kelibsiz!")
                while True:
                    karta = input("Karta Raqamingizni kiriting: ")
                    res = karta_tekshirish(cards, karta, phones, kodlar, kommunals)
                    print(res)

