---
title: Установите цвет заливки пункта легенды графика в none, используя Aspose.Cells for Node.js via C++
linktitle: Установите текст заливки записи легенды диаграммы на отсутствие с использованием Aspose.Cells
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для установки цвета заливки пункта легенды графика в None. Это руководство продемонстрирует, как изменить цвет заливки элементов легенды в графиках Microsoft Excel для лучшей визуализации и кастомизации.
keywords: Aspose.Cells for Node.js via C++, Заполнение пункта легенды графика, Microsoft Excel, визуализация, настройка.
type: docs
weight: 320
url: /ru/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Если хотите установить цвет заливки пункта легенды графика в none, чтобы он не отображался внутри легенды графика, установите [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--) в **true**.

{{% /alert %}}

В следующем образце кода устанавливается текст заливки второй записи легенды графика на никуда. Скачайте [образец excel-файла](5115219.xlsx), использованный в этом коде, и [выходной excel-файл](5115217.xlsx), который он создает, для вашего ориентира.

Следующий снимок экрана демонстрирует эффект этого кода на [пример файле Excel](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
