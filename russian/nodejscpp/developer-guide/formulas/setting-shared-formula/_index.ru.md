---
title: Установка общей формулы с помощью Node.js через C++
linktitle: Настройка общих формул
type: docs
weight: 10
url: /ru/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Если вы хотите добавить функцию в лист, которая будет выполнять какие-либо вычисления, это руководство объяснит, как достичь этой задачи с помощью Aspose.Cells for Node.js via C++.

{{% /alert %}}

## Установка общей формулы с помощью Aspose.Cells for Node.js via C++

Предположим, у вас есть лист с данными в формате, который выглядит как приведенный ниже образец листа.

|**Входной файл с одним столбцом данных**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Вы хотите добавить функцию в B2, которая будет вычислять налог с продаж для первой строки данных. Налог составляет **9%**. Формула, вычисляющая налог с продаж, такова: **"=A2*0.09"**. В этой статье объясняется, как применить эту формулу с помощью Aspose.Cells.

Aspose.Cells позволяет указывать формулу, используя свойство [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--). Для других ячеек (B3, B4, B5 и так далее) в столбце есть два варианта добавления формул.

Либо выполните то, что вы делали для первой ячейки, фактически устанавливая формулу для каждой ячейки, соответствующим образом обновляя ссылку на ячейку (A3*0.09, A4*0.09, A5*0.09 и так далее). Это требует обновления ссылок на ячейки для каждой строки. Также необходимо, чтобы Aspose.Cells анализировал каждую формулу отдельно, что может быть затратным по времени для больших таблиц и сложных формул. Кроме того, это требует дополнительных строк кода, хотя циклы могут немного сократить их.

Другой подход - использовать **общую формулу**. С общей формулой формулы автоматически обновляются для ссылок на ячейки в каждой строке, чтобы налог был рассчитан правильно. Метод [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) более эффективен, чем первый метод.

Приведенный ниже пример демонстрирует, как его использовать.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
