---
title: Как создать солнечную диаграмму с помощью Node.js через C++
linktitle: Как создать диаграмму солнце
description: Узнайте, как создать солнечную диаграмму в Aspose.Cells for Node.js via C++ — диаграмму, которая отображает данные в круге. Наше руководство поможет вам настроить различные свойства и форматирование вашей диаграммы, включая метки данных, легенды, цвета и многое другое.
keywords: Aspose.Cells for Node.js via C++, солнечная диаграмма, создание, установка свойств, метки данных, легенда, формат, цвет, круг, отображение данных.
type: docs
weight: 162
url: /ru/nodejs-cpp/creating-sunburst-chart/
---

## **Возможные сценарии использования**
Круговые диаграммы хороши для сравнения пропорций внутри иерархии; однако круговые диаграммы не очень подходят для отображения уровней внутри иерархии между крупнейшими категориями и отдельными точками данных. Солнечная диаграмма значительно лучше показывает это. Солнечная диаграмма идеально подходит для отображения иерархических данных. Каждый уровень иерархии представлен одним кольцом или кругом, при этом внутреннее кольцо — вершина иерархии. Солнечная диаграмма без иерархических данных (один уровень категорий) выглядит похожей на кольцевую диаграмму. Однако солнечная диаграмма с несколькими уровнями категорий показывает, как внешние кольца связаны с внутренними. Эффективность солнечной диаграммы заключается в показе того, как одно кольцо делится на его составные части, в то время как другой тип иерархической диаграммы, график-дерево, отлично подходит для сравнения относительных размеров.

![todo:image_alt_text](sample.png)
## **Диаграмма созвездия**
После выполнения приведенного ниже кода вы увидите диаграмму созвездия, как показано ниже.

![todo:image_alt_text](result.png)
## **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](sunburst.xlsx) и генерирует [выходной файл Excel](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
