---
title: 更改图表位置和大小
type: docs
weight: 20
url: /zh/java/change-chart-position-and-size/
---
## **Aspose.Cells - 更改图表位置和大小**
要更改图表的位置（X、Y 坐标）和大小（高度、宽度），请使用 Aspose.Cells 使用这些属性：

1. Chart.getChartObject().get/setWidth() 方法
1. 图表.getChartObject().get/setHeight()
1. 图表.getChartObject().get/setX()
1. 图表.getChartObject().get/setY()

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[更改图表位置和大小](/cells/zh/java/change-chart-position-and-size/).

{{% /alert %}}
