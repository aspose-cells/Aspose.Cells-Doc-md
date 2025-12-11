---  
title: Add Word Art Watermark to Chart  
type: docs  
weight: 10  
url: /java/add-word-art-watermark-to-chart/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Add Word Art Watermark to Chart**  
You can use WordArt to add special text effects to spreadsheets. For example, stretch a title, decorate text, make text fit a preset shape, or apply the text as a watermark to a chart’s plot area. The WordArt becomes an object that you can move or position in your spreadsheets to add decoration.  

**Java**  

{{< highlight java >}}  

 // Instantiate a new workbook.  

 // Open the existing Excel file.  

Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");  

 // Get the chart in the first worksheet.  

com.aspose.cells.Chart chart = workbook.getWorksheets().get(0).getCharts().get(0);  

 // Add a WordArt watermark (shape) to the chart's plot area.  

com.aspose.cells.Shape wordart = chart.getShapes().addTextEffectInChart(MsoPresetTextEffect.TEXT_EFFECT_2,  

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);  

 // Get the shape's fill format.  

FillFormat wordArtFormat = wordart.getFill();  

 // Set the transparency.  

wordArtFormat.setTransparency(0.9);  

 // Make the line invisible.  

wordart.setHasLine(false);  

 // Save the Excel file.  

workbook.save(dataDir + "AsposeChartWatermarked_Out.xls", SaveFormat.EXCEL_97_TO_2003);  

{{< /highlight >}}  

## **Download Running Code**  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)  

## **Download Sample Code**  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)  

{{% alert color="primary" %}}  

For more details, visit [Add WordArt Watermark to Chart](/cells/java/add-wordart-watermark-to-chart).  

{{% /alert %}}  
{{< app/cells/assistant language="java" >}}  
