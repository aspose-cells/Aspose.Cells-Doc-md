---
title: Renderizza il foglio di lavoro su un contesto grafico con Node.js tramite C++
linktitle: Rappresentare il foglio di calcolo nel contesto grafico
type: docs
weight: 300
url: /it/nodejs-cpp/render-worksheet-to-graphic-context/
description: Impara come rendere un foglio di lavoro in un contesto grafico usando Aspose.Cells for Node.js via C++. Questo include la stampa su file immagine, schermi e stampanti.
---

{{% alert color="primary" %}}

Aspose.Cells ora può rendere i fogli di lavoro in un contesto grafico. Il contesto grafico può essere qualsiasi cosa come un file immagine, schermo o stampante, ecc. Usa uno dei seguenti due metodi per rendere un foglio di lavoro in un contesto grafico.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Il seguente codice illustra come usare Aspose.Cells per rendere un foglio di lavoro in un contesto grafico. Una volta eseguito, stamperà l'intero foglio di lavoro e riempirà lo spazio vuoto residuo con colore blu nel contesto grafico, salvando l'immagine come file **OutputImage_out_.png**. Puoi usare qualsiasi file Excel di origine per provare questo codice. Si consiglia anche di leggere i commenti all’interno del codice per una migliore comprensione.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
{{< app/cells/assistant language="nodejs-cpp" >}}
