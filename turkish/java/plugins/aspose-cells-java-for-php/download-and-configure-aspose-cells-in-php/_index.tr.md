---
title: PHP'de Aspose.Cells'i İndirin ve Yapılandırın
type: docs
weight: 10
url: /tr/java/download-and-configure-aspose-cells-in-php/
---
## **Gerekli Kitaplıkları İndirin**
Aşağıda belirtilen gerekli kütüphaneleri indirin. Bunlar Aspose.Cells Java for PHP örneklerini çalıştırmak için gereklidir.

- **Aspose:** [Aspose.Cells for Java Bileşen](https://downloads.aspose.com/cells/java/)
- [PHP/Java Köprü](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Sosyal Kodlama Sitelerinden Örnekler İndirin**
Çalışan örneklerin aşağıdaki yayınları, aşağıda belirtilen sosyal kodlama sitelerinden indirilebilir:

-----
### **GitHub**
- **Aspose.Cells Java for PHP Örnekler** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Linux Platformunda kaynak kodu nasıl yapılandırılır**
Kullanırken kaynak kodunu açmak ve genişletmek için lütfen şu basit adımları izleyin:
## **1. Tomcat Sunucusunu Kurun**
 Tomcat sunucusunu kurmak için linux konsolunda aşağıdaki komutu verin. Bu, Tomcat sunucusunu başarıyla yükleyecektir.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. PHP/JavaBridge'i İndirin ve Yapılandırın**
 PHP/JavaBridge ikili dosyalarını indirmek için linux konsolunda aşağıdaki komutu verin.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Linux konsolunda aşağıdaki komutu vererek PHP/JavaBridge ikili dosyalarını açın.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Bu ayıklayacak**JavaBridge.savaş**dosya. Tomcat88'e kopyalayın**ağ uygulamaları** Linux konsolunda aşağıdaki komutu vererek klasör.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


Tomcat8 kopyalayarak otomatik olarak yeni bir klasör oluşturacaktır "**Java Köprüsü**" içinde**ağ uygulamaları**. Klasör oluşturulduktan sonra, Tomcat8'inizin çalıştığından emin olun ve ardından kontrol edin.<http://localhost:8080/JavaBridge> tarayıcıda, varsayılan bir JavaBridge sayfası açmalıdır.

 Herhangi bir hata mesajı görünürse, yükleyin**HızlıCGI**Linux konsolunda aşağıdaki komutu vererek.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

php5.5 cgi'yi kurduktan sonra Tomcat8 sunucusunu yeniden başlatın ve kontrol edin<http://localhost:8080/JavaBridge>tekrar tarayıcıda.

Eğer**Java_HOME**hatası görüntüleniyorsa, /etc/default/tomcat8 dosyasını açın ve Java_HOME'u ayarlayan satırın açıklamasını kaldırın. Tarayıcıda <http://localhost:8080/JavaBridge> öğesini tekrar kontrol edin, PHP/JavaBridge Örnekleri sayfasıyla gelmelidir.
## **3. Yapılandırma Aspose.Cells Java for PHP Örnekler**
 Webapps/JavaBridge klasörü içinde aşağıdaki komutları vererek PHP örneklerini klonlayın.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Windows Platformunda kaynak kodu nasıl yapılandırılır**
Windows Platformunda PHP/Java Bridge'i yapılandırmak için lütfen aşağıdaki basit adımları izleyin.

\1. PHP5'i yükleyin ve normalde yaptığınız gibi yapılandırın
\2. Henüz sahip değilseniz JRE 6'yı (Java Çalışma Zamanı Ortamı) yükleyin. Bunu C:\Program Files vb. içinden kontrol edebilirsiniz. Buradan indirebilirsiniz. PHP Java Bridge (PJB) ile uyumlu olduğu için JRE 6 kullanıyorum.

\3. Apache Tomcat 8.0'ı kurun. buradan indirebilirsiniz

 4.İndir[JavaBridge.savaş](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Bu dosyayı Tomcat webapps dizinine kopyalayın.
(ör: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Tomcat apache hizmetini yeniden başlatın.

 6. Git<http://localhost:8080/JavaBridge/test.php> php çalışıp çalışmadığını kontrol etmek için. diğer örnekleri orda bulabilirsin

7. Aspose.Cells Java jar dosyanızı C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib konumuna kopyalayın

 \8. Klon[Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ klasörü içindeki örnekler.

\8. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java klasörünü Aspose.Cells Java for PHP örnekler klasörünüze kopyalayın.

 \10. Apache Tomcat hizmetini yeniden başlatın ve örnekleri kullanmaya başlayın.
