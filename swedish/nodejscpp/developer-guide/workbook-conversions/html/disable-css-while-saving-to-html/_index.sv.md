---
title: Inaktivera CSS vid sparande till HTML med Node.js via C++
linktitle: Inaktivera CSS vid sparning till HTML
type: docs
weight: 320
url: /sv/nodejs-cpp/disable-css-while-saving-to-html/
description: Lär dig hur man inaktiverar CSS när man sparar Excel filer till HTML med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till en enkel HTML-sida kommer CSS-elementen vanligtvis att inbäddas i HTML-filen och befinna sig i `<head>`-sektionen. Om du bifogar denna fil som innehåll/kropp i ett e-postmeddelande, kommer de flesta e-postklienter att ta bort CSS-elementen, vilket resulterar i felaktig rendering. Version 24.12 av Aspose.Cells introducerar ett alternativ som gör det möjligt att inaktivera CSS, vilket gör att stilar kan tillämpas direkt inom HTML-elementen. Om du vill använda HTML som innehåll/kropp i e-postmeddelandet, använd [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--)-egenskapen och ställ in den till **true**.

## **Inaktivera CSS vid sparning till HTML**

Följande exempel visar användningen av [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) egenskapen. 

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
