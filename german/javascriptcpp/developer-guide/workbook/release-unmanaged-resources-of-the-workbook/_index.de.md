---
title: unmanaged Ressourcen des Arbeitsbuchs mit JavaScript über C++ freigeben
linktitle: Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe
type: docs
weight: 310
url: /de/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: Erfahren Sie, wie Sie die unmanaged Ressourcen des Arbeitsbuch Objekts mit Aspose.Cells for JavaScript über C++ freigeben. 
---

{{% alert color="primary" %}}

Aspose.Cells stellt die [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) Methode bereit, um die nicht verwalteten Ressourcen des [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) Objekts freizugeben. Das Dispose-Muster wird nur für Objekte verwendet, die nicht verwaltete Ressourcen wie Dateien, Pipe-Handles, Registry-Handles, Warte-Handles oder Zeiger auf Blockspeicher zugreifen. Dies liegt daran, dass der Garbage Collector sehr effizient bei der Rückgewinnung ungenutzter verwalteter Objekte ist, aber nicht in der Lage ist, nicht verwaltete Objekte zurückzuholen.

{{% /alert %}}

Das [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) Objekt implementiert jetzt die *System.IDisposable* Schnittstelle, die eine einzelne Methode [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) hat. Sie können entweder direkt die [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) Methode aufrufen oder den *Using* Befehl verwenden, um diese Methode automatisch aufzurufen.

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
