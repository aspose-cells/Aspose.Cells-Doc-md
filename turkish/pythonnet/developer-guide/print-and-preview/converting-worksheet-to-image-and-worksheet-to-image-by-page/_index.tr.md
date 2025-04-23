---
title: Çalışma Sayfasını Görüntüye Dönüştürme ve Sayfa Başına Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 80
url: /tr/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Bu belge, geliştiricilere bir çalışma sayfasını bir görüntü dosyasına nasıl dönüştürecekleri ve bir çalışma sayfasının birden fazla sayfasının nasıl ayrı bir görüntü dosyasına dönüştürecekleri konusunda detaylı bir anlayış sağlamak üzere tasarlanmıştır.

Bazen, çalışma sayfalarını görüntü olarak göstermeniz gerekebilir, örneğin, uygulamalar veya web sayfalarında kullanmak için. Resimleri Word, PDF veya PowerPoint'e eklemek veya başka senaryolarda kullanmak isteyebilirsiniz. Basitçe, çalışma sayfasını görüntü olarak render etmek istersiniz. Aspose.Cells for Python via .NET, Excel dosyalarındaki çalışma sayfalarını resme dönüştürmeyi destekler. Ayrıca, her sayfa için ayrı resim dosyaları şeklinde çoklu dönüşüm de desteklenir.

Bunu başarmak için Office Automation'ı kullanabilirsiniz, ancak Office Automation'ın kendi dezavantajları vardır. Güvenlik, istikrar, ölçeklenebilirlik/hız, fiyat ve özellikler gibi birçok neden ve sorun bulunmaktadır. Kısacası, birçok neden bulunmaktadır, ancak ana nedenlerden biri Microsoft'un Office Automation'u kesinlikle önermemesidir.

{{% /alert %}}

## **Aspose.Cells Kullanarak Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu makale, Visual Studio'da nasıl konsol uygulaması oluşturulacağı, çalışma sayfasının nasıl görüntüye dönüştürüleceği ve birkaç basit satır kodla bütün çalışma sayfalarının tek bir görüntüye nasıl dönüştürüleceği konusunda bilgi verir, Aspose.Cells for Python via .NET API kullanılarak.

Programınıza/projenize [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) ad alanını eklemeniz gerekecektir. [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) vb. gibi birçok değerli sınıfı bulunmaktadır. [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) sınıfı bir çalışma sayfasını resimlendirmek için temsil eder ve aşırı yüklenmiş [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) yöntemi, herhangi bir özellik veya seçenek belirtilmeden çalışma sayfasını doğrudan resim dosyalarına dönüştürebilir. Bir System.Drawing.Bitmap nesnesi döndürebilir ve bir resim dosyasını disk/akışa kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF ve diğerleri gibi birçok resim formatı desteklenmektedir.

Bu makale, çalışma sayfasını görüntüye dönüştürmenin nasıl yapılacağını anlatır. Bu görev, Aspose.Cells for Python via .NET kullanarak, bir şablon çalışma kitabından çalışma sayfasını görüntü dosyasına dönüştürmek içindir.


### **Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook.xlsx** (1 çalışma sayfası). Daha sonra, şablon dosyasının Sheet1 çalışma sayfasını SheetImage.jpg adında bir resim dosyasına dönüştürdüm.

Bileşen tarafından görevi tamamlamak için kullanılan kod aşağıda verilmiştir. Bu kod, **Testbook.xlsx**'teki Sheet1'i, bu dönüşümün ne kadar kolay olduğunu açıklamak için bir resim dosyasına dönüştürür.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Aspose.Cells Kullanarak Sayfa Sayfa Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu örnek, Aspose.Cells for Python via .NET kullanarak, birkaç sayfadan oluşan şablon çalışma kitabını her sayfa için tek bir resim dosyasına dönüştürmeyi gösterir.

### **Sayfaya Göre Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook2.xlsx** (1 çalışma sayfası).

Şimdi, şablon dosyasının Sheet1 çalışma sayfasını resim dosyalarına dönüştür (sayfa başına bir dosya). Zaten kopyalama görevini gerçekleştirmek için konsol uygulaması oluşturmuştum, bu nedenle konsol uygulaması oluşturma adımlarını atlayacak ve doğrudan çalışma sayfası dönüşüm adımlarına geçeceğim.

Bileşen tarafından görevi tamamlamak için kullanılan kod aşağıda verilmiştir. Bu kod, Testbook2.xls'deki Sheet1'i sayfa başına resim dosyalarına dönüştürür.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

