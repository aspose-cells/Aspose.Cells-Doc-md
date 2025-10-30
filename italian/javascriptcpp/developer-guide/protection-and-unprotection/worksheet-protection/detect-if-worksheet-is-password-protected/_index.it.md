---
title: Rilevare se il Foglio di lavoro è Proteggo da Password con JavaScript tramite C++
linktitle: Scoprire se il foglio di lavoro è protetto da password
type: docs
weight: 360
url: /it/javascript-cpp/detect-if-worksheet-is-password-protected/
description: Impara come rilevare se un foglio di lavoro è protetto da password usando Aspose.Cells for JavaScript tramite C++. 
keywords: Rilevare la Protezione con Password del Foglio di Lavoro JavaScript tramite C++, Verificare se il Foglio di Lavoro è Protetto da Password JavaScript tramite C++, Aspose.Cells for JavaScript tramite C++
---

{{% alert color="primary" %}}

È possibile proteggere i libri di lavoro e i fogli di lavoro separatamente. Ad esempio, un foglio di calcolo può contenere uno o più fogli protetti da password, tuttavia, il libro di lavoro stesso può o meno essere protetto. Le API Aspose.Cells forniscono i mezzi per rilevare se un determinato foglio di lavoro è protetto da password o no. Questo articolo dimostra l'uso di Aspose.Cells for JavaScript tramite API C++ per ottenere lo stesso.

{{% /alert %}}

Aspose.Cells for JavaScript via C++ ha esposto la proprietà [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) per rilevare se un foglio di lavoro è protetto da password o no. La proprietà di tipo booleana [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) restituisce **true** se [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) è protetto da password e **false** se non lo è.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```
