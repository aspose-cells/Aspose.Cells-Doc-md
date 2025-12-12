---  
title: Protecting Worksheets with Node.js via C++  
linktitle: Protecting Worksheets  
type: docs  
weight: 10  
url: /nodejs-cpp/protecting-worksheets/  
description: Learn how to protect worksheets in Excel using Aspose.Cells for Node.js via C++, including protecting rows, columns, and specific cells.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  
  
{{% alert color="primary" %}}  
  
When a worksheet is protected, the actions a user can take are restricted. For example, they cannot input data, insert, or delete rows or columns, etc.  
  
{{% /alert %}}  
  
## **Protect Worksheets**  
  
### **Introduction**  
  
The general protection options in Microsoft Excel are:  
  
- Contents  
- Objects  
- Scenarios  
  
Protected worksheets don't hide or protect sensitive data, so they're different from file encryption. Generally, worksheet protection is suitable for presentation purposes. It prevents the end user from modifying data, content, and formatting in the worksheet.  
  
### **Protect a Worksheet**  
  
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a **getWorksheets()** collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class.  
  
The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides the **protect(ProtectionType)** method that is used to apply protection to the worksheet. The **protect(ProtectionType)** method accepts the following parameters:  
  
- **Protection Type** – the type of protection to apply to the worksheet. The protection type is applied with the help of the **ProtectionType** enumeration.  
- **New Password** – the new password used to protect the worksheet.  
- **Old Password** – the old password, if the worksheet is already password‑protected. If the worksheet is not already protected, then just pass **null**.  
  
The **ProtectionType** enumeration contains the following predefined protection types:  
  
| **Protection Types** | **Description** |  
| :- | :- |  
| All | The user cannot modify anything on this worksheet |  
| Contents | The user cannot enter data in this worksheet |  
| Objects | The user cannot modify drawing objects |  
| Scenarios | The user cannot modify saved scenarios |  
| Structure | The user cannot modify the structure |  
| Windows | Protection is applied to windows |  
| None | No protection is applied |  
  
The example below shows how to protect a worksheet with a password.  
  
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
  
After using the above code to protect the worksheet, you can verify the protection by opening the file. When you try to add data to the worksheet, you will see the following dialog:  
  
| **A dialog warning that a user can't modify the worksheet** |  
| :- |  
| ![todo:image_alt_text](protecting-worksheets_1.png) |  
  
To work on the worksheet, unprotect it by selecting **Protection**, then **Unprotect Sheet** from the **Tools** menu.  
  
After you select the **Unprotect Sheet** menu item, a dialog opens prompting you to enter the password so that you may work on the worksheet, as shown below:  
  
| ![todo:image_alt_text](protecting-worksheets_2.png) |  
  
### **Protect a Few Cells in the Worksheet Using Microsoft Excel**  
  
There are scenarios where you need to lock only a few cells in the worksheet. To lock specific cells, you must unlock all the other cells first. All cells are locked by default; you can verify this by opening any Excel file, selecting **Format | Cells…**, and checking the **Protection** tab where the **Locked** checkbox is checked.  
  
The following steps describe how to lock a few cells using MS Excel. This method applies to Microsoft Office Excel 97, 2000, 2002, 2003, and later versions.  
  
1. Select the entire worksheet by clicking the **Select All** button (the gray rectangle directly above row 1 and to the left of column A).  
2. Click **Cells** on the **Format** menu, choose the **Protection** tab, and then clear the **Locked** checkbox. This unlocks all the cells on the worksheet. If the **Cells** command is not available, parts of the worksheet may already be locked. On the **Tools** menu, point to **Protection**, and then click **Unprotect Sheet**.  
3. Select the cells you want to lock and repeat step 2, but this time check the **Locked** checkbox.  
4. On the **Tools** menu, point to **Protection**, click **Protect Sheet**, and then click **OK**.  
5. In the **Protect Sheet** dialog box, you can specify a password and select the elements that you want users to be able to change.  
  
### **Protect a Few Cells in the Worksheet Using Aspose.Cells**  
  
In this method, we use only the Aspose.Cells API to perform the task.  
  
**Example:** The following example demonstrates how to protect a few cells in the worksheet. It first unlocks all the cells, then locks three cells (A1, B1, C1), and finally protects the worksheet. The **Style** object contains a boolean property **isLocked()**. You can set **isLocked()** to **true** or **false** and apply the *Column/Row.applyStyle()* method to lock or unlock the row/column with the desired attributes.  
  
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
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
    style = sheet.getCells().getColumns().get(i).getStyle();
    style.setIsLocked(false);
    styleflag.setLocked(true);
    sheet.getCells().getColumns().get(i).applyStyle(style, styleflag);
}

// Lock the three cells, i.e., A1, B1, and C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);

style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);

style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```  
  
### **Protect a Row in the Worksheet**  
  
Aspose.Cells allows you to easily lock any row in the worksheet. Use the **applyStyle(Style, StyleFlag)** method of the **Aspose.Cells.Row** class to apply a **Style** to a particular row. This method takes two arguments: a **Style** object and a **StyleFlag** object that contains the members related to applied formatting.  
  
The following example shows how to protect a row in the worksheet. It first unlocks all the cells, then locks the first row, and finally protects the worksheet.  
  
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

// Save the Excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```  
  
### **Protect a Column in the Worksheet**  
  
Aspose.Cells also lets you lock any column in the worksheet. Use the **applyStyle(Style, StyleFlag)** method of the **Aspose.Cells.Column** class to apply a **Style** to a particular column.  
  
The following example shows how to protect a column in the worksheet. It first unlocks all the cells, then locks the first column, and finally protects the worksheet.  
  
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

// Save the Excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```  
  
### **Allow Users to Edit Ranges**  
  
The following example shows how to allow users to edit a range in a protected worksheet.  
  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges collection
const allowRanges = sheet.getAllowEditRanges();

// Define a protected range
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
  
{{< app/cells/assistant language="nodejs-cpp" >}}
