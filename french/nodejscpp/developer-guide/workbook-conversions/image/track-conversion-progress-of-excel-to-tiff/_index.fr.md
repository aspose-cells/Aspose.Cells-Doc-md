---
title: Suivi de la progression de la conversion d Excel en TIFF avec Node.js via C++
linktitle: Suivre la progression de la conversion d Excel en TIFF
type: docs
weight: 190
url: /fr/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Apprenez comment suivre la progression de la conversion de fichiers Excel en TIFF en utilisant Aspose.Cells for Node.js via C++. Améliorez l expérience utilisateur pendant le processus de conversion.
---

## **Scénarios d'utilisation possibles**

Parfois, la conversion de grands fichiers Excel peut prendre du temps. Pendant ce temps, vous pouvez vouloir afficher la progression de la conversion du document au lieu d'une simple écran de chargement pour améliorer l'utilisabilité de votre application. Aspose.Cells for Node.js via C++ prend en charge le suivi du processus de conversion du document en fournissant l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). L'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) fournit les méthodes [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) et [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues, comme démontré dans la classe personnalisée *TestPageSavingCallback*.

## **Suivre la progression de la conversion d'Excel en TIFF**

Le code ci-dessous charge le [fichier Excel source](95584311.xlsx) et affiche la progression de sa conversion dans la console en utilisant la classe personnalisée *TestPageSavingCallback* qui implémente l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). Le fichier de sortie généré est joint pour votre référence.

[Output File](95584312.tiff)

## **Code d'exemple**

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

Voici le code de la classe personnalisée *TestTiffPageSavingCallback*.

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

## **Sortie console**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
