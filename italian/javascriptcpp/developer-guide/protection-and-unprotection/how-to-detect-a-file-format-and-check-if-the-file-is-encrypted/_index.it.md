---
title: Come rilevare il formato di un file e verificare se il file è crittografato con JavaScript via C++
linktitle: Come individuare un formato di file e verificare se il file è criptato
type: docs
weight: 2700
url: /it/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Impara come rilevare il formato di un file e verificare se un file è crittografato usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
A volte è necessario rilevare il formato di un file prima di aprirlo perché l'estensione del file non garantisce che il contenuto sia appropriato. Il file potrebbe essere crittografato (protetto da password) e quindi non può essere letto direttamente, o potrebbe essere meglio non leggerlo. Aspose.Cells for JavaScript via C++ fornisce il metodo statico [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) e alcune API pertinenti che puoi usare per elaborare documenti.  
{{% /alert %}}  

Il seguente codice di esempio illustra come individuare un formato di file (utilizzando il percorso del file) e verificare la sua estensione. È anche possibile determinare se il file è criptato.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells File Format Detection Example</h1>
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

            // Detect file format
            const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(arrayBuffer));

            // Gets the detected load format (converted getter -> property)
            const extension = AsposeCells.FileFormatUtil.loadFormatToExtension(info.loadFormat);
            const encrypted = info.isEncrypted;

            console.log("The spreadsheet format is: " + extension);
            console.log("The file is encrypted: " + encrypted);

            resultDiv.innerHTML = `<p>The spreadsheet format is: <strong>${extension}</strong></p>
                                   <p>The file is encrypted: <strong>${encrypted}</strong></p>`;
        });
    </script>
</html>
```
