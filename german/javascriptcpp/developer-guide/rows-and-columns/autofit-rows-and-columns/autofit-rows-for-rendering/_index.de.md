---
title: Zeilen für die Darstellung mit JavaScript über C++ automatisch anpassen
linktitle: AutoFit für das Rendern von Zeilen
type: docs
weight: 130
url: /de/javascript-cpp/autofit-rows-for-rendering/
description: Lernen Sie, wie Sie Zeilen für die Darstellung in Excel mit Aspose.Cells for JavaScript über C++ automatisch anpassen. Verhindern Sie, dass Text beim Speichern als PDF Datei abgeschnitten wird.
---

Im Allgemeinen können Sie beim Anzeigen aller Textinhalte in einer Zelle die Zeile im Normalansicht mit 100 % Zoom in Microsoft Excel automatisch anpassen. Dadurch ist der Text in der Normalansicht vollständig sichtbar, und auch beim Drucken oder Speichern als PDF wird der Text korrekt angezeigt.

In einigen Fällen funktioniert die automatische Zeilenanpassung in der Normalansicht gut, aber beim Wechsel in die Druckansicht oder beim Speichern als PDF wird der Text abgeschnitten. Bitte prüfen Sie die Quelldatei [Book1.xlsx](Book1.xlsx) und Screenshots.

![Text wird in der Druckansicht beschnitten](text_clipped_in_printview.png)

Wenn Sie verhindern möchten, dass Text in der gespeicherten PDF-Datei abgeschnitten wird, können Sie die Zeile mit der [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--) Option automatisch anpassen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Nun wird der Text nicht in der Ausgabe-PDF-Datei beschnitten.

![Text wird in der gespeicherten PDF-Datei nicht beschnitten](text_not_clipped_in_saved_pdf.png)
