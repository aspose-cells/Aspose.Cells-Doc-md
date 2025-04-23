---  
title: Traccia lo stato di avanzamento della conversione del documento con Node.js tramite C++  
linktitle: Monitora il progresso della conversione del documento  
type: docs  
weight: 970  
url: /it/nodejs-cpp/track-document-conversion-progress/  
description: Scopri come monitorare il progresso della conversione dei documenti in file Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

 A volte, convertire grandi file Excel può richiedere del tempo. Durante questo, potresti voler mostrare lo stato di avanzamento della conversione del documento invece di una semplice schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells for Node.js via C++ supporta il tracciamento del processo di conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) fornisce i metodi [**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) e [**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata *TestPageSavingCallback*.  

## **Monitorare il progresso della conversione dei documenti**  

Il seguente esempio di codice carica il [file Excel sorgente](94896151.xlsx) e stampa il progresso della conversione nella console utilizzando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback).  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Define TestPageSavingCallback class
class TestPageSavingCallback {
// Implement the required methods of this callback as needed
onPageSaving(pageIndex, fileName) {
console.log(`Saving page ${pageIndex} to ${fileName}`);
}
}

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "PagesBook1.xlsx"));

const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setPageSavingCallback(new TestPageSavingCallback());

workbook.save(path.join(outputDir, "DocumentConversionProgress.pdf"), pdfSaveOptions);
```  

Di seguito è riportato il codice della classe personalizzata *TestPageSavingCallback*.  

```javascript
const AsposeCells = require("aspose.cells.node");

class TestPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages before page index 2.
if (args.getPageIndex() < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages after page index 8.
if (args.getPageIndex() >= 8) {
args.setHasMorePages(false);
}
}
}
```  

## **Output della console**  

{{< highlight java >}}  

Start saving page index 0 of pages 11</br>  
End saving page index 0 of pages 11</br>  
Start saving page index 1 of pages 11</br>  
End saving page index 1 of pages 11</br>  
Start saving page index 2 of pages 11</br>  
End saving page index 2 of pages 11</br>  
Start saving page index 3 of pages 11</br>  
End saving page index 3 of pages 11</br>  
Start saving page index 4 of pages 11</br>  
End saving page index 4 of pages 11</br>  
Start saving page index 5 of pages 11</br>  
End saving page index 5 of pages 11</br>  
Start saving page index 6 of pages 11</br>  
End saving page index 6 of pages 11</br>  
Start saving page index 7 of pages 11</br>  
End saving page index 7 of pages 11</br>  
Start saving page index 8 of pages 11</br>  
End saving page index 8 of pages 11  

{{< /highlight >}}  

