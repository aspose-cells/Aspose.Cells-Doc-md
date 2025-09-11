---
title: Export Comments while Saving Excel file to HTML with Node.js via C++
linktitle: Export Comments while Saving Excel file to HTML
type: docs
weight: 40
url: /nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Possible Usage Scenarios**

When you save your Excel file into HTML, comments are not exported. However, Aspose.Cells for Node.js via C++ provides this feature using the [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/) property. If you set it **true**, then HTML will also display comments present in your Excel file.

## **Export Comments while Saving Excel file to HTML**

The following sample code explains the usage of [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/) property. The screenshot shows the effect of the code on the HTML when it is set to **true**. Please download the [sample Excel file](50528260.xlsx) and the [generated HTML](5052826.txt) for a reference.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}