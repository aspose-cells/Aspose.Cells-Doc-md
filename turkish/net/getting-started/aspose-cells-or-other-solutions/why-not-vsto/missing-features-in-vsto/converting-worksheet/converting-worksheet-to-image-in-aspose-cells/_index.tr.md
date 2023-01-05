---
title: Aspose.Cells'de Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 20
url: /tr/net/converting-worksheet-to-image-in-aspose-cells/
---
Bu belge, geliştiricilere bir çalışma sayfasını bir görüntü dosyasına ve birden çok sayfa içeren bir çalışma sayfasını sayfa başına bir görüntü dosyasına dönüştürme konusunda ayrıntılı bir anlayış sağlamak için tasarlanmıştır.
 Bazen, örneğin uygulamalarda veya web sayfalarında kullanmak için çalışma sayfalarını resim olarak sunmanız gerekebilir. Görüntüleri bir Word belgesine eklemeniz gerekebilir.**PDF** dosya, bir PowerPoint sunumu veya başka bir senaryoda kullanın. Basitçe, çalışma sayfasını bir görüntü olarak işlemek istiyorsunuz. Aspose.Cells, Microsoft Excel dosyalarındaki çalışma sayfalarının görüntülere dönüştürülmesini destekler. Ayrıca,**Aspose.Cells** bir çalışma kitabını sayfa başına bir tane olmak üzere birden çok görüntü dosyasına dönüştürmeyi destekler.

Bunu başarmak için Office Otomasyonu'nu kullanabilirsiniz, ancak Office otomasyonunun kendi dezavantajları vardır. İlgili birkaç neden ve sorun vardır: örneğin güvenlik, kararlılık, ölçeklenebilirlik/Hız, fiyat ve özellikler. Kısacası, birçok neden var, ancak asıl sebep, Microsoft'in Office otomasyonuna karşı şiddetle tavsiye etmesidir.

Bu makalede, Visual Studio.Net'te bir konsol uygulamasının nasıl oluşturulacağı, Aspose.Cells API kullanılarak birkaç ve en basit kod satırıyla bir çalışma sayfasının bir görüntüye ve bir çalışma sayfasının her çalışma sayfası için tek bir görüntüye nasıl dönüştürüleceği gösterilmektedir. programınıza/projenize ad alanı. Birkaç değerli sınıfı vardır, örneğin SheetRender, ImageOrPrintOptions, WorkbookRender vb.Aspose.Cells.Rendering.SheetRender sınıfı, çalışma sayfası için görüntüleri işlemek üzere bir çalışma sayfasını temsil eder, aşırı**Hayal etmek** bir çalışma sayfasını, istediğiniz nitelikler veya seçeneklerle belirtilen görüntü dosya(lar)ına doğrudan dönüştürebilen yöntem. geri dönebilir**System.Drawing.Bitmap** nesne ve bir görüntü dosyasını diske/akışa kaydedebilirsiniz. .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf vb. gibi desteklenen birkaç görüntü formatı vardır.

{{< highlight "csharp" >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
