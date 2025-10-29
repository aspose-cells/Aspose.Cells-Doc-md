---  
title: Управление DataLabels графиков Excel с Node.js через C++  
description: Научитесь эффективно управлять метками данных в графиках Excel с помощью Aspose.Cells for Node.js via C++. Этот подробный гид охватывает различные задачи управления, включая добавление, удаление и изменение меток для повышения читаемости и удобства использования графиков.  
keywords: Aspose.Cells для Node.js, графики Excel, метки данных, управление, читаемость, удобство, добавление, удаление, изменение.  
linktitle: Метки данных  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

Метки данных - важная часть диаграммы.  
Мы легко можем узнать значение, процент и т. д. каждого ряда  

{{% /alert %}}  

## **Опции меток данных**  
Aspose.Cells for Node.js via C++ также позволяет управлять метками данных графика во время выполнения с помощью объекта [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/), его просто перемещать, обновлять и форматировать метки графика.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Управление метками данных диаграммы**  
Управление метками данных графика с Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/) — просто.  

Следующий фрагмент кода демонстрирует, как управлять DataLabels:  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **Продвинутые темы**  
- [Добавление пользовательских меток к данным точек в серии диаграммы](/cells/ru/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Отключение переноса текста для меток данных диаграммы](/cells/ru/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Изменение формы метки данных диаграммы для подгонки текста](/cells/ru/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Настройка метки данных диаграммы точки с использованием разностных стилей](/cells/ru/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Установка типа формы меток данных диаграммы](/cells/ru/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Показ диапазона ячеек в качестве меток данных](/cells/ru/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
