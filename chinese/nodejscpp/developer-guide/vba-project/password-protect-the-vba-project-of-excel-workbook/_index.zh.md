---  
title: 通过Node.js和C++为Excel工作簿的VBA项目设置密码保护  
linktitle: 密码保护 Excel 工作簿的 VBA 项目  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: 学习如何使用Aspose.Cells for Node.js via C++为Excel工作簿的VBA项目加密密码。  
---  

## **在Node.js中为Excel工作簿的VBA项目设置密码保护**  

你可以使用[**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-)方法用Aspose.Cells为工作簿的VBA（Visual Basic for Applications）项目设置密码保护。  

## **示例代码**  

以下示例代码加载[示例Excel文件](43352067.xlsm)，访问其VBA项目并设置密码保护，最后将其保存为[输出Excel文件](43352068.xlsm)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
