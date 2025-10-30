---
title: Stellen Sie die Spaltenbreite mit skalierbaren Einheiten wie em oder Prozent mit JavaScript über C++ ein
linktitle: Spaltenbreite in skalierbare Einheiten wie em oder Prozent einstellen
type: docs
weight: 130
url: /de/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Erfahren Sie, wie Sie die Spaltenbreite in skalierbaren Einheiten wie em oder Prozent in Aspose.Cells for JavaScript über C++ setzen. Verbessern Sie die Darstellung der generierten HTML Tabellen.
---

Das Erstellen einer HTML-Datei aus einer Tabelle ist sehr üblich. Die Größe der Spalten wird in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch Fälle geben, in denen diese feste Größe nicht erforderlich ist. Zum Beispiel, wenn die Breite eines Container-Panels 600px beträgt, wo diese HTML-Seite angezeigt wird, erhalten Sie möglicherweise eine horizontale Bildlaufleiste, wenn die generierte Tabellengröße größer ist. Es wurde verlangt, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent geändert wird, um eine bessere Präsentation zu erreichen. Das folgende Beispiel kann verwendet werden, wobei [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) auf **true** gesetzt wird, um eine skalierbare Breite zu erstellen.

Beispiel-Quelldatei und Ausgabedateien können von folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
