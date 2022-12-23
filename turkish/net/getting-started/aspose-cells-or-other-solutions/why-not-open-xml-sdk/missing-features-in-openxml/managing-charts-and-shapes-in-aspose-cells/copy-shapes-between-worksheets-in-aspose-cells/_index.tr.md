---
title: Aspose.Cells'de Çalışma Sayfaları Arasında Şekilleri Kopyala
type: docs
weight: 30
url: /tr/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

Bazen, bir çalışma sayfasındaki öğeleri, örneğin resimleri, çizelgeleri ve diğer çizim nesnelerini çalışma sayfaları arasında kopyalamanız gerekir. Aspose.Cells bu özelliği destekler. Grafikler, resimler ve diğer nesneler en yüksek hassasiyetle kopyalanabilir.

Bu makale, çalışma sayfaları arasında şekillerin nasıl kopyalanacağı hakkında ayrıntılı bilgi verir. Örnek olarak, Visual Studio.Net'te bir konsol uygulaması oluşturur, resimleri, çizelgeleri ve diğer çizim nesnelerini çalışma sayfaları arasında Aspose.Cells kullanarak kopyalar.

{{% /alert %}} 

Bir grafiği çalışma sayfasından diğerine kopyalamak için kullanılan kod aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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

**Not:** Birden çok şekli kopyalama hakkında daha fazla ayrıntı için şu adresi ziyaret etmeniz gerekir:[Burada](/cells/tr/net/copy-shapes-between-worksheets/)
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Çalışan Örneği İndirin**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
