---
title: Converti il workbook Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice calc) via Node.js
linktitle: Ods
type: docs
weight: 20
url: /it/nodejs-cpp/convert-excel-to-ods/
description: Come convertire Excel in Ods (OpenOffice / LibreOffice Calc) o convertire Ods (OpenOffice / LibreOffice Calc) in Excel con Aspose.Cells for Node.js via C++.
---

## **Informazioni su OpenDocument**
Il [formato OpenDocument (ODF)](https://it.wikipedia.org/wiki/OpenDocument) è un formato file libero e aperto per documenti elettronici originariamente sviluppato da Sun per la suite Open Office. Il formato file per i documenti Excel è OpenDocument Spreadsheet (ODS). OpenDocument è attualmente uno standard OASIS e ISO.

## **Converti Ods (OpenOffice / LibreOffice calc) in Excel**
Aspose.Cells for Node.js via C++ supporta il caricamento di Ods, Sxc e Fods, supportati da OpenOffice / LibreOffice Calc, e la conversione di [Ods](book1.ods), [Sxc](book1.sxc) e [Fods](book1.fods) in file Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **Converti Excel in Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Node.js via C++ supporta la conversione di file Excel in file Ods, Sxc e Fods. Il seguente esempio di codice mostra come convertire il [modello](book1.xlsx) in file Ods, Sxc e Fods.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Argomenti avanzati**
- [Salva il file ODS nelle specifiche ODF 1.1 e 1.2](/cells/it/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Lavorare con lo sfondo nei file ODS](/cells/it/nodejs-cpp/working-with-background-in-ods-files/)
