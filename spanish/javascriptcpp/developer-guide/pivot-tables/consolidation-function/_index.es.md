---
title: Función de consolidación
type: docs
weight: 20
url: /es/javascript-cpp/consolidation-function/
description: Cómo aplicar la función de consolidación a los campos de datos de la tabla dinámica con Aspose.Cells for JavaScript vía C++.
keywords: Aspose.Cells for JavaScript vía C++ Excel, biblioteca JavaScript de Excel, función de consolidación a los campos de datos de la tabla dinámica usando Aspose.Cells for JavaScript vía C++ Excel Library.
---

## **Función de consolidación**

Aspose.Cells for JavaScript vía C++ puede usarse para aplicar la función de consolidación a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puede hacer clic derecho en el campo de valor y seleccionar la opción **Configuración del campo de valor...** y luego seleccionar la pestaña **Resumir valores por**. Desde allí, puede seleccionar cualquier función de consolidación de su elección como Suma, Cuenta, Promedio, Máximo, Mínimo, Producto, Cuenta distinta, etc.

La API Aspose.Cells for JavaScript vía C++ proporciona la enumeración [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/) para soportar las siguientes funciones de consolidación.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Cómo aplicar la función de consolidación a los campos de datos de la tabla dinámica usando Aspose.Cells for JavaScript vía C++**

El siguiente código aplica la función de consolidación **Promedio** al primer campo de datos (o campo de valor) y la función de consolidación **Conteo de valores distintos** al segundo campo de datos (o campo de valor).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
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

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

La función de consolidación CUENTA_DISTINTA es compatible solo con Microsoft Excel 2013.

{{% /alert %}}
