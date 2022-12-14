---
title: Создание сводных диаграмм в xlsx4j
type: docs
weight: 30
url: /ru/java/create-pivot-charts-in-xlsx4j/
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

// Saving the Excel file

workbook.save(dataDir + "Aspose_PivotChart_Out.xls");


{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Создание сводных таблиц и сводных диаграмм](/cells/ru/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
