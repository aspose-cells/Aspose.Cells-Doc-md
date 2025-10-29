---
title: Как установить серию невидимой с помощью Node.js через C++
linktitle: Как сделать серию невидимой
description: Узнайте, как скрыть серию в Excel с помощью Aspose.Cells for Node.js via C++. 
keywords: Диаграмма Excel, серия, невидима, IsFiltered Node.js через C++
type: docs
weight: 74
url: /ru/nodejs-cpp/how-to-set-series-invisible/
---

## Как сделать серию невидимой в диаграмме Excel

В Excel можно щёлкнуть правой кнопкой по диаграмме, выбрать "Выбрать данные", и в появившемся окне проверить или снять выделение с серии, чтобы сделать её невидимой. Вы можете скачать [пример файла](SeriesFiltered.xlsx) и работать с ним в Excel, как показано на рисунке, чтобы реализовать эту функцию. Далее мы расскажем, как достичь этого с помощью библиотеки Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Как сделать серию невидимой с помощью Aspose.Cells 

Мы используем следующий код, чтобы сделать серию невидимой с помощью Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Вы можете получить следующий [входной файл](SeriesFiltered.xlsx) и [выходной файл](output.xlsx).

Как показано на рисунке ниже, первые две серии, которые изначально были видимы, стали невидимыми в выходном файле.
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="nodejs-cpp" >}}
