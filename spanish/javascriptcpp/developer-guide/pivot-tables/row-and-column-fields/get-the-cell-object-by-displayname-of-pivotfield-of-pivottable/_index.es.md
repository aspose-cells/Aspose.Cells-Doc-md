---
title: Obtener el objeto Celda por el Nombre de Visualización del Campo de Tabla Dinámica de la Tabla Dinámica
type: docs
weight: 70
url: /es/javascript-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Cómo obtener el objeto Celda por el DisplayName del campo Pivot de una tabla dinámica con Aspose.Cells for JavaScript vía C++.
keywords: Aspose.Cells for JavaScript vía C++ Excel, biblioteca JavaScript de Excel, obtener el objeto Celda por el DisplayName del campo Pivot de una tabla dinámica usando Aspose.Cells for JavaScript vía C++ Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript vía C++ proporciona el método [**PivotTable.cellByDisplayName(string)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#cellByDisplayName-string-) que puedes usar para acceder al objeto celda por el nombre de pantalla del campo pivote. Este método es útil cuando quieres destacar o dar formato al encabezado del campo pivote. Este artículo explica cómo recuperar el objeto celda por el nombre de pantalla del campo de datos y luego aplicar formato a ello.

{{% /alert %}}

## **Cómo obtener el objeto de celda por DisplayName de PivotField de PivotTable**

El siguiente código accede a la primera tabla dinámica de la hoja de cálculo y luego obtiene la celda por el nombre de visualización del segundo campo de datos de la tabla dinámica. Luego cambia el color de relleno y el color de fuente de la celda a azul claro y negro respectivamente. Las capturas de pantalla siguientes muestran cómo se ve la tabla dinámica antes y después de la ejecución del código.

|**Tabla Dinámica - Antes**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Cell Styling Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table inside the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Access cell by display name of 2nd data field of the pivot table
            const dataFieldDisplayName = pivotTable.dataFields.get(1).displayName;
            const cell = pivotTable.cellByDisplayName(dataFieldDisplayName);

            // Access cell style and set its fill color and font color
            const style = cell.style;
            style.foregroundColor = AsposeCells.Color.LightBlue;
            style.font.color = AsposeCells.Color.Black;

            // Set the style of the cell
            pivotTable.format(cell.row, cell.column, style);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

|**Tabla Dinámica - Después**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
