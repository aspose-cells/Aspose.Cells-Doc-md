---
title: Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона с помощью Node.js через C++
linktitle: Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона
description: Узнайте, как изменить источник данных диаграммы на целевой лист при копировании строк или диапазона в Aspose.Cells for Node.js via C++. Руководство демонстрирует, как обновить диапазон данных диаграммы и связать его с целевым листом.
keywords: Aspose.Cells for Node.js via C++, построение графиков, источник данных, целевой лист, строки, диапазон, копирование, обновление, диапазон данных, связка.
type: docs
weight: 440
url: /ru/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Возможные сценарии использования**

Когда вы копируете строки или диапазон, содержащий диаграммы, на новый лист, источник данных диаграммы не изменяется. Например, если источник данных диаграммы `=Sheet1!$A$1:$B$4`, то после копирования строк или диапазона на новый лист, источник данных останется таким же - `=Sheet1!$A$1:$B$4`. Он по-прежнему ссылается на старый лист, то есть Sheet1. Это поведение также в Microsoft Excel. Но если вы хотите, чтобы он ссылался на новый целевой лист, используйте свойство [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) и задайте его значение **true** при вызове метода [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-). Например, если ваш целевой лист DestSheet, источник данных диаграммы изменится с `=Sheet1!$A$1:$B$4` на `=DestSheet!$A$1:$B$4`.

## **Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона**

Следующий пример кода объясняет использование свойства [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) при копировании строк или диапазона с диаграммами на новый лист. Код использует [образец файла Excel](5113699.xlsx) и создает [выходной файл Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
