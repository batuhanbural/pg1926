<h1 align="center">OHEKA (Omurilik Hastalarının Engellerini Kaldıran Araç)</h1>

> ***OHEKA (Omurilik Hastalarının Engellerini Kaldıran Araç)*** genel anlamda omurilik hastalarının öz güvenini arttırmak, bir şeyleri başarmanın verdiği haz ile hayata daha güçlü bağlanmalarını sağlamak amacıyla tasarlanmış bir nevi tekerlekli sandalyedir. Engelli bireylerin teknolojiden yararlanarak özgürlüklerine kavuşmalarını, onların öz güvenini arttırmayı ve başarmanın verdiği hazzı onlara yaşatmayı istiyoruz. Bu amaç doğrultusunda çalışan ekibimiz, engelli bireylerin (bakıcı gözetimi olmadan) özgürce hareket edebilmesi için bir araç üretmeyi hedeflemektedir. Söz konusu araç, engelli bireyin yüzünü algılayarak algılanan kişinin kafa hareketiyle tekerlekli sandalyenin kontrol edilmesi üzerine tasarlanmaktadır.

## *oheka.py* gereksinimleri
```pip
opencv-python 4.4.0.46
numpy 1.20.0rc1
```

## *oheka.py* kullanımı

_oheka.py_ dosyası nasıl kullanılır.


![ex2 (3)](https://user-images.githubusercontent.com/60934501/101936564-bed94800-3bf1-11eb-90b7-84e449c20e06.gif)


### Sending messages

`login()` : Use for login to your account.

`get_main_page()` : Use for reach the home page of instagram.

- ###### If you don't use this code you can get some errors.

`reply_message()` : Use for add targets to message list.

`send_message()` : Use for send message to targets.

###### The sample usage of code below. :point_down:

```python
from instagram import Instagram

# Create an Instagram object.
intgrm = Instagram("Your username", "Your password")

# Login to your account.
intgrm.login() 

# Send message to target.
intgrm.get_main_page()
intgrm.reply_message(["List of targets"])
intgrm.send_message("Your message")
```

### Unfollow all users

`unfollow_all()` : Use for  __unfollow all users__.

###### The sample usage of code below. :point_down:

```python
from instagram import Instagram

# Create an Instagram object.
intgrm = Instagram("Your username", "Your password")

# Login to your account.
intgrm.login() 

# Reach the homepage and unfollow all.
intgrm.get_main_page()
intgrm.unfollow_all()
```

## ✨ Usage of WhatsApp

This is how to use whatsapp.py

### Spam messages

It is easy to send message with this code!

`login()` : Use for login your WhatsApp acoount. (In this part it will ask you for scan the QR code. And if you ***don't
scan the QR code*** code will **__not__** continue.)

`spam_messages()` : Use for spam messages to target.

###### The sample usage of code below. :point_down:

```python
from whatsapp import Whatsapp

# Create an Whatsapp object.
wp = Whatsapp()

# Login to your account. 
wp.login()

# Spam messages
wp.spam_messages("Target", "Spam message", spam_count)
```
