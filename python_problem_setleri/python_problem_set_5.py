import asyncio


class School:
    def __init__(self):
        pass

    class Teacher:
        def __init__(self):
            self.odev_verme = 80
            self.disiplin = 75
            self.yas_ort = 40

        def odev_ver(self):
            print("Ödev düşünülüyor.")
            asyncio.sleep(10)
            print("Ödeviniz sayfa 86'dan 150'ye kadar.\nYarın sabaha teslim ediniz.")

        def ceza_ver(self):
            print("Sözlün 50")

        def azarla(self):
            print("NEDEN ÖDEVİNİ YAPMADIN!")
            asyncio.sleep(3)
            self.ceza_ver()

        def dikkati_topla(self):
            print("EVET ARKADAŞLAR BU NOKTADA...")

    class Students:
        def __init__(self):
            self.zeka = 75
            self.eglence = 75
            self.disiplin = 75

        def odev_yap(self):
            print("Ödev yapmaya başlanılıyor.")
            asyncio.sleep(3)
            print("* Telefondan bildirim gelir!")
            asyncio.sleep(5)
            print("* Tuvalete gidilir.")
            asyncio.sleep(3)
            print("* Saat 11.23\nÖdev yapmaya başlanır!")
            asyncio.sleep(5)
            print("Ödev yapılamadı!")

    class Class:
        def __init__(self):
            pass

        def ders_dinle(self):
            print("zzzzzzZZZZZZzzzzZZZZzzz")

    class Lessons:
        def __init__(self):
            self.matematik = "012313"
            self.fen = "Hayvanlar alemi"
            self.felsefe = "Aristotales"


class GoynukFenLisesi(School):
    class Students:
        def __init__(self):
            self.zeka = 100

    class Teacher:
        def __init__(self):
            self.odev_verme = 110
            self.disiplin = 65
            self.yas_ort = 35

        class Class:
            def dersi_dinle(self):
                print("* Hocaya sorular sorulur.")
                asyncio.sleep(3)
                print("* Anlaşılmayan noktaların güzelce anlatılması beklenir")
                asyncio.sleep(5)
                print("Hocam bu soruya da bakar mısınız?")
                asyncio.sleep(3)
                print("Ders biter")


class AksuFenLisesi(School):
    class Class:
        def haylazlik(self):
            print("Hocam bugün ders işlemesek mi?")
            asyncio.sleep(5)
            print("* Hoca düşünür...")
            asyncio.sleep(20)
            print("Ders işlenir")


class GaziUniversitesi(School):
    class Class:
        def __init__(self):
            self.zeka = 100000
            self.renk = "Lacivert"
            self.kisi_sayisi = 50
            self.ogretmen_yas_ort = 50

        def proje_uret(self):
            proje_fikri = "Şaşılık Testi"
            proje_tamamlanma_suresi = "1 Ay"
            print(f"Projemiz: {proje_fikri}\nTamamlanma süresi yaklaşık {proje_tamamlanma_suresi}")