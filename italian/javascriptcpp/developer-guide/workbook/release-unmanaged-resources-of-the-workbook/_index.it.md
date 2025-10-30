---
title: Rilascia risorse non gestite del Workbook con JavaScript tramite C++
linktitle: Rilascia le risorse non gestite del libro di lavoro
type: docs
weight: 310
url: /it/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: Impara come rilasciare risorse non gestite dell oggetto Workbook usando Aspose.Cells for JavaScript tramite C++. 
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il metodo [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) per rilasciare le risorse non gestite dell’oggetto [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Il pattern dispose viene usato solo per oggetti che accedono a risorse non gestite, come handle di file e pipe, handle del registro di sistema, handle di attesa o puntatori a blocchi di memoria non gestita. Questo perché il garbage collector è molto efficiente nel recuperare gli oggetti gestiti inutilizzati, ma non può recuperare gli oggetti non gestiti.

{{% /alert %}}

L’oggetto [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) ora implementa l’interfaccia *System.IDisposable* che ha un singolo metodo [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--). Puoi chiamare direttamente il metodo [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) oppure usare la dichiarazione *Using* per chiamarlo automaticamente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
