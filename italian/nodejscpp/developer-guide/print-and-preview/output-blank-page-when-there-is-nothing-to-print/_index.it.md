---
title: Output Pagina Bianca quando non c è nulla da stampare con Node.js tramite C++
linktitle: Genera una pagina vuota quando non c è nulla da stampare
type: docs
weight: 90
url: /it/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Possibili Scenari di Utilizzo**

Se il foglio è vuoto, Aspose.Cells non stamperà nulla quando esporti il foglio di lavoro in un'immagine. Puoi modificare questo comportamento usando la proprietà [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--). Quando la imposti su **true**, stamperà la pagina vuota.

## **Output Pagina Bianca quando non c'è Nulla da Stampare**

Il seguente esempio crea un workbook vuoto che ha un foglio di lavoro vuoto e lo rende in immagine dopo aver impostato la proprietà [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) su **true**. Di conseguenza, genera una pagina vuota come si può vedere nell'immagine sotto.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
