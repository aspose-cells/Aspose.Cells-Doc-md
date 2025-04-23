---  
title: 在使用Node.js通过C++写保护工作簿时指定作者  
linktitle: 在写保护工作簿时指定作者  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: 在使用Aspose.Cells for Node.js via C++写保护工作簿时，指定作者姓名。  
---  

## **可能的使用场景**

 您可以在使用Aspose.Cells API写保护工作簿时指定作者姓名。请使用[**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--)属性完成此操作。

## **在保护工作簿时指定作者**

 以下示例代码说明了[**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--)属性的用法。该代码创建一个空白工作簿，用密码进行写保护，指定作者姓名，并保存为[输出Excel文件](67338582.xlsx)。下图展示了示例代码对输出Excel文件的效果，供您参考。

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

