---
title: Ottieni l ID univoco del foglio di lavoro con JavaScript tramite C++
linktitle: Ottieni l ID univoco del foglio di lavoro
type: docs
weight: 190
url: /it/javascript-cpp/get-worksheet-unique-id/
description: Questo articolo mostra come ottenere l ID univoco del foglio di lavoro Excel usando la libreria JavaScript e l API C++ programmaticamente.
keywords: ID univoco del foglio di lavoro Excel JavaScript tramite C++, ID univoco del foglio di lavoro JavaScript tramite C++
---

## **Ottieni l'ID univoco del foglio di lavoro**

Aspose.Cells for JavaScript tramite C++ fornisce la capacità di ottenere l'ID univoco di un foglio di lavoro usando la proprietà [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--). Il seguente blocco di codice dimostra l'uso della proprietà [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--) per stampare l'ID univoco di un foglio di lavoro. Il codice utilizza questo [file Excel di esempio](105480213.xlsx).

### Codice Sorgente

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Worksheet Unique Id Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Unique Id
            const uniqueId = worksheet.uniqueId;
            console.log("Unique Id: " + uniqueId);

            document.getElementById('result').innerHTML = '<p style="color: green;">Unique Id: ' + uniqueId + '</p>';
        });
    </script>
</html>
```
