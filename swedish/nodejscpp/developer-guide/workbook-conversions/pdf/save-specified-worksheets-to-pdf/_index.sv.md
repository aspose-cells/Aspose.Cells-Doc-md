---
title: Spara angivna kalkylblad till PDF med Node.js via C++
linktitle: Spara angivna arkpapper till PDF
type: docs
weight: 140
url: /sv/nodejs-cpp/save-specified-worksheets-to-pdf/
description: Lär dig hur du sparar angivna kalkylblad till PDF med Aspose.Cells for Node.js via C++. 
---


Som standard sparar Aspose.Cells alla **synliga** kalkylblad i ett arbetsbok till en PDF-fil. Med [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) -alternativet kan du spara angivna kalkylblad till en PDF-fil. Till exempel kan du spara det aktiva kalkylbladet till PDF, spara alla kalkylblad (både synliga och dolda) till PDF, spara anpassade flera kalkylblad till PDF.

## **Spara aktivt arkpapp till PDF**

Om du bara vill exportera det aktiva bladet till PDF kan du uppnå detta genom att ange [**SheetSet.getActive()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getActive--) till [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)-alternativet.

Arbetsbladet `Sheet2` är det aktiva bladet i källfilen [sheetset-example.xlsx](sheetset-example.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set active sheet to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getActive());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **Spara alla arbetsblad till PDF**

[**SheetSet.getVisible()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getVisible--) indikerar synliga blad i en arbetsbok, och [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) indikerar alla blad inklusive både synliga och dolda/osynliga blad i en arbetsbok. Om du vill exportera alla blad till PDF kan du bara skicka [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) till [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) alternativet.

Källfilen [sheetset-example.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Ark3`.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set all sheets to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getAll());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **Spara angivna arbetsblad som PDF**

Om du vill exportera önskat/anpassat flera blad till PDF kan du göra detta genom att ange flera bladindextal till [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)-alternativet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set custom multiple sheets(Sheet1, Sheet3) to output
const sheetSet = new AsposeCells.SheetSet([0, 2]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **Omordna arbetsblad till PDF**

Om du vill omordna blad (t.ex. i omvänd ordning) till PDF utan att ändra källfilen kan du uppnå detta genom att skicka omordnade bladindextal till [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) alternativet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");
// Open the template excel file
const wb = new AsposeCells.Workbook(filePath);

// Reorder sheets(Sheet1, Sheet2, Sheet3, Sheet4) to sheets(Sheet4, Sheet3, Sheet2, Sheet1)
const sheetSet = new AsposeCells.SheetSet([3, 2, 1, 0]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
