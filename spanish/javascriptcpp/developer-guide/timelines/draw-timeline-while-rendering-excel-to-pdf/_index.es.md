---
title: Dibujar línea de tiempo mientras renderizas Excel a PDF con JavaScript a través de C++
linktitle: Dibujar línea de tiempo al renderizar Excel a PDF
type: docs
weight: 60
url: /es/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Gestiona líneas de tiempo de archivos Excel con Script Aspose.Cells for Java a través de C++.
keywords: Renderizando línea de tiempo a PDF sin Office 2013, Office 2016, Office 2019 y Office 365 JavaScript a través de C++
---

## **Dibuje una línea de tiempo mientras renderiza Excel a PDF**
Si tienes un archivo Excel con una línea de tiempo aplicada y deseas exportar el Excel a PDF con la configuración de línea de tiempo, Script Aspose.Cells for Java a través de C++ ahora admite esto por defecto. Simplemente exporta el archivo Excel con línea de tiempo a PDF y el PDF generado mostrará la línea de tiempo aplicada.

El siguiente código de muestra carga el [archivo Excel de muestra](input.xlsx) que contiene una línea de tiempo existente. Luego guarda el libro de trabajo como [archivo PDF de salida](out.pdf). La siguiente captura de pantalla compara el archivo Excel fuente y el archivo PDF generado.

<img src="out.png" width="60%">

## **Código de muestra**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
