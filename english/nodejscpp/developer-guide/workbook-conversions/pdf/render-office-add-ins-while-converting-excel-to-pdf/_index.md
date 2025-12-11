---
title: Render Office Add-Ins while converting Excel to PDF with Node.js via C++
linktitle: Render Office Add-Ins while converting Excel to PDF
type: docs
weight: 100
url: /nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Earlier, Aspose.Cells could not render Office Add-Ins when an Excel file is saved to PDF format. Now Aspose.Cells renders it fine. You do not need to use any special method or property to render the Office Add-Ins in the output PDF. Just save your Excel file to PDF format, and it will render the Office Add-Ins.

## **Render Office Add-Ins while converting Excel to PDF**

The following sample code saves the [sample Excel file](60489769.xlsx) which contains the Office Add-Ins. Please see the [output PDF generated with the previous version, i.e., 17.11](60489770.pdf) and the [output PDF generated with the newer version, i.e., 17.12 and onward](60489771.pdf). The previous version output PDF is blank, but the newer version output PDF shows the Office Add-In.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to PDF format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
