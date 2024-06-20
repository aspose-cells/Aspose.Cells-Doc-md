---
title: GridWeb Tanıtımı
type: docs
weight: 10
url: /tr/java/introduction-of-gridweb/
---
## **GridWeb Temelleri**
Aspose.Cells.GridWeb, JSP web sayfalarına veya java sunucusundaki herhangi bir html sayfasına gömülebilen GUI tabanlı bir web kontrolüdür. 
{{% alert color="primary" %}} 

Kullanımı kolay ve basittir.

Size çevrimiçi elektronik tablo dosyası düzenleyicisi oluşturmanıza hızlı bir şekilde yardımcı olur.

Ayrıca, MS excel dosyası ile %100 uyumlu olan tüm elektronik tablo format dosyalarını içe ve dışa aktarmayı destekler.

## **Aspose.Cells.GridWeb - Demolar**
{{% alert color="primary" %}} 

Hızlı bir şekilde başlamanız için Aspose.Cells.GridWeb API'sını nasıl kullanacağını gösteren bir dizi kod örneği ve demo sunuyoruz.

Lütfen aşağıdaki bağlantıdan demo'ları indirin:
[Aspose.Cells.GridWeb Demoları](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **Aspose.Cells for GridWeb Java Demolarını nasıl çalıştıracağınız**
{{% alert color="primary" %}} 

Aspose.Cells for GridWeb Java demo'ları kolayca çalıştırılabilir. Tek yapmanız gereken **gridwebdemo.war**'ı web sunucunuza dağıtmaktır. Lütfen demo'ları bu [bağlantıdan](https://forum.aspose.com/uploads/discourse_instance3/22292) indirin.

Bu makale, Aspose.Cells for GridWeb Java Demolarını Apache Tomcat Sunucusunda nasıl çalıştıracağınızı açıklar.

{{% /alert %}} 
### **GridWeb Java Demolarını Çalıştırmak İçin Adım Adım Kılavuz**
1. Herhangi bir dizine **apache-tomcat-7.0.52.zip**'i çıkarın, örneğin C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



Aşağıdaki ekran görüntüsü, Apache Tomcat sunucusunun çıkarılmış dizinlerini ve dosyalarını göstermektedir 

![todo:image_alt_text](introduction-of-gridweb_2.png)



Ayrıca **CATALINA_HOME** ortam değişkenini ayarlamanız gerekebilir 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. **tomcat-users.xml** dosyasını açın. 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Bu kullanıcıyı ekleyin:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Burada kullanıcı adı tomcat ve şifre secret'tir** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. **startup.bat** dosyasını çalıştırın.
   Bu, Apache Tomcat Sunucusunu çalıştıracaktır. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Komut penceresinde çalışan Tomcat sunucusu** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Şimdi tarayıcıyı açın ve **localhost:8080** yazın.
   Apache Tomcat web sayfası görüntülenir. 

   **Apache Tomcat web sayfası** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. **Yönetici Uygulaması**nı tıklayın ve kullanıcı adı ve şifre yazın. (Yukarıdaki gibi: tomcat, secret) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. **Yayınlamak için WAR dosyası** bölümüne kaydırın ve **gridwebdemo.war** dosyasını göz atın.
1. **Yayınla**'yı tıklayın. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. **gridwebdemo.war** dosyasını göz atın. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. **Yayınla**'yı tıklayın. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. Yayınlandıktan sonra **/gridwebdemo**'ya tıklayın ve demoları çalıştırmaya başlayın. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


GridWeb Demo sayfası görüntülenir. 

**The GridWeb Demo sayfası** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. Herhangi bir demo seçin ve çalıştırın. 

   **İçerik oluşturma demo çalışıyor** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Çalışma sayfaları demo çalışıyor** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar ve CommandButton demo çalışıyor** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
## **Tarayıcı Yetenekleri ve Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb, diğer web kontrolleri gibi JSP web sayfalarına gömülebilen bir GUI tabanlı web kontrolüdür. Web kontrolü hakkında en önemli şey, çapraz tarayıcı desteği sağlamaktır. Aspose.Cells.GridWeb, çapraz tarayıcı desteği sağlar.
### **Karşılaştırma**
Aspose.Cells.GridWeb, Microsoft'un Internet Explorer (IE)'da tamamen desteklenmektedir. Ancak, diğer tarayıcılarda bazı kısıtlamaları vardır. Bu konu, farklı tarayıcılar tarafından desteklenen özelliklerin detaylı bir karşılaştırmasını sağlar.

|**İstemci Tarafı Özellikleri**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Hücre İçeriği Menüsü|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|İstemci Tarafı Doğrulama|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Çift Tıklama Olayı|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList ( *ComboBox Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList ( *Açılır Menü Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formül Girişi/Düzenleme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satırları/Sütunları Sabitleme ya da Çözme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hyperlinkler ( *CellCommand Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hyperlinkler ( *URL Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hücreleri Birleştirme ya da Ayırma|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Birden Fazla Hücre Kopyalama/Yapıştırma|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Birden Fazla Hücre Girişi/Düzenleme, Tek Postback|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Numara Biçimi|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayfa Gezinme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Salt Okunur Hücreler|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Salt Okunur Satırlar/Sütunlar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Düzenli İfadeler Kullanarak Veri Doğrulama|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sütun Genişliğini Yeniden Boyutlandırma|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satır Yüksekliğini Yeniden Boyutlandırma|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satırlar ve Sütunlar Ekle/Sil|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|İçeriği Kaydır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayfa Sekmelerini Kaydır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hücre Sınırlarını Ayarla|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hücrenin Yazı Tipi Ayarlarını Belirle|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
