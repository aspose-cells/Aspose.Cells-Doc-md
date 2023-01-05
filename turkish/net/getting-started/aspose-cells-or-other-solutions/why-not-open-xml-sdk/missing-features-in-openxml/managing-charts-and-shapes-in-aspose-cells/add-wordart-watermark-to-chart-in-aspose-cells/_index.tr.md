---
title: Aspose.Cells'de Grafiğe WordArt Filigranı Ekleyin
type: docs
weight: 10
url: /tr/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

Elektronik tablolara özel metin efektleri eklemek için WordArt'ı kullanabilirsiniz. Örneğin, bir başlığı genişletin, metni süsleyin, metni önceden ayarlanmış bir şekle sığdırın veya etkilenen metni bir grafiğin çizim alanına filigran olarak uygulayın. WordArt, dekorasyon eklemek için elektronik tablolarınızda taşıyabileceğiniz veya konumlandırabileceğiniz bir nesne haline gelir.

{{% /alert %}} 

Aşağıdaki örnek, mevcut bir grafiğin çizim alanı için bir WordArt şeklinin filigran olarak nasıl ekleneceğini gösterir. Örnek, zaten grafiği içeren bir şablon Excel dosyası kullanır.

**giriş dosyası** 

![yapılacaklar:resim_alternatif_metin](picture1.png)

**çıktı dosyası**

![yapılacaklar:resim_alternatif_metin](picture2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Örnek Kodu İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Çalışan Örneği İndirin**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
