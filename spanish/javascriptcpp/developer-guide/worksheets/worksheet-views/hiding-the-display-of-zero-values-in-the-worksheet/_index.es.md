---
title: Ocultar la visualización de valores cero en la hoja de cálculo con JavaScript vía C++
linktitle: Ocultar la visualización de los valores cero en la hoja de cálculo
type: docs
weight: 50
url: /es/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Este artículo te mostrará un código de ejemplo que explica cómo ocultar programáticamente los valores cero en una hoja de cálculo de Excel usando la biblioteca JavaScript vía C++.
keywords: ocultar valores cero de la hoja de cálculo en JavaScript vía C++
---

{{% alert color="primary" %}} 

A veces, es necesario ocultar los valores cero en una hoja de cálculo. Puede ser una preferencia personal o un estándar de formato.

{{% /alert %}} 

Para ocultar los valores cero en una hoja de cálculo en Microsoft Excel (por ejemplo, Microsoft Excel 2003):

1. Desde el menú **Herramientas**, seleccione **Opciones**, y luego seleccione la pestaña **Ver**.
1. Desmarque la opción **Valores de cero**.
1. Haz clic en **Aceptar**.

 Por favor, vea el siguiente código de ejemplo que demuestra cómo ocultar ceros usando Aspose.Cells for JavaScript vía C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
