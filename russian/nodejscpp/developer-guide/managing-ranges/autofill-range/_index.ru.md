---
title: Автоматическое заполнение диапазона файла Excel с помощью Node.js через C++
linktitle: Автозаполнение диапазона
type: docs
weight: 105
url: /ru/nodejs-cpp/autofill-ranges/
description: Узнайте, как выполнить операцию автоматического заполнения в указанном диапазоне файла Excel с помощью Aspose.Cells for Node.js via C++.
---

##  **Выполните автозаполнение в указанном диапазоне в Excel**

В Excel выберите диапазон, переместите мышь в правый нижний угол и перетащите "плюс" для автозаполнения данных.

## **Автозаполнение диапазонов с помощью Aspose.Cells for Node.js via C++**

Следующий пример показывает, как выполнить операцию автозаполнения диапазона, а также приводится пример файла, который можно скачать для тестирования этой функции:

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
