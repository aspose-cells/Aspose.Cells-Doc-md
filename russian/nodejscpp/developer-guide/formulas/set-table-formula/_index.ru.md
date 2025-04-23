---
title: Автоматическое распространение формулы в таблице или списке при вводе данных в новые строки с помощью Node.js через C++
linktitle: Устанавливает формулу таблицы
type: docs
weight: 260
url: /ru/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Узнайте, как автоматически распространять формулы в таблицах или списковых объектах при вводе данных в новые строки с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**
Иногда вы хотите, чтобы формула в вашей таблице или списковом объекте автоматически распространялась на новые строки при вводе новых данных. Это поведение по умолчанию в Microsoft Excel. Чтобы достичь той же функциональности с помощью Aspose.Cells for Node.js via C++, используйте свойство [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--).

## **Автоматически распространяйте формулу в таблице или списковом объекте при вводе данных в новые строки**
Следующий пример кода создает таблицу или списковый объект таким образом, что формула в столбце B автоматически распространяется на новые строки при вводе новых данных. Проверьте [созданный экспортированный файл Excel](5115469.xlsx). Если вы введете любое число в ячейку A3, вы увидите, что формула в ячейке B2 автоматически распространяется на ячейку B3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
