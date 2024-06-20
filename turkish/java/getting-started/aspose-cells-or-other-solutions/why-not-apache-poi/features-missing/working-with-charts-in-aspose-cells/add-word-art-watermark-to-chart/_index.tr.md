---
title: Tabloya Word Art Filigran Ekle
type: docs
weight: 10
url: /tr/java/add-word-art-watermark-to-chart/
---

## **Aspose.Cells - Tabloya Word Art Filigran Ekle**
Tablolara özel metin efektlerini eklemek için WordArt'ı kullanabilirsiniz. Örneğin, bir başlığı gererek, metni süsleyerek, metni önceden belirlenmiş bir şekile sığdırarak veya etkilenen metni bir grafik bölgesine filigran olarak uygulayarak elektronik tablolarınıza dekorasyon ekleyebilirsiniz. WordArt, elektronik tablonuza hareket ettirebileceğiniz veya konumlandırabileceğiniz bir nesne olur.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook.

//Open the existing excel file.

Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

//Get the chart in the first worksheet.

com.aspose.cells.Chart chart = workbook.getWorksheets().get(0).getCharts().get(0);

//Add a WordArt watermark (shape) to the chart's plot area.

com.aspose.cells.Shape wordart = chart.getShapes().addTextEffectInChart(MsoPresetTextEffect.TEXT_EFFECT_2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency.

wordArtFormat.setTransparency(0.9);

//Make the line invisible.

wordart.setHasLine(false);

//Save the excel file.

workbook.save(dataDir + "AsposeChartWatermarked_Out.xls", SaveFormat.EXCEL_97_TO_2003);

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Tabloya Word Art Filigranı Ekle](/cells/tr/java/add-wordart-watermark-to-chart)'ı ziyaret edin.

{{% /alert %}}
