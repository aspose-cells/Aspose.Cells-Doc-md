---
title: Lectura y escritura de la tabla de consultas de la hoja de cálculo con JavaScript a través de C++
linktitle: Leer y Escribir Tabla de Consulta de Hoja de Cálculo
type: docs
weight: 40
url: /es/javascript-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la colección Worksheet.QueryTables que devuelve el objeto de tipo QueryTable por índice. Tiene las siguientes dos propiedades

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Ambos son valores booleanos. Puedes verlos en Microsoft Excel a través de Datos > Conexiones > Propiedades.

{{% /alert %}}

## Lectura y Escritura de Tabla de Consulta de Hoja de Cálculo

El siguiente código de ejemplo lee la primera QueryTable de la primera hoja de cálculo y luego imprime ambas propiedades de la QueryTable. Luego establece QueryTable.preserveFormatting en verdadero.

Puedes descargar el archivo de Excel fuente utilizado en este código y el archivo de Excel de salida generado por el código desde los siguientes enlaces.

- [Archivo de Excel Fuente](5115533.xlsx)
- [Archivo de Excel de Salida](5115537.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells QueryTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
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

            // Create workbook from source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first Query Table
            const qt = worksheet.queryTables.get(0);

            // Read Query Table Data (properties converted from getters)
            const adjustColumnWidth = qt.adjustColumnWidth;
            const preserveFormatting = qt.preserveFormatting;

            resultDiv.innerHTML = `<p>Adjust Column Width: ${adjustColumnWidth}</p><p>Preserve Formatting: ${preserveFormatting}</p>`;

            // Now set Preserve Formatting to true (setter converted to property assignment)
            qt.preserveFormatting = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">PreserveFormatting set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Salida en Consola



{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recuperar rango de resultados de tabla de consulta

Aspose.Cells proporciona la opción de leer la dirección, es decir, el rango de resultados de celdas para una tabla de consulta. El siguiente código demuestra esta función leyendo la dirección del rango de resultados para una tabla de consulta. El archivo de ejemplo se puede descargar [aquí](72417290.xlsx).

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const queryTable = worksheet.queryTables.get(0);
            const resultRange = queryTable.resultRange;
            const address = resultRange.address;

            const addressText = (address && typeof address.toString === 'function') ? address.toString() : String(address);
            console.log(addressText);
            document.getElementById('result').innerHTML = `<p>Query table result range address: ${addressText}</p>`;
        });
    </script>
</html>
```
