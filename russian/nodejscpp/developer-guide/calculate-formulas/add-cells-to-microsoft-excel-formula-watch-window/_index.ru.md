---
title: Добавление ячеек в окно отслеживания формул Microsoft Excel с Node.js через C++
linktitle: Добавление ячеек в окно наблюдения формул Microsoft Excel
description: Как использовать библиотеку Aspose.Cells для добавления ячеек в окно отслеживания формул в Excel с помощью Node.js через C++. Загружая существующий файл Excel или создавая новый, мы можем манипулировать ячейками и задавать формулы. В конце мы сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, окно отслеживания формул, ячейки, добавление, Node.js через C++
type: docs
weight: 60
url: /ru/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Возможные сценарии использования**

Окно наблюдения Microsoft Excel — полезный инструмент для удобного отслеживания значений ячеек и их формул. Вы можете открыть *Окно наблюдения* в Microsoft Excel, щёлкнув по *Формулы > Окно наблюдения*. В нём есть кнопка *Добавить наблюдение*, которую можно использовать для добавления ячеек для проверки. Аналогично, вы можете использовать метод [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-), чтобы добавлять ячейки в *Окно наблюдения* через API Aspose.Cells.

## **Добавление ячеек в окно наблюдения формул Microsoft Excel**

Следующий пример кода задаёт формулу ячеек C1 и E1 и добавляет их в Окно наблюдения. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338481.xlsx). Если открыть выходной файл Excel и просмотреть *Окно наблюдения*, вы увидите обе ячейки, как показано на скриншоте.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

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

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
