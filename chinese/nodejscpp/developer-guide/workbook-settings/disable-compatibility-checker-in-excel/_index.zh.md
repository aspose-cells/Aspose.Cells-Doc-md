---  
title: 使用C++通过Node.js禁用Excel的兼容性检查器  
linktitle: 在Excel中禁用兼容性检查程序  
type: docs  
weight: 170  
url: /zh/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: 学习如何通过Aspose.Cells for Node.js via C++ API禁用兼容性检查器。  
keywords: 在Node.js中禁用兼容性检查器，使用C++通过Node.js禁用Excel兼容性检查器，禁用工作簿中的兼容性检查器。  
---  

## 在Node.js中禁用Excel工作表的兼容性检查器  

{{% alert color="primary" %}}  
Microsoft Excel的兼容性检查器在将文件保存为较早文件格式时可能会出现功能问题或保真度丢失。 兼容性检查器是Microsoft Office Excel 2007和Microsoft Excel 2010的功能。  

当您从Excel 2007或Excel 2010将工作簿保存在较早的版本中（Excel 97至Excel 2003），兼容性检查程序将扫描工作簿，以查看它是否包含较早版本不支持的功能。为了帮助您决定如何处理兼容性问题，兼容性检查程序显示带有选项的对话框。它还可用于创建有关工作簿中任何问题的报告，或者禁用该功能。  

有时，你需要为特定的电子表格禁用兼容性检查器。通过Aspose.Cells的API，你可以以编程方式实现此功能，避免用户在手动在Microsoft Excel中重新保存文件时弹出兼容性检查器对话框带来的困扰或困惑。  
{{% /alert %}}  

## **如何使用Microsoft Excel禁用兼容性检查器**  

要在Microsoft Excel中禁用兼容性检查程序（例如Microsoft Excel 2007/2010）：  

- （Excel 2007）在办公按钮上，单击**准备**，然后单击**运行兼容性检查**，然后清除**保存此工作簿时检查兼容性**选项。  
- （Excel 2010）单击“文件”选项卡，然后单击**信息**，再单击“检查问题”，再单击“检查兼容性”，最后清除“保存此工作簿时检查兼容性”选项。  

## **如何使用Aspose.Cells API禁用兼容性检查器**  

将[**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--)属性设置为**false**以禁用Microsoft Excel的兼容性检查器。  

### **代码示例**  

以下示例演示如何使用Aspose.Cells for Node.js via C++禁用兼容性检查器。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

