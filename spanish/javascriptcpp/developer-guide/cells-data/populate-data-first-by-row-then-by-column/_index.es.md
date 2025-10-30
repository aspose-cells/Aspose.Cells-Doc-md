---
title: Primero llenar datos por fila y luego por columna
type: docs
weight: 1000
url: /es/javascript-cpp/populate-data-first-by-row-then-by-column/
description: Aprende cómo rellenar datos primero por fila y luego por columna mediante la API de Aspose.Cells for JavaScript via C++.
keywords: Rellenar datos primero por fila y luego por columna JavaScript via C++, Insertar datos primero por fila y luego por columna JavaScript via C++, Añadir datos primero por fila y luego por columna JavaScript via C++, Inserción de datos de alto rendimiento JavaScript via C++, Añadido de datos de alto rendimiento JavaScript via C++
---

{{% alert color="primary" %}}  

Llenar una hoja de cálculo con datos primero por fila y luego por columna mejora el rendimiento general.  

{{% /alert %}}  

Poner datos en la secuencia A1, B1, A2, B2 es más rápido que A1, A2, B1, B2. Si hay muchas celdas en una hoja de cálculo y sigues la segunda secuencia, es decir, estás llenando los datos fila por fila, este consejo puede hacer que el programa sea mucho más rápido.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
