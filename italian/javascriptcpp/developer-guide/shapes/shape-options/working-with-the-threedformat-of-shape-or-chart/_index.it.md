---
title: Lavorare con il ThreeDFormat di Shape o Chart con JavaScript tramite C++
linktitle: Lavorare con il ThreeDFormat della forma o del grafico
type: docs
weight: 250
url: /it/javascript-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for JavaScript tramite C++ fornisce la proprietà [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) assieme alla classe [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) per lavorare con il formato 3D di forma o grafico. La classe [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) contiene diverse proprietà che possono essere impostate per ottenere risultati differenti secondo i requisiti dell'applicazione.

## **Lavorare con il ThreeDFormat della forma o del grafico**
Il seguente esempio di codice carica il [file excel di origine](5115419.xlsx) e accede alla prima forma nel primo foglio di lavoro impostando le sottopropietà della proprietà [Forma.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) e poi salva il workbook nel [file excel di output](5115410.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Apply 3D Format Example</title>
    </head>
    <body>
        <h1>Apply 3D Format to Shape</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const ws = workbook.worksheets.get(0);

            const sh = ws.shapes.get(0);

            const n3df = sh.threeDFormat;
            n3df.contourWidth = 17;
            n3df.extrusionHeight = 32;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">3D formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
