---
title: GridWeb'in Tanıtımı
type: docs
weight: 10
url: /tr/java/introduction-of-gridweb/
---
##  **GridWeb'in Temelleri**
 Aspose.Cells.GridWeb, JSP web sayfalarına veya java sunucusundaki herhangi bir html sayfasına gömülebilen GUI tabanlı bir web kontrolüdür.
{{% alert color="primary" %}} 

Kullanımı kolay ve basittir.

Elektronik tablo dosyası için hızlı bir şekilde çevrimiçi web düzenleyici oluşturmanıza yardımcı olur.

Ayrıca, MS Excel dosyasıyla %100 uyumlu olan her türlü elektronik tablo formatındaki dosyaların içe ve dışa aktarılmasını da destekler.

##  **Aspose.Cells.GridWeb - Demolar**
{{% alert color="primary" %}} 

Hızlı bir şekilde çalışmaya başlamanızı sağlamak için Aspose.Cells.GridWeb API'in nasıl kullanılacağını gösteren bir dizi kod örneği ve demo sağlıyoruz.

Lütfen demoları aşağıdaki bağlantıdan indirin:
[Aspose.Cells.GridWeb Demoları](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **GridWeb Java Demoları için Aspose.Cells nasıl çalıştırılır**
{{% alert color="primary" %}} 

 GridWeb için Aspose.Cells Java demolarının çalıştırılması kolaydır. Sadece konuşlandırmanız gerekiyor**gridwebdemo.war** web sunucunuzda. Lütfen demoları buradan indirin[bağlantı](https://forum.aspose.com/uploads/discourse_instance3/22292).

Bu makalede, Apache Tomcat Sunucusunda GridWeb Java Demoları için Aspose.Cells'in nasıl çalıştırılacağı açıklanmaktadır.

{{% /alert %}} 
###  **GridWeb'i Çalıştırmak İçin Adım Adım Kılavuz Java Demolar**
1.  Çıkarmak**apache-tomcat-7.0.52.zip** herhangi bir dizinde örneğin C:\Tomcat

![yapılacak şey:image_alt_text](introduction-of-gridweb_1.png)



 Aşağıdaki anlık görüntü Apache Tomcat sunucusunun çıkarılan dizinlerini ve dosyalarını göstermektedir

![yapılacak şey:image_alt_text](introduction-of-gridweb_2.png)



 Ayrıca ortam değişkenini de ayarlamanız gerekebilir.**CATALINA_HOME** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_3.png)

1.  Aç**Tomcat-users.xml** dosya.

![yapılacak şey:image_alt_text](introduction-of-gridweb_4.png)

1. Bu kullanıcıyı ekle:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Burada kullanıcı adı Tomcat ve şifre gizlidir** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_5.png)

1.  Çalıştır**başlangıç.bat** dosya.
 Apache Tomcat Sunucusunu çalıştıracaktır.

![yapılacak şey:image_alt_text](introduction-of-gridweb_6.png)



**Tomcat sunucusu bir komut penceresinde çalışıyor** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_7.png)

1. Şimdi tarayıcıyı açın ve *localhost:8080** yazın.
 Apache Tomcat web sayfası görüntülenir.

   **Apache Tomcat web sayfası** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_8.png)

1.  Tıklamak**Yönetici Uygulaması** ve kullanıcı adını ve şifreyi yazın. (Yukarıdaki gibi: erkek kedi, gizli)

![yapılacak şey:image_alt_text](introduction-of-gridweb_9.png)

1.  Bölüme doğru aşağı kaydırın**Dağıtılacak WAR dosyası** ve göz atın**gridwebdemo.war** dosya.
1.  *Dağıt**'ı tıklayın.

![yapılacak şey:image_alt_text](introduction-of-gridweb_10.png)

1. Araştır**gridwebdemo.war** dosya.

![yapılacak şey:image_alt_text](introduction-of-gridweb_11.png)

1.  *Dağıt**'ı tıklayın.

![yapılacak şey:image_alt_text](introduction-of-gridweb_12.png)

1.  Dağıtıldıktan sonra tıklayın**/gridwebdemo** ve demoları çalıştırmaya başlayın.

![yapılacak şey:image_alt_text](introduction-of-gridweb_13.png)


 GridWeb Demo sayfası görüntülenir.

**GridWeb Demo sayfası** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_14.png)

1.  Herhangi bir demoyu tıklayın ve çalıştırın.

   **İçerik demosu oluşturma çalışması** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_15.png)



**Çalışma sayfaları demosu çalışıyor** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar ve CommandButton demosu çalışıyor** 

![yapılacak şey:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **Tarayıcı Özellikleri ve Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb, diğer web kontrolleri gibi JSP web sayfalarına gömülebilen GUI tabanlı bir web kontrolüdür. Web kontrolüyle ilgili en önemli şey tarayıcılar arası destek sağlamaktır. Aspose.Cells.GridWeb tarayıcılar arası destek sağlar.
###  **Karşılaştırmak**
Aspose.Cells.GridWeb, Microsoft'in Internet Explorer'ında (IE) tam olarak desteklenir. Ancak diğer tarayıcılarda küçük sınırlamalar vardır. Bu konu, farklı tarayıcılar tarafından hangi özelliklerin desteklendiğine ilişkin ayrıntılı bir karşılaştırma sağlar.

|**İstemci Tarafı Özellikleri**|**Microsoft İnternet Explorer**|**Google Krom**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Cell Bağlam Menüsü|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|İstemci Tarafı Doğrulaması|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Çift Tıklama Etkinliği|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Açılır liste (*ComboBox Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Açılır liste (*Açılır Menü Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formül Girişi/Düzenleme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satırları/Sütunları Dondurun veya Çözün|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Köprüler (*HücreKomut Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Köprüler (*URL Modu* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Birleştir veya Ayır Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Çoklu Cells Kopyala/Yapıştır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Çoklu Cells Giriş/Düzenleme, Tek Geri Gönderme|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayı Formatı|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayfa Sayfalama|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Salt okunur Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Salt Okunur Satırlar/Sütunlar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Normal İfadeler Kullanarak Veri Doğrulama|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sütun Genişliğini Yeniden Boyutlandır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satır Yüksekliğini Yeniden Boyutlandır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Satır ve Sütun Ekle/Sil|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|İçeriği Kaydır|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sayfa Sekmelerini Kaydırın|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cells Kenarlıklarını Ayarla|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cells Yazı Tipi Ayarlarını Ayarlayın|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Bir hücrenin içerik menüsü yalnızca İstemci tarafı menü düğmesine tıklanarak etkinleştirilebilir.
