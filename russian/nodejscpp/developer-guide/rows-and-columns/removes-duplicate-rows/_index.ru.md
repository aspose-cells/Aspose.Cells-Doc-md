---
title: Удаление дублирующихся строк в рабочем листе с помощью Node.js через C++
linktitle: Удаление дублирующихся строк в листе
type: docs
weight: 370
url: /ru/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Узнайте, как удалять дублирующиеся строки в рабочем листе с использованием Aspose.Cells for Node.js via C++ и выбрать конкретные столбцы для проверки на дубликаты.
---


Удаление дублирующихся строк — одна из полезных функций Microsoft Excel. Она позволяет пользователям удалять повторяющиеся строки в рабочем листе, и вы можете выбрать, какие столбцы проверять на дублирование информации.

Aspose.Cells for Node.js via C++ предоставляет метод `Cells.removeDuplicates()` для этой цели. Также можно задать `startRow`, `startColumn`, `endRow`, и `endColumn`, чтобы указать диапазон, в котором искать дубликаты.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
