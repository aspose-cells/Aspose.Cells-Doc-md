---
title: Excel till HTML  Använd PresentationPreference alternativ för bättre layout med Node.js via C++
linktitle: Excel till HTML  Använd PresentationPreference alternativet för bättre layout
type: docs
weight: 220
url: /sv/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells erbjuder en användbar HtmlSaveOptions.presentationPreference-egenskap för utvecklare som behöver bättre layout vid sparande av en Microsoft Excel-fil till HTML eller MHT-format. Standardvärdet för egenskapen är false. Vi rekommenderar att ställa in denna egenskap på true för att få en mer attraktiv presentation av Excel-rapporter.

{{% /alert %}} 

Se nedan kodexempel som demonstrerar hur man renderar en HTML-fil från en Excel-rapport med presentationsinställning aktiverad.



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
