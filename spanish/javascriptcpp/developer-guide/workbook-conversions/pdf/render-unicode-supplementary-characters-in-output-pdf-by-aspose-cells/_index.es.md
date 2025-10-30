---
title: Renderizar caracteres suplementarios Unicode en el PDF de salida mediante Aspose.Cells for JavaScript vía C++
linktitle: Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells
type: docs
weight: 350
url: /es/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aprende cómo renderizar caracteres suplementarios Unicode en el PDF de salida usando Aspose.Cells for JavaScript vía C++. 
---

{{% alert color="primary" %}}

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientra que los caracteres Unicode suplementarios tienen una longitud de 4 bytes. Ahora, Aspose.Cells admite la renderización de estos caracteres Unicode de 4 bytes.

En el Estándar de Caracteres Unicode, los Caracteres Suplementarios son los caracteres asignados a puntos de código desde U+10000 hasta U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8 estos caracteres tienen cada uno una longitud de 4 bytes.
- En UTF-16 estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}}

## Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells for JavaScript vía C++

La siguiente captura muestra cómo Aspose.Cells renderizó el [archivo de Excel de origen](5115563.xlsx) en el [PDF de salida](5115564.pdf). Como puedes ver, los tres caracteres suplementarios Unicode se han renderizado exactamente igual que en Microsoft Excel.

![todo:image_alt_text](output.png)

## Código de Muestra

Puede usar este código de ejemplo para convertir [archivo de Excel fuente](5115563.xlsx) en [PDF de salida](5115564.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
