---
title: Specify how to cross a string in output HTML using HtmlCrossType with Node.js via C++
linktitle: Specify how to cross a string in output HTML using HtmlCrossType
type: docs
weight: 140
url: /nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Learn how to control string overflow in HTML output by specifying HtmlCrossType in Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When a cell contains text or a string that is larger than the width of the cell, the string overflows if the next cell in the adjacent column is empty. When you save your Excel file as HTML, you can control this overflow by specifying the cross type using the [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) enumeration. It has the following values:

- **HtmlCrossType.Default**: Displays like MS Excel; behavior depends on the next cell. If the next cell is empty, the string will cross, otherwise it will be truncated.

- **HtmlCrossType.MSExport**: Displays the string as MS Excel exports HTML.

- **HtmlCrossType.Cross**: Displays an HTML cross string; performance when creating large HTML files will be more than ten times faster than when the value is set to **Default** or **FitToCell**.

- **HtmlCrossType.FitToCell**: Displays only the string within the width of the cell.

## **Specify how to cross a string in output HTML using HtmlCrossType**

The following sample code loads the [sample Excel file](51740732.xlsx) and saves it to HTML format by specifying different [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) values. Please download the [output HTML files](51740734.zip) generated with this code. The sample Excel file contains an image bordered in red, as shown in this screenshot, which demonstrates the effect of the **HtmlCrossType** values on the output HTML.

![Screenshot showing the effect of HtmlCrossType on output HTML](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output HTML
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
