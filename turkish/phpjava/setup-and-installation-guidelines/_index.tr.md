---
title: Kurulum ve Kurulum Kılavuzları
type: docs
weight: 20
url: /tr/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "Aspose.Cells for PHP via Java ve kurulum kılavuzunu kuruluyor."
---



## **Sistem Gereksinimleri**
Aspose.Cells for PHP via Java platform bağımsız bir API'dir ve [PHP](https://www.php.net/downloads.php) 7 veya daha üst sürümlerinin yüklü olduğu herhangi bir platformda (Windows, Linux, MacOS vb.) kullanılabilir. Makinenin Oracle JDK 7 veya daha üst sürümlerine sahip olması kurulumdan önce gereklidir.
## **Kurulum ve Kullanım**
Aspose.Cells for PHP via Java ZIP arşivi olarak dağıtılır.

Çevre kurmak, Aspose.Cells for PHP via Java'ü yüklemek ve kullanmak için talimatları izleyin:
### **Linux:**
- [PHP](https://www.php.net/downloads.php) kaynağını indirin ve kurun. Veya, php ikili dosyasını yüklemek için “sudo apt install php-xxx” komutunu kullanın.
- Linux için Oracle JDK (1.7 veya 1.8) yükleyin, JAVA_HOME ortam değişkenini yapılandırın.
- "Aspose.Cells for PHP via Java" API'sini indirin ve çıkartın. "aspose.cells" adında bir klasör bulunacaktır.
- http://php-java-bridge.sourceforge.net/pjb/download.php adresinden PHP/Java Bridge ikili dosyasını (JavaBridge.jar) indirin ve "aspose.cells" klasörüne kaydedin.
- http://php-java-bridge.sourceforge.net/pjb/download.php adresinden java/Java.inc PHP kütüphanesini (Java.inc) indirin ve "aspose.cells" klasörüne kaydedin.
- Aşağıdaki komutla yukarıdaki klasörde “PHP/Java Bridge” çalıştırın.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- "aspose.cells" klasöründe "example.php"'yi aşağıdaki komutla çalıştırın:

|$ php example.php|
| :- |
### **Windows:**
- [PHP](https://www.php.net/downloads.php) Windows ikili dosyasını indirin ve "php.exe" dosyasını PATH'e ekleyin.
- Windows için Oracle JDK (1.7 veya 1.8) yükleyin ve JAVA_HOME ortam değişkenini yapılandırın.
- "Aspose.Cells for PHP via Java" API'sını indirin ve çıkarın. "aspose.cells" adında bir klasör olacak.
- http://php-java-bridge.sourceforge.net/pjb/download.php adresinden PHP/Java Bridge ikili dosyasını (JavaBridge.jar) indirin ve "aspose.cells" klasörüne kaydedin.
- http://php-java-bridge.sourceforge.net/pjb/download.php adresinden java/Java.inc PHP kütüphanesini (Java.inc) indirin ve "aspose.cells" klasörüne kaydedin.
- Yukarıdaki klasörde aşağıdaki komutla "PHP/Java Bridge"'i çalıştırın. Köprü başladığında 8080 http dinleyici bağlantı noktasını seçin ve Tamam düğmesine tıklayın.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- "aspose.cells" klasöründe "example.php"'yi aşağıdaki komutla çalıştırın:

|> php example.php|
| :- |
### **Mac:**
- [PHP](https://www.php.net/downloads.php) yükleyin.
- Mac için Oracle JDK (1.7 veya 1.8) yükleyin ve JAVA_HOME ortam değişkenini yapılandırın.
- "Aspose.Cells for PHP via Java" API'sını indirin ve çıkarın. "aspose.cells" adında bir klasör olacak.
- http://php-java-bridge.sourceforge.net/pjb/download.php adresinden PHP/Java Bridge ikili dosyasını (JavaBridge.jar) indirin ve "aspose.cells" klasörüne kaydedin.
- http://php-java-bridge.sourceforge.net/pjb/download.php adresinden java/Java.inc PHP kütüphanesini (Java.inc) indirin ve "aspose.cells" klasörüne kaydedin.
- Yukarıdaki klasörde aşağıdaki komutla "PHP/Java Bridge"'i çalıştırın. Köprü başladığında 8080 http dinleyici bağlantı noktasını seçin ve Tamam düğmesine tıklayın.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- "aspose.cells" klasöründe "example.php"'yi aşağıdaki komutla çalıştırın:

|$ php example.php|
| :- |


