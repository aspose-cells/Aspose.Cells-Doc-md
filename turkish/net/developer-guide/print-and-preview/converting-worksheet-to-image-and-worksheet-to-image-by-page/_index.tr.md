---
title: Çalışma Sayfasını Görüntüye ve Çalışma Sayfasını Görüntüye Sayfa Sayfa Dönüştürme
type: docs
weight: 80
url: /tr/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Bu belge, geliştiricilere bir çalışma sayfasını bir görüntü dosyasına ve birden fazla sayfa içeren bir çalışma sayfasını sayfa başına bir görüntü dosyasına dönüştürme konusunda ayrıntılı bir anlayış sağlamak için tasarlanmıştır.

Bazen, örneğin uygulamalarda veya web sayfalarında kullanmak için çalışma sayfalarını resim olarak sunmanız gerekebilir. Görüntüleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya başka bir senaryoda kullanmanız gerekebilir. Basitçe, çalışma sayfasını bir görüntü olarak işlemek istiyorsunuz. Aspose.Cells, Microsoft Excel dosyalarındaki çalışma sayfalarının görüntülere dönüştürülmesini destekler. Ayrıca Aspose.Cells, bir çalışma kitabının her sayfada bir tane olmak üzere birden çok görüntü dosyasına dönüştürülmesini destekler.

Bunu başarmak için Office Otomasyonu'nu kullanabilirsiniz, ancak Office otomasyonunun kendi dezavantajları vardır. İlgili birkaç neden ve sorun vardır: örneğin güvenlik, kararlılık, ölçeklenebilirlik/Hız, fiyat ve özellikler. Kısacası, birçok neden var, ancak asıl sebep, Microsoft'in Office otomasyonuna karşı şiddetle tavsiye etmesidir.

{{% /alert %}}

## **Çalışma Sayfasını Görüntü Dosyasına Dönüştürmek için Aspose.Cells'i Kullanma**

Bu makale, Aspose.Cells API kullanarak birkaç ve en basit kod satırıyla Visual Studio'da bir konsol uygulamasının nasıl oluşturulacağını, bir çalışma sayfasının görüntüye nasıl dönüştürüleceğini ve bir çalışma sayfasının her çalışma sayfası için tek bir görüntüye nasıl dönüştürüleceğini gösterir.

 içe aktarmanız gerekir[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) programınıza/projenize ad alanı. Gibi birkaç değerli sınıfı vardır.[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**Çalışma KitabıRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), ve bunun gibi. bu[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class, çalışma sayfası için görüntüleri işlemek üzere bir çalışma sayfasını temsil eder ve aşırı yüklenmiş[**Hayal etmek**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)herhangi bir nitelik veya seçenek kümesiyle bir çalışma sayfasını doğrudan görüntü dosyalarına dönüştürebilen bir yöntem. Bir System.Drawing.Bitmap nesnesi döndürebilir ve bir görüntü dosyasını diske/akışa kaydedebilirsiniz. Çeşitli görüntü formatları desteklenir, örneğin BMP, PNG, GIF, JPG, JPEG, TIFF, EMF ve diğerleri.

Bu makalede, aşağıdakilerin nasıl yapılacağı açıklanmaktadır:

- Çalışma sayfasını resme dönüştürme
- Çalışma sayfasındaki her sayfayı bir resme dönüştürün

Bu görev, bir çalışma sayfasını bir şablon çalışma kitabından bir görüntü dosyasına dönüştürmek için Aspose.Cells'in nasıl kullanılacağını gösterir.

### **Kurulum Projesi**

1.  Birinci,[indir Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1.  Geliştirme bilgisayarınıza kurun. Herşey[Aspose](http://www.aspose.com/)bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler. Şimdi Visual Studio.Net'i başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C# konsol uygulamasını kullanır, ancak VB.NET'i de kullanabilirsiniz. Oluşturulan projeye Aspose.Cells referansını ekleyin.

### **Çalışma Sayfasını Görüntü Dosyasına Dönüştür**

 Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim:**Testbook.xlsx** (1 çalışma sayfası). Ardından, şablon dosyasının çalışma sayfası Sheet1'i SheetImage.jpg adlı bir görüntü dosyasına dönüştürün.

 Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır. Sayfa1'i şuraya dönüştürür:**Testbook.xlsx** Bu dönüştürmenin ne kadar kolay olduğunu açıklamak için bir resim dosyasına.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Çalışma Sayfasını Sayfaya Göre Görüntü Dosyasına Dönüştürmek için Aspose.Cells'i Kullanma**

Bu örnek, birkaç sayfası olan bir şablon çalışma kitabından bir çalışma sayfasını sayfa başına bir görüntü dosyasına dönüştürmek için Aspose.Cells'in nasıl kullanılacağını gösterir.

### **Çalışma Sayfasını Sayfaya Göre Görüntüye Dönüştür**

 Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim:**Testbook2.xlsx** (1 çalışma sayfası).

Şimdi, şablon dosyasının çalışma sayfası Sayfa1'i görüntü dosyalarına dönüştürün (sayfa başına bir dosya). Kopyalama görevini gerçekleştirmek için konsol uygulamasını zaten oluşturduğum için, bu konsol uygulaması oluşturma adımlarını atlayacağım ve doğrudan çalışma sayfası dönüştürme adımlarına geçeceğim.

Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır. Testbook2.xls'deki Sayfa1'i sayfa sayfa görüntü dosyalarına dönüştürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

