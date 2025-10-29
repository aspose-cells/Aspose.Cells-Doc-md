---  
title: Suivi de la progression de la conversion du document avec Node.js via C++  
linktitle: Suivre l avancement de la conversion du document  
type: docs  
weight: 970  
url: /fr/nodejs-cpp/track-document-conversion-progress/  
description: Apprenez comment suivre la progression de la conversion de documents dans les fichiers Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Parfois, la conversion de grands fichiers Excel peut prendre du temps. Pendant ce temps, vous pouvez vouloir afficher la progression de la conversion du document au lieu d'une simple écran de chargement pour améliorer l'utilisabilité de votre application. Aspose.Cells for Node.js via C++ prend en charge le suivi du processus de conversion du document en fournissant l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). L'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) fournit les méthodes [**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) et [**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues, comme démontré dans la classe personnalisée *TestPageSavingCallback*.  

## **Suivre la progression de la conversion des documents**  

L’exemple de code suivant charge le [fichier Excel source](94896151.xlsx) et affiche sa progression de conversion dans la console en utilisant la classe personnalisée *TestPageSavingCallback* qui implémente l’interface [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback).  

## **Code d'exemple**  

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

Le code pour la classe personnalisée *TestPageSavingCallback*.  

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

## **Sortie console**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
