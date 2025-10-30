---
title: Erweiterung von Text von rechts nach links beim Exportieren von Excel in HTML mit JavaScript via C++
linktitle: Text von rechts nach links erweitern, während Excel Datei in HTML exportiert wird
type: docs
weight: 60
url: /de/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt jetzt das Erweitern von Text von rechts nach links beim Exportieren von Excel-Dateien in HTML. Diese Funktion wurde seit der Version v8.9.0.0 implementiert. Wenn Ihre Quell-Excel-Datei also einen Text enthält, der von rechts nach links erweitert, exportiert Aspose.Cells dies korrekt in HTML.

{{% /alert %}}
## **Text von rechts nach links erweitern, während Excel-Datei in HTML exportiert wird**
Der folgende Beispielscode konvertiert die [Beispiel-Excel-Datei](5115502.xlsx) in HTML. Dieser Screenshot zeigt, wie das Beispiel-Excel in Microsoft Excel 2013 aussieht.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Dieser Screenshot zeigt die [ausgegebene HTML mit älterer Version](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Dieser Screenshot zeigt die [ausgegebene HTML mit neuerer Version](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Wie Sie in den Screenshots sehen können, erweitert die neuere Version den rechtsbündigen Text genau wie Microsoft Excel korrekt nach links.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Expand Text From Right To Left Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load source excel file inside the workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get CellsHelper version (converted from getVersion())
            const version = CellsHelper.version;

            // Save workbook in html format
            const outputData = wb.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `ExpandTextFromRightToLeft_out_${version}.html`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to HTML successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
