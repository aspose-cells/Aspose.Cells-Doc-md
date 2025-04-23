---
title: Считать Подзаголовок графика из файла ODS с помощью Node.js и C++
linktitle: Чтение подзаголовка диаграммы из файла ODS
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для чтения подзаголовка графика из файла OpenDocument Spreadsheet (ODS). Наше руководство покажет, как извлечь и получить доступ к подзаголовку графика для дальнейшего анализа или отображения.
keywords: Aspose.Cells for Node.js via C++, чтение подзаголовка графика, OpenDocument Spreadsheet, файл ODS, извлечение графика, анализ данных.
type: docs
weight: 160
url: /ru/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **Чтение подзаголовка диаграммы из файла ODS**

Aspose.Cells позволяет читать подзаголовки графиков в файлах ODS с помощью свойства [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--). Следующий пример кода загружает [пример файла ODS](89620481.ods) и читает подзаголовок графика с помощью свойства [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) и выводит его в окно консоли. Пожалуйста, ознакомьтесь с выводом кода ниже для справки.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Вывод в консоль**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
