---
title: Arbeitsblatt in Grafik Kontext rendern mit JavaScript via C++
linktitle: Arbeitsblatt in Grafikkontext rendern
type: docs
weight: 300
url: /de/javascript-cpp/render-worksheet-to-graphic-context/
description: Erfahren Sie, wie Sie ein Arbeitsblatt unter Verwendung von Aspose.Cells for JavaScript via C++ in einen Grafik Kontext rendern. Dies umfasst das Rendern in Bilddateien, auf Bildschirmen und Druckern.
---

{{% alert color="primary" %}}

Aspose.Cells kann jetzt Arbeitsblätter in einen Grafik-Kontext rendern. Der Grafik-Kontext kann alles Mögliche sein, z. B. eine Bilddatei, ein Bildschirm oder ein Drucker. Bitte verwenden Sie eine der beiden folgenden Methoden, um ein Arbeitsblatt in einen Grafik-Kontext zu rendern.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Der folgende Code veranschaulicht, wie man mit Aspose.Cells ein Arbeitsblatt in einen Grafik-Kontext rendert. Nach der Ausführung des Codes wird das gesamte Arbeitsblatt ausgegeben und der verbleibende leere Raum im Grafik-Kontext wird mit blauer Farbe ausgefüllt, und das Bild wird als **OutputImage_out_.png** gespeichert. Sie können jede Quelldatei Excel verwenden, um diesen Code auszuprobieren. Bitte lesen Sie auch die Kommentare im Code für ein besseres Verständnis.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
