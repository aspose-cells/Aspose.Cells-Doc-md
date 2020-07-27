+++
title = "Add Word Art Watermark to Chart" 
description = "" 
weight = 20646 
+++

Aspose.Cells for Java : Add Word Art Watermark to Chart  

# Aspose.Cells for Java : Add Word Art Watermark to Chart


## Aspose.Cells - Add Word Art Watermark to Chart

You can use WordArt to add special text effects to spreadsheets. For example, stretch a title, decorate text, make text fit a preset shape, or apply the affected text to a chart’s plot area as a watermark. The WordArt becomes an object that you can move or position in your spreadsheets to add decoration.

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

For more details, visit [Add WordArt Watermark to Chart](http://docs.aspose.com:8082/docs/display/cellsjava/Add+WordArt+Watermark+to+Chart).

