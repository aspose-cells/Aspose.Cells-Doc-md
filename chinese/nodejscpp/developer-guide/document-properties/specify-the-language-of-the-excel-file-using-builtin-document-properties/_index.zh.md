---
title: 使用内置文档属性指定Excel文件的语言（Node.js via C++）
linktitle: 使用内置文档属性指定Excel文件的语言
type: docs
weight: 30
url: /zh/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **可能的使用场景**

你可以右键点击文件，选择属性 > 详细信息，然后编辑语言字段，来更改Excel文件的语言。请使用[**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--)属性以程序方式更改它，使用Aspose.Cells for Node.js via C++ APIs。

## **使用内置文档属性指定Excel文件的语言**

以下示例代码创建一个工作簿并更改其内置文档属性中的语言字段。请查看由此代码生成的[输出Excel文件](64716891.xlsx)，以及显示由[**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--)属性修改的语言字段的截图。

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object.
const wb = new AsposeCells.Workbook();

// Access built-in document property collection.
const bdpc = wb.getBuiltInDocumentProperties();

// Set the language of the Excel file.
bdpc.setLanguage("German, French");

// Save the workbook in xlsx format.
wb.save(path.join(outputDir, "outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
