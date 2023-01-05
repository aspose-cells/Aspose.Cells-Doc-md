---
title: GridWeb'i Web Formuna Ekleme
type: docs
weight: 10
url: /tr/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

Bu konuda, yeni başlayanlara web uygulamalarında Aspose.Cells.GridWeb denetimi oluşturmalarına ve kullanmalarına yardımcı olacak temel bir adım adım kılavuz sağlanmaktadır.

{{% /alert %}} 
## **Aspose.Cells.GridWeb Denetimi Oluşturma ve Kullanma**
### **1. Adım: Bir Web Uygulama Projesi Oluşturma**
Öncelikle, Aspose.Cells.GridWeb kontrolünün kullanılacağı bir web uygulaması projesi oluşturun:

1. Visual Studio'yu açın.
1.  itibaren**Dosya** menü, seç**Yeni** bunu takiben**Proje**. 

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_1.png)



Yeni Bir Proje İletişim Kutusu görünür.

1.  Seçme**ASP.NET Web Uygulaması** istediğiniz dil için

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_2.png)

1.  Seçme**Web Formları** şablon.

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_3.png)

1. Projeye yeni bir web formu ekleyin.
### **2. Adım: Denetimi Web Formuna Katıştırma**
 Aspose.Cells.GridWeb denetimini Visual Studio araç kutusundan web formuna sürükleyip bırakın.

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

 Visual Studio Toolbox'a Aspose.Cells Kılavuz denetimlerinin nasıl ekleneceğini öğrenmek için lütfen okuyun[Aspose.Cells.Grid Kontrollerini Visual Studio.NET ile entegre edin](/cells/tr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

 Kontrol forma eklendiğinde şu şekilde işlenir:

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_5.png)
### **3. Adım: Denetimi Yeniden Boyutlandırma**
Form, varsayılan bir boyutta işlenir. Kenarlıkları veya köşeleri sürükleyerek boyutu ayarlayın.

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_6.png)
### **4. Adım: Kontrol Özelliklerini Ayarlama**
 Aspose.Cells.GridWeb kontrolü, çeşitli özellikler kullanılarak da yapılandırılabilir.

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_7.png)

Özellikler iletişim kutusu ile kontrolün birçok özelliğini ayarlamak mümkündür. Temel özellikler yükseklik, genişlik, renk ve görsel stilleri içerir. Gelişmiş özellikler, düzenleme modunu, oturum modunu ve çift tıklama modunu içerir. Ayrıca, Özellikler iletişim kutusunda özelleştirilmiş olay işleyicileri ayarlamak mümkündür.

Ayrıca, Aspose.Cells.GridWeb için, Özellikler iletişim kutusunun altında köprüler olarak görülebilen veya GridWeb denetiminde sağ tıklatarak bulunabilen bazı ekstra yapılandırma araçları da vardır. Bu yapılandırma araçları şunları içerir:

- Özel Komut Düğmeleri
#### **Özel Komut Düğmeleri**
Özel komut düğmeleri düzenleyicisini açmak için:
 GridWeb denetimine sağ tıklayın ve seçin**Özel Komut Düğmeleri**. 

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_8.png)



 CustomCommandButton Koleksiyon Düzenleyici iletişim kutusu görüntülenir.

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_9.png)

İletişim kutusu, geliştiricilerin GridWeb denetiminde özel komut düğmeleri eklemesine ve kaldırmasına olanak tanır.


### **Önemli**
Aspose.Cells.GridWeb, kaynak dosyalarına da denetim sağlar. "acw_client", dosyaları içeren bir klasördür (kurulum dizininiz). config dosyası, gömülü istemci kaynaklarını (resimler, komut dosyaları vb.) yönetmek için kullanılır.Ayrıca, GridWeb kontrolüne sahip web uygulamasını dağıtmanız gerektiğinde, "acw" dosyasını da kopyalarsınız._client" dizinini proje klasörünüze ekleyin, en azından web uygulamanız (sunucu üzerinden dağıtılan) onu bulamadı. Yapılandırma bölümüne aşağıdaki kod satırlarını ekleyerek (örn. VS.NET Projesi):



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

Yol her zaman projenin dizini ile ilişkilidir. Proje dizini dışında herhangi bir dizini kullanmamalısınız. Bu nedenle, "acw_client" dizinini (@GridWeb kurulum klasörünüz) projenin dizinine/alt dizinine kopyalamanız gerekir.

{{% /alert %}}
### **Adım 5: Web Uygulamasını Çalıştırma**
 Ctrl+F5 tuşlarına basarak veya tıklayarak uygulamayı çalıştırın.**Başlama** buton.

 Uygulama bir tarayıcıda çalıştığında, artık boş bir Aspose.Cells.GridWeb denetimi içeren WebForm1.aspx sayfası görüntülenir. Hücrelere tıklayarak değerler ekleyin. Bir satırın yüksekliğini veya bir sütunun genişliğini değiştirmek, hücre verilerini panoya kopyalamak (Ctrl+C) veya kesmek (Ctrl+X) ve verileri hücreye yapıştırmak (Ctrl+V) gibi diğer görevleri gerçekleştirmek de mümkündür. . Daha fazla işlem gerçekleştirmek için, seçeneklerin tam listesini görmek üzere kontrole sağ tıklayın.

**GridWeb kontrolünün içerik menüsü** 

![yapılacaklar:resim_alternatif_metin](add-gridweb-to-web-form_10.png)
