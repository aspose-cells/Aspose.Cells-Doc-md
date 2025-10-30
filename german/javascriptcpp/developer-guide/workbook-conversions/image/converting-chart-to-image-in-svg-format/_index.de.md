---
title: Konvertieren eines Diagramms in SVG Format mit JavaScript über C++
linktitle: Diagramm in SVG Format konvertieren
type: docs
weight: 240
url: /de/javascript-cpp/converting-chart-to-image-in-svg-format/
description: Erfahren Sie, wie Sie ein Diagramm mit Aspose.Cells for JavaScript über C++ in SVG Format umwandeln.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) ist ein auf XML basierendes Vektorbildformat für zweidimensionale Grafiken, das auch Interaktivität und Animation unterstützt. Die SVG-Spezifikation ist ein offener Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

SVG-Bilder und ihr Verhalten sind in XML-Textdateien definiert. Das bedeutet, dass sie durchsucht, indexiert, skriptgesteuert und komprimiert werden können. Als XML-Dateien können SVG-Bilder mit jedem Texteditor erstellt und bearbeitet werden, werden jedoch häufiger mit Zeichensoftware erstellt.

Aspose.Cells kann Diagramme in verschiedenen Formaten wie BMP, JPEG, PNG, GIF, SVG usw. als Bild speichern. Dieser Artikel erklärt, wie man ein Diagramm im SVG-Format speichert.

{{% /alert %}}

Der folgende Beispielcode erläutert, wie Aspose.Cells verwendet wird, um ein Diagramm in ein SVG-Formatbild zu konvertieren. Der Code lädt die Quelldatei von Microsoft Excel und speichert dann das erste auf dem ersten Arbeitsblatt gefunden Diagramm als SVG.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Chart to SVG</title>
    </head>
    <body>
        <h1>Export First Chart to SVG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType } = AsposeCells;

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

            // Access first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Set image or print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;

            // Export the chart to SVG format (returns image bytes)
            const imageData = chart.toImage(opts);

            // Create downloadable SVG blob
            const blob = new Blob([imageData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to SVG. Click the download link to download the SVG file.</p>';
        });
    </script>
</html>
```
