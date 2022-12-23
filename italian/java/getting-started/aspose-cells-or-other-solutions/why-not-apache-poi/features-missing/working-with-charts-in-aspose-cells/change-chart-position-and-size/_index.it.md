---
title: Cambia la posizione e le dimensioni del grafico
type: docs
weight: 20
url: /it/java/change-chart-position-and-size/
---
## **Aspose.Cells - Cambia posizione e dimensione del grafico**
Per modificare la posizione del grafico (coordinate X, Y) e le dimensioni (altezza, larghezza), utilizzare queste proprietà utilizzando Aspose.Cells:

1. Grafico.getChartObject().get/setWidth()
1. Grafico.getChartObject().get/setHeight()
1. Grafico.getChartObject().get/setX()
1. Grafico.getChartObject().get/setY()

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Modificare la posizione e le dimensioni del grafico](/cells/it/java/change-chart-position-and-size/).

{{% /alert %}}
