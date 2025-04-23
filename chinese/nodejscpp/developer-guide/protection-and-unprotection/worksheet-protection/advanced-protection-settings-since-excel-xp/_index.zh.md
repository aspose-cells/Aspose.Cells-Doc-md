---
title: 使用Node.js通过C++实现Excel XP及以后版本的高级保护设置
linktitle: 自Excel XP以来的高级保护设置
type: docs
weight: 30
url: /zh/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

自Excel 2002或XP发布以来，微软已添加了许多高级保护设置。

{{% /alert %}}


## **介绍**

这些保护设置限制或允许用户:

- 删除行或列。
- 编辑内容、对象或场景。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等功能。

Aspose.Cells for Node.js via C++支持Excel XP及更高版本提供的所有高级保护设置。

### **使用Excel XP和更高版本的高级保护设置**

要查看Excel XP中提供的保护设置：

1. 从**工具**菜单中选择**保护**，然后选择**保护工作表**。将显示一个对话框。

 在Excel 2016中查看可用的保护设置：

1. 从**文件**菜单中选择**保护工作簿**，然后选择**保护当前工作表**。
1. 在**审阅**菜单中选择**保护工作表**。

 按照上述步骤操作，将弹出一个对话框，您可以在其中允许或限制工作表功能，或为工作表设置密码。

### **使用Aspose.Cells for Node.js via C++实现高级保护设置**

Aspose.Cells for Node.js via C++支持所有高级保护设置。

Aspose.Cells 提供了一个类，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，它代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供了 [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) 属性，用于应用这些高级保护设置。[**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) 属性实际上是 [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) 类的对象，封装了几个布尔属性，用于禁用或启用限制。

下面是一个小例子应用程序。它打开一个 Excel 文件，并使用 Excel XP 及更新版本支持的大部分高级保护设置。

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

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

 在使用 [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) 属性时，请勿调用 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类的 [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) 方法。此外，应将文件保存为Excel97至2003或Xlsx格式，因为高级保护设置只支持Excel XP及更高版本。

{{% /alert %}}

### **单元格锁定问题**

 如果要限制用户编辑单元格，必须在应用任何保护设置之前将单元格锁定。否则，即使工作表受保护，单元格仍可编辑。在Microsoft Excel XP中，可以通过以下对话框锁定单元格：

|**在Excel XP中锁定单元格的对话框**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

也可以使用 Aspose.Cells API 来锁定单元格。每个单元格可以获得 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 格式，其中包含一个布尔属性 [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)。将 [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) 属性设置为 **true** 或 **false**，即可锁定或解锁单元格。

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
