---
title: Firma digitalmente un progetto di codice VBA con certificato usando JavaScript via C++
linktitle: Firma digitalmente un progetto di codice VBA con certificato
type: docs
weight: 110
url: /it/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Impara come firmare digitalmente un progetto di codice VBA con un certificato usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Puoi firmare digitalmente il progetto di codice VBA usando Aspose.Cells con il suo metodo [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-). Segui questi passaggi per verificare se il file Excel è firmato digitalmente con un certificato.

- Fare clic su **Visual Basic** dalla scheda **Sviluppo** per aprire l'**IDE di Visual Basic for Applications**
- Fare clic su **Strumenti** > **Firme digitali...** dell' **IDE di Visual Basic for Applications**

e verrà mostrato il **Modulo di firma digitale** che indica se il documento è firmato digitalmente con un certificato o meno.

{{% /alert %}} 

## **Firma digitalmente un progetto di codice VBA con certificato in JavaScript**

Il seguente esempio di codice illustra come utilizzare il metodo [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-). Ecco i file di input e output del codice di esempio. Puoi usare qualsiasi file Excel e qualsiasi certificato per testare questo codice.

- [File Excel di origine](5115028.xlsm) utilizzato nel codice di esempio.
- [File pfx di esempio](5115039.pfx) per creare una firma digitale. Si prega di installarlo sul computer per eseguire questo codice. La password è 1234.
- [File Excel di output](5115029.xlsm) generato dal codice di esempio.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sign VBA Project with Digital Signature</h1>
        <div>
            <label for="fileInput">Select Excel Workbook (.xlsm): </label>
            <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        </div>
        <div>
            <label for="pfxInput">Select PFX Certificate (.pfx): </label>
            <input type="file" id="pfxInput" accept=".pfx" />
        </div>
        <button id="runExample">Sign VBA Project</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature } = AsposeCells;

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
            const pfxInput = document.getElementById('pfxInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length || !pfxInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both the Excel workbook and the PFX certificate files.</p>';
                return;
            }

            const workbookFile = fileInput.files[0];
            const pfxFile = pfxInput.files[0];

            // Read files as ArrayBuffer
            const [wbArrayBuffer, pfxArrayBuffer] = await Promise.all([
                workbookFile.arrayBuffer(),
                pfxFile.arrayBuffer()
            ]);

            // Prepare bytes
            const wbBytes = new Uint8Array(wbArrayBuffer);
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // Set Digital Signature parameters
            const password = "1234";
            const comment = "Signing Digital Signature using Aspose.Cells";
            const digitalSignature = new DigitalSignature(pfxBytes, password, comment, new Date());

            // Create workbook object from excel file
            const workbook = new Workbook(wbBytes);

            // Sign VBA Code Project with Digital Signature
            workbook.vbaProject.sign(digitalSignature);

            // Save the workbook as XLSM
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignVbaProjectWithCertificate.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Workbook signed successfully! Click the download link to download the signed workbook.</p>';
        });
    </script>
</html>
```
