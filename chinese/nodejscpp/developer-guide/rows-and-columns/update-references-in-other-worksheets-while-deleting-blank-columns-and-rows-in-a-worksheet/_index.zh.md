---
title: 删除工作表中的空白列和行时更新其他工作表中的引用
linktitle: 删除工作表中的空白列和行时更新其他工作表中的引用
type: docs
weight: 5000
url: /zh/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: 学习如何在删除空白列和行时保持其他工作表中的引用不变，使用 Aspose.Cells for Node.js via C++。
---

{{% alert color="primary" %}}

当您删除工作表中的空白列和行时，其他工作表中对它们的引用将变得无效。如果您想避免此行为，并希望其他工作表中对当前工作表的引用也得到更新，那么请使用[**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--)属性并将其设置为**true**。

{{% /alert %}}

## **删除工作表中的空白列和行时更新其他工作表中的引用**

请查看以下示例代码及其控制台输出。第二个工作表中的单元格 E3 具有公式 =Sheet1!C3，引用第一个工作表中的 C3 单元格。如果将 [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) 属性设置为**true**，删除第一个工作表中的空白列和行后，该公式将更新为 =Sheet1!A1。然而，如果将 [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) 属性设置为**false**，第二个工作表中的 E3 单元格中的公式将保持不变，仍然是 =Sheet1!C3，此时公式无效。

### **编程示例**

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

### **控制台输出**

这是上述示例代码在将 [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) 属性设置为**true**时的控制台输出。

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

这是上述示例代码在将 [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) 属性设置为**false**时的控制台输出。可以看到，E3 单元格中的公式没有被更新，其值变为 0，而非 4，公式因此无效。

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
