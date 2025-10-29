---
title: Создание пользовательских цветов сегментов или секторов в круговой диаграмме с помощью Node.js через C++
linktitle: Настройка цветов круговой диаграммы
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для настройки цветов сегментов и секторов в круговой диаграмме. Наше руководство покажет, как назначить уникальные цвета каждому сегменту, сектору или легиону для улучшения визуальной привлекательности и представления данных.
keywords: Aspose.Cells for Node.js via C++, Круговая диаграмма, Пользовательские цвета сегментов, Пользовательские цвета секторов, Визуальная привлекательность, Представление данных.
type: docs
weight: 60
url: /ru/nodejs-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета к сегментам/секторам круговой диаграммы. По умолчанию круговые диаграммы используют шаблон Microsoft Excel по умолчанию. Чтобы использовать другие цвета, перепределите цвета в диаграмме.

{{% /alert %}}

Чтобы установить пользоватский цвет для отдельных секторов или секторов круговой диаграммы:

1. Получите доступ к объекту [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) через его свойство [**ChartPoint**](https://reference.aspose.com/cells/nodejs-cpp/chartpoint).
1. Назначьте цвет по вашему выбору, используя свойство [**ChartPoint.getForegroundColor()**](https://reference.aspose.com/cells/nodejs-cpp/area/#getForegroundColor--).

В этой статье также объясняется, как:

- Категорийные данные диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Положение легенды.

{{% alert color="primary" %}}

[**ChartPoint.getForegroundColor()**](https://reference.aspose.com/cells/nodejs-cpp/area/#getForegroundColor--) не является специфичным для круговых диаграмм, но может быть использован для всех типов диаграмм.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a pie chart
worksheet.getCells().get("C3").putValue("India");
worksheet.getCells().get("C4").putValue("China");
worksheet.getCells().get("C5").putValue("United States");
worksheet.getCells().get("C6").putValue("Russia");
worksheet.getCells().get("C7").putValue("United Kingdom");
worksheet.getCells().get("C8").putValue("Others");

// Put the sample values used in a pie chart
worksheet.getCells().get("D2").putValue("% of world population");
worksheet.getCells().get("D3").putValue(25);
worksheet.getCells().get("D4").putValue(30);
worksheet.getCells().get("D5").putValue(10);
worksheet.getCells().get("D6").putValue(13);
worksheet.getCells().get("D7").putValue(9);
worksheet.getCells().get("D8").putValue(13);

// Create a pie chart with desired length and width
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 1, 6, 15, 14);

// Access the pie chart
const pie = worksheet.getCharts().get(pieIdx);

// Set the pie chart series
pie.getNSeries().add("D3:D8", true);

// Set the category data
pie.getNSeries().setCategoryData("=Sheet1!$C$3:$C$8");

// Set the chart title that is linked to cell D2
pie.getTitle().setLinkedSource("D2");

// Set the legend position at the bottom.
pie.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Set the chart title's font name and color
pie.getTitle().getFont().setName("Calibri");
pie.getTitle().getFont().setSize(18);

// Access the chart series
const srs = pie.getNSeries().get(0);

// Color the individual points with custom colors
srs.getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 246, 22, 219));
srs.getPoints().get(1).getArea().setForegroundColor(new AsposeCells.Color(0, 51, 34, 84));
srs.getPoints().get(2).getArea().setForegroundColor(new AsposeCells.Color(0, 46, 74, 44));
srs.getPoints().get(3).getArea().setForegroundColor(new AsposeCells.Color(0, 19, 99, 44));
srs.getPoints().get(4).getArea().setForegroundColor(new AsposeCells.Color(0, 208, 223, 7));
srs.getPoints().get(5).getArea().setForegroundColor(new AsposeCells.Color(0, 222, 69, 8));

// Autofit all columns
worksheet.autoFitColumns();

const outputPath = path.join(dataDir, "output.out.xlsx");
// Save the workbook
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
