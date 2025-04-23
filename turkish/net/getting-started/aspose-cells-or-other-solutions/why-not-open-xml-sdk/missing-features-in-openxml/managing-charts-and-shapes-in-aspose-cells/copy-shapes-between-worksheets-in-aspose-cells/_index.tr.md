---
title: Aspose.Cells İçinde Çalışma Sayfaları Arasında Şekilleri Kopyalama
type: docs
weight: 30
url: /tr/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

Bazen, bir çalışma sayfası üzerindeki öğeleri, örneğin resimleri, grafikleri ve diğer çizim nesnelerini, çalışma sayfaları arasında kopyalamanız gerekebilir. Aspose.Cells bu özelliği destekler. Grafikler, resimler ve diğer nesneler en yüksek hassasiyetle kopyalanabilir.

Bu makale, çalışma sayfaları arasında şekilleri kopyalamanın ayrıntılı anlayışını verir. Örneğin, Visual Studio.Net'te bir konsol uygulaması oluşturur, Aspose.Cells kullanarak resimleri, grafikleri ve diğer çizim nesnelerini çalışma sayfaları arasında kopyalar.

{{% /alert %}} 

Aşağıda bir çalışma sayfasından başka bir çalışma sayfasına bir grafik kopyalamak için kod bulunmaktadır

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**Not:** Birden fazla şekli kopyalamanın ayrıntıları için [buraya](/cells/tr/net/copy-shapes-between-worksheets/) ziyaret etmeniz gerekmektedir.
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Örnek Çalışmayı İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
