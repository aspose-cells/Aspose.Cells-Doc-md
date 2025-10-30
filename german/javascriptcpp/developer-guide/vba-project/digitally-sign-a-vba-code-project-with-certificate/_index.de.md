---
title: Signieren Sie ein VBA Code Projekt digital mit Zertifikat in JavaScript über C++
linktitle: Digitale Signatur eines VBA Codeprojekts mit Zertifikat
type: docs
weight: 110
url: /de/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Erfahren Sie, wie Sie ein VBA Code Projekt mit einem Zertifikat digital signieren, mit Aspose.Cells for JavaScript über C++.
---

{{% alert color="primary" %}}

Sie können Ihr VBA-Codeprojekt mit Aspose.Cells und seiner [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-) Methode digital signieren. Bitte folgen Sie diesen Schritten, um zu prüfen, ob Ihre Excel-Datei mit einem Zertifikat digital signiert ist.

- Klicken Sie auf **Visual Basic** im **Entwicklertools**-Tab, um die **Visual Basic for Applications-IDE** zu öffnen
- Klicken Sie auf **Extras** > **Digitale Signaturen...** des **Visual Basic for Applications IDE**

und es wird das **Digitale Signaturformular** anzeigen, das anzeigt, ob das Dokument digital mit einem Zertifikat signiert ist oder nicht.

{{% /alert %}} 

## **Digital Signieren eines VBA-Code-Projekts mit Zertifikat in JavaScript**

Der folgende Beispielcode zeigt, wie man die [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-)-Methode nutzt. Hier sind die Eingabe- und Ausgabedateien des Beispielcodes. Sie können jede Excel-Datei und jedes Zertifikat zum Testen dieses Codes verwenden.

- [Quell-Excel-Datei](5115028.xlsm), die im Beispielcode verwendet wird.
- [Beispiel-PFX-Datei](5115039.pfx) zur Erstellung einer digitalen Signatur. Bitte installieren Sie diese auf Ihrem Computer, um diesen Code auszuführen. Das Kennwort lautet 1234.
- [Ausgabe-Excel-Datei](5115029.xlsm), die vom Beispielcode generiert wurde.

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
