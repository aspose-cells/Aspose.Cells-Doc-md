---
title: Imposta la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions con priorità tramite Node.js tramite C++
linktitle: Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per avere la priorità
type: docs
weight: 30
url: /it/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Scopri come impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions usando Aspose.Cells for Node.js via C++. Assicura una corretta resa del font quando i font mancano.
---

## **Possibili Scenari di Utilizzo**

Mentre si imposta la proprietà **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), potresti aspettarti che il salvataggio in PDF o immagine imposti quel DefaultFont a tutto il testo in un foglio di lavoro che ha un carattere mancante (non installato).

In generale, quando si salva in PDF o immagine, Aspose.Cells for Node.js via C++ proverà prima ad impostare il carattere predefinito del workbook (cioè, `Workbook.DefaultStyle.Font`). Se il carattere predefinito del workbook ancora non può mostrare/rendere correttamente il testo, Aspose.Cells tenterà di rendere il testo con il font menzionato nell'attributo DefaultFont in [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/).

Per far fronte alle tue aspettative, abbiamo una proprietà booleana chiamata "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Puoi impostarla su **false** per disabilitare il tentativo del carattere predefinito del foglio di lavoro o lasciare che l'impostazione **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) abbia la priorità.

## **Impostare la proprietà DefaultFont di PdfSaveOptions/ImageOrPrintOptions**

Il seguente esempio di codice apre un file Excel. La cella A1 (nel primo foglio di lavoro) contiene il testo "Christmas Time Font text". Il nome del font è "Christmas Time Personal Use" che non è installato sulla macchina. Impostiamo l'attributo **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) su "Times New Roman". Impostiamo anche la proprietà booleana **CheckWorkbookDefaultFont** su **"false"** che garantisce che il testo della cella A1 venga reso con il font "Times New Roman" e non utilizzi il font di default del workbook ("Calibri" in questo caso). Il codice rende il primo foglio di lavoro in formati immagine PNG e TIFF. Infine, viene esportato come file PDF.

{{% alert color="primary" %}}

Il valore predefinito dell'attributo **CheckWorkbookDefaultFont** è **true**.

{{% /alert %}}

Questa è la schermata del file di [modello](49446913.xlsx) utilizzato nel codice di esempio.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Questa è l'immagine PNG di output dopo aver impostato la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) su "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Guarda l'immagine [TIFF](48496672.tiff) di output dopo aver impostato la proprietà [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) su "Times New Roman".

Guarda il file [PDF](48496673.pdf) di output dopo aver impostato la proprietà [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) su "Times New Roman".

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
