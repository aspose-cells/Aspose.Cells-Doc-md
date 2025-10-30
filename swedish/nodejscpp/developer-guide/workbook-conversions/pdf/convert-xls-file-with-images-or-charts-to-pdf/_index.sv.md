---
title: Konvertera XLS fil med bilder eller diagram till PDF med Node.js via C++
linktitle: Konvertera XLS fil med bilder eller diagram till PDF
type: docs
weight: 50
url: /sv/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder konvertering av XLS-filer som innehåller bilder och diagram till PDF-dokument. Aspose.Cells for Node.js via C++ kan fungera självständigt för att konvertera ett kalkylblad till PDF: Aspose.PDF för Node.js via C++ krävs inte för konverteringen. Processen kan göras i minnet eftersom den inte beror på tillfälliga eller mellanliggande XML-filer. Detta innebär att stora Excel-filer, till exempel de som innehåller bilder, diagram och andra teckningsobjekt, kan konverteras snabbt och effektivt.

{{% /alert %}} 
## **Exempelkod**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

Om kalkylbladet innehåller formel är det bäst att anropa [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) precis innan det renderas till PDF. Detta säkerställer att formelberoende värden omräknas och att korrekta värden renderas i PDF:en.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
