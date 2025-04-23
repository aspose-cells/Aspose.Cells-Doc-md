---
title: Monitora lo stato di conversione da Excel a TIFF con Node.js tramite C++
linktitle: Monitora il progresso della conversione di Excel in TIFF
type: docs
weight: 190
url: /it/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Impara come monitorare il progresso della conversione dei file Excel in TIFF usando Aspose.Cells for Node.js via C++. Migliora l esperienza utente durante il processo di conversione.
---

## **Possibili Scenari di Utilizzo**

 A volte, convertire grandi file Excel può richiedere del tempo. Durante questo, potresti voler mostrare lo stato di avanzamento della conversione del documento invece di una semplice schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells for Node.js via C++ supporta il tracciamento del processo di conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) fornisce i metodi [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) e [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata *TestPageSavingCallback*.

## **Monitora il progresso della conversione di Excel in TIFF**

 Il seguente esempio di codice carica il [file Excel origine](95584311.xlsx) e stampa il suo progresso di conversione nella console usando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). Il file di output generato è allegato per tua referenza.

[Output File](95584312.tiff)

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

 Il seguente è il codice per la classe personalizzata *TestTiffPageSavingCallback*.

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **Output della console**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
