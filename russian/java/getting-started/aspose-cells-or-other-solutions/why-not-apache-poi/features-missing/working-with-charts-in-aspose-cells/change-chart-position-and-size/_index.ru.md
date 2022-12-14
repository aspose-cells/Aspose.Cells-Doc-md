---
title: Изменить положение и размер диаграммы
type: docs
weight: 20
url: /ru/java/change-chart-position-and-size/
---
## **Aspose.Cells - Изменить положение и размер диаграммы**
Чтобы изменить положение диаграммы (координаты X, Y) и размер (высота, ширина), используйте эти свойства, используя Aspose.Cells:

1. Диаграмма.getChartObject().get/setWidth()
1. Диаграмма.getChartObject().get/setHeight()
1. Диаграмма.getChartObject().get/setX()
1. Диаграмма.getChartObject().get/setY()

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
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Изменить положение и размер диаграммы](/cells/ru/java/change-chart-position-and-size/).

{{% /alert %}}
