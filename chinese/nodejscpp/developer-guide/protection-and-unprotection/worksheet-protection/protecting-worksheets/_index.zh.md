---
title: 用Node.js通过C++保护工作表
linktitle: 保护工作表
type: docs
weight: 10
url: /zh/nodejs-cpp/protecting-worksheets/
description: 学习如何使用Aspose.Cells for Node.js via C++保护Excel中的工作表，包括保护行、列和特定单元格。
---


{{% alert color="primary" %}}

当工作表被保护时，用户可以执行的操作受到限制。例如，不能输入数据、插入或删除行或列等。

{{% /alert %}}

## **保护工作表**

### **介绍**

Microsoft Excel中的常规保护选项包括：

- 内容
- 对象
- 方案

受保护的工作表不会隐藏或保护敏感数据，因此它与文件加密不同。通常，工作表保护适用于展示目的。它防止最终用户修改工作表中的数据、内容和格式。

### **保护工作表**

Aspose.Cells提供一个类[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，可以访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供用于在工作表上应用保护的[**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)方法。[**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)方法接受以下参数：

- 保护类型，应用于工作表的保护类型。保护类型是使用[**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype)枚举来应用的。
- 新密码，用于保护工作表的新密码。
- 旧密码，如果工作表已经受到密码保护，则传入旧密码。如果工作表尚未受到保护，则传递 null。

[**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype)枚举包含以下预定义的保护类型：

|**保护类型**|**描述**|
| :- | :- |
|All| 用户无法修改工作表中的任何内容
|Contents| 用户无法在工作表中输入数据
|Objects| 用户无法修改绘图对象
|Scenarios| 用户无法修改已保存的情景
|Structure| 用户无法修改结构
|Windows| 保护应用于窗口
|None| 不应用任何保护

下例显示如何使用密码保护工作表。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

使用上述代码保护工作表后，打开工作表即可检查工作表的保护。一旦打开文件并尝试向工作表添加一些数据，您将会看到以下对话框：

|**警告对话框，提示用户无法修改工作表**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

要在工作表上操作，请选择 **保护**，然后在 **工具** 菜单项中选择 **取消保护工作表**。

选择取消保护工作表菜单项后，将会打开一个对话框，提示您输入密码，以便您可以在工作表上进行操作，如下所示：

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **使用Microsoft Excel保护工作表的部分单元格**

某些情况下你可能只需要锁定工作表中的部分单元格。如果你想锁定工作表中的特定单元格，你必须解锁工作表中的所有其他单元格。工作表中的所有单元格默认都已初始化为锁定状态；你可以通过在MS Excel中打开任何Excel文件，点击“格式|单元格...”弹出“单元格格式”对话框，再点击“保护”标签，看到被选中的“锁定”复选框（默认已勾选）来确认这一点。

以下内容描述了如何使用MS Excel锁定部分单元格。此方法适用于Microsoft Office Excel 97、2000、2002、2003及更高版本。

1. 点击**全选**按钮（位于行号1上方和列号A左侧的灰色矩形）来选择整个工作表。
2. 在“格式”菜单中点击“单元格”，切换到“保护”标签，然后取消选中“锁定”复选框。
   这样就解锁了工作表上的所有单元格。
   如果**单元格**命令不可用，工作表的部分可能已被锁定。在**工具**菜单上，指向**保护**，然后点击**取消保护工作表**。
3. 仅选择你想锁定的单元格，重复第2步，但这次勾选“锁定”。
4. 在“工具”菜单中，指向“保护”，点击“保护工作表”，然后点击“确定”。
5. 在“保护工作表”对话框中，你可以设置密码，并选择用户可更改的元素。

### **使用Aspose.Cells保护工作表中的部分单元格**

在此方法中，我们仅使用Aspose.Cells API完成任务。

示例：以下示例演示如何保护工作表中的部分单元格。它先解锁所有单元格，然后锁定3个单元格（A1、B1、C1），最后保护工作表。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象包含一个布尔属性[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)，你可以将[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)属性设置为true或false，并使用*Column/Row.applyStyle()*方法锁定或解锁行/列，使用你希望的属性。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **在工作表中保护一行**

Aspose.Cells允许你轻松锁定工作表中的任一行。在这里，我们可以使用[**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row)类的[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)方法，将[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)应用于工作表中的特定行。此方法接受两个参数：一个[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象和一个[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)对象，后者包含所有与应用格式相关的成员。

以下示例演示如何保护工作表中的某一行。它先解锁所有单元格，然后锁定第一行，最后保护工作表。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象包含一个布尔属性[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)，你可以将[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)设为true或false，以锁定或解锁该行/列，使用 [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)对象。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **在工作表中保护一列**

Aspose.Cells允许你轻松锁定工作表中的某一列。这里，我们可以使用[**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column)类的[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-)方法，将[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)应用于工作表中的特定列。此方法接受两个参数：一个[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象和一个[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)对象，后者包含所有相关格式成员。

以下示例显示如何保护工作表中的某一列。它先解锁所有单元格，然后锁定第一列，最后保护工作表。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象包含一个布尔属性[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)，你可以将[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)设为true或false，以锁定或解锁该列，使用[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)对象。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **允许用户编辑范围**

下面的示例展示了如何允许用户在受保护的工作表中编辑范围。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
