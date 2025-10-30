---
title: Obtener validación aplicada en una celda
type: docs
weight: 200
url: /es/javascript-cpp/get-validation-applied-on-a-cell/
description: Este artículo muestra cómo aplicar validación en una celda con JavaScript vía C++.
keywords: aplicar validación de celda en Excel con JavaScript vía C++, aplicar validación en una celda en Excel con JavaScript vía C++, aplicar validación en Excel con JavaScript vía C++, validación de celda en Excel con JavaScript vía C++, JavaScript vía C++ aplicar validación de celda en Excel, JavaScript vía C++ aplicar validación en una celda en Excel, JavaScript vía C++ validación de celda en Excel
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells for JavaScript vía C++ para obtener la validación aplicada a una celda. Aspose.Cells proporciona el método [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) para este propósito. Si no hay validación aplicada en la celda, devuelve null.

De manera similar, puede usar el método [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) para adquirir la validación aplicada a una celda proporcionando sus índices de fila y columna.

{{% /alert %}}

## Código JavaScript para obtener la validación aplicada en una celda

El siguiente ejemplo de código muestra cómo obtener la validación aplicada en una celda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Validation Properties Example</h1>
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

            // Instantiate the workbook from the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Cell C1 has the Decimal Validation applied on it.
            const cell = worksheet.cells.get("C1");

            // Access the validation applied on this cell
            const validation = cell.validation;

            // Read various properties of the validation
            let output = '';
            output += '<p>Reading Properties of Validation</p>';
            output += '<hr />';
            output += `<p>Type: ${validation.type}</p>`;
            output += `<p>Operator: ${validation.operator}</p>`;
            output += `<p>Formula1: ${validation.formula1}</p>`;
            output += `<p>Formula2: ${validation.formula2}</p>`;
            output += `<p>Ignore blank: ${validation.ignoreBlank}</p>`;

            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```


## Artículos relacionados

- [Validación de datos](/cells/es/javascript-cpp/data-validation/)
