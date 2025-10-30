---
title: Imposta il colore della scheda del foglio di lavoro con JavaScript tramite C++
linktitle: Impostare il Colore della Scheda del Foglio di Lavoro
type: docs
weight: 120
url: /it/javascript-cpp/set-worksheet-tab-color/
description: Questo articolo dimostra un esempio di codice che imposta programmaticamente il colore della scheda del foglio Excel usando JavaScript tramite C++.
keywords: imposta il colore della scheda Excel JavaScript tramite C++, codice per impostare il colore della scheda Excel con JavaScript tramite C++
---

{{% alert color="primary" %}}

Aspose.Cells consente di cambiare il colore delle singole schede del foglio di lavoro per renderle evidenti rispetto alle altre. Ad esempio, è possibile rendere Rosso le Spese, Verde le Vendite, Blu i Beni, ecc.

{{% /alert %}}
## **Impostare il Colore della Scheda del Foglio di Lavoro con Microsoft Excel**
1. Fare clic con il pulsante destro del mouse su una scheda nell'insieme di schede nella parte inferiore della scheda corrente.
1. Seleziona **Colore scheda**.
1. Seleziona un colore dalla tavolozza.
1. Fai clic su **OK**.
## **Impostazione colore scheda foglio di calcolo con Aspose.Cells**
Il codice di esempio di seguito mostra come impostare il colore della scheda con Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
