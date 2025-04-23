---
title: Resim veya Yazdır Seçeneklerini Kullanarak Çalışma Sayfasını Resme Dönüştürme
type: docs
weight: 90
url: /tr/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Bu belge, bir çalışma sayfasını bir resim dosyasına dönüştürme ve resim için farklı resim ve yazdır seçeneklerini (çözünürlük, TIFF sıkıştırma, resim formatı ve sayfa kalitesi gibi) uygulama konusunda ayrıntılı bir anlayış sağlamak amacıyla tasarlanmıştır.

{{% /alert %}}

## **Çalışma Sayfalarını Resim Olarak Kaydetme - Farklı Yaklaşımlar**

Bazen çalışsayılarınızı resimsel bir temsil olarak sunmanız gerekebilir. Çalışsayı resimlerini uygulamalarınıza veya web sayfalarınıza eklemeniz veya kullanmanız gerekebilir. Resimlerini bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya bunları başka bir senaryoda kullanmanız gerekebilir. Basitçe başka bir yerde kullanabilmek için çalışsayısının bir resim olarak görüntülenmesini istersiniz. Aspose.Cells, Excel dosyalarındaki çalışsayıları resme dönüştürmeyi destekler. Ayrıca, Aspose.Cells, resim formatı, çözünürlük (dikey ve yatay), resim kalitesi ve diğer resim ve yazdırma seçenekleri belirleme gibi farklı seçenekleri destekler.

Bu işlem için Office Otomasyonunu deneyebilirsiniz ancak Office otomasyonunun kendi dezavantajları vardır. Güvenlik, kararlılık, ölçeklenebilirlik ve hız, fiyat ve özellikler gibi çeşitli nedenler ve sorunlar bulunmaktadır. Kısacası, birçok neden bulunmakla birlikte en önemli neden, Microsoft'un Office otomasyonuna karşı kesinlikle tavsiye etmemesidir.

Bu makale, Visual Studio .NET'te bir konsol uygulaması oluşturmayı, Aspose.Cells API'sını kullanarak bir çalışma sayfasını farklı resim ve yazdır seçenekleriyle bir resme dönüştürmeyi ve bunu birkaç basit satır kodla gerçekleştirmeyi gösteriyor.

Programınıza/projenize [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) ad alanını eklemeniz gerekecektir. [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) vb. gibi birçok değerli sınıfı bulunmaktadır.

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) sınıfı, çalışma sayfası için resimleri oluşturmak için temsil eder, istenen öznitelikler veya seçenekler belirtilmiş çalışma sayfasını doğrudan resim dosyasına dönüştürebilen aşırı yüklenmiş [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) yöntemine sahiptir. System.Drawing.Bitmap nesnesi döndürebilir ve bir resim dosyasını disk/akışa kaydedebilirsiniz. BMP, PNG, GIFF, JPG, JPEG, TIFF, EMF ve diğerleri gibi birçok resim formatı desteklenmektedir.

## **Aspose.Cells'ı Kullanarak Resme Dönüştürme İçin Resim veya Yazdır Seçeneklerini Kullanma**

### **Microsoft Excel'de şablon çalışma kitabı oluşturma**

MS Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim. Şimdi, şablon dosyasının "Sheet1" adlı çalışma sayfasını "SheetImage.tiff" adlı bir görüntü dosyasına dönüştüreceğim ve yatay ve dikey çözünürlük, TiffCompression vb. gibi farklı görüntü seçenekleri uygulayacağım.

### **Aspose.Cells'i İndirin ve Yükleyin**

Öncelikle, .Net için [Aspose.Cells'i](https://downloads.aspose.com/cells/net) indirmeniz gerekmektedir. Geliştirme bilgisayarınıza kurun. Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun bir süre sınırlaması yoktur ve yalnızca üretilen belgelere filigranlar enjekte eder.

### **Bir Proje Oluşturun**

Visual Studio. Net'i başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek bir C# konsol uygulaması gösterecektir, ancak VB.NET'i de kullanabilirsiniz.

### **Referanslar Ekle**

Bu proje Aspose.Cells'i kullanacaktır. Bu nedenle, projenize Aspose.Cells bileşenine referans eklemeniz gerekmektedir. Örneğin, ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll'ye bir referans ekleyin.

### **Çalışma Sayfasını Bir Görüntü Dosyasına Dönüştürme**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Dönüşüm Seçenekleri**

Belirli sayfaları resme kaydetmek mümkündür. Aşağıdaki kod, bir çalışma kitabındaki ilk ve ikinci çalışsayılarını JPG resimlerine dönüştürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **WorkbookRender kullanarak Görüntü dönüşümü**

Bir TIFF görüntüsü birden fazla çerçeve içerebilir. Tüm çalışma kitabını tek bir TIFF görüntüsüne çoğaltılmış çerçeveler veya sayfalarla kaydedebilirsiniz:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
