---
title: PHP için Aspose.Cells i İndirme ve Yapılandırma
type: docs
weight: 10
url: /tr/java/download-and-configure-aspose-cells-in-php/
---

## **Gerekli Kütüphaneleri İndirme**
Aşağıda belirtilen gerekli kütüphaneleri indirin. Bu, Aspose.Cells Java for PHP örneklerini yürütmek için gereklidir.

- **Aspose:** [Aspose.Cells for Java Bileşen](https://downloads.aspose.com/cells/java/)
- [PHP/Java Köprüsü](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Sosyal Kodlama Sitelerinden Örnekleri İndirme**
Aşağıda belirtilen sosyal kodlama sitelerinde çalıştırılan örneklerin indirilebilir sürümleri bulunmaktadır:

-----
### **GitHub**
- **Aspose.Cells Java için PHP Örnekleri** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Linux Platformunda kaynak kodunu nasıl yapılandıracağınız**
Kullanırken kaynak kodunu açmak ve genişletmek için lütfen aşağıdaki basit adımları izleyin:
## **1. Tomcat Sunucusu Kurma**
Tomcat sunucusunu kurmak için linux konsolunda aşağıdaki komutu verin. Bu, tomcat sunucusunu başarıyla kuracaktır. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. PHP/JavaBridge İndirme ve Yapılandırma**
PHP/JavaBridge ikililerini indirmek için linux konsolunda aşağıdaki komutu verin. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


PHP/JavaBridge ikililerini aşağıdaki komutu vererek linux konsolunda açın. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Bu, **JavaBridge.war** dosyasını açacaktır. Aşağıdaki komutu vererek dosyayı tomcat88 **webapps** klasörüne kopyalayın. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

Herhangi bir hata mesajı görünürse, aşağıdaki komutu linux konsolunda vererek **FastCGI**'yi kurun.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Aspose.Cells Java için PHP Örneklerini Yapılandırma**
Webapps/JavaBridge klasörü içinde aşağıdaki komutları vererek PHP örneklerini kopyalayın.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Windows Platformunda kaynak kodunun yapılandırılması**
Windows Platformunda PHP/Java Bridge'i yapılandırmak için lütfen aşağıdaki basit adımları takip edin

\1. PHP5'i yükleyin ve normalde yaptığınız gibi yapılandırın
\2. Eğer zaten yoksa JRE 6 (Java Çalışma Ortamı) yükleyin. Bunun C:\Program Files vb. klasörlerde olduğunu kontrol edebilirsiniz. İndirmek için buraya bakabilirsiniz. Ben PJB ile uyumlu olduğu için JRE 6 kullanıyorum.

\3. Apache Tomcat 8.0'ı yükleyin. Buradan indirebilirsiniz

4. [JavaBridge.war'ı](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download) indirin. Bu dosyayı tomcat webapps dizinine kopyalayın.
(örn: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Tomcat apache servisini yeniden başlatın.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Aspose.Cells Java jar dosyanızı C:\Program Dosyaları\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib dizinine kopyalayın

\8. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ klasörü içine [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) örneklerini klonlayın.

\8. Klasörü C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java'yı Aspose.Cells Java için PHP örneklerinizin klasörüne kopyalayın.

\10. apache tomcat servisini yeniden başlatın ve örnekleri kullanmaya başlayın. 
