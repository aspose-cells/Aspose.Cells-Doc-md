---
title: Разделение экрана листа Excel с помощью Node.js и C++
linktitle: Разделенный экран
type: docs
weight: 190
url: /ru/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: В этой статье вы узнаете, как программно разбивать лист Excel на две или четыре части с помощью Node.js C++ Addon с помощью разделения листа на отдельные области.
keywords: Заморозить верхние строки, Заморозить верхнюю строку.
---

## **Введение**

В этой статье мы узнаем, как отображать определенные строки и/или столбцы в отдельных панелях с помощью разделения листа на две или четыре части. При работе с большими наборами данных нам нужно видеть несколько областей одного листа одновременно, чтобы сравнить разные подмножества данных. Функция разделения экрана поможет вам в этом.

## **Как разделить экран в Excel**
Чтобы разделить таблицу на две или четыре части, выполните следующее:

1. Выберите строку/столбец/ячейку до которой вы хотите разместить разбиение.
2. На вкладке Вид в группе Окна нажмите кнопку Разделить.

**![Разделить экран](Split-Screen.png)**

## **Разделить лист вертикально по столбцам**

Для разделения двух областей электронной таблицы вертикально выберите столбец справа от столбца, где вы хотите появление разделения, и нажмите кнопку Разделить в Excel.

Легко разделить лист вертикально по столбцам программным способом с помощью Aspose.Cells for Node.js via C++, нам нужно выбрать одну ячейку в верхней строке в качестве активной, затем выполнить деление с помощью метода [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **Разделить лист горизонтально по строкам**
Чтобы разделить ваше окно Excel горизонтально, выберите строку ниже строки, где вы хотите, чтобы произошло разделение в Excel.

Легко разделить лист горизонтально по строкам программным способом с помощью Aspose.Cells for Node.js via C++, нам нужно выбрать одну ячейку в левом столбце в качестве активной, затем выполнить деление с помощью метода [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **Разделение листа на четыре части**
Чтобы просматривать одновременно четыре различных раздела одного листа, разделите экран как вертикально, так и горизонтально в Excel.

Легко разделить лист вертикально по столбцам программным способом с помощью Aspose.Cells for Node.js via C++, необходимо выбрать одну ячейку не в первой строке и не в первом столбце в качестве активной, затем выполнить деление с помощью метода [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **Как удалить разделение**
Чтобы удалить разделение листа, просто повторно нажмите кнопку Разделить.

Aspose.Cells for Node.js via C++ предоставляет метод [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) для удаления настроек разделения.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

