---  
title: 使用内置文档属性指定Excel文件的版本号（Node.js via C++）  
linktitle: 使用内置文档属性指定Excel文件的文档版本  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: 学习如何使用内置文档属性以编程方式指定Excel文件的版本号（Node.js via C++）。  
---  

## **可能的使用场景**  

你可以右键点击文件，选择属性 > 详细信息，然后编辑“版本号”字段，来更改Excel文件的“版本号”。请使用[**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--)属性以程序方式更改它，使用Aspose.Cells APIs。  

## **使用内置文档属性指定Excel文件的文档版本**  

下面的示例代码创建一个工作簿并更改其内置文档属性，包括标题、作者和版本号。请查看由此代码生成的[输出Excel文件](64716811.xlsx)，以及显示由[**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--)属性修改的版本号的截图。  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "outputSpecifyDocumentVersionOfExcelFile.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access built-in document property collection
const bdpc = wb.getBuiltInDocumentProperties();

// Set the title
bdpc.setTitle("Aspose File Format APIs");

// Set the author
bdpc.setAuthor("Aspose APIs Developers");

// Set the document version
bdpc.setDocumentVersion("Aspose.Cells Version - 18.3");

// Save the workbook in xlsx format
wb.save(filePath, AsposeCells.SaveFormat.Xlsx);
```  

