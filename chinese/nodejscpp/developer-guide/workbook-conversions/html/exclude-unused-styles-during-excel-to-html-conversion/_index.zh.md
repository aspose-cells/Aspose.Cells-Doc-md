---  
title: 使用Node.js通过C++在Excel转换为HTML时排除未使用的样式  
linktitle: 在Excel转换为HTML时排除未使用的样式  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: 了解如何在使用Aspose.Cells for Node.js via C++转换Excel为HTML时排除未使用的样式。  
---  

## **可能的使用场景**  

 Microsoft Excel文件可能包含许多未使用的样式。当将Excel文件导出为HTML格式时，这些未使用的样式也会被导出。这可能会增加HTML的大小。您可以在将Excel文件转换为HTML的过程中排除未使用的样式，方法是设置[**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--)属性。当将其设置为**true**时，所有未使用的样式将从输出的HTML中排除。以下截图显示了输出HTML中的一个未使用样式的示例。  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **在将 Excel 转换为 HTML 时排除未使用的样式**  

 以下示例代码创建了一个工作簿，并且还创建了一个未使用的命名样式。由于将[**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--)设置为**true**，此未使用的命名样式不会导出到[输出HTML](61767778.zip)。但如果将其设置为**false**，则此未使用的样式将存在于输出的HTML中，你可以在HTML标记中看到，如上方截图所示。  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

