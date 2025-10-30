---
title: Ställ in kolumnbredd till skalbar enhet som em eller procent med Node.js via C++
linktitle: Ställ in kolumnbredd till skalbar enhet som em eller procent
type: docs
weight: 130
url: /sv/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Lär dig hur man ställer in kolumnbredd till skalbara enheter som em eller procent i Aspose.Cells for Node.js via C++. Förbättra presentationen av genererade HTML tabeller.
---

Att generera en HTML-fil från ett kalkylblad är mycket vanligt. Storleken på kolumnerna är definierad i "pt," vilket fungerar i många fall. Men det kan finnas tillfällen där denna fasta storlek inte är nödvändig. Till exempel, om en behållar-panelbredd är 600px, där den här HTML-sidan visas, kan du få ett horisontellt rullningsfält om den genererade tabellens bredd är större. Det krävdes att denna fasta storlek skulle ändras till en skalbar enhet som em eller procent för att få en bättre presentation. Följande kodexempel kan användas där [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) är inställd på **true** för att skapa skalbar bredd.

Källfilen och utdatafiler kan laddas ned från följande länkar:

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
