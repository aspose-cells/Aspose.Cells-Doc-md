---
title: Создание сводных диаграмм с помощью Aspose.Cells
type: docs
weight: 40
url: /ru/java/create-pivot-charts-using-aspose-cells/
---
## **Aspose.Cells - Создание сводных диаграмм**
Сводная таблица — это интерактивная сводка записей. Например, у вас могут быть сотни записей счетов в списке на листе. Сводная таблица может суммировать счета по клиентам, продуктам или датам. С Microsoft Excel можно быстро переупорядочить информацию в сводной таблице, перетаскивая кнопки в новое положение.
Сводная диаграмма — это интерактивное графическое представление данных в сводной таблице. Сводные диаграммы были представлены в Excel 2000. Использование сводных диаграмм еще больше упрощает понимание данных, поскольку сводная таблица автоматически создает промежуточные итоги и итоги.

Aspose.Cells поддерживает сводные таблицы и сводные диаграммы.

**Java**

{{< highlight "java" >}}

 // Instantiating an Workbook object

Workbook workbook = new Workbook(dataDir + "AsposePivotTable.xls");

// Adding a new sheet

int sheetIndex = workbook.getWorksheets().add(SheetType.CHART);

Worksheet sheet3 = workbook.getWorksheets().get(sheetIndex);

// Naming the sheet

sheet3.setName("PivotChart");

// Adding a column chart

int chartIndex = sheet3.getCharts().add(ChartType.COLUMN, 0, 5, 28, 16);

Chart chart = sheet3.getCharts().get(chartIndex);

// Setting the pivot chart data source

chart.setPivotSource("PivotTable!PivotTable1");

chart.setHidePivotFieldButtons(false);

{{< /highlight >}}
## **Скачать рабочий код**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Создание сводных таблиц и сводных диаграмм](/cells/ru/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
