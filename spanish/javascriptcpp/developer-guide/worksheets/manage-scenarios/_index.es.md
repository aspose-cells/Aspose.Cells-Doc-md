---
title: Crear, manipular o eliminar escenarios de hojas de cálculo con JavaScript vía C++
linktitle: Gestionar Escenarios
type: docs
weight: 190
url: /es/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Aprenda cómo crear, manipular o eliminar escenarios de hojas de cálculo de Excel programáticamente usando la API de JavaScript a través de C++.
keywords: Crear escenario de hoja de cálculo JavaScript vía C++, eliminar escenario de hoja de cálculo JavaScript vía C++, manipular escenario de hoja de cálculo JavaScript vía C++
---

{{% alert color="primary" %}}

A veces, necesitas crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un modelo de 'qué pasaría si' que incluye celdas de entrada variables vinculadas por una o más fórmulas. Antes de crear un escenario, diseña la hoja de cálculo para que contenga al menos una fórmula que dependa de celdas en las que se puedan insertar diferentes valores. El siguiente ejemplo muestra cómo crear y eliminar escenarios de una hoja de cálculo en un libro mediante las API de Aspose.Cells.

{{% /alert %}}

Aspose.Cells ofrece algunas clases útiles, por ejemplo, [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection) y [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell). También proporciona la propiedad [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--). El código de ejemplo a continuación abre un archivo XLSX que contiene algunos escenarios y elimina un escenario existente. También añade un nuevo escenario en la hoja de cálculo antes de guardar el archivo Excel. El ejemplo usa un archivo de plantilla muy simple que contiene un escenario.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Scenarios Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Scenarios Example</h1>
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

            // Instantiate the Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            if (worksheet.scenarios.count > 0) {
                // Remove the existing first scenario from the sheet
                worksheet.scenarios.removeAt(0);
            }

            // Create a scenario
            const i = worksheet.scenarios.add("MyScenario");
            // Get the scenario
            const scenario = worksheet.scenarios.get(i);
            // Add comment to it
            scenario.comment = "Test scenario is created.";
            // Get the input cells for the scenario
            const sic = scenario.inputCells;
            // Add the scenario on B4 (as changing cell) with default value
            sic.add(3, 1, "1100000");

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outBk_scenarios1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Process completed successfully. File ready for download.</p>';
        });
    </script>
</html>
```
