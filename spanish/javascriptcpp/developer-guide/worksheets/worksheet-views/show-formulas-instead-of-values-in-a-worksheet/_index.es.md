---
title: Mostrar fórmulas en lugar de valores en una hoja de cálculo con JavaScript a través de C++
linktitle: Mostrar Fórmulas en lugar de Valores en una Hoja de Trabajo
type: docs
weight: 20
url: /es/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Este artículo proporciona ejemplo de código para usar la API de JavaScript a través de C++ para mostrar programáticamente fórmulas en lugar de valores en una hoja de cálculo o libro de Excel.
---

{{% alert color="primary" %}}

Es posible mostrar fórmulas en lugar de valores calculados en Microsoft Excel usando la opción **Mostrar fórmulas** desde la cinta **Fórmulas**. Cuando se muestran las fórmulas, Microsoft Excel muestra fórmulas en la hoja de cálculo. Puedes lograr lo mismo usando Script Aspose.Cells for Java a través de C++.

{{% /alert %}}

Aspose.Cells proporciona una propiedad [**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--). Establecer esto en **true** hace que Microsoft Excel muestre fórmulas.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Show Formulas Example</title>
    </head>
    <body>
        <h1>Show Formulas Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Show formulas of the worksheet
            worksheet.showFormulas = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'source.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas are now visible. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
