---  
title: 导出打印区域范围到HTML，使用Node.js通过C++  
linktitle: 将打印区域范围导出为HTML  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/export-print-area-range-to/  
---  

## **可能的使用场景**

 这是一个常见场景，我们只需导出打印区域即所选的单元格范围，而非整张工作表的内容到HTML。此功能已支持PDF渲染，现在也支持HTML。首先，在工作表的页面设置对象中设置打印区域。然后，使用[**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--)标志导出所选范围。

## 示例代码

下面的示例代码加载一个工作簿，然后将打印区域导出到 HTML。用于测试此功能的示例文件可以从以下链接下载：

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
