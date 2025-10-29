---
title: Получить адрес, количество ячеек, смещение, весь столбец и всю строку диапазона с помощью Node.js через C++
linktitle: Получить адрес ячейки, количество ячеек смещение, весь столбец и вся строка диапазона
type: docs
weight: 330
url: /ru/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Возможные сценарии использования**
Aspose.Cells for Node.js via C++ предоставляет объект Range, который имеет различные утилитные методы, облегчающие работу с диапазонами Excel для пользователя. В этой статье иллюстрируется использование следующих методов или свойств объекта Range.

- **Адрес**

Получает адрес диапазона.

- **Количество ячеек**

Получает общее количество ячеек в диапазоне.

- **Смещение**

Получает диапазон смещения.

- **Весь столбец**

Получает объект Range, представляющий весь столбец (или столбцы), содержащий указанный диапазон.

- **Вся строка**

Получает объект Range, представляющий всю строку (или строки), содержащий указанный диапазон.

## **Получить адрес, количество ячеек, смещение, весь столбец и всю строку диапазона**
Приведенный ниже образец кода объясняет использование методов и свойств, описанных выше. Пожалуйста, обратитесь к выводу консоли приведенного ниже кода в качестве справки.

## **Образец кода**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **Вывод в консоль**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
