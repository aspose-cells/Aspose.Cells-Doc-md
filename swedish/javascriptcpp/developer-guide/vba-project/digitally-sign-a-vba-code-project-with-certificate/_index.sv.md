---
title: Signera ett VBA kodprojekt digitalt med certifikat med JavaScript via C++
linktitle: Signera digitalt ett VBA kodprojekt med certifikat
type: docs
weight: 110
url: /sv/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Lär dig hur du digitalt signerar ett VBA kodprojekt med ett certifikat med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Du kan digitalt signera ditt VBA-kodprojekt med Aspose.Cells med dess [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-)-metod. Följ dessa steg för att kontrollera om din Excel-fil är digitalt signerad med ett certifikat.

- Klicka på **Visual Basic** från fliken **Utvecklare** för att öppna **Visual Basic for Applications IDE**
- Klicka på **Verktyg** > **Digitala signaturer...** av **Visual Basic for Applications IDE**

och det kommer att visa **Digital Signature Form** och visa om dokumentet är signerat digitalt med ett certifikat eller inte.

{{% /alert %}} 

## **Digitalt signera ett VBA-kodprojekt med certifikat i JavaScript**

Följande exempel illustrerar hur du använder [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-)-metoden. Här är in- och utdatafiler för exempelkoden. Du kan använda vilken Excel-fil som helst och vilket certifikat som helst för att testa denna kod.

- [Källa Excel-fil](5115028.xlsm) använd i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa digital signatur. Installera den på din dator för att köra denna kod. Dess lösenord är 1234.
- [Utdatat Excel-fil](5115029.xlsm) genererad av exempelkoden.

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
