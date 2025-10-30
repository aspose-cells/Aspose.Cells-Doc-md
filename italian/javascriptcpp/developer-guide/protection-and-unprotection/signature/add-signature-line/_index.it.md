---
title: Aggiungi linea di firma al foglio di lavoro con JavaScript tramite C++
linktitle: Aggiungi linea di firma al foglio di lavoro
type: docs
weight: 200
url: /it/javascript-cpp/add-signature-line/
description: Questo articolo descrive come aggiungere una linea di firma al foglio di lavoro utilizzando codice JavaScript con Aspose.Cells for JavaScript tramite C++.
keywords: Aggiungi linea di firma al foglio di lavoro JavaScript tramite C++, come aggiungere una linea di firma al foglio di lavoro JavaScript tramite C++, come aggiungere la linea di firma al foglio di lavoro JavaScript tramite C++.
---

## **Introduzione**

Aspose.Cells fornisce la proprietà [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) per aggiungere la linea di firma del foglio di lavoro.

## **Come Aggiungere una Linea di Firma al Foglio di Lavoro**

Il codice di esempio seguente dimostra come usare la proprietà [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) per aggiungere la linea di firma del foglio di lavoro. La schermata mostra l'effetto del codice di esempio sul file Excel dopo l'esecuzione.

![todo:image_alt_text](add-signature-line.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Signature Line</title>
    </head>
    <body>
        <h1>Signature Line Example</h1>
        <p>Optional: select an existing Excel file to add the signature line to. Otherwise a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select a PFX certificate file (required):</p>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <button id="runExample">Add Signature Line and Sign Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, SignatureLine, DigitalSignature, DigitalSignatureCollection } = AsposeCells;

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
            const certInput = document.getElementById('certInput');
            const resultDiv = document.getElementById('result');

            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a PFX certificate file.</p>';
                return;
            }

            const certFile = certInput.files[0];
            const certArrayBuffer = await certFile.arrayBuffer();
            const certBytes = new Uint8Array(certArrayBuffer);

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create and configure signature line
            const signatureLine = new SignatureLine();
            signatureLine.signer = "Aspose.Cells";
            signatureLine.title = "signed by Aspose.Cells";

            // Access first worksheet and add signature line
            const worksheet = workbook.worksheets.get(0);
            worksheet.shapes.addSignatureLine(1, 1, signatureLine);

            // Create digital signature from certificate bytes
            const signature = new DigitalSignature(certBytes, "aspose", "test Microsoft Office signature line", new Date());

            // Add signature to collection and assign to workbook
            const dsCollection = new DigitalSignatureCollection();
            dsCollection.add(signature);
            workbook.digitalSignature = dsCollection;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'signatureLine.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Signature line added and workbook signed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
