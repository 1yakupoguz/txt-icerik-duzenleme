#Aşağıdaki bulunan degistirilecekTxtlerinYolu değişkenini tırnak işaretlerine dikkat ederek kendi bilgisayarınızda labels klasörünün yoluyla değiştiriniz.
#Sonrasında tabelanızın index numarasına göre kaclaDegistirilecek değişkenini yine tırnak işaretine dikkat ederek düzenleyiniz.
import os

degistirilecekTxtlerinYolu="C:\\Users\\Yakup\\Resimler\\Yeniklasor\\"
kaclaDegistirilecek='23'

def degistirmeFonksiyonu(yol,data):
    if not os.path.exists(yol):
        raise FileNotFoundError("Geçersiz yol")
    if not isinstance(kaclaDegistirilecek, str):
        raise TypeError("kaclaDegistirilecek değişkenini tanımlarken tırnak koyunuz. Örnek kaclaDegistirilecek='22'")
    if not 0 <= int(kaclaDegistirilecek) <= 22:
        raise ValueError("kaclaDegistirilecek değişkeni 0 ile 22 aralığında olmalıdır")
    else:
        for (dirname, dirs, files) in os.walk(yol):
            for filename in files:
                if filename.endswith('.txt'):
                    with open(yol+filename,"r") as dosya:
                        dosyaIcerigi = dosya.readlines()
                        with open(yol+filename,"w") as dosya:
                            for icerik in dosyaIcerigi: 
                                if icerik.startswith("0 "):
                                    icerik=icerik.replace("0 ",data+" ",2)
                                dosya.write(icerik)


degistirmeFonksiyonu(degistirilecekTxtlerinYolu,kaclaDegistirilecek)
