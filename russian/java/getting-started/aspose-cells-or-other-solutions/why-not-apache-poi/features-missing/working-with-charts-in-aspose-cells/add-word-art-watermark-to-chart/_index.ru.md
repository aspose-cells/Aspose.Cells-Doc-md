---
title: Добавить водный знак Word Art на диаграмму
type: docs
weight: 10
url: /ru/java/add-word-art-watermark-to-chart/
---

## **Aspose.Cells - Добавить водный знак Word Art на диаграмму**
Вы можете использовать WordArt для добавления специальных текстовых эффектов к таблицам. Например, растянуть заголовок, украсить текст, подогнать текст под заданную форму или применить измененный текст к области построения диаграммы в качестве водяного знака. WordArt становится объектом, который можно перемещать или располагать в ваших таблицах для добавления украшений.

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
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Добавьте водяной знак WordArt на график](/cells/ru/java/add-wordart-watermark-to-chart).

{{% /alert %}}
