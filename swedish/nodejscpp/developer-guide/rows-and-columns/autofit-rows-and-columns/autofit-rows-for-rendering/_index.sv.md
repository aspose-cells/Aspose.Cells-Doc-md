---  
title: Autofit Rader för Renderering med Node.js via C++  
linktitle: Autoanpassa rader för rendering  
type: docs  
weight: 130  
url: /sv/nodejs-cpp/autofit-rows-for-rendering/  
description: Lär dig att autofitta rader för renderering i Excel med Aspose.Cells for Node.js via C++. Förhindra att text klipps i sparade PDF filer.  
---  

Generellt, när du vill visa all text i en cell kan du autofitta raden i Normalvy med 100% zoom i Microsoft Excel. Detta gör att texten är fullt synlig i Normalvy, och även när du skriver ut eller sparar filen som PDF, visas texten korrekt.

Men, i vissa fall fungerar autofittning av raden bra i Normalvy, men när du växlar till utskriftsvy eller sparar filen som PDF, klipps texten. Kontrollera källfilen [Book1.xlsx](Book1.xlsx) och skärmbilder.

![text klipps i utskriftsvyn](text_klipps_i_utskriftsvyn.png)

Vill du förhindra att text klipps i den sparade PDF-filen kan du autofitta raden med alternativet [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

Nu är texten inte klippt i den här PDF-filen.

![text klipps inte i sparad pdf](text_klipps_inte_i_sparad_pdf.png)  
