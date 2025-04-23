---
title: Изменить позицию и размер графика
type: docs
weight: 20
url: /ru/java/change-chart-position-and-size/
---

## **Aspose.Cells - Изменить позицию и размер графика**
Чтобы изменить позицию графика (координаты X, Y) и размер (высоту, ширину), используйте эти свойства с помощью Aspose.Cells:

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
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Изменить позицию и размер графика](/cells/ru/java/change-chart-position-and-size/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
