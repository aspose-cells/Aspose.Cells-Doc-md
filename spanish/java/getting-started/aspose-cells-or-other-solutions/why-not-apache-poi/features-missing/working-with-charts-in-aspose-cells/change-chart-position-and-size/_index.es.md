---
title: Cambiar la posición y el tamaño del gráfico
type: docs
weight: 20
url: /es/java/change-chart-position-and-size/
---
## **Aspose.Cells - Cambiar posición y tamaño del gráfico**
Para cambiar la posición del gráfico (coordenadas X, Y) y el tamaño (alto, ancho), use estas propiedades usando Aspose.Cells:

1. Gráfico.getChartObject().get/setWidth()
1. Gráfico.getChartObject().get/setHeight()
1. Gráfico.getChartObject().get/setX()
1. Gráfico.getChartObject().get/setY()

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

Worksheet worksheet = workbook.getWorksheets().get(0);

//Load the chart from source worksheet

Chart chart = worksheet.getCharts().get(0);

//Resize the chart

chart.getChartObject().setWidth(400);

chart.getChartObject().setHeight(300);

//Reposition the chart

chart.getChartObject().setX(250);

chart.getChartObject().setY(150);

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Cambiar la posición y el tamaño del gráfico](/cells/es/java/change-chart-position-and-size/).

{{% /alert %}}
