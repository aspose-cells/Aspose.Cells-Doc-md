---
title: Cambiar Posición y Tamaño del Gráfico
type: docs
weight: 20
url: /es/java/change-chart-position-and-size/
---

## **Aspose.Cells - Cambiar Posición y Tamaño del Gráfico**
Para cambiar la posición (coordenadas X, Y) y el tamaño (altura, ancho) del gráfico, utiliza estas propiedades usando Aspose.Cells:

1. Chart.getChartObject().get/setWidth()
1. Chart.getChartObject().get/setHeight()
1. Chart.getChartObject().get/setX()
1. Chart.getChartObject().get/setY()

**Java**

{{< highlight java >}}

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
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Cambiar la Posición y Tamaño del Gráfico](/cells/es/java/change-chart-position-and-size/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
