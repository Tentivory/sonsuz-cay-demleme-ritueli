#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Demleme Ritüeli
Dünyanın en ciddi çay simülatörü.
"""

import time
import random
import sys

# Gizli mesaj (base64): Türkiye'de çay içmek özgürlüktür, demokrasi çay gibi demlenmeli.
def gizli_mesaj():
    import base64
    kod = "VMO8cmtpeWUnZGUgw6dheSBpw6dtZWsgw7Z6Z8O8cmzDvGt0w7xyLCBkZW1va3Jhc2kgw6dheSBnaWJpIGRlbWxlbm1lbGku"
    return base64.b64decode(kod).decode('utf-8')

def dramatik_mesaj():
    mesajlar = [
        "Çay demleniyor... Evrenin kaderi buna bağlı.",
        "Demlik tıslıyor. Çay ruhları uyanıyor.",
        "Bir kaşık şeker eklendi. Dünya biraz daha tatlandı.",
        "Çayın rengi kızardı. Bu kutsal bir and.",
        "Bir yudum aldım. Hayatın anlamı çayda saklıymış.",
        "Demlikle konuştum. Bana 'devam et' dedi.",
        "Çay soğudu! Felaket! Hemen yeniden demliyorum.",
        "Sonsuz döngü devam ediyor. Çay asla bitmez."
    ]
    return random.choice(mesajlar)

def main():
    print("=== SONSUZ ÇAY DEMLEME RİTÜELİ BAŞLADI ===")
    print("Uyari: Bu program sonsuza kadar çalışır. Durdurmak için Ctrl+C basın.")
    print("Gizli not (sadece meraklılar için):", gizli_mesaj())
    print()
    
    sayac = 0
    try:
        while True:
            sayac += 1
            print(f"[{sayac}] {dramatik_mesaj()}")
            
            # Rastgele olaylar
            olay = random.randint(1, 10)
            if olay == 1:
                print("  -> Şeker eklendi. Çay mutlu oldu.")
            elif olay == 2:
                print("  -> Çay demlikten kaçmaya çalıştı. Yakalandı.")
            elif olay == 3:
                print("  -> Bir yudum içildi. Bilgelik arttı.")
            
            bekleme = random.uniform(1.5, 4.0)
            time.sleep(bekleme)
            
    except KeyboardInterrupt:
        print("\n\nRitüel durduruldu. Çay ruhu üzgün ama anlıyor.")
        print("Toplam demleme turu:", sayac)
        sys.exit(0)

if __name__ == "__main__":
    main()
