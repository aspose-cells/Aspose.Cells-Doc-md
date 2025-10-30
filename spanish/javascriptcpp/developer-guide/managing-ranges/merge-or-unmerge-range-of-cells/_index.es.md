---
title: Combinar o Deshacer la combinación de un rango de celdas con JavaScript vía C++
linktitle: Combinar o dividir rango de celdas
type: docs
weight: 190
url: /es/javascript-cpp/merge-or-unmerge-range-of-cells/
description: Fusionar y deshacer la fusión de celdas en un rango en Excel con JavaScript mediante código C++.
keywords: Fusionar y deshacer la fusión de celdas en JavaScript en un rango, fusionar y deshacer la fusión de celdas en rango, fusionar y deshacer celdas en rango con JavaScript, fusionar y deshacer celdas en rango usando JavaScript, fusionar y deshacer celdas en Excel usando JavaScript, fusionar y deshacer celdas en Excel con JavaScript, JavaScript fusiona y deshace la fusión de celdas en Excel, JavaScript fusiona celdas en Excel, JavaScript deshace la fusión de celdas en Excel, fusionar celdas en rango con JavaScript
---

{{% alert color="primary" %}}

Puede utilizar Aspose.Cells para combinar o dividir un rango de celdas. Aspose.Cells ofrece los métodos [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) y [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) para este propósito. Este artículo explica cómo combinar un rango de celdas en una sola celda.

{{% /alert %}}

## **Ejemplo**

El siguiente código de ejemplo primero crea un rango - A1:D4 - luego combina las celdas del rango en una sola usando el método [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--). De manera similar, puedes dividir celdas creando un rango y llamando al método [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create and Merge Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeInitialized = false;
        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeInitialized = true;
            runButton.disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait.</p>';
                return;
            }

            // Creating a workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a range
            const range = worksheet.cells.createRange("A1:D4");

            // Merge range into a single cell
            range.merge();

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range merged successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
