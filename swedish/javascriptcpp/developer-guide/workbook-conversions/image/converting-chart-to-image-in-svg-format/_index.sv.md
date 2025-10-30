---
title: Konvertera diagram till bild i SVG format med JavaScript via C++
linktitle: Konvertera diagram till bild i SVG format
type: docs
weight: 240
url: /sv/javascript-cpp/converting-chart-to-image-in-svg-format/
description: Lär dig hur man konverterar ett diagram till SVG format med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) är ett XML-baserat vektorbildformat för tvådimensionell grafik som också stöder interaktivitet och animation. SVG-specifikationen är en öppen standard som utvecklats av World Wide Web Consortium (W3C) sedan 1999.

SVG-bilder och deras beteenden definieras i XML-textfiler. Detta innebär att de kan sökas, indexeras, skriptas och komprimeras. Som XML-filer kan SVG-bilder skapas och redigeras med vilken textredigerare som helst, men skapas oftare med ritprogram.

Aspose.Cells kan spara diagram till bilder i olika format som BMP, JPEG, PNG, GIF, SVG osv. Denna artikel förklarar hur man sparar ett diagram i SVG-format.

{{% /alert %}}

Följande exempelkod förklarar hur man använder Aspose.Cells för att konvertera ett diagram till en bild i SVG-format. Koden laddar den ursprungliga Microsoft Excel-filen och sparar sedan det första diagrammet som hittas på den första arbetsbladet till SVG.

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
