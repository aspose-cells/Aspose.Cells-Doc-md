---
title: Renderizar Línea de Tiempo
type: docs
weight: 40
url: /es/javascript-cpp/rendering-timeline/
description: Gestiona líneas de tiempo de archivos Excel con Script Aspose.Cells for Java a través de C++.
keywords: Renderización de línea de tiempo sin Office 2013, Office 2016, Office 2019 y Office 365
---

## **Escenarios de uso posibles**
Script Aspose.Cells for Java a través de de C++ soporta la renderización de forma de línea de tiempo sin usar Office 2013, Office 2016, Office 2019 y Office 365. Si conviertes tu hoja de cálculo en una imagen o guardas tu libro de trabajo en formatos PDF o HTML, verás que las líneas de tiempo se renderizan correctamente.

## **Renderización de Línea de tiempo**
 El siguiente código de ejemplo carga el [archivo Excel de ejemplo](input.xlsx) que contiene una línea de tiempo existente. Obtén el objeto forma de acuerdo al nombre de la línea de tiempo, y luego renderízalo en una imagen mediante el método Shape.ToImage(). La siguiente imagen es la [imagen de salida](out.png) que muestra la línea de tiempo renderizada. Como puedes ver, la línea de tiempo ha sido renderizada correctamente y se ve igual que en el archivo Excel de ejemplo.

![todo:image_alt_text](out.png)
### **Código de muestra**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Timeline Shape as Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Add timeline relating to pivot table (access first timeline)
            const timeline = sheet.timelines.get(0);

            // Prepare image options
            const options = new ImageOrPrintOptions();
            options.imageType = ImageType.Png;

            // Get timeline shape object by timeline's name
            const timeLineShape = sheet.shapes.get(timeline.name);

            // Export shape to image (browser returns image bytes)
            const imageData = timeLineShape.toImage(options);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Timeline Image';

            resultDiv.innerHTML = '<p style="color: green;">Timeline image generated successfully. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
