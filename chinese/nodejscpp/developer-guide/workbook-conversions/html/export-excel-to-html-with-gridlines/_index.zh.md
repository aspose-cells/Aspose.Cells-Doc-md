---  
title: 使用Node.js导出带有网格线的Excel到HTML  
linktitle: 将Excel导出为带有网格线的HTML  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: 了解如何使用Aspose.Cells for Node.js via C++将带有网格线的Excel文件导出为HTML格式。  
---  

{{% alert color="primary" %}}  

 如果希望导出带有网格线的Excel文件为HTML，请使用[HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--)属性并设置为**true**。

{{% /alert %}}  
## **将Excel导出为带有网格线的HTML**  
 以下示例代码创建了一个工作簿，填充了一些值，然后在设置[HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--)为**true**后将其保存为HTML格式。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create your workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Fill worksheet with some integer values
for (let r = 0; r < 10; r++) {
for (let c = 0; c < 10; c++) {
ws.getCells().get(r, c).putValue(r * 1);
}
}

// Save your workbook in HTML format and export gridlines
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportGridLines(true);
wb.save(path.join(dataDir, "ExportToHTMLWithGridLines_out.html"), opts);
```  

