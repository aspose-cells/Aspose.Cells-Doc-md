---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /tr/java/java-security-invalidkeyexception/
---

## **Özet**
Varsayılan olarak, AES 128 bit anahtarını destekler, eğer 192 bit veya 256 bit anahtar kullanmayı planlıyorsanız, java derleyicisi Illegal key size exception hatası atacaktır. Bu Aspose.Cells API'nın bir hatası değil, JDK/JRE'nin kısıtlı özelliklerinden kaynaklanmaktadır. JDK/JRE'nin varsayılan politika dosyaları bazı ülkelerdeki ithalat kısıtlamaları nedeniyle kısıtlanmıştır. Kullanıcıların gelişmiş şifreleme/şifre çözme işlevselliğini kullanabilmek için 'Sınırsız Güçlük' politika dosyalarını indirip JRE'lerine yüklemeleri gerekmektedir.
## **Belirtiler**
Korunan bir elektronik tabloyu yüklerken java.security.InvalidKeyException: Illegal key size veya varsayılan parametreler veya java.security.InvalidKeyException: Illegal key size alabilirsiniz. 
## **Çözüm**
Çözüm aslında aşağıda detaylı olarak belirtilmiştir.

1. Java Kriptografi Uzantısı (JCE) Sınırsız Güçlük Yetki Politika Dosyalarını indirin.
1. İndirilen arşivden JAR dosyalarını çıkarın ve bunları ${java.home}/jre/lib/security/ dizinine yerleştirin.
1. Programı yeniden çalıştırın.
## **İndirme Bağlantıları**
Lütfen JDK/JRE sürümünüze uygun indirme bağlantısını kullanın.

- [Java Kriptografi Uzantısı (JCE) Sınırsız Güçlük Yetki Politika Dosyaları 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Kriptografi Uzantısı (JCE) Sınırsız Güçlük Yetki Politika Dosyaları 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Kriptografi Uzantısı (JCE) Sınırsız Güçlük Yetki Politika Dosyaları 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
