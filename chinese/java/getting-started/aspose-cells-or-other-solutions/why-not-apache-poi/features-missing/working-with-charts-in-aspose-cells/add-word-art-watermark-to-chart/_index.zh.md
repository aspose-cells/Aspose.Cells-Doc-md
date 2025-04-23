---
title: 向图表添加Word Art水印
type: docs
weight: 10
url: /zh/java/add-word-art-watermark-to-chart/
---

## **Aspose.Cells - 向图表添加Word Art水印**
您可以使用WordArt在电子表格中添加特殊文本效果。例如，拉伸标题、装饰文本、使文本适合预设形状，或将受影响的文本应用于图表的绘图区作为水印。WordArt成为您可以在电子表格中移动或定位的对象，以添加装饰。

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
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[向图表添加Word Art水印](/cells/zh/java/add-wordart-watermark-to-chart)。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
