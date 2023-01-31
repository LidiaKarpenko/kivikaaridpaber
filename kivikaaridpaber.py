import random
 
while True:
    teie_valik = input("tehke valik — kivi, kaarid voi paber: ")
    võimalik_valikud = ["kivi", "paber", "kaarid"]
    bot_valik = random.choice(võimalik_valikud)

    print(f"\nTe valisite {teie_valik}, bot valis {bot_valik}\n")

    if teie_valik == bot_valik:
        print(f"Mõlemad kasutajad on valinud {teie_valik}. viit!")
    elif teie_valik == "kivi":
        if bot_valik == "kaarid":
            print("kivi loob kaarid! te voitsite!")
        else:
            print("paber mahib kivi umber! te kaotasite.")
    elif teie_valik == "paber":
        if bot_valik == "kivi":
            print("paber mahib kivi! te voitsite!")
        else:
            print("kaarid lõikavad paberit! te kaotasite.")
    elif teie_valik == "kaarid":
        if bot_valik == "paber":
            print("kaarid lõikavad paberit! te voitsite!")
        else:
            print("kivi loob kaarid! te kaotasite.")
    mang_veel = "" 
    mang_veel = input("mangime veel kord? (jah/ei): ") 
    if mang_veel == "jah": 
        continue
    else:
        break