---
title: Excel to HTML - Use PresentationPreference Option for Better Layout with Node.js via C++
linktitle: Excel to HTML - Use PresentationPreference Option for Better Layout
type: docs
weight: 220
url: /nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells provides a useful HtmlSaveOptions.presentationPreference property for developers who need to render better layout when saving a Microsoft Excel file to HTML or MHT format. The default value of the property is false. We recommend setting this property to true to get a more attractive presentation of Excel reports.

{{% /alert %}} 

Please see the sample code below that demonstrates how to render an HTML file from an Excel report with presentation preference on.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}