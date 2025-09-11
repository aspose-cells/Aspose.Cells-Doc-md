---
title: Disable Exporting Frame Scripts and Document Properties with Node.js via C++
linktitle: Disable Exporting Frame Scripts and Document Properties
type: docs
weight: 310
url: /nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Learn how to disable exporting frame scripts and document properties when converting a workbook to HTML using Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells exports frame scripts and document properties while converting a workbook into HTML. The 8.6.0 version of Aspose.Cells for Node.js via C++ introduces an option which allows you to optionally disable exporting frame scripts and document properties. Please use the `HtmlSaveOptions.exportFrameScriptsAndProperties` property to disable the export.

{{% /alert %}}

## **Disable exporting frame scripts and document properties**

The following sample code allows you to disable exporting frame scripts and document properties. Once you convert a workbook into HTML, the output file will not contain any frame scripts and document properties.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}