---  
title: 导出边框样式（Web浏览器不支持的边框样式）使用Node.js通过C++  
linktitle: 在Web浏览器不支持边框样式时导出类似的边框样式  
type: docs  
weight: 70  
url: /zh/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: 了解如何在将Excel文件转换为HTML时导出Web浏览器不支持的边框样式，使用Aspose.Cells for Node.js via C++。  
---  

## **可能的使用场景**  

 Microsoft Excel支持一些虚线边框类型，但Web浏览器不支持。当使用Aspose.Cells for Node.js via C++将此类Excel转换为HTML时，这些边框会被删除。但Aspose.Cells也支持显示此类边框，通过设置[**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)属性，请将其值设为**true**，未支持的边框也会导出到HTML文件中。  

## **在Web浏览器不支持边框样式时导出相似的边框样式**  

 以下示例代码加载包含一些不支持的边框的[示例Excel文件](64716806.xlsx)，如截图所示。截图还展示了[**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)属性在[输出HTML](64716804.zip)中的效果。  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
