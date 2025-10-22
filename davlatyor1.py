import random
tanlang = input("  (tosh, qaychi, qagoz) buladan birini tanlang:  ").lower()

uslublar = ["tosh", "qaychi", "qogoz"]
bot = random.choice(uslublar)
print(bot,tanlang)
if tanlang == bot:
    print("durrang")
elif (tanlang == "tosh" and bot == "qaychi") or \
     (tanlang == "qaychi" and bot == "qogoz") or \
     (tanlang == "qogoz" and bot == "tosh"):
    print("Siz yutdingiz!")
else:
    print("siz yutqazdingiz")
