---
title: Отключить перенос текста для меток данных диаграммы с помощью Node.js через C++
description: Узнайте, как отключить перенос текста для меток данных в диаграммах с помощью Aspose.Cells for Node.js via C++. Наше руководство покажет вам, как предотвратить наложение длинных меток и обеспечить более понятное отображение графика.
keywords: Aspose.Cells for Node.js via C++, построение диаграмм, метки данных, перенос текста, наложение, читаемость, отображение.
type: docs
weight: 70
url: /ru/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 позволяет пользователям включать или отключать перенос текста в метках данных диаграммы. По умолчанию текст в метках данных диаграммы находится в перенесенном состоянии.

Aspose.Cells предоставляет свойство [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--), которое можно установить в true или false для включения или отключения переноса текста меток данных соответственно.

{{% /alert %}}

Ниже приведен образец кода, показывающий, как отключить перенос текста для меток данных диаграммы.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
