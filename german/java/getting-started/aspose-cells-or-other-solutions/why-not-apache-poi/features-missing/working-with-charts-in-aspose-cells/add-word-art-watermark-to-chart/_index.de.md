---
title: Fügen Sie dem Diagramm ein Word Art-Wasserzeichen hinzu
type: docs
weight: 10
url: /de/java/add-word-art-watermark-to-chart/
---
## **Aspose.Cells - Wortkunst-Wasserzeichen zum Diagramm hinzufügen**
Sie können WordArt verwenden, um Tabellenkalkulationen spezielle Texteffekte hinzuzufügen. Sie können beispielsweise einen Titel dehnen, Text dekorieren, Text an eine voreingestellte Form anpassen oder den betroffenen Text als Wasserzeichen auf den Plotbereich eines Diagramms anwenden. Das WordArt wird zu einem Objekt, das Sie verschieben oder in Ihren Tabellenkalkulationen positionieren können, um Dekoration hinzuzufügen.

**Java**

{{< highlight "java" >}}

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
## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[WordArt-Wasserzeichen zum Diagramm hinzufügen](/cells/de/java/add-wordart-watermark-to-chart).

{{% /alert %}}
