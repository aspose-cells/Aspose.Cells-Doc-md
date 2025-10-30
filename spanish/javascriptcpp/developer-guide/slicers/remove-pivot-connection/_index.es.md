---
title: Eliminar conexión de pivote con JavaScript a través de C++
linktitle: Eliminar conexión de tabla dinámica
type: docs
weight: 30
url: /es/javascript-cpp/remove-pivot-connection/
description: Aprende cómo eliminar la conexión de pivote usando Aspose.Cells for JavaScript a través de C++.
keywords: Eliminar la conexión de pivote sin Office 2013, Office 2016, Office 2019 y Office 365 JavaScript a través de C++.
---

## **Escenarios de uso posibles**

Si deseas disociar un segmentador y tabla dinámica en Excel, debes hacer clic derecho en el segmentador y seleccionar "Conexiones de informes...". En la lista de opciones, puedes operar sobre la casilla de verificación. De manera similar, si deseas disociar un segmentador y tabla dinámica usando la API Aspose.Cells for JavaScript a través de C++ de forma programática, por favor usa el método [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-). Esto disociará el segmentador y la tabla dinámica.

## **Desasociar filtro y tabla dinámica**

El siguiente código de ejemplo carga el [archivo Excel de muestra](remove-pivot-connection.xlsx) que contiene un segmentador existente. Accede a los segmentadores y luego disocia el segmentador y la tabla dinámica. Finalmente, guarda el libro como [archivo Excel de salida](remove-pivot-connection-out.xlsx).

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
