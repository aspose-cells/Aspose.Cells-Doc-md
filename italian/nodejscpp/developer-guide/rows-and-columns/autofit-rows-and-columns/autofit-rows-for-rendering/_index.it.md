---  
title: AutoAdatta righe per rendering con Node.js tramite C++  
linktitle: AutoAdattamento righe per il rendering  
type: docs  
weight: 130  
url: /it/nodejs-cpp/autofit-rows-for-rendering/  
description: Impara come autofittare le righe per il rendering in Excel usando Aspose.Cells for Node.js via C++. Impedisci il taglio del testo nei file PDF salvati.  
---  

Generalmente, quando vuoi visualizzare tutto il testo in una cella, puoi autofittare la riga in visualizzazione normale con zoom al 100% in Microsoft Excel. Questo permette al testo di essere completamente visibile in visualizzazione normale, e anche quando stampi o salvi il file come PDF, il testo sarà visualizzato correttamente.

Tuttavia, in alcuni casi, l'autofitting della riga funziona bene in visualizzazione normale, ma quando passi in modalità anteprima di stampa o salvi il file come PDF, il testo viene tagliato. Verifica il file di origine [Book1.xlsx](Book1.xlsx) e gli screenshot.

![il testo viene tagliato nella visualizzazione di stampa](text_clipped_in_printview.png)

Se vuoi prevenire il taglio del testo nel file PDF salvato, puoi autofittare la riga con l'opzione [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--)

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

Ora, il testo non è tagliato nel file PDF di output.

![il testo non è tagliato nel pdf salvato](text_not_clipped_in_saved_pdf.png)  
