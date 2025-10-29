---
title: Использование функции FormulaText в Aspose.Cells for Node.js via C++
linktitle: Использование функции FormulaText в Aspose.Cells
description: В этой статье показано, как использовать функцию FormulaText в библиотеке Aspose.Cells для обработки формул в Microsoft Excel. Узнайте, как получать и задавать текст формулы в ячейках и сохранять измененные файлы Excel с помощью Node.js через C++.
keywords: Aspose.Cells, Excel, функции FormulaText, Node.js через C++
type: docs
weight: 60
url: /ru/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText — функция для Excel 2013 и более новых версий. Она не поддерживается в предыдущих версиях, таких как Excel 2010 или 2007. Как следует из названия, она выводит текст формулы, содержащейся в заданной ячейке. В этой статье показано, как использовать эту функцию с Aspose.Cells for Node.js via C++.

{{% /alert %}} 

Следующий пример кода показывает использование FormulaText с Aspose.Cells for Node.js via C++. В коде сначала записывается формула в ячейку A1, а затем текст формулы выводится с помощью FormulaText в ячейке A2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
