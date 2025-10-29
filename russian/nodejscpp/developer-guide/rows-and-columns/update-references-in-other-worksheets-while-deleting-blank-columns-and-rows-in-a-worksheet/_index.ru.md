---
title: Обновление ссылок в других листах при удалении пустых столбцов и строк на листе
linktitle: Обновление ссылок в других листах при удалении пустых столбцов и строк на листе
type: docs
weight: 5000
url: /ru/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Узнайте, как сохранять ссылки на другие рабочие листы при удалении пустых столбцов и строк в рабочем листе с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Когда вы удаляете пустые столбцы и строки в листе, их ссылки в других листах становятся недействительными. Если вы хотите избежать этого поведения и хотите, чтобы эти ссылки текущего листа в других листах также обновлялись, то, пожалуйста, используйте свойство [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) и установите его в **true**.

{{% /alert %}}

## **Обновление ссылок в других листах при удалении пустых столбцов и строк на листе**

Пожалуйста, смотрите пример кода ниже и его вывод в консоли. В ячейке E3 второго листа находится формула =Sheet1!C3, которая ссылается на ячейку C3 первого листа. Если установить свойство [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) в **true**, эта формула будет обновлена и станет =Sheet1!A1 при удалении пустых столбцов и строк в первом листе. Однако, если установить свойство [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) в **false**, формула в ячейке E3 второго листа останется =Sheet1!C3 и станет недействительной.

### **Пример программирования**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add second sheet with name Sheet2
wb.getWorksheets().add("Sheet2");

// Access first sheet and add some integer value in cell C1
// Also add some value in any cell to increase the number of blank rows and columns
const sht1 = wb.getWorksheets().get(0);
sht1.getCells().get("C1").putValue(4);
sht1.getCells().get("K30").putValue(4);

// Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
const sht2 = wb.getWorksheets().get(1);
sht2.getCells().get("E3").setFormula("'Sheet1'!C1");

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
console.log("Cell E3 before deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());

// If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
const opts = new AsposeCells.DeleteOptions();
opts.setUpdateReference(true);

// Delete all blank rows and columns with delete options
sht1.getCells().deleteBlankColumns(opts);
sht1.getCells().deleteBlankRows(opts);

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
console.log("");
console.log("");
console.log("Cell E3 after deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());
```

### **Вывод в консоль**

Это вывод консоли вышеприведенного кода, когда свойство [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) установлено как **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Это вывод консоли вышеуказанного кода, когда свойство [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) установлено как **ложь**. Как видно, формула в ячейке E3 второго листа не обновляется, и ее значение ячейки теперь равно 0 вместо 4, что является недопустимым.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
