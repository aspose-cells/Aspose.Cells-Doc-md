---  
title: Verfolgung des Dokumentenkonvertierungsfortschritts mit Node.js via C++  
linktitle: Fortschritt der Dokumentkonvertierung verfolgen  
type: docs  
weight: 970  
url: /de/nodejs-cpp/track-document-conversion-progress/  
description: Erfahren Sie, wie Sie den Fortschritt der Dokumentenkonvertierung bei Excel Dateien mit Aspose.Cells for Node.js via C++ verfolgen.  
---  

## **Mögliche Verwendungsszenarien**  

Manchmal kann die Konvertierung großer Excel-Dateien einige Zeit in Anspruch nehmen. Während dieser Zeit möchten Sie vielleicht den Dokumentenkonversionsfortschritt anzeigen, anstatt nur einen Ladebildschirm, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells for Node.js via C++ unterstützt die Verfolgung des Dokumentenkonversionsprozesses durch Bereitstellung der [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-Schnittstelle. Die [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-Schnittstelle bietet [**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-)- und [**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-)-Methoden, die Sie in Ihrer benutzerdefinierten Klasse implementieren können. Sie können auch steuern, welche Seiten gerendert werden, wie in der *TestPageSavingCallback*-Benutzerklasse demonstriert.  

## **Fortschritt der Dokumentkonvertierung nachverfolgen**  

Der folgende Code lädt die [Quellexceldatei](94896151.xlsx) und gibt den Fortschritt ihrer Konvertierung in der Konsole aus, indem die benutzerdefinierte Klasse *TestPageSavingCallback* verwendet wird, die das [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-Interface implementiert.  

## **Beispielcode**  

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

Der folgende Code ist für die benutzerdefinierte Klasse *TestPageSavingCallback*.  

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

## **Konsolenausgabe**  

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
