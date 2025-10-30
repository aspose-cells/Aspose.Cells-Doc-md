---
title: Imposta il carattere predefinito durante la conversione di fogli di calcolo in immagini con Node.js tramite C++
linktitle: Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini
type: docs
weight: 360
url: /it/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Impara come impostare il carattere predefinito durante la conversione di fogli di calcolo in immagini utilizzando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Si prega di utilizzare la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) per impostare il carattere predefinito durante la rappresentazione dei fogli di calcolo in immagini. Questa proprietà avrà effetto solo quando il carattere predefinito del foglio di lavoro non potrà rappresentare i tuoi caratteri. Il carattere predefinito specificato con la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) viene utilizzato per tutte quelle celle che hanno caratteri non validi o inesistenti.

{{% /alert %}}

## Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini

Il seguente esempio crea un file di lavoro, aggiunge del testo nella cella A4 del primo foglio di lavoro e imposta il suo carattere su un carattere non valido o inesistente. Poi, prende due immagini del foglio di lavoro. La prima immagine è scattata impostando la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) a *Courier New* e la seconda impostando la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) a *Times New Roman*.

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) su *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) su *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Codice di esempio

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
