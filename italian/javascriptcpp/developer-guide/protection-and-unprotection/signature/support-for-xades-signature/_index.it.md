---
title: Supporto per la firma XAdES con JavaScript tramite C++
linktitle: Supporto per la firma XAdES
type: docs
weight: 110
url: /it/javascript-cpp/support-for-xades-signature/
description: Questo articolo descrive il supporto per la firma XAdES usando JavaScript tramite C++ con Aspose.Cells.
keywords: Supporto per la firma XAdES JavaScript tramite C++, come firmare Excel con firma XAdES JavaScript tramite C++, come aggiungere una firma XAdES JavaScript tramite C++.  
---  

## **Introduzione**  

Aspose.Cells offre supporto per la firma dei fogli di lavoro con XAdES Signature. Per questo, l'API fornisce la classe [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature) e l'enumerazione [**XAdESType**](https://reference.aspose.com/cells/javascript-cpp/xadestype).  

## **Come Aggiungere la Firma XAdES per Excel**  

Il seguente esempio di codice dimostra l'uso della classe [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature) per firmare il foglio di lavoro [source](101089323.xlsx).  

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
