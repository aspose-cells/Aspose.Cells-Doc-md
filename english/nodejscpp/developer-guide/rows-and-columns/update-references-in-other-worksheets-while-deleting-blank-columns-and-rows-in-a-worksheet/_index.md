---
title: Update references in other worksheets while deleting blank columns and rows in a worksheet
linktitle: Update references in other worksheets while deleting blank columns and rows in a worksheet
type: docs
weight: 5000
url: /nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Learn how to maintain references in other worksheets when deleting blank columns and rows in a worksheet using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

When you delete blank columns and rows in a worksheet, then its references in other worksheets become invalid. If you want to avoid this behavior and want those references of the current worksheet in other worksheets are also updated, then please use the [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#updatereference) property and set it to **true**.

{{% /alert %}}

## **Update references in other worksheets while deleting blank columns and rows in a worksheet**

Please see the following sample code and its console output. The cell E3 in the second worksheet has a formula =Sheet1!C3 which is referring to cell C3 in the first worksheet. If you will set [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#updatereference) property as **true**, this formula will be updated and become =Sheet1!A1 on deleting blank columns and rows in the first worksheet. However, if you will set [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#updatereference) property as **false**, the formula in cell E3 of the second worksheet will remain =Sheet1!C3 and become invalid.

### **Programming Sample**

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

### **Console Output**

This is the console output of the above sample code when [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#updatereference) property has been set as **true**.

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

This is the console output of the above sample code when [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#updatereference) property has been set as **false**. As you can see, the formula in cell E3 of the second worksheet is not updated and its cell value is now 0 instead of 4 which is invalid.

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
