---
title: Visual Studio ile Çalışmak
type: docs
weight: 20
url: /tr/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

Bu konuda, Visual Studio.NET 2005 kullanılarak ASP.NET uygulamalarında Aspose.Cells.GridWeb'in nasıl kullanılacağı açıklanmaktadır. Bu konu, Aspose.Cells.GridWeb ile çalışan başlangıç düzeyindeki geliştiriciler için yararlıdır.

{{% /alert %}} 
## **Visual Studio 2013'ü Kullanarak Aspose.Cells.GridWeb ile Çalışma**
Bu konu, Visual Studio 2013'te örnek bir web sitesi yaparak Aspose.Cells.GridWeb'in nasıl kullanılacağını gösterir. İşlem, adımlara ayrılmıştır.
### **1. Adım: Yeni Web Sitesi Oluşturma**
1. Visual Studio 2013'ü açın.
1.  itibaren**Dosya** menü, seç**Yeni Menü** , sonra**İnternet sitesi**. 

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_1.png)


 Yeni Web Sitesi iletişim kutusu açılır.

1.  Seçme**ASP.NET Web Formları Sitesi** Visual Studio yüklü şablonlardan.
1.  Web sitesinin konumu için HTTP modunu seçin.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_2.png)




1.  Web sitesi dosyalarının oluşturulacağı ve depolanacağı konumu belirtin.
 1. tıklayın**Araştır** Yeni Web Sitesi iletişim kutusunda.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_3.png)



 Konum Seç iletişim kutusu görüntülenir.

1.  Tıkla**Yerel IIS** sekme.
IIS kök klasörünüzde saklanan tüm klasörler ve web uygulamaları görüntülenir (örneğin: C:\Inetpub\wwwroot).

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_4.png)




1. Şimdi yerel IIS'nizde web sitesi dosyalarının depolanacağı yeni bir web uygulaması oluşturun.
 Konum Seç iletişim kutusu, yerel IIS'nizde web uygulamaları veya sanal dizinler oluşturmanıza ve silmenize olanak tanır. Bir web uygulaması oluşturmak için aşağıdaki şekilde gösterildiği gibi bir düğmeyi tıklayın.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_5.png)



 WebSite varsayılan adıyla yeni bir web uygulaması oluşturulur.

1. Web uygulamasını yeniden adlandırın. Adını GridWebOn2013 olarak değiştirdik.
1.  Tıklamak**Açık**. 

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_6.png)



 Yeni Web Sitesi iletişim kutusuna dönersiniz. Web sitesi konumunun yolu şu şekilde ayarlanmıştır:<http://localhost/GridWebOn2013>. 

1.  Tıklamak**TAMAM** Visual Studio'nun bir web sitesi oluşturmasına izin vermek için.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_7.png)
### **2. Adım: Bir Web Sayfasının Kaynak ve Tasarım Görünümlerini Kontrol Etme**
 Varsayılan bir web sitesi, Visual Studio 2013 tarafından oluşturulmuş olacaktır. Bu, bazı sahte metin ve işaretlemeler içeren bir default.aspx web sayfası içerir.

**default.aspx sayfasının kaynak görünümü** 

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_8.png)



Tüm web sayfaları (ASP.NET dahil) iki modda açılabilir. Biri, geliştiricilerin kaynak koduna erişmesine ve değiştirmesine izin veren kaynak görünümüdür. İkinci mod, web sayfalarını WYSIWYG tarzında tasarlamak için kullanılabilen tasarım görünümüdür. Yukarıdaki ekran görüntüsü default.aspx web sayfasının kaynak görünümünü göstermektedir. Tasarım görünümünü görüntülemek için tıklayın**Tasarım**. 

**default.aspx sayfasının tasarım görünümü** 

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_9.png)




Visual Studio tarafından eklenen Default.aspx sayfasını silin ve yeni bir boş Default.aspx sayfası ekleyin.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_10.png)
### **3. Adım: Aspose.Cells.GridWeb'i Web Sayfasına Ekleme**
 Aspose.Cells.GridWeb (veya GridWeb) kontrolünü araç kutusundan sürükleyerek bir web sayfasına ekleyebilirsiniz.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb'i araç kutusuna nasıl ekleyeceğinizi bilmiyorsanız, bkz.[Aspose.Cells Izgara Denetimlerini Visual Studio.NET ile entegre edin](/cells/tr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

 GridWeb kontrolü web sayfasına bırakıldığında, şöyle görünür:

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_12.png)



### **4. Adım: <!DOCTYPE> etiketini değiştirin**
1.  Kaynak görünüme geçin ve aşağıdakileri bulun**<!BELGE TÜRÜ>** kaynak kodundaki etiket:

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1.  Tam etiketi seçin.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_13.png)




1.  Saklayın, değiştirin veya silin<!DOCTYPE>etiket.
1.  Veya değiştir<!DOCTYPE> aşağıdaki ile etiketleyin:

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **5. Adım: Aspose.Cells.GridWeb Denetimini Yeniden Boyutlandırma**
 Web sitesine sürükledikten sonra GridWeb kontrolünün genişliğini ve yüksekliğini değiştirebilirsiniz.

 Tasarım görünümünde, GridWeb'in genişliğini ve yüksekliğini yeniden boyutlandırabilirsiniz.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_14.png)



### **Adım 6: Aspose.Cells.GridWeb'in Özelliklerini Yapılandırma**
 Aspose.Cells.GridWeb özelliklerini WYSIWYG'de aşağıdakilere tıklayarak yapılandırın:**Özellikleri** Visual Studio 2013 IDE'nin sağ tarafındaki düğme.
 Bir Özellikler iletişim kutusu görüntülenir.

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_15.png)



Özellikler bölmesi, GridWeb'in görünüşünü ve hissini ve GridWeb'in davranışını kontrol etmek için diğer bazı özellikleri yapılandırmayı mümkün kılar.
### **7. Adım: Aspose.Cells.GridWeb İçeren İlk Web Sitenizi Çalıştırma**
 Web sitesini oluşturun ve çalıştırın.

1.  Ctrl+F5 tuşlarına basarak veya tıklayarak web sitesini doğrudan Visual Studio'dan çalıştırın.**Hata Ayıklamayı Başlat**. 

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_16.png)

 Artık GridWeb kontrolü ile oynamaya başlayabilirsiniz.

**Eylemde GridWeb kontrolü** 

![yapılacaklar:resim_alternatif_Metin](working-with-visual-studio_17.png)
