---  
title: 通过Node.js和C++保护和取消保护工作表  
linktitle: 保护和取消保护工作表  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/protect-and-unprotect-worksheets/  
description: 使用Aspose.Cells for Node.js via C++保护和取消保护Excel文件的工作表。  
---  

{{% alert color="primary" %}}  
为防止其他用户意外或故意更改、移动或删除工作表中的数据，您可以锁定 Excel 工作表上的单元格，然后使用密码保护工作表。  
{{% /alert %}}  

## **在 MS Excel 中保护和取消保护工作表**  

**![保护和取消保护工作表](protect-and-unprotect-worksheet.png)**  

1. 点击 **审阅 > 保护工作表**。  
1. 在 **密码框** 中输入密码。  
1. 选择 **允许** 选项。  
1. 选择 **确定**，重新输入密码以确认，然后再次选择 **确定**。  

## **使用Aspose.Cells for Node.js via C++保护工作表**  
只需要以下简单代码行来实现保护 Excel 文件的工作簿结构。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **使用Aspose.Cells for Node.js via C++取消保护工作表**  
使用Aspose.Cells API轻松取消保护工作表。如果工作表被密码保护，则需要提供正确的密码。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **高级主题**  
- [自 Excel XP 以来的高级保护设置](/cells/zh/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [检测工作表是否受密码保护](/cells/zh/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [保护工作表](/cells/zh/nodejs-cpp/protecting-worksheets/)  
- [取消保护工作表](/cells/zh/nodejs-cpp/unprotect-a-worksheet/)  
- [验证用于保护工作表的密码](/cells/zh/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

