---
title: Kurulum ve Kurulum Yönergeleri
type: docs
weight: 20
url: /tr/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: Java aracılığıyla PHP için Aspose.Cells kurulumu ve kurulum yönergeleri
---
## **sistem gereksinimleri**
Java aracılığıyla PHP için Aspose.Cells, platformdan bağımsızdır API ve herhangi bir platformda (Windows, Linux, MacOS vb.) kullanılabilir.[PHP](https://www.php.net/downloads.php)veya daha büyük sürümler kurulur. Kurulumu kurmadan önce makinede Oracle JDK 7 veya üzeri sürümler bulunmalıdır.
## **Kurulum ve Kullanım**
PHP için Aspose.Cells, Java aracılığıyla bir ZIP arşivi olarak dağıtılır.

Ortamı kurmak için, Java aracılığıyla PHP için Aspose.Cells'i yükleyin ve kullanın, talimatları izleyin:
### **Linux:**
- İndirmek[PHP](https://www.php.net/downloads.php)kaynak ve yükleyin. Veya ikili php yüklemek için “sudo apt install php-xxx” komutunu kullanın.
- Linux için Oracle JDK (1.7 veya 1.8) yükleyin, Java_HOME ortam değişkenini yapılandırın.
- "Aspose.Cells for PHP via Java" API'i indirin/alın ve ayıklayın. "aspose.cells" adında bir klasör olacak.
- PHP/Java Bridge ikili dosyasını (JavaBridge.jar) http://php-java-bridge.sourceforge.net/pjb/download.php adresinden indirin ve "aspose.cells" klasörüne kaydedin.
- Java/Java.inc PHP kitaplığını (Java.inc) http://php-java-bridge.sourceforge.net/pjb/download.php adresinden indirin ve "aspose.cells" klasörüne kaydedin.
- Aşağıdaki komutla yukarıdaki klasörde “PHP/Java Bridge” çalıştırın.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_YEREL:8080 >/dev/null 2>&1 &|
|:- |
- Örneği aşağıdaki komutla çalıştırmak için "aspose.cells" klasöründeki "example.php" dosyasını çalıştırın:

|$ php örneği.php|
|:- |
### **Windows:**
- İndirmek[PHP](https://www.php.net/downloads.php)windows ikili dosyasını açın ve PATH'e "php.exe" ekleyin.
- Windows için Oracle JDK'yi (1.7 veya 1.8) yükleyin ve Java_HOME ortam değişkenini yapılandırın.
- "Aspose.Cells for PHP via Java" API dosyasını indirin ve ayıklayın. "aspose.cells" adında bir klasör olacak.
- PHP/Java Bridge ikili dosyasını (JavaBridge.jar) http://php-java-bridge.sourceforge.net/pjb/download.php adresinden indirin ve "aspose.cells" klasörüne kaydedin.
- Java/Java.inc PHP kitaplığını (Java.inc) http://php-java-bridge.sourceforge.net/pjb/download.php adresinden indirin ve "aspose.cells" klasörüne kaydedin.
- Aşağıdaki komutla yukarıdaki klasörde “PHP/Java Bridge” çalıştırın. Köprü başladığında 8080 http listener portunu seçin ve OK butonuna tıklayın.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Örneği aşağıdaki komutla çalıştırmak için "aspose.cells" klasöründeki "example.php" dosyasını çalıştırın:

|> php örneği.php|
|:- |
### **Mac:**
- Düzenlemek[PHP](https://www.php.net/downloads.php).
- Mac için Oracle JDK (1.7 veya 1.8) kurun, Java_HOME ortam değişkenini yapılandırın.
- "Aspose.Cells for PHP via Java" API dosyasını indirin ve ayıklayın. "aspose.cells" adında bir klasör olacak.
- PHP/Java Bridge ikili dosyasını (JavaBridge.jar) http://php-java-bridge.sourceforge.net/pjb/download.php adresinden indirin ve "aspose.cells" klasörüne kaydedin.
- Java/Java.inc PHP kitaplığını (Java.inc) http://php-java-bridge.sourceforge.net/pjb/download.php adresinden indirin ve "aspose.cells" klasörüne kaydedin.
- Aşağıdaki komutla yukarıdaki klasörde “PHP/Java Bridge” çalıştırın. Köprü başladığında 8080 http listener portunu seçin ve OK butonuna tıklayın.

|$$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Örneği aşağıdaki komutla çalıştırmak için "aspose.cells" klasöründeki "example.php" dosyasını çalıştırın:

|$ php örneği.php|
|:- |


