---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /tr/java/java-security-invalidkeyexception/
---
## **Özet**
Varsayılan olarak, AES 128 bitlik bir anahtarı destekler, 192 bitlik veya 256 bitlik bir anahtar kullanmayı planlıyorsanız, java derleyici Geçersiz anahtar boyutu istisnası atar. Bunun nedeni Aspose.Cells API'deki bir hata değil, JDK/JRE'nin kendisinin sınırlı özelliğidir. Bazı ülkelerdeki ithalat kısıtlamaları nedeniyle JDK/JRE'nin varsayılan ilke dosyaları sakatlanmıştır. Kullanıcıların, şifreleme/şifre çözme için gelişmiş kriptografi işlevselliğini kullanmak üzere "Sınırsız Güç" ilke dosyalarını almaları ve bunları JRE'lerine yüklemeleri gerekir.
## **belirtiler**
 Korumalı bir elektronik tablo yüklerken java.security.InvalidKeyException: Illegal key size or default parameter veya Java.security.InvalidKeyException: Illegal key size alabilirsiniz.
## **Çözüm**
Çözüm aslında aşağıda detaylandırıldığı gibi çok basit.

1. Java Kriptografi Uzantısı (JCE) Sınırsız Güç Yetkisi Politikası Dosyalarını indirin.
1. JAR dosyalarını indirilen arşivden çıkarın ve ${java.home}/jre/lib/security/ dizinine yerleştirin.
1. Programı yeniden çalıştırın.
## **Bağlantılar İndir**
Lütfen JDK/JRE sürümünüze karşılık gelen indirme bağlantısını kullanın.

- [Java Kriptografi Uzantısı (JCE) Sınırsız Güç Yargı Yetkisi Politikası Dosyaları 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Kriptografi Uzantısı (JCE) Sınırsız Güç Yargı Yetkisi Politikası Dosyaları 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Kriptografi Uzantısı (JCE) Sınırsız Güç Yargı Yetkisi Politikası Dosyaları 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
