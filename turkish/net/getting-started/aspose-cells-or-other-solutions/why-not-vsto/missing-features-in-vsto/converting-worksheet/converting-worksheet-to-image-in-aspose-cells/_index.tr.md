---
title: Aspose.Cells te Çalışsayıyı Görüntüye Dönüştürme
type: docs
weight: 20
url: /tr/net/converting-worksheet-to-image-in-aspose-cells/
---

Bu belge, geliştiricilere bir çalışsayıyı bir görüntü dosyasına dönüştürmek ve birden çok sayfa çalışsayısını bir sayfa başına bir görüntü dosyasına dönüştürmek için ayrıntılı bir anlayış sağlamak amacıyla tasarlanmıştır.
Bazı durumlarda, çalışsayıları resim olarak sunmanız gerekebilir, örneğin bunları uygulamalarda veya web sayfalarında kullanmak için. Resimleri bir Word belgesine, bir **PDF** dosyasına, bir PowerPoint sunumuna eklemeniz gerekebilir veya bunları başka bir senaryoda kullanmanız gerekebilir. Basitçe söylemek gerekirse, çalışsayıyı bir resim gibi işlemek istiyorsunuz. Aspose.Cells, Microsoft Excel dosyalarındaki çalışsayılarını resimlere dönüştürmeyi destekler. Ayrıca, **Aspose.Cells**, bir çalışbook'u birden fazla görüntü dosyasına dönüştürmeyi destekler, her biri sayfa başına bir tane.

Bunu başarmak için Office Automation'ı kullanabilirsiniz, ancak Office Automation'ın kendi dezavantajları vardır. Güvenlik, istikrar, ölçeklenebilirlik/hız, fiyat ve özellikler gibi birçok neden ve sorun bulunmaktadır. Kısacası, birçok neden bulunmaktadır, ancak ana nedenlerden biri Microsoft'un Office Automation'u kesinlikle önermemesidir.

Bu makale, Visual Studio.Net'te konsol uygulaması oluşturmayı, bir çalışsayıyı bir resme ve her çalışsayıyı birkaç ve en basit kod satırıyla Aspose.Cells API'sini kullanarak bir resim haline getirmeyi göstermektedir. Program/projenize Aspose.Cells.Rendering ad alanını içe aktarmanız gereklidir. Önemli sayıda sınıf içeren Aspose.Cells.Rendering ad alanı, örn. SheetRender, ImageOrPrintOptions, WorkbookRender vb.

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
