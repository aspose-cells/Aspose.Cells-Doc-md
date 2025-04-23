---
title: Verfolgen Sie den Konversionsfortschritt von Excel zu TIFF mit Node.js via C++
linktitle: Konvertierungsvorgang von Excel nach TIFF verfolgen
type: docs
weight: 190
url: /de/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Lernen Sie, wie Sie den Konversionsfortschritt von Excel Dateien zu TIFF mithilfe von Aspose.Cells for Node.js via C++ verfolgen. Verbessern Sie die Benutzererfahrung während des Konvertierungsvorgangs.
---

## **Mögliche Verwendungsszenarien**

Manchmal kann die Konvertierung großer Excel-Dateien einige Zeit in Anspruch nehmen. Während dieser Zeit möchten Sie vielleicht den Dokumentenkonversionsfortschritt anzeigen, anstatt nur einen Ladebildschirm, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells for Node.js via C++ unterstützt die Verfolgung des Dokumentenkonversionsprozesses durch Bereitstellung der [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-Schnittstelle. Die [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-Schnittstelle bietet [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-)- und [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-)-Methoden, die Sie in Ihrer benutzerdefinierten Klasse implementieren können. Sie können auch steuern, welche Seiten gerendert werden, wie in der *TestPageSavingCallback*-Benutzerklasse demonstriert.

## **Konvertierungsvorgang von Excel nach TIFF verfolgen**

Der folgende Code lädt die [Quell-Excel-Datei](95584311.xlsx) und gibt den Fortschritt der Konvertierung in der Konsole aus, indem die benutzerdefinierte Klasse *TestPageSavingCallback* verwendet wird, die die [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-Schnittstelle implementiert. Die erzeugte Ausgabedatei ist zu Ihrer Referenz beigefügt.

[Output File](95584312.tiff)

## **Beispielcode**

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

Der folgende Code ist für die benutzerdefinierte Klasse *TestTiffPageSavingCallback*.

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

## **Konsolenausgabe**

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
