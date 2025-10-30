---
title: Unisci o disseunisci l intervallo di celle con JavaScript tramite C++
linktitle: Unisci o separa un intervallo di celle
type: docs
weight: 190
url: /it/javascript-cpp/merge-or-unmerge-range-of-cells/
description: Unisci e disuno le celle in un intervallo in Excel con JavaScript tramite codice C++.
keywords: Unisci e disunisci celle in JavaScript in un intervallo, unisci e disunisci celle in un intervallo, unisci e disunisci celle in intervallo con JavaScript, unisci e disunisci celle in intervallo usando JavaScript, unisci e disunisci celle in Excel usando JavaScript, unisci e disunisci celle in Excel con JavaScript, JavaScript unisci e disunisci celle in Excel, JavaScript unisci celle in Excel, JavaScript disunisci celle in Excel, unisci celle in intervallo con JavaScript
---

{{% alert color="primary" %}}

Puoi utilizzare Aspose.Cells per unire o dividere un intervallo di celle. Aspose.Cells fornisce i metodi [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) e [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) a questo scopo. Questo articolo spiega come unire un intervallo di celle in una singola cella.

{{% /alert %}}

## **Esempio**

Il seguente esempio di codice crea prima un intervallo - A1:D4 - quindi unisce le celle dell'intervallo in una singola cella usando il metodo [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--). Analogamente, puoi suddividere le celle creando un intervallo e chiamando il metodo [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--).

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
