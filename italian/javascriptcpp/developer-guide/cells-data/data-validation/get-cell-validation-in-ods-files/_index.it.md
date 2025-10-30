---
title: Ottieni la convalida della cella nei file ODS
type: docs
weight: 180
url: /it/javascript-cpp/get-cell-validation-in-ods-files/
description: Impara come ottenere la convalida della cella nei file ODS tramite lo script Aspose.Cells for Java tramite API C++.
keywords: Ottieni la validazione della cella JavaScript tramite C++, Ottieni la validazione della cella JavaScript tramite C++
---

## **Ottieni la Convalida Cellulare nei File ODS**  

Con Aspose.Cells for JavaScript via C++, puoi ottenere la convalida applicata a una cella nei file ODS. Per questo, l'API fornisce la proprietà [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/).  

Il seguente esempio di codice dimostra l'uso della proprietà [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) caricando il file [source ODS](101089354.ods) e leggendo la validazione della cella A9.  

### **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
