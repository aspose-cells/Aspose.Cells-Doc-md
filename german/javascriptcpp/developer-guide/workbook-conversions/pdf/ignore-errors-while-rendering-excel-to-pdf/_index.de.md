---
title: Fehler beim Rendern von Excel nach PDF mit JavaScript über C++ ignorieren
linktitle: Fehler ignorieren beim Umsetzen von Excel in PDF
type: docs
weight: 80
url: /de/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Erfahren Sie, wie Sie Fehler während der Konvertierung von Excel Dateien zu PDF mit Aspose.Cells for JavaScript über C++ ignorieren.
---

## **Mögliche Verwendungsszenarien**  

Manchmal treten beim Konvertieren Ihrer Excel-Datei in PDF Fehler oder Ausnahmen auf und der Konvertierungsprozess wird beendet. Sie können alle solchen Fehler während der Konvertierung mithilfe der [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) Eigenschaft ignorieren. Dadurch wird der Konvertierungsprozess reibungslos abgeschlossen, ohne Fehler auszulösen, aber es kann zu Datenverlust kommen. Verwenden Sie diese Eigenschaft daher nur, wenn Datenverlust für Sie nicht kritisch ist.  

## **Ignorieren Sie Fehler beim Rendern von Excel in PDF**  

Der folgende Code lädt die [Beispiel-Excel-Datei](55541778.xlsx), aber die Beispiel-Excel-Datei ist fehlerhaft und löst während [der Konvertierung zu PDF](55541779.pdf) in 17.11 einen Fehler aus, aber da wir die [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) Eigenschaft verwenden, wird kein Fehler ausgelöst. Ein *abgerundeter roter Pfeil wie in diesem Screenshot* geht jedoch verloren.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
