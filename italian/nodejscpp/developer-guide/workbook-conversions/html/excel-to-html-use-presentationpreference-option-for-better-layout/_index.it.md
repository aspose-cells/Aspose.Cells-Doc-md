---
title: Excel in HTML  Usa l opzione PresentationPreference per una migliore disposizione con Node.js tramite C++
linktitle: Excel to HTML  Utilizzare l Opzione PresentationPreference per una Migliore Layout
type: docs
weight: 220
url: /it/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce una utile proprietà HtmlSaveOptions.presentationPreference per gli sviluppatori che necessitano di un layout migliore quando salvano un file Microsoft Excel in formato HTML o MHT. Il valore predefinito di questa proprietà è false. Si raccomanda di impostarla su true per ottenere una presentazione più accattivante dei report Excel.

{{% /alert %}} 

Vedi il codice di esempio di seguito che dimostra come rendere un file HTML da un report Excel con preferenza di presentazione attivata.



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
