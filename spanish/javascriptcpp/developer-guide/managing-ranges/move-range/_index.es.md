---
title: Mover rango de celdas en una hoja de cálculo con JavaScript mediante C++
linktitle: Mover rango de celdas en una hoja de cálculo
type: docs
weight: 370
url: /es/javascript-cpp/move-range-of-cells-in-a-worksheet/
description: Aprenda cómo mover un rango de celdas en una hoja de cálculo usando Aspose.Cells for JavaScript con C++.
---

{{% alert color="primary" %}}
Este artículo muestra cómo mover un rango de celdas en una hoja de cálculo.
{{% /alert %}}

## **Mover rango de celdas en una hoja de cálculo**
El código de ejemplo utiliza un archivo de plantilla para demostrar la tarea.

**El archivo de entrada**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Por favor, vea el siguiente archivo generado con el rango A1:B5 movido a C1:D5.

**El archivo de salida**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiate the workbook object. Open the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const cells = workbook.worksheets.get(0).cells;

            const range = cells.createRange("A1", "B5");
            // move the range to right.
            range.moveTo(0, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
