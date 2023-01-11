---
title: Change Chart Position and Size
type: docs
weight: 20
url: /java/change-chart-position-and-size/
---

## **Aspose.Cells - Change Chart Position and Size**
To change the chart's position (X, Y coordinates) and size (height, width), use these properties using Aspose.Cells:

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
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

For more details, visit [Change the Chart Position and Size](/cells/java/change-chart-position-and-size/).

{{% /alert %}}