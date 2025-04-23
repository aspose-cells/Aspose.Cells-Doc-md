---  
title: 输出HTML时单独导出工作表CSS，使用Node.js通过C++  
linktitle: 在输出 HTML 中单独导出工作表 CSS  
type: docs  
weight: 80  
url: /zh/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: 了解如何在将Excel文件转换为HTML时单独导出工作表CSS，使用Aspose.Cells for Node.js via C++。  
---  

## **可能的使用场景**

 Aspose.Cells for Node.js via C++提供了在转换Excel为HTML时单独导出工作表CSS的功能。请使用[**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)属性实现，并在将Excel保存为HTML格式时将其设为**true**。

## **在输出 HTML 中单独导出工作表 CSS**

 以下示例代码创建了一个Excel文件，在单元格**B5**中添加了红色文字，然后使用[**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)属性将其保存为HTML格式。请参考代码生成的[输出HTML](60489766.zip)。里面包含了**stylesheet.css**作为示例代码的输出结果。

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **将单个工作簿表导出到 HTML**

 如果使用Aspose.Cells for Node.js via C++将含多个工作表的工作簿转换为HTML，它会生成一个HTML文件以及包含CSS和多个HTML文件的文件夹。当在浏览器中打开此HTML主文件时，可以看到标签。对于仅有一个工作表的工作簿，亦是如此。以前，不会为单个工作表的工作簿单独创建文件夹，只是生成一个HTML文件。该HTML文件在浏览器中打开时不显示标签。Microsoft Excel会为单个工作表创建一个正确的文件夹和HTML文件，因此使用Aspose.Cells API实现了相同的行为。以下链接提供示例文件，用于下面的示例代码：

[sampleSingleSheet.xlsx](79527937.xlsx)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

