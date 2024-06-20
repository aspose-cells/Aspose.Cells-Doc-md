---
title: Aspose.Cells te Grafiğe WordArt Filigranı Ekle
type: docs
weight: 10
url: /tr/net/add-wordart-watermark-to-chart-in-aspose-cells/
---

{{% alert color="primary" %}} 

Tablolara özel metin efektlerini eklemek için WordArt'ı kullanabilirsiniz. Örneğin, bir başlığı gererek, metni süsleyerek, metni önceden belirlenmiş bir şekile sığdırarak veya etkilenen metni bir grafik bölgesine filigran olarak uygulayarak elektronik tablolarınıza dekorasyon ekleyebilirsiniz. WordArt, elektronik tablonuza hareket ettirebileceğiniz veya konumlandırabileceğiniz bir nesne olur.

{{% /alert %}} 

Aşağıdaki örnek, mevcut bir grafik alanının filigranı için WordArt şekli eklemenin nasıl yapıldığını göstermektedir. Örnek, zaten bir grafik içeren bir şablon Excel dosyasını kullanmaktadır.

**Giriş dosyası** 

![todo:image_alt_text](picture1.png)

**Çıkış dosyası**

![todo:image_alt_text](picture2.png)

**C#**

{{< highlight csharp >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Chart.xlsx";

//Open the existing excel file.

Workbook workbook = new Workbook(FileName);

//Get the chart in the first worksheet.

Aspose.Cells.Charts.Chart chart = workbook.Worksheets[0].Charts[0];

//Add a WordArt watermark (shape) to the chart's plot area.

Aspose.Cells.Drawing.Shape wordart = chart.Shapes.AddTextEffectInChart(MsoPresetTextEffect.TextEffect2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

Aspose.Cells.Drawing.MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the transparency.

wordArtFormat.Transparency = 0.9;

//Get the line format and make it invisible.

Aspose.Cells.Drawing.MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the excel file.

workbook.Save(FileName);

{{< /highlight >}}

## **Örnek Kod İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Örnek Çalışmayı İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
