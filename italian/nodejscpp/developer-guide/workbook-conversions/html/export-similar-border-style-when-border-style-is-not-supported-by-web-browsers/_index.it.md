---  
title: Esporta lo stile del bordo simile quando il stile del bordo non è supportato dai browser Web con Node.js tramite C++  
linktitle: Esportare uno stile di bordo simile quando lo stile di bordo non è supportato dai browser web  
type: docs  
weight: 70  
url: /it/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Impara come esportare i bordi che non sono supportati dai browser web durante la conversione di file Excel in HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Microsoft Excel supporta alcuni tipi di bordi tratteggiati che non sono supportati dai browser Web. Quando converti un tale file Excel in HTML usando Aspose.Cells for Node.js via C++, tali bordi vengono rimossi. Tuttavia, Aspose.Cells può anche supportare la visualizzazione di tali bordi con la proprietà [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--). Imposta il suo valore su **true** e i bordi non supportati saranno esportati nel file HTML.  

## **Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web**  

Il seguente esempio di codice carica il [file Excel di esempio](64716806.xlsx) che contiene alcuni bordi non supportati come mostrato nella seguente schermata. La schermata illustra inoltre l'effetto della proprietà [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) all'interno dell'[HTML di output](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

