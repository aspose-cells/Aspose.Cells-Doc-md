---
title: Stöd för XAdES signatur med JavaScript via C++
linktitle: Stöd för XAdES signatur
type: docs
weight: 110
url: /sv/javascript-cpp/support-for-xades-signature/
description: Denna artikel beskriver stödet för XAdES signatur med JavaScript via C++ med Aspose.Cells.
keywords: Stöd för XAdES signatur JavaScript via C++, Hur man signerar Excel med XAdES signatur JavaScript via C++, Hur man lägger till XAdES signatur JavaScript via C++.  
---  

## **Introduktion**  

Aspose.Cells ger stöd för att signera arbetsböcker med XAdES-signatur. För detta tillhandahåller API:n klassen [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature) och enumeneringen [**XAdESType**](https://reference.aspose.com/cells/javascript-cpp/xadestype).  

## **Hur man lägger till XAdES-signatur för Excel**  

Följande kodstycke visar användningen av klassen [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature) för att signera [källfilen](101089323.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells XAdES Signature Example</title>
    </head>
    <body>
        <h1>XAdES Digital Signature Example</h1>
        <p>
            Select an Excel file and a PFX certificate file (.pfx). Then click "Run Example" to sign the workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="pfxInput" accept=".pfx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature, DigitalSignatureCollection, XAdESType, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!pfxInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a PFX certificate file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const pfxFile = pfxInput.files[0];

            // Read Excel file
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Read PFX file
            const pfxArrayBuffer = await pfxFile.arrayBuffer();
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // Create DigitalSignature using PFX bytes, password, signature name and signing time
            const signature = new DigitalSignature(pfxBytes, "aspose", "testXAdES", new Date());
            // Set XAdES type property (converted from setXAdESType)
            signature.xAdESType = AsposeCells.XAdESType.XAdES;

            const dsCollection = new DigitalSignatureCollection();
            dsCollection.add(signature);

            // Assign digital signature collection to workbook (converted from setDigitalSignature)
            workbook.digitalSignature = dsCollection;

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'XAdESSignatureSupport_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook signed successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
