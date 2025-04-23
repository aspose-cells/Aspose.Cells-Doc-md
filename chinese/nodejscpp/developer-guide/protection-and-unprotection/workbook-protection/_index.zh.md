---  
title: 使用Node.js与C++保护和取消保护工作簿结构  
linktitle: 保护和取消保护工作簿结构  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: 使用Node.js通过C++保护和取消保护Excel文件的工作簿结构。  
---  


{{% alert color="primary" %}}  
为防止其他用户查看隐藏工作表、添加、移动、删除或隐藏工作表，并重命名工作表，您可以使用密码保护 Excel 工作簿的结构。  
{{% /alert %}}  


## **在 MS Excel 中保护和取消保护工作簿结构**  

**![保护和取消保护工作簿结构](protect-and-unprotect-workbook-structure.png)**  

1. 点击 **审阅 > 保护工作簿**。  
1. 在 **密码框** 中输入密码。  
1. 选择 **确定**，重新输入密码以确认，然后再次选择 **确定**。  


## ** 使用Aspose.Cells for Node.js via C++保护工作簿结构**  
只需要以下简单代码行来实现保护 Excel 文件的工作簿结构。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **使用Aspose.Cells for Node.js via C++取消保护工作簿结构**  
使用 Aspose.Cells API 轻松取消工作簿结构保护。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
注意：需要正确的密码。  
{{% /alert %}}  

