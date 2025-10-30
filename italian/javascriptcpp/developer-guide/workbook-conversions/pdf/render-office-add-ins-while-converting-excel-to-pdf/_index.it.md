---
title: Renderizza Add In di Office durante la conversione di Excel in PDF con JavaScript via C++
linktitle: Render Office Add Ins durante la conversione di Excel in PDF
type: docs
weight: 100
url: /it/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Possibili Scenari di Utilizzo**

In passato, Aspose.Cells non riusciva a rendere i Componenti Aggiuntivi di Office quando un file Excel veniva salvato in formato PDF. Ora Aspose.Cells li rende correttamente. Non è necessario utilizzare alcun metodo o proprietà speciale per rendere i Componenti Aggiuntivi di Office nel PDF di output. Basta salvare il file Excel in formato PDF e i componenti verranno renderizzati.

## **Render Office Add-Ins durante la conversione di Excel in PDF**

Il seguente esempio di codice salva il [file Excel di esempio](60489769.xlsx) che contiene gli componenti aggiuntivi di Office. Si prega di vedere il [PDF in output generato con la versione precedente, cioè 17.11](60489770.pdf) e il [PDF in output generato con la versione più recente, cioè 17.12 e successive](60489771.pdf). Il PDF della versione precedente è vuoto, mentre quello della versione più recente mostra l'Add-In di Office.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
