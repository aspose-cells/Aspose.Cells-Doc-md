---
title: Çalışma Sayfasını Görüntüye Dönüştürme ve Sayfa Başına Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 80
url: /tr/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Bu belge, geliştiricilere bir çalışma sayfasını bir görüntü dosyasına nasıl dönüştürecekleri ve bir çalışma sayfasının birden fazla sayfasının nasıl ayrı bir görüntü dosyasına dönüştürecekleri konusunda detaylı bir anlayış sağlamak üzere tasarlanmıştır.

Bazı durumlarda, çalışma sayfalarını örneğin uygulamalarda veya web sayfalarında kullanmak için resim olarak sunmanız gerekebilir. Resimleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemek veya başka bir senaryoda kullanmak gerekebilir. Temel olarak, çalışma sayfasını bir resim olarak oluşturmak istersiniz. Aspose.Cells, Microsoft Excel dosyalarındaki çalışma sayfalarını resimlere dönüştürmeyi destekler. Ayrıca, Aspose.Cells, bir çalışma kitabını birden fazla resim dosyasına, sayfa başına bir tane olmak üzere dönüştürmeyi destekler.

Bunu başarmak için Office Automation'ı kullanabilirsiniz, ancak Office Automation'ın kendi dezavantajları vardır. Güvenlik, istikrar, ölçeklenebilirlik/hız, fiyat ve özellikler gibi birçok neden ve sorun bulunmaktadır. Kısacası, birçok neden bulunmaktadır, ancak ana nedenlerden biri Microsoft'un Office Automation'u kesinlikle önermemesidir.

{{% /alert %}}

## **Aspose.Cells Kullanarak Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu makalede, Visual Studio'da bir konsol uygulaması oluşturmayı, bir çalışma sayfasını bir resme dönüştürmeyi ve Aspose.Cells API'sını kullanarak birkaç basit satır kodla her çalışma sayfasını bir resim olarak dönüştürmeyi gösteriyor.

Programınıza/projenize [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) ad alanını eklemeniz gerekecektir. [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) vb. gibi birçok değerli sınıfı bulunmaktadır. [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) sınıfı bir çalışma sayfasını resimlendirmek için temsil eder ve aşırı yüklenmiş [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) yöntemi, herhangi bir özellik veya seçenek belirtilmeden çalışma sayfasını doğrudan resim dosyalarına dönüştürebilir. Bir System.Drawing.Bitmap nesnesi döndürebilir ve bir resim dosyasını disk/akışa kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF ve diğerleri gibi birçok resim formatı desteklenmektedir.

Bu makalede şunları açıklar:

- Bir çalışma sayfasını bir resme dönüştürme
- Bir çalışma sayfasındaki her sayfayı bir resme dönüştürme

Bu görev, Aspose.Cells'ı kullanarak bir şablon çalışma kitabındaki bir çalışma sayfasını bir resim dosyasına dönüştürmenin nasıl yapıldığını gösterir.

### **Proje Kurulumu**

1. İlk olarak, [Aspose.Cells for .NET'i indirin](https://downloads.aspose.com/cells/net).
1. Geliştirme bilgisayarınıza indirip yükleyin. Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun süresi yoktur ve sadece üretilen belgelere filigran ekler. Şimdi Visual Studio.Net'i başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek C# konsol uygulaması kullanıyor ancak VB.NET de kullanabilirsiniz. Oluşturulan projeye Aspose.Cells'a bir referans ekleyin.

### **Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook.xlsx** (1 çalışma sayfası). Daha sonra, şablon dosyasının Sheet1 çalışma sayfasını SheetImage.jpg adında bir resim dosyasına dönüştürdüm.

Bileşen tarafından görevi tamamlamak için kullanılan kod aşağıda verilmiştir. Bu kod, **Testbook.xlsx**'teki Sheet1'i, bu dönüşümün ne kadar kolay olduğunu açıklamak için bir resim dosyasına dönüştürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Aspose.Cells Kullanarak Sayfa Sayfa Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu örnek, birkaç sayfası olan bir şablon çalışma kitabından bir çalışma sayfasını bir resim dosyasına dönüştürmek için Aspose.Cells'ı kullanmanın nasıl yapıldığını göstermektedir.

### **Sayfaya Göre Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook2.xlsx** (1 çalışma sayfası).

Şimdi, şablon dosyasının Sheet1 çalışma sayfasını resim dosyalarına dönüştür (sayfa başına bir dosya). Zaten kopyalama görevini gerçekleştirmek için konsol uygulaması oluşturmuştum, bu nedenle konsol uygulaması oluşturma adımlarını atlayacak ve doğrudan çalışma sayfası dönüşüm adımlarına geçeceğim.

Bileşen tarafından görevi tamamlamak için kullanılan kod aşağıda verilmiştir. Bu kod, Testbook2.xls'deki Sheet1'i sayfa başına resim dosyalarına dönüştürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
