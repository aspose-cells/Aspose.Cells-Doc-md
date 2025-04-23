---
title: Ausgewählte Arbeitsblätter mit Node.js über C++ in PDF speichern
linktitle: Gewählte Arbeitsblätter als PDF speichern
type: docs
weight: 140
url: /de/nodejs-cpp/save-specified-worksheets-to-pdf/
description: Erfahren Sie, wie Sie ausgewählte Arbeitsblätter mit Aspose.Cells for Node.js via C++ in PDF speichern. 
---


Standardmäßig speichert Aspose.Cells alle **sichtbaren** Arbeitsblätter in einer Arbeitsmappe als PDF. Mit der [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)-Option können Sie ausgewählte Arbeitsblätter in einer PDF speichern, z.B. das aktive Arbeitsblatt, alle sichtbaren (und ausgeblendeten) Arbeitsblätter oder benutzerdefinierte mehrere Arbeitsblätter.

## **Aktives Arbeitsblatt als PDF speichern**

Wenn Sie nur das aktive Blatt in PDF exportieren möchten, können Sie dies erreichen, indem Sie [**SheetSet.getActive()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getActive--) an die [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)-Option übergeben.

Das Blatt `Sheet2` ist das aktive Blatt der Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx).

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

## **Alle Arbeitsblätter in PDF speichern**

[**SheetSet.getVisible()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getVisible--) zeigt sichtbare Blätter in einer Arbeitsmappe an, und [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) zeigt alle Blätter einschließlich sichtbarer und unsichtbarer Blätter an. Wenn Sie alle Blätter als PDF exportieren möchten, können Sie einfach [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) an die [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)-Option übergeben.

Die Quelldatei [sheetset-example.xlsx](sheetset-example.xlsx) enthält alle vier Blätter mit dem versteckten Blatt `Blatt3`.

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

## **Bestimmte Arbeitsblätter als PDF speichern**

Wenn Sie gewünschte/benutzerdefinierte mehrere Blätter in PDF exportieren möchten, können Sie dies erreichen, indem Sie mehrere Blattsindizes an [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) übergeben.

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

## **Arbeitsblätter nach PDF neu anordnen**

Wenn Sie Blätter in eine andere Reihenfolge bringen möchten (z. B. in umgekehrter Reihenfolge), um sie als PDF zu exportieren, ohne die Quelldatei zu ändern, können Sie dies erreichen, indem Sie die neu angeordneten Blattindizes an die [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)-Option übergeben.

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

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
