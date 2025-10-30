---
title: Renderizar hoja de cálculo a contexto gráfico con JavaScript via C++
linktitle: Renderizar hoja de cálculo en contexto gráfico
type: docs
weight: 300
url: /es/javascript-cpp/render-worksheet-to-graphic-context/
description: Aprende cómo renderizar una hoja de cálculo a un contexto gráfico usando Aspose.Cells for JavaScript via C++. Esto incluye renderizar a archivos de imagen, pantallas y impresoras.
---

{{% alert color="primary" %}}

Ahora Aspose.Cells puede renderizar hojas de cálculo a un contexto gráfico. El contexto gráfico puede ser cualquier cosa como un archivo de imagen, pantalla o impresora, etc. Usa uno de los siguientes dos métodos para renderizar una hoja de cálculo a un contexto gráfico.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

El siguiente código ilustra cómo usar Aspose.Cells para renderizar una hoja de cálculo en un contexto gráfico. Una vez que ejecutes el código, imprimirá toda la hoja y llenará el espacio vacío restante con color azul en el contexto gráfico y guardará la imagen como archivo **OutputImage_out_.png**. Puedes usar cualquier archivo de Excel para probar este código. También lee los comentarios dentro del código para mejor comprensión.

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
