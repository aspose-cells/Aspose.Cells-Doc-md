---
title: Configurando fórmula compartida con JavaScript a través de C++
linktitle: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Si deseas agregar una función en una hoja de cálculo que realice algunos cálculos, este artículo explica cómo lograr esta tarea usando Aspose.Cells for JavaScript a través de C++.

{{% /alert %}}

## Configurando fórmula compartida usando Aspose.Cells for JavaScript a través de C++

Supongamos que tienes una hoja de trabajo llena de datos con el formato que se muestra en la siguiente hoja de cálculo de ejemplo.

|Archivo de entrada con una columna de datos|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Quieres agregar una función en B2 que calculará el impuesto sobre las ventas para la primera fila de datos. El impuesto es del **9%**. La fórmula que calcula el impuesto sobre las ventas es: **"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

Aspose.Cells te permite especificar una fórmula utilizando la propiedad [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--). Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, y así sucesivamente) en la columna.

O haga lo que hizo para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de la celda en consecuencia (A3*0.09, A4*0.09, A5*0.09 y así sucesivamente). Esto requiere que las referencias de celda para cada fila se actualicen. También requiere que Aspose.Cells analice cada fórmula individualmente, lo cual puede ser lento para hojas de cálculo grandes y fórmulas complejas. Además, agrega líneas adicionales de código, aunque los bucles pueden reducirlas en cierta medida.

Otro enfoque es usar una **fórmula compartida**. Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. El método [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
