---
title: Configurar Opción de tabla dinámica  Mostrar celdas vacías
type: docs
weight: 40
url: /es/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

Puedes configurar diferentes opciones de tablas dinámicas usando Aspose.Cells for JavaScript vía C++. Una de estas opciones es "Mostrar en celdas vacías". Al configurar esta opción, todas las celdas vacías en una tabla dinámica se muestran como una cadena especificada.

{{% /alert %}}

## **Configuración de opción de tabla dinámica en Microsoft Excel**

Para encontrar y configurar esta opción en Microsoft Excel:

1. Seleccione una tabla dinámica y haga clic derecho.
2. Seleccione **Opciones de tabla dinámica**.
3. Seleccione la pestaña **Diseño y formato**.
4. Seleccione la opción **Mostrar celdas vacías** y especifique una cadena.

## **Configurando la opción de tabla dinámica usando Aspose.Cells for JavaScript vía C++**

Aspose.Cells for JavaScript vía C++ proporciona las propiedades [**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-) y [**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-) para configurar la opción "Mostrar en celdas vacías" en la tabla dinámica.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Artículos relacionados

- [Dar formato a la tabla dinámica](/cells/es/javascript-cpp/formatting-pivot-table/)
