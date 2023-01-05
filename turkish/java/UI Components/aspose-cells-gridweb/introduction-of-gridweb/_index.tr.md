---
title: GridWeb'in Tanıtımı
type: docs
weight: 10
url: /tr/java/introduction-of-gridweb/
---
## **GridWeb Java Demoları için Aspose.Cells nasıl çalıştırılır**
{{% alert color="primary" %}} 

 GridWeb için Aspose.Cells Java demolarının çalıştırılması kolaydır. Sadece konuşlandırmanız gerekiyor**gridwebdemo.savaş** web sunucunuzda. Lütfen buradan demoları indirin[bağlantı](https://forum.aspose.com/uploads/discourse_instance3/22292).

Bu makalede, Apache Tomcat Sunucusunda GridWeb Java Demoları için Aspose.Cells'in nasıl çalıştırılacağı açıklanmaktadır.

{{% /alert %}} 
### **GridWeb Java Demolarını Çalıştırmak İçin Adım Adım Kılavuz**
1.  Çıkarmak**apache-tomcat-7.0.52.zip** herhangi bir dizinde, örneğin C:\Tomcat

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_1.png)



 Aşağıdaki anlık görüntü, Apache Tomcat sunucusunun çıkarılan dizinlerini ve dosyalarını gösterir.

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_2.png)



 Ortam değişkenini de ayarlamanız gerekebilir.**CATALINA_HOME** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_3.png)

1. Aç**erkek kedi kullanıcıları.xml** dosya.

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_4.png)

1. Bu kullanıcıyı ekle:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Burada kullanıcı adı tomcat ve şifre gizlidir.** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_5.png)

1.  çalıştır**başlangıç.bat** dosya.
 Apache Tomcat Sunucusunu çalıştıracaktır.

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_6.png)



**Bir komut penceresinde çalışan Tomcat sunucusu** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_7.png)

1.  Şimdi tarayıcıyı açın ve yazın**yerel ana bilgisayar: 8080**.
 Apache Tomcat web sayfası görüntülenir.

   **Apache Tomcat web sayfası** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_8.png)

1.  Tıklamak**Yönetici Uygulaması** ve kullanıcı adı ve şifreyi yazın. (Yukarıdaki gibi: erkek kedi, gizli)

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_9.png)

1.  bölüme ilerleyin**Dağıtılacak WAR dosyası** ve göz atın**gridwebdemo.savaş** dosya.
1.  Tıklamak**Dağıtmak**. 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_10.png)

1.  Araştır**gridwebdemo.savaş** dosya.

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_11.png)

1.  Tıklamak**Dağıtmak**. 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_12.png)

1.  Dağıtıldıktan sonra, tıklayın**/gridweb demosu** ve demoları çalıştırmaya başlayın.

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_13.png)


 GridWeb Demo sayfası görüntülenir.

**GridWeb Demo sayfası** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_14.png)

1.  Herhangi bir demoya tıklayın ve çalıştırın.

   **İçerik oluşturma demosu çalışıyor** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_15.png)



**Çalışma sayfaları demosu çalışıyor** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_16.png)



**HeaderBar ve CommandButton demosu çalışıyor** 

![yapılacaklar:resim_alternatif_metin](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - Demolar**
{{% alert color="primary" %}} 

Hızla çalışmaya başlamanız için, Aspose.Cells.GridWeb API'in nasıl kullanılacağını gösteren bir dizi kod örneği ve demo sağlıyoruz.

Lütfen demoları aşağıdaki bağlantıdan indirin:
[Aspose.Cells.GridWeb Demoları](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **Tarayıcı Özellikleri ve Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb, diğer web kontrolleri gibi JSP web sayfalarına gömülebilen GUI tabanlı bir web kontrolüdür. Web denetimiyle ilgili en önemli şey, tarayıcılar arası destek sağlamaktır. Aspose.Cells.GridWeb tarayıcılar arası destek sağlar.
### **Karşılaştırmak**
Aspose.Cells.GridWeb, Microsoft'in Internet Explorer'ında (IE) tamamen desteklenir. Ancak, diğer tarayıcılarda küçük sınırlamaları vardır. Bu konu, farklı tarayıcılar tarafından desteklenen özelliklerin ayrıntılı bir karşılaştırmasını sağlar.

|**İstemci Tarafı Özellikleri**|**Microsoft Internet Explorer**|**Google krom**|**Mozilla Firefox**|**Opera**|
|:- |:- |:- |:- |:- |
|Cell Bağlam Menüsü|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|İstemci Tarafı Doğrulaması|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Çift Tıklama Etkinliği|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Açılır liste (*ComboBox Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Açılır liste (*Açılır Menü Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formül Girişi/Düzenleme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satırları/Sütunları Dondur veya Çöz|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| köprüler (*Hücre Komut Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| köprüler (*URL Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Birleştir veya Ayır Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Çoklu Cells Kopyala/Yapıştır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Çoklu Cells Giriş/Düzenleme, Tek Geri Gönderme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayı Biçimi|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayfa Sayfalama|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Salt okunur Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Salt Okunur Satırlar/Sütunlar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Normal İfadeler Kullanarak Veri Doğrulama|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sütun Genişliğini Yeniden Boyutlandır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satır Yüksekliğini Yeniden Boyutlandır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satır ve Sütun Ekleme/Silme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|İçeriği Kaydır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayfa Sekmelerini Kaydır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cells'in Kenarlıklarını Ayarla|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cells Yazı Tipi Ayarlarını Ayarlayın|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Bir hücrenin bağlam menüsü yalnızca İstemci tarafı menü düğmesine tıklanarak etkinleştirilebilir.
