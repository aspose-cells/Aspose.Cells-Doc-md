---
title : "Change Chart Position and Size" 
description : "" 
weight : 20647 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/featuresmissinginaph/charts/change+chart+position+and+size/
---

# Aspose.Cells for Java : Change Chart Position and Size


## Aspose.Cells - Change Chart Position and Size

To change the chart's position (X, Y coordinates) and size (height, width), use these properties using Aspose.Cells:

1.  Chart.getChartObject().get/setWidth()
2.  Chart.getChartObject().get/setHeight()
3.  Chart.getChartObject().get/setX()
4.  Chart.getChartObject().get/setY()

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

For more details, visit [Change the Chart Position and Size](http://www.aspose.com/docs/display/cellsjava/Change+the+Chart+Position+and+Size).

