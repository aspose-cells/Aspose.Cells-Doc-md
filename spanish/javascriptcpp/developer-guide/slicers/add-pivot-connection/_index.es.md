---
title: Agregar conexión de Pivote con JavaScript vía C++
linktitle: Agregar conexión de tabla dinámica
type: docs
weight: 30
url: /es/javascript-cpp/add-pivot-connection/
description: Aprende cómo agregar una conexión de pivote usando Aspose.Cells for JavaScript vía C++.
keywords: Agregar conexión de pivote sin Office 2013, Office 2016, Office 2019 y Office 365 JavaScript vía C++.
---

## **Escenarios de uso posibles**

Si deseas asociar un segmentador y una tabla dinámica en Excel, debes hacer clic derecho en el segmentador y seleccionar la opción "Conexiones de informe...". En la lista de opciones, puedes operar con la casilla de verificación. De manera similar, si quieres asociar un segmentador y una tabla dinámica mediante la API de Aspose.Cells programáticamente, usa el método [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-). Esto asociará el segmentador y la tabla dinámica.

## **Asociar filtro y tabla dinámica**

El siguiente código de ejemplo carga el [archivo Excel de muestra](add-pivot-connection.xlsx) que contiene un segmentador existente. Accede al segmentador y luego asocia el segmentador con la tabla dinámica. Finalmente, guarda el libro como [archivo Excel de salida](add-pivot-connection-out.xlsx).

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
