---
title: Copia le impostazioni di configurazione pagina dal foglio di lavoro di origine a quello di destinazione con Node.js tramite C++
linktitle: Copia le impostazioni di configurazione pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione
type: docs
weight: 80
url: /it/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Questo articolo spiega come usare l API Node.js o il codice di esempio della libreria C++ per copiare le impostazioni di configurazione pagina da un foglio di lavoro sorgente a uno di destinazione programmaticamente.
keywords: Copia le impostazioni di configurazione pagina con Node.js tramite C++, copia le impostazioni di configurazione pagina nel foglio di lavoro di destinazione con Node.js tramite C++
---

## **Possibili Scenari di Utilizzo**

Quando aggiungi un nuovo foglio a una cartella di lavoro, contiene le impostazioni di *Page Setup* predefinite. Potresti aver bisogno di trasferire le impostazioni ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) da un foglio di lavoro a un altro. Questo documento spiega come copiare le impostazioni di configurazione pagina da un foglio di lavoro all'altro usando le API Aspose.Cells for Node.js via C++.

## **Copia le impostazioni del layout pagina dal foglio di origine al foglio di destinazione**

Il seguente codice di esempio illustra come copiare le *impostazioni di configurazione pagina* da un foglio all'altro utilizzando il metodo [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-). Si prega di vedere il seguente codice di esempio e il suo output sulla console per un riferimento.

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **Output della console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
