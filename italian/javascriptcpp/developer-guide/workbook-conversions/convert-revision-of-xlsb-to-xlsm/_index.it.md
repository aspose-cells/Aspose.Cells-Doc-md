---
title: Converti la revisione di XLSB in XLSM con JavaScript tramite C++
linktitle: Convertire la Revisione da XLSB a XLSM
type: docs
weight: 290
url: /it/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Impara come convertire completamente le revisioni dei file XLSB in formato XLSM usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta ora la conversione completa delle revisioni dei file XLSB in file XLSM. Le revisioni si trovano all’interno del percorso \xl\revisions. Puoi visualizzarle modificando l’estensione del tuo file XLSB in ZIP. Il percorso \xl\revisions contiene file con estensione .bin.

Quando converti il tuo file XLSB in un file XLSM usando Aspose.Cells, questi file .bin vengono convertiti correttamente in file .xml come mostrato in queste due schermate.

{{% /alert %}}

 Il seguente esempio di codice mostra come convertire il file XLSB in formato XLSM usando Aspose.Cells for JavaScript tramite C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
