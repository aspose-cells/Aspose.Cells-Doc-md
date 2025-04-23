---
title: Как проверить состояние фиксации без Excel, используя Node.js и C++
linktitle: Замороженное состояние
type: docs
weight: 190
url: /ru/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: В этой статье вы узнаете, как программно проверить состояние фиксации листа Excel, используя Node.js с библиотекой C++.

---

## **Введение**

В этой статье мы научимся программно проверять, зафиксирован ли лист Excel. В MS Excel легко определить, зафиксирован ли лист или разделён. Но есть ли способ узнать это с помощью Node.js? Мы можем сделать это с помощью Aspose.Cells for Node.js via C++.

## **Заморожены ли оконные рамы**
С помощью Aspose.Cells for Node.js via C++ мы можем проверить, зафиксировано ли окно и сколько строк и столбцов заблокировано.

Пожалуйста, используйте свойство [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--), чтобы проверить состояние оконных панелей и получить заблокированные строки и столбцы с помощью метода [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--).
1. Создайте рабочую книгу для открытия файла.
2. Проверьте, заморожен ли лист.
3. Получить заблокированные строки и столбцы.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
