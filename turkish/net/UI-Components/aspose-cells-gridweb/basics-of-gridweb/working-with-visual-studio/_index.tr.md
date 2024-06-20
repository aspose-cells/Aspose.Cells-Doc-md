---
title: Visual Studio ile Çalışma
type: docs
weight: 20
url: /tr/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: Bu makale, GridWeb i visual stüdyoda nasıl kullanılacağını tanıtır.
---

{{% alert color="primary" %}} 

Bu konu, ASP.Net uygulamalarında Visual Studio.NET 2005 kullanılarak Aspose.Cells.GridWeb'in nasıl kullanılacağını açıklar. Bu konu, Aspose.Cells.GridWeb ile çalışan başlangıç düzeyindeki geliştiriciler için faydalıdır.

{{% /alert %}} 
## **Visual Studio 2013 Kullanarak Aspose.Cells.GridWeb ile Çalışma**
Bu konu, Visual Studio 2013'te bir örnek web sitesi oluşturarak Aspose.Cells.GridWeb'i nasıl kullanacağını gösterir. İşlem adımlara bölünmüştür.
### **Adım 1: Yeni Web Sitesi Oluşturma**
1. Visual Studio 2013'ü açın.
1. **Dosya** menüsünden **Yeni** menüsünü seçin, ardından **Web Sitesi**'ni seçin. 

![todo:image_alt_text](working-with-visual-studio_1.png)


Yeni Web Sitesi iletişim kutusu açılır. 

1. Visual Studio yüklü şablonlardan **ASP.NET Web Forms Sitesi**'ni seçin.
1. Web sitesi konumu için HTTP modunu seçin. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Web sitesi dosyalarının oluşturulacağı ve depolanacağı bir konum belirtin. 
   1. Yeni Web Sitesi iletişim kutusunda **Gözat**'a tıklayın. 

![todo:image_alt_text](working-with-visual-studio_3.png)



Konum Seç iletişim kutusu görüntülenir. 

1. **Yerel IIS** sekmesine tıklayın.
   IIS kök klasöründe depolanan tüm klasörler ve web uygulamaları görüntülenir (örneğin: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Şimdi, web sitesi dosyalarının depolanacağı yerel IIS'de yeni bir web uygulaması oluşturun.
   Konum Seçme iletişim kutusu, yerel IIS'de web uygulamaları veya sanal dizinler oluşturmanıza veya silmenize izin verir. Bir web uygulaması oluşturmak için, aşağıdaki şekilde gösterildiği gibi bir düğmeye tıklayın. 

![todo:image_alt_text](working-with-visual-studio_5.png)



Varsayılan adı WebSite olan yeni bir web uygulaması oluşturulur. 

1. Web uygulamasının adını değiştirin. Biz ona GridWebOn2013 olarak yeniden adlandırdık.
1. **Aç**'a tıklayın. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Visual Studio'nun bir web sitesi oluşturmasına izin vermek için **Tamam**'a tıklayın. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Adım 2: Bir Web Sayfasının Kaynak ve Tasarım Görünümlerini Kontrol Etme**
Visual Studio 2013 tarafından varsayılan bir web sitesi oluşturulmuş olacak. Bazı sahte metin ve işaretleme içeren default.aspx web sayfasını içerir. 

**default.aspx sayfasının kaynak görünümü** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Tüm web sayfaları (ASP.NET dahil) iki modda açılabilir. Birincisi geliştiricilere kaynak koduna erişme ve değiştirme imkanı veren kaynak görünümdür. İkinci mod ise WYSIWYG şekilde web sayfalarını tasarlamak için kullanılan tasarım görünümüdür. Yukarıdaki ekran görüntüsü, default.aspx web sayfasının kaynak görünümünü gösterir. Tasarım görünümünü görmek için **Tasarım**'a tıklayın. 

**default.aspx sayfasının tasarım görünümü** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Visual Studio tarafından eklenen Default.aspx sayfasını silin ve yeni boş bir Default.aspx sayfası ekleyin.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Adım 3: Bir Web Sayfasına Aspose.Cells.GridWeb Eklemek**
Aspose.Cells.GridWeb (veya GridWeb) denetimini, araç kutusundan sürükleyerek bir web sayfasına kolayca ekleyebilirsiniz. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Aspose.Cells.GridWeb'i araç kutusuna nasıl ekleyeceğiniz hakkında bilginiz yoksa, [Visual Studio.NET ile Aspose.Cells Grid Kontrollerini Entegre Etmek](/cells/tr/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/) sayfasına bakın. 

{{% /alert %}} 

GridWeb denetimi bir web sayfasına sürüklenirse şöyle görünecektir: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Tüm etiketi seçin. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Adım 5: Aspose.Cells.GridWeb Denetimini Yeniden Boyutlandırma**
GridWeb denetimini web sitesine sürükledikten sonra genişlik ve yüksekliğini değiştirebilirsiniz. 

Tasarım görünümünde, GridWeb'in genişliğini ve yüksekliğini yeniden boyutlandırabilirsiniz. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Adım 6: Aspose.Cells.GridWeb Özelliklerini Yapılandırma**
Aspose.Cells.GridWeb özelliklerini Visual Studio 2013 IDE'nin sağ tarafındaki **Özellikler** düğmesine tıklayarak WYSIWYG şekilde yapılandırın. 
Bir Özellikler iletişim kutusu görüntülenir. 

![todo:image_alt_text](working-with-visual-studio_15.png)



Özellikler paneli, GridWeb'in görünümünü yapılandırmanızı ve diğer bazı özellikleri kontrol etmenizi sağlar.
### **Adım 7: İçinde Aspose.Cells.GridWeb Bulunan İlk Web Sitesini Çalıştırma**
Web sitesini derleyin ve çalıştırın. 

1. Ctrl+F5'e basarak veya **Hata Ayıklamayı Başlat**'a tıklayarak web sitesini doğrudan Visual Studio'dan çalıştırın. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Şimdi GridWeb denetimiyle oynamaya başlayabilirsiniz. 

**Aksiyon Halindeki GridWeb denetimi** 

![todo:image_alt_text](working-with-visual-studio_17.png)
