---
title: Añadir Marca de Agua de WordArt a Gráfico
type: docs
weight: 10
url: /es/java/add-word-art-watermark-to-chart/
---

## **Aspose.Cells - Añadir Marca de Agua de WordArt a Gráfico**
Puede usar WordArt para agregar efectos de texto especiales a las hojas de cálculo. Por ejemplo, estirar un título, decorar texto, ajustar texto a una forma predefinida o aplicar el texto afectado al área de trama de un gráfico como marca de agua. El WordArt se convierte en un objeto que puede mover o posicionar en sus hojas de cálculo para agregar decoración.

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
## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Agregar Marca de Agua de WordArt a Gráfico](/cells/es/java/add-wordart-watermark-to-chart).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
