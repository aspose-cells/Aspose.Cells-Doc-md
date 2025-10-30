---
title: Desactivar los paneles de control de la tabla dinámica
type: docs
weight: 90
url: /es/javascript-cpp/disable-pivot-table-ribbons/
description: Cómo desactivar las cintas de opciones de la tabla dinámica con Aspose.Cells for JavaScript vía C++.
keywords: Aspose.Cells for JavaScript vía C++ Excel, biblioteca JavaScript de Excel, desactivar las cintas de opciones de la tabla dinámica usando Aspose.Cells for JavaScript vía biblioteca de C++ para Excel.
---

{{% alert color="primary" %}}

Los informes basados en tablas dinámicas son útiles pero propensos a errores si los usuarios de destino no tienen conocimientos detallados de Excel para configurar estos informes. En estas circunstancias, las organizaciones querrán restringir a los usuarios para que no puedan modificar estos informes basados en tablas dinámicas. Funciones comunes de una tabla dinámica como agregar filtros adicionales, segmentaciones, campos o cambiar el orden de ciertos elementos en el informe no se recomiendan para todos los usuarios. Por otro lado, estos usuarios también deberían poder actualizar el informe y usar filtros o segmentaciones existentes. Aspose.Cells for JavaScript vía C++ ha proporcionado esta capacidad a los desarrolladores para restringir a los usuarios de modificar estos informes mientras los crean. Para este propósito, Excel ofrece una función para deshabilitar la cinta de opciones de la tabla dinámica y la misma la proporciona Aspose.Cells for JavaScript vía C++, es decir, el desarrollador puede desactivar la cinta que contiene controles para modificar estos informes.

{{% /alert %}}

## **Cómo desactivar la cinta de opciones de la tabla dinámica usando Aspose.Cells for JavaScript vía C++**

El siguiente código demuestra esta característica accediendo a una tabla dinámica de una hoja y luego estableciendo [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) en **falso**. El archivo de tabla dinámica de ejemplo se puede descargar desde este [enlace](pivot_table_test.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
