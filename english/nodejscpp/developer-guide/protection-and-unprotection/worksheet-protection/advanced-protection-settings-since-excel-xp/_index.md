---
title: Advanced Protection Settings since Excel XP with Node.js via C++
linktitle: Advanced Protection Settings since Excel XP
type: docs
weight: 30
url: /nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

Since the release of Excel 2002 or XP, Microsoft has added many advanced protection settings.

{{% /alert %}}


## **Introduction**

These protection settings restrict or allow users to:

- Delete rows or columns.
- Edit contents, objects, or scenarios.
- Format cells, rows, or columns.
- Insert rows, columns, or hyperlinks.
- Select locked or unlocked cells.
- Use pivot tables and much more.

Aspose.Cells for Node.js via C++ supports all the advanced protection settings offered by Excel XP or later versions.

### **Advanced Protection Settings Using Excel XP and Later Versions**

To view the protection settings available in Excel XP:

1. From the **Tools** menu, select **Protection** followed by **Protect Sheet**. A dialog will be displayed.

To view the protection settings available in Excel 2016:

1. From the **File** menu, select **Protect Workbook** followed by **Protect Current Sheet**.
1. Select the **Protect Sheet** in the **Review** menu.

Following the steps mentioned above will show a dialog where you can allow or restrict worksheet features or apply a password to the worksheet.

### **Advanced Protection Settings Using Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ supports all of the advanced protection settings.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class.

The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides the [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/protection) property that is used to apply these advanced protection settings. The [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/protection) property is in fact an object of the [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) class that encapsulates several Boolean properties for disabling or enabling restrictions.

Below is a small example application. It opens an Excel file and uses most of the advanced protection settings supported by Excel XP and later versions.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

Please don't call the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class' [**Protect**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/protect/index) method when using the [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/protection) property. Also, save the file to Excel97To2003 or Xlsx format because the advanced protection settings are only supported by Excel XP and later versions.

{{% /alert %}}

### **Cell Locking Issue**

If you want to restrict users from editing cells, the cells must be locked before any protection settings are applied. Otherwise, the cells can be edited even if the worksheet is protected. In Microsoft Excel XP, cells can be locked through the following dialog:

|**Dialog to lock cells in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

It is possible to lock cells using the Aspose.Cells API too. Each cell can get [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) formatting that contains a Boolean property, [**IsLocked**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/islocked). Set the [**IsLocked**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/islocked) property to **true** or **false** to lock or unlock the cell.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
