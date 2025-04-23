---  
title: Rimuovi stili inutilizzati all’interno del workbook con Node.js tramite C++  
linktitle: Rimuovere gli Stili Non Utilizzati all interno del Workbook  
type: docs  
weight: 340  
url: /it/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Impara come rimuovere stili non utilizzati da un workbook usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
 Gli stili inutilizzati nei file Excel non solo occupano spazio ma causano anche problemi di prestazioni durante la conversione in formati diversi come PDF, HTML, ecc. Aspose.Cells fornisce il funzionalità [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) per rimuovere tutti gli stili inutilizzati all’interno del libro di lavoro.  
{{% /alert %}}  

 Il seguente codice spiega l'uso di {0}. Il codice carica il {1} file Excel modello che puoi scaricare dal link fornito. Contiene uno stile inutilizzato chiamato **AsposeStyle**; questo stile e tutti gli altri stili inutilizzati verranno rimossi dopo l'esecuzione del codice.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

