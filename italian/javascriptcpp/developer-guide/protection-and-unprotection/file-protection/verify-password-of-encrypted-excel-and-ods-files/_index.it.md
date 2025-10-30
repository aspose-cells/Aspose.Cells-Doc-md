---
title: Verifica la password di file criptati con JavaScript via C++
linktitle: Verifica password dei file crittografati
type: docs
weight: 10
url: /it/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verifica la password di file Excel criptati (xlsx, xlsb, xls, xlsm) e Open Office (ODS) usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Se i file Excel (xlsx, xlsb, xls, xlsm) e Open Office (ODS) sono bloccati con una password, Aspose supporta la verifica semplice della password senza analizzare dati specifici dei file.  
{{% /alert %}}  

## **Verifica la password del file crittografato**  

Per verificare la password del file criptato, Aspose.Cells for JavaScript via C++ fornisce il metodo [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). Questo metodo accetta due parametri, il flusso del file e la password che deve essere verificata.  
Il seguente frammento di codice dimostra l'uso del metodo [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) per verificare se la password fornita è valida o meno.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```
