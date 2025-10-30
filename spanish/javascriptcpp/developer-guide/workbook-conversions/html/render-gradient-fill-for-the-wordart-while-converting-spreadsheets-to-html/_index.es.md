---
title: Renderizar relleno de gradiente para WordArt al convertir hojas de cálculo a HTML con JavaScript vía C++
linktitle: Renderizar relleno degradado para WordArt al convertir hojas de cálculo a HTML
type: docs
weight: 90
url: /es/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Aprende cómo renderizar relleno de gradiente en WordArt al convertir hojas de cálculo a HTML usando Aspose.Cells for JavaScript vía C++.
---

## **Escenarios de uso posibles**  
Antes de Aspose.Cells 17.1, Aspose.Cells no renderizaba el relleno de degradado del WordArt al convertir el archivo de Excel a formato HTML. Desde el lanzamiento de Aspose.Cells 17.1, se soporta el relleno de WordArt con degradado. La siguiente captura de pantalla compara el efecto del relleno de degradado al convertir el archivo de Excel usando Aspose.Cells 17.1 y la versión más antigua.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Renderizar relleno degradado para WordArt al convertir hojas de cálculo a HTML**  
El siguiente código de ejemplo convierte el [archivo de Excel fuente](22774111.xlsx) en [formato HTML de salida](22774109.zip). El archivo de Excel de origen contiene un objeto WordArt con relleno de degradado como se muestra en la captura anterior.  

## **Código de muestra**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
