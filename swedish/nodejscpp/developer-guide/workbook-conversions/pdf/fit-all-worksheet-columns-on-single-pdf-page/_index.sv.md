---
title: Anpassa alla kalkylblads kolumner till en enda PDF sida med Node.js via C++
linktitle: Anpassa alla kalkylbladskolumner på en enda PDF sida
type: docs
weight: 160
url: /sv/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Ibland vill du generera en PDF-fil där alla kalkylbladets kolumner passar på en sida. Egenskapen [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) tillhandahåller denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar som höjden och bredden på utdata-PDF:en hanteras internt och baseras på data i kalkylbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) säkerställer att alla kolumner i ett kalkylblad renderas till en enda PDF-sida, även om rader kan sträcka sig över flera sidor beroende på data i kalkylbladet.

Exempelkoden nedan visar hur du använder [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--)-egenskapen för att rendera ett stort kalkylblad med 100 kolumner.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den genererade PDF-filen visa innehållet i väldigt liten storlek. Det är fortfarande läsbart när det skalas upp i en visningsapplikation som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
