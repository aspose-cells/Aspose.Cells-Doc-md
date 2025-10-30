---
title: Resampling hinzugefügter Bilder  Excel zu PDF Konvertierung mit JavaScript via C++
linktitle: Resampling hinzugefügter Bilder
type: docs
weight: 150
url: /de/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Lernen Sie, wie Sie in Excel Dateien hinzugefügte Bilder komprimieren, um die PDF Größe zu reduzieren und die Konvertierungsleistung mit Aspose.Cells for JavaScript via C++ zu verbessern.
---

{{% alert color="primary" %}}

Bei der Arbeit mit großen Microsoft-Excel-Dateien mit vielen Bildern müssen Sie möglicherweise Bilder komprimieren, die hinzugefügt wurden, um die AusgabepDF-Größe zu verringern und die Gesamtleistung der Konvertierung zu verbessern. Aspose.Cells for JavaScript via C++ unterstützt das Resampling hinzugefügter Bilder, um die Ausgabe-PDF-Größe zu verringern und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte beachten Sie den folgenden Beispiellcode, der beschreibt, wie die Aufgabe mithilfe der Aspose.Cells-API ausgeführt wird. Das Beispiel konvertiert eine Microsoft Excel-Datei in eine PDF-Datei und komprimiert dabei die Bilder in der Datei.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set Image Resample properties (converted from setImageResample(300, 70))
            // Universal setter->property conversion: setImageResample(...) -> imageResample = [...]
            pdfSaveOptions.imageResample = [300, 70];

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out_pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Die Verwendung der [**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-)-Option minimiert die Größe der Ausgabedatei, kann aber die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
