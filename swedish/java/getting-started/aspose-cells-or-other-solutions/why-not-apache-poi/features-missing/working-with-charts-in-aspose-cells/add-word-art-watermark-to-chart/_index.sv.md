---
title: Lägg till Word Art vattenstämpel på diagram
type: docs
weight: 10
url: /sv/java/add-word-art-watermark-to-chart/
---

## **Aspose.Cells – Lägg till Word Art-vattenstämpel på diagram**
Du kan använda WordArt för att lägga till speciella texteffekter i kalkylblad. Till exempel, sträcka ut en titel, dekorera text, få text att passa en förinställd form, eller tillämpa den påverkade texten på ett diagramområde som en vattenstämpel. WordArt blir en objekt som du kan flytta eller positionera i dina kalkylblad för att lägga till dekoration.

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
## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

För mer detaljer, besök [Lägg till WordArt-vattenstämpel på diagram](/cells/sv/java/add-wordart-watermark-to-chart).

{{% /alert %}}
