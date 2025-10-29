---  
title: Как создать график TreeMap с помощью Node.js через C++  
linktitle: Как создать диаграмму древовидной карты  
description: Узнайте, как создать график Treemap в Aspose.Cells for Node.js via C++. Наше руководство поможет вам понять различные свойства и параметры форматирования для графиков TreeMap, включая цвета, метки и отображение данных.  
keywords: Aspose.Cells для Node.js, график Treemap, создание, свойства, форматирование, цвета, метки, отображение данных, круговая диаграмма, иерархическое моделирование.  
type: docs  
weight: 161  
url: /ru/nodejs-cpp/creating-treemap-chart/  
---  

## **Возможные сценарии использования**  
Диаграмма древовидной карты обеспечивает иерархический обзор ваших данных и упрощает обнаружение шаблонов, таких как наиболее продаваемые товары в магазине. Ветки дерева представлены прямоугольниками, и каждая подветка отображается в виде меньшего прямоугольника. Диаграмма древовидной карты отображает категории цветом и близостью и легко позволяет отображать большое количество данных, что было бы сложно с другими типами диаграмм.  

![todo:image_alt_text](sample.png)  
## **Диаграмма древовидной карты**  
После выполнения приведенного ниже кода вы увидите диаграмму древовидной карты, как показано ниже.  

![todo:image_alt_text](result.png)  
## **Образец кода**  
Приведенный ниже образец кода загружает [образец файла Excel](treemap.xlsx) и генерирует [выходной файл Excel](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
