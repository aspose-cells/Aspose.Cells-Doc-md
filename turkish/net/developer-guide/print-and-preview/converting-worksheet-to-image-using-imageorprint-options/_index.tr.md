---
title: ImageOrPrint Seçeneklerini Kullanarak Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 90
url: /tr/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

Bu belge, bir çalışma sayfasının bir görüntü dosyasına nasıl dönüştürüleceğinin ve görüntü için farklı görüntü ve yazdırma seçeneklerinin, çözünürlük, TIFF sıkıştırma, görüntü formatı ve sayfa kalitesi gibi seçeneklerin nasıl uygulanacağının ayrıntılı olarak anlaşılmasını sağlamak için tasarlanmıştır.

{{% /alert %}}

##  **Çalışma Sayfalarını Görüntülere Kaydetme - Farklı Yaklaşımlar**

Bazen, çalışma sayfalarınızı resimli bir sunum olarak sunmanız gerekebilir. Çalışma sayfası görüntülerini uygulamalarınıza veya web sayfalarınıza sunmanız gerekir. Görüntüleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya başka bir senaryoda kullanmanız gerekebilir. Basitçe, başka bir yerde kullanabilmeniz için bir çalışma sayfasının görüntü olarak işlenmesini istiyorsunuz. Aspose.Cells, Excel dosyalarındaki çalışma sayfalarının görüntülere dönüştürülmesini destekler. Ayrıca Aspose.Cells, görüntü formatı, çözünürlük (dikey ve yatay), görüntü kalitesi ve diğer görüntü ve baskı seçenekleri gibi farklı seçeneklerin ayarlanmasını destekler.

Office Otomasyonu'nu deneyebilirsiniz, ancak Office otomasyonunun kendi dezavantajları vardır. İlgili birkaç neden ve sorun vardır: örneğin, güvenlik, kararlılık, ölçeklenebilirlik ve hız, fiyat ve özellikler. Kısacası, pek çok neden var ve bunlardan en önemlisi Microsoft'in yazılım çözümlerinden Office otomasyonuna karşı şiddetle tavsiye etmesi.

Bu makale, Visual Studio .NET'de bir konsol uygulamasının nasıl oluşturulacağını, Aspose.Cells API kullanarak birkaç ve en basit kod satırıyla farklı görüntü ve yazdırma seçeneklerini kullanarak bir çalışma sayfasının görüntüye dönüştürülmesini nasıl gerçekleştireceğinizi gösterir.

 içe aktarmanız gerekiyor[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)programınıza/projenize ad alanı. Birkaç değerli sınıfı vardır, örneğin,[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**Çalışma KitabıRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)vesaire.

bu[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class, çalışma sayfası için görüntüleri işlemek üzere bir çalışma sayfasını temsil eder, aşırı yüklenmiş[**Hayal etmek**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)bir çalışma sayfasını, istediğiniz nitelikler veya seçeneklerle belirtilen görüntü dosya(lar)ına doğrudan dönüştürebilen yöntem. System.Drawing.Bitmap nesnesini döndürebilir ve bir görüntü dosyasını diske/akışa kaydedebilirsiniz. Desteklenen birkaç resim formatı vardır, örneğin BMP, PNG, GIFF, JPEG, TIFF, EMF vb.

##  **ImageOrPrint seçeneklerini kullanarak Çalışma Sayfasını Görüntüye Dönüştürmek için Aspose.Cells'i kullanma.**

###  **Microsoft Excel'de şablon çalışma kitabı oluşturma**

MS Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim. Şimdi şablon dosyasının “Sheet1” çalışma sayfasını “SheetImage.tiff” imaj dosyasına çevireceğim ve yatay ve dikey çözünürlükler, TiffCompression vb. farklı resim seçeneklerini uygulayacağım.

###  **İndirin ve yükleyin Aspose.Cells**

 Öncelikle yapmanız gerekenler[indirmek](https://downloads.aspose.com/cells/net) .Net için Aspose.Cells. Geliştirme bilgisayarınıza kurun. Tüm[Aspose](http://www.aspose.com/)bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.

###  **Proje Oluştur**

Visual Studio'yu başlatın. Net ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C# konsol uygulamasını gösterecektir, ancak VB.NET'i de kullanabilirsiniz.

###  **Referans Ekle**

Bu proje Aspose.Cells'i kullanacaktır. Bu nedenle, projenize Aspose.Cells bileşenine referans eklemelisiniz. Örneğin, ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll dosyasına bir başvuru ekleyin.

###  **Çalışma Sayfasını bir Görüntü dosyasına dönüştürün**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

##  **Dönüşüm Seçenekleri**

Görüntüye belirli sayfaları kaydetmek mümkündür. Aşağıdaki kod, bir çalışma kitabındaki birinci ve ikinci çalışma sayfalarını JPG resimlerine dönüştürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

##  **WorkbookRender kullanarak görüntü dönüştürme**

Bir TIFF görüntüsü birden fazla çerçeve içerebilir. Tüm çalışma kitabını birden fazla çerçeve veya sayfa içeren tek bir TIFF görüntüsüne kaydedebilirsiniz:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

