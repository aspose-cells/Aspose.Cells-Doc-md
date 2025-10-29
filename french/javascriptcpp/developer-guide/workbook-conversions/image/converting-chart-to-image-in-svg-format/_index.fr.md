---
title: Conversion de graphique en image au format SVG avec JavaScript via C++
linktitle: Conversion de graphique en image au format SVG
type: docs
weight: 240
url: /fr/javascript-cpp/converting-chart-to-image-in-svg-format/
description: Apprenez comment convertir un graphique en une image au format SVG en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) est un format d'image vectorielle basé sur XML pour les graphiques en deux dimensions qui prend également en charge l'interactivité et l'animation. La spécification SVG est une norme ouverte développée par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées et compressées. En tant que fichiers XML, les images SVG peuvent être créées et modifiées avec n'importe quel éditeur de texte, mais sont plus souvent créées avec un logiciel de dessin.

Aspose.Cells peut sauvegarder un graphique en images dans divers formats comme BMP, JPEG, PNG, GIF, SVG, etc. Cet article explique comment sauvegarder un graphique au format SVG.

{{% /alert %}}

Le code d'exemple suivant explique comment utiliser Aspose.Cells pour convertir un graphique en une image au format SVG. Le code charge le fichier source Microsoft Excel, puis enregistre le premier graphique trouvé sur la première feuille de calcul en SVG.

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
