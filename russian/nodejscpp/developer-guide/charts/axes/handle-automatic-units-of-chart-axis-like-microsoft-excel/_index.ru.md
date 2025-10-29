---  
title: Обработка автоматических единиц оси диаграммы, как в Microsoft Excel, с помощью Node.js через C++  
linktitle: Обработка автоматических единиц оси диаграммы, как в Microsoft Excel  
description: Узнайте, как управлять автоматическими единицами осей диаграмм в Aspose.Cells for Node.js via C++. Наш гид покажет вам, как настроить и кастомизировать автоматические единицы на оси диаграммы, включая отображение научной нотации и корректировку масштаба.  
keywords: Aspose.Cells for Node.js via C++, оси диаграмм, автоматические единицы, Microsoft Excel, настройка, кастомизация, научная нотация, масштабирование.  
type: docs  
weight: 120  
url: /ru/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **Возможные сценарии использования**  
Ранние версии Aspose.Cells for Node.js via C++ не могли правильно обрабатывать автоматические единицы оси диаграммы при создании изображения или PDF. Сейчас Aspose.Cells for Node.js via C++ поддерживает обработку автоматических единиц оси диаграммы. Нет необходимости менять код. Просто преобразуйте вашу диаграмму в изображение или PDF, и она отобразит ось так же, как в Microsoft Excel.  

## **Обработка автоматических единиц оси диаграммы, как в Microsoft Excel**  
Следующий пример кода загружает [образец Excel файла](61767755.xlsx) и создает [выходной PDF с диаграммой](61767752.pdf). Скриншот показывает автоматические единицы оси диаграммы в красных прямоугольниках и сравнивает диаграмму из файла Excel с PDF-выводом. Оба точно совпадают.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Образец кода**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
