---
title: Set Column Width to Scalable Unit like em or percent with Node.js via C++
linktitle: Set Column Width to Scalable Unit like em or percent
type: docs
weight: 130
url: /nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Learn how to set column width to scalable units like em or percent in Aspose.Cells for Node.js via C++. Improve the presentation of generated HTML tables.
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt," which works in many cases. However, there can be a case where this fixed size may not be required. For example, if a container panel width is 600px, where this HTML page is being displayed, you may get a horizontal scrollbar if the generated table width is bigger. It was required that this fixed size shall be changed into a scalable unit like em or percent to get a better presentation. Following sample code can be used where [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}