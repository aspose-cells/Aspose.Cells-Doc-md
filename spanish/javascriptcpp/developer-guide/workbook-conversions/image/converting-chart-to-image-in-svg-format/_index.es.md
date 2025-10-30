---
title: Convertir gráfico a imagen en formato SVG con JavaScript mediante C++
linktitle: Conversión de gráfico a imagen en formato SVG
type: docs
weight: 240
url: /es/javascript-cpp/converting-chart-to-image-in-svg-format/
description: Aprenda cómo convertir un gráfico en una imagen en formato SVG usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) es un formato de imagen vectorial en XML para gráficos bidimensionales que también admite interactividad y animación. La especificación SVG es un estándar abierto desarrollado por el World Wide Web Consortium (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, escritos en script y comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero más a menudo se crean con software de dibujo.

Aspose.Cells puede guardar gráficos en imágenes en varios formatos como BMP, JPEG, PNG, GIF, SVG, etc. Este artículo explica cómo guardar un gráfico en formato SVG.

{{% /alert %}}

El siguiente código de ejemplo explica cómo usar Aspose.Cells para convertir un gráfico en una imagen en formato SVG. El código carga el archivo de Microsoft Excel fuente y luego guarda el primer gráfico encontrado en la primera hoja de cálculo como SVG.

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
