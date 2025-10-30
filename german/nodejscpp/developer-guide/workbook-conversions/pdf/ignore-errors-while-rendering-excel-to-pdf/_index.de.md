---  
title: Fehler beim Rendern von Excel zu PDF mit Node.js via C++ ignorieren  
linktitle: Fehler ignorieren beim Umsetzen von Excel in PDF  
type: docs  
weight: 80  
url: /de/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Erfahren Sie, wie Sie Fehler während der Konvertierung von Excel Dateien in PDF mit Aspose.Cells for Node.js via C++ ignorieren können.  
---  

## **Mögliche Verwendungsszenarien**  

Manchmal treten beim Konvertieren Ihrer Excel-Datei in PDF Fehler oder Ausnahmen auf und der Konvertierungsprozess wird beendet. Sie können alle solchen Fehler während der Konvertierung mithilfe der [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) Eigenschaft ignorieren. Dadurch wird der Konvertierungsprozess reibungslos abgeschlossen, ohne Fehler auszulösen, aber es kann zu Datenverlust kommen. Verwenden Sie diese Eigenschaft daher nur, wenn Datenverlust für Sie nicht kritisch ist.  

## **Ignorieren Sie Fehler beim Rendern von Excel in PDF**  

Der folgende Code lädt die [Beispiel-Excel-Datei](55541778.xlsx), aber die Beispiel-Excel-Datei ist fehlerhaft und löst während [der Konvertierung zu PDF](55541779.pdf) in 17.11 einen Fehler aus, aber da wir die [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) Eigenschaft verwenden, wird kein Fehler ausgelöst. Ein *abgerundeter roter Pfeil wie in diesem Screenshot* geht jedoch verloren.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
