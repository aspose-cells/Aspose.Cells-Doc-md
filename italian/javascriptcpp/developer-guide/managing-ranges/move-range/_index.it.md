---
title: Sposta un intervallo di celle in un foglio di lavoro con JavaScript tramite C++
linktitle: Sposta intervallo di celle in un foglio di lavoro
type: docs
weight: 370
url: /it/javascript-cpp/move-range-of-cells-in-a-worksheet/
description: Impara come spostare un intervallo di celle in un foglio di lavoro usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}
Questo articolo mostra come spostare un intervallo di celle in un foglio di lavoro.
{{% /alert %}}

## **Sposta Intervallo di Celle in un Foglio di Lavoro**
Il codice di esempio utilizza un file modello per dimostrare il compito.

**Il file di input**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Si prega di vedere il file generato seguente con l'intervallo da A1:B5 spostato in C1:D5.

**Il file di output

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
