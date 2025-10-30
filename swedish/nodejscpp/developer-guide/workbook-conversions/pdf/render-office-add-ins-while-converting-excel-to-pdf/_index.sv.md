---
title: Rendera Office tillägg vid konvertering av Excel till PDF med Node.js via C++
linktitle: Rendera Office tillägg vid konvertering av Excel till PDF
type: docs
weight: 100
url: /sv/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Möjliga användningsscenario**

Tidigare kunde Aspose.Cells inte rendera Office-tillägg när en Excel-fil sparas till PDF-format. Nu renderar Aspose.Cells det utan problem. Du behöver inte använda någon speciell metod eller egenskap för att rendera Office-tillägg i output-PDF:en. Spara helt enkelt din Excel-fil som PDF, så renderas Office-tillägget.

## **Rendera Office-tillägg vid konvertering av Excel till PDF**

Följande exempel kod sparar [exempel Excel-fil](60489769.xlsx) som innehåller Office-tillägg. Se [utdata PDF genererad med den tidigare versionen, dvs. 17.11](60489770.pdf) och den [nyare versionen, dvs. 17.12 och senare](60489771.pdf). Den föregående versionens utdata PDF är tom, men den nyare versionen visar Office-tillägget.

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
