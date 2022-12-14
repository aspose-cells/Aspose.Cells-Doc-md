---
title: Agregar marca de agua de Word Art al gráfico
type: docs
weight: 10
url: /es/java/add-word-art-watermark-to-chart/
---
## **Aspose.Cells - Agregar marca de agua de Word Art al gráfico**
Puede usar WordArt para agregar efectos de texto especiales a las hojas de cálculo. Por ejemplo, estire un título, decore el texto, haga que el texto se ajuste a una forma preestablecida o aplique el texto afectado al área de trazado de un gráfico como una marca de agua. El WordArt se convierte en un objeto que puede mover o colocar en sus hojas de cálculo para agregar decoración.

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
## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Agregar marca de agua de WordArt al gráfico](/cells/es/java/add-wordart-watermark-to-chart).

{{% /alert %}}
