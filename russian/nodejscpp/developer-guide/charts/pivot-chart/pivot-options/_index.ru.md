---
title: Как управлять PivotChart с PivotOptions для Node.js через C++
linktitle: Опции сводной таблицы
type: docs
weight: 10
url: /ru/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Как управлять PivotChart с помощью PivotOptions в Node.js через C++.
keywords: Сводная диаграмма Node.js через C++
---
## Что такое сводная диаграмма

Сводная диаграмма в Excel - это графическое представление данных, созданное на основе сводной таблицы. Она позволяет пользователям визуализировать и анализировать данные динамически, суммируя и отображая информацию в виде диаграммы. Сводные диаграммы интерактивны и их легко изменять, чтобы показать различные перспективы данных, что делает их мощным инструментом для анализа и презентации данных в Excel.

## Как управлять сводной диаграммой с опциями сводной таблицы

Используя Aspose.Cells for Node.js via C++, вы можете использовать [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) для управления PivotChart.

Пример файла и кода:
[Образец файла](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

С помощью вышеуказанного примера кода вы можете проверить результатный файл с следующим эффектом, как показано на рисунке:

**![Вывод](Output.png)**
