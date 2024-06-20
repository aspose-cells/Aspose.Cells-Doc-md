---
title: Web Form a GridWeb Ekle
type: docs
weight: 10
url: /tr/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: Bu makale, GridWeb içinde web form ile nasıl çalışılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konu, başlangıç seviyesindeki kullanıcılara web uygulamalarında Aspose.Cells.GridWeb kontrolünü oluşturup kullanmalarına yardımcı olmak için temel adım adım kılavuz sağlar.

{{% /alert %}} 
## **Aspose.Cells.GridWeb Kontrolünü Oluşturma ve Kullanma**
### **Adım 1: Bir Web Uygulama Projesi Oluşturma**
İlk olarak, Aspose.Cells.GridWeb kontrolünü kullanacağınız bir web uygulama projesi oluşturun:

1. Visual Studio'u açın.
1. **Dosya** menüsünden, ardından **Proje**'yi seçin. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



Yeni Proje Dialog kutusu görüntülenir.

1. Arzu edilen dil için **ASP.NET Web Uygulaması**'nı seçin. 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. **Web Formları** şablonunu seçin. 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. Projeye yeni bir web form ekleyin.
### **Adım 2: Kontrolü Web Forma Gömme**
Aspose.Cells.GridWeb kontrolünü Visual Studio araç kutusundan web formuna sürükleyip bırakın. 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

Aspose.Cells Grid kontrollerini Visual Studio Aracı Kutusu'na nasıl ekleyeceğinizi öğrenmek için [Visual Studio.NET ile Aspose.Cells Grid Kontrolleri Entegre Etme](/cells/tr/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/)'yi okuyun.

{{% /alert %}} 

Kontrol form içine eklendiğinde, şu şekilde render edilir: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **Adım 3: Kontrolü Yeniden Boyutlandırma**
Form varsayılan bir boyutta render edilir. Kenarları veya köşeleri sürükleyerek boyutu ayarlayın. 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **Adım 4: Kontrol Özelliklerini Ayarlama**
Aspose.Cells.GridWeb kontrolü çeşitli özellikler kullanılarak yapılandırılabilir. 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

Özellikler ile ilgili birçok ayar, Yükseklik, Genişlik, Renk ve Görsel Stiller gibi temel özellikleri içerir. Gelişmiş özellikler arasında düzenleme modu, oturum modu ve çift tıklama modu bulunmaktadır. Ayrıca, özellikler diyaloğunda özel olay işleyicilerini ayarlamak da mümkündür.

Ayrıca, Aspose.Cells.GridWeb için bazı ek yapılandırma araçları, özelliklerin altında hiperbağlantılar olarak veya GridWeb kontrolüne sağ tıklanarak bulunabilir. Bu yapılandırma araçları şunları içerir:

- Özel Komut Düğmeleri
#### **Özel Komut Düğmeleri**
Özel komut düğmeleri düzenleyicisini açmak için:
GridWeb kontrolüne sağ tıklayın ve **Özel Komut Düğmeleri**'ni seçin. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



ÖzelKomutDüğme Koleksiyon Düzenleyici diyaloğu görüntülenir. 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

Bu diyalog, geliştiricilere GridWeb kontrolüne özel komut düğmeleri eklemelerine ve kaldırmalarına olanak tanır.


### **Önemli**
Ayrıca, Aspose.Cells.GridWeb, kontrol ile ilgili kaynak dosyalarını sağlar. "acw_client", iç konfigürasyonunu yönetmek ve diğer işlevleri gerçekleştirmek için bu klasörü kullanır, script dosyaları, görüntü dosyaları ve diğer dosyaları içerir. Ayrıca, GridWeb kontrolünü içeren web uygulamasını dağıtmanız gerektiğinde, "acw_client" klasörünü projeniz klasörüne eklemeniz gerekecektir (sunucu üzerine dağıtılan web uygulaması) ya da web uygulamanızın en azında bu klasörü bulamaz yanıt vermeyecektir. Kaynak klasörünü her zaman vs.net projenizdeki yapılandırma bölümüne ekleyerek belirtebilirsiniz. (Örn. web.config dosyası içinde)



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

Yol her zaman proje diziniyle ilgilidir. Projede olmayan hiçbir dizini kullanmamalısınız. Bu nedenle, "acw_client" dizinini (GridWeb kurulum klasörüne) proje dizini/alt dizinine kopyalamak gerekir.

{{% /alert %}}
### **Adım 5: Web Uygulaması Çalıştırma**
Uygulamayı Ctrl+F5'e basarak veya **Başlat** düğmesine tıklayarak çalıştırın. 

Uygulama bir tarayıcıda çalıştığında, WebForm1.aspx sayfası görüntülenir ve şimdi içinde boş bir Aspose.Cells.GridWeb kontrolü bulunmaktadır. Hücrelere değer eklemek için onlara tıklayabilirsiniz. Bir satırın yüksekliğini veya bir sütunun genişliğini değiştirme, hücre verilerini panoya kopyalama (Ctrl+C) veya kesme (Ctrl+X) ve yapıştırma (Ctrl+V) gibi diğer görevleri de gerçekleştirmek mümkündür. Daha fazla işlem yapmak için kontrolün üzerine sağ tıklayarak tüm seçeneklerin listesini görebilirsiniz. 

**GridWeb kontrolünün İçerik menüsü** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
