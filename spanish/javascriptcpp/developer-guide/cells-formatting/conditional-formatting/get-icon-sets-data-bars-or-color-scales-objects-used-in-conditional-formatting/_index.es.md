---
title: Obtener conjuntos de iconos, barras de datos o escalas de colores utilizadas en el formato condicional
linktitle: Obtener conjuntos de iconos, barras de datos o escalas de colores utilizadas en el formato condicional
description: Aprende cómo usar Aspose.Cells for JavaScript a través de C++ para recuperar conjuntos de iconos, barras de datos y objetos de escala de colores en formato condicional desde archivos de hojas de cálculo.
keywords: Aspose.Cells, Formato condicional, Conjunto de iconos, Barra de datos, Escala de colores, Hoja de cálculo, JavaScript a través de C++
type: docs
weight: 10
url: /es/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

A veces, es necesario recuperar conjuntos de iconos que se utilizan en el formato condicional de una celda o un rango de celdas y queremos crear un archivo de imagen basado en él. Es posible que necesite leer las barras de datos o escalas de colores utilizadas en el formato condicional. Aspose.Cells admite esta característica.

{{% /alert %}}  

El siguiente ejemplo muestra cómo leer conjuntos de íconos utilizados en formato condicional. Con la API sencilla de Aspose.Cells, los datos de la imagen del conjunto de íconos se guardan como una imagen.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Extract Conditional Formatting Icon</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon and create a downloadable blob
            const imageData = icon.imageData;
            const blob = new Blob([imageData], { type: 'image/jpeg' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Icon Image';

            resultEl.innerHTML = '<p style="color: green;">Icon image extracted. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
