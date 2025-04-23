---  
title: Создание PDF из диаграммы с помощью Node.js через C++  
linktitle: Диаграмма в PDF  
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для преобразования диаграммы в документ PDF. Наш гид покажет, как экспортировать диаграмму из Microsoft Excel и сохранить её как PDF для дальнейшего распространения и архивации.  
keywords: Aspose.Cells for Node.js via C++, Диаграмма в PDF, Microsoft Excel, Конвертация в PDF, Экспорт, Распространение, Архивирование.  
type: docs  
weight: 47  
url: /ru/nodejs-cpp/chart-to-pdf/  
---  

## **Отображение диаграммы в формат PDF**

Чтобы отобразить диаграмму в формате PDF, API Aspose.Cells предоставили метод [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) с возможностью сохранить полученный PDF на диск или в поток.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to PDF
chart.toPdf(path.join(dataDir, "chartPDF_out.pdf"));
```

## **Создание PDF-файла диаграммы с выбранным размером страницы**  
Вы можете создать PDF диаграммы с желаемым размером страницы, используя Aspose.Cells, и указать, как вы хотите выровнять диаграмму внутри страницы: сверху, снизу, по центру, слева, справа и т.д. Также результативная диаграмма может быть создана в потоке или на диске. Ознакомьтесь с примером кода, который загружает [образец файла Excel](64716906.xlsx), получает первую диаграмму в листе и конвертирует её в [выходной PDF](64716907.pdf) с нужным размером страницы. Следующий скриншот показывает, что размер страницы в выходном PDF — 7x7, как указано в коде, а диаграмма выровнена по центру как по горизонтали, так и по вертикали.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Образец кода**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing the chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateChartPDFWithDesiredPageSize.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet.
const chart = worksheet.getCharts().get(0);

// Create chart pdf with desired page size.
chart.toPdf(path.join(outputDir, "outputCreateChartPDFWithDesiredPageSize.pdf"), 7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);
```  


