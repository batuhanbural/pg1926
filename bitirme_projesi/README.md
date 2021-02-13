<h1 align="center">OHEKA (Omurilik Hastalarının Engellerini Kaldıran Araç)</h1>

> ***OHEKA (Omurilik Hastalarının Engellerini Kaldıran Araç)*** genel anlamda omurilik hastalarının öz güvenini arttırmak, bir şeyleri başarmanın verdiği haz ile hayata daha güçlü bağlanmalarını sağlamak amacıyla tasarlanmış bir nevi tekerlekli sandalyedir. Engelli bireylerin teknolojiden yararlanarak özgürlüklerine kavuşmalarını, onların öz güvenini arttırmayı ve başarmanın verdiği hazzı onlara yaşatmayı istiyoruz. Bu amaç doğrultusunda çalışan ekibimiz, engelli bireylerin (bakıcı gözetimi olmadan) özgürce hareket edebilmesi için bir araç üretmeyi hedeflemektedir. Söz konusu araç, engelli bireyin yüzünü algılayarak algılanan kişinin kafa hareketiyle tekerlekli sandalyenin kontrol edilmesi üzerine tasarlanmaktadır.

## *oheka.py* gereksinimleri
```pip
opencv-python 4.4.0.46
numpy 1.20.0rc1
```

## *oheka_rpi.py* gereksinimleri
```pip
opencv-python 4.4.0.46
numpy 1.20.0rc1
RPi.GPIO 
```

## ✨ Önemli Notlar 
```python
self.face_cascade = cv2.CascadeClassifier("HaarCascades/haarcascade_frontalface_default.xml")
self.eye_cascade = cv2.CascadeClassifier("HaarCascades/haarcascade_eye.xml")
```
Bölümlerinde .xml dosyalarının `oheka.py` dosyasının bulunduğu dizin altında `HaarCascades` adındaki dizin altına konmalıdır.

**oheka_rpi.py** dosyası raspberry pi ile kullanılması için yapılmıştır. Bu dosya ile gerçek bir tekerlekli sandalye gözler ve kafa hareketleri ile hareket ettirilebilmektedir.

## *oheka.py* kullanımı

oheka.py __iyi__ ve __yüzü eşit aydınlatan__ bir ışık altında kullanılmalıdır. Program çalışmaya başladıktan sonra __kişinin kafasını ilk saptadığı anda__ kafanın o anki konumunu kafanın __normal duruşu__ olarak almaktadır. Kişi _kafasını_ **ileri** götürdüğü anda araç **ileri gitmeye**, **geri** götürmeye başladığı anda **geriye**, **sağ gözünü** kapattığında **sağa**, **sol gözünü** kapattığında **sola** gitmektedir.

## OHEKA Galeri

![oheka_yeni](https://user-images.githubusercontent.com/60934501/107847919-9bed2f00-6e00-11eb-83b1-06c53382fd26.png)


