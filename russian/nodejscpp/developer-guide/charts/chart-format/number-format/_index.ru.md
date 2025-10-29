---
title: Настройка кода формата значений для серии диаграммы с помощью Node.js через C++
description: Узнайте, как установить код формата значений серии диаграммы в Aspose.Cells for Node.js via C++. Руководство поможет вам понять, как форматировать данные серии диаграммы с помощью соответствующего кода формата, позволяя точно и профессионально представлять ваши данные.
keywords: Aspose.Cells для Node.js, серия диаграммы, код формата значений, форматирование, представление данных, точность, профессионализм.
linktitle: Формат числа
type: docs
weight: 100
url: /ru/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **Возможные сценарии использования**
Вы можете установить код формата значений серии диаграммы, используя свойство [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--). Это свойство полезно не только для серий, основанных на диапазоне внутри листа, но и хорошо работает для серий, созданных с массивом значений.

## **Установить код формата значений серии графика**
Следующий пример кода добавляет серию в пустую диаграмму, которая раньше не имела серий. Он добавляет серию с помощью массива значений. После добавления серии, она форматируется с кодом $#,##0 с помощью свойства [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--), и число 10000 становится $10,000. Скриншот показывает эффект кода на [пример файле Excel](51740712.xlsx) и [выходном файле Excel](51740713.xlsx) после выполнения.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Образец кода**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
