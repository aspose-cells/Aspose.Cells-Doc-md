---
title: Aggiungi firma digitale a un file Excel già firmato con JavaScript via C++
linktitle: Aggiungere firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Questo articolo descrive come aggiungere una firma digitale a un file Excel già firmato utilizzando JavaScript con Aspose.Cells for JavaScript tramite C++.
keywords: Aggiungi Firma Digitale a un file Excel già firmato, Come aggiungere una firma digitale a un documento Excel già firmato usando JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**

 Aspose.Cells for JavaScript tramite C++ fornisce il metodo [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) che puoi usare per aggiungere una firma digitale a un file Excel già firmato.

{{% alert color="primary" %}}

Si prega di notare che durante l'aggiunta di una firma digitale a un documento Excel già firmato, se il documento originale è stato generato da Aspose.Cells, tutto funziona correttamente. Ma se il documento originale è stato generato da altri motori (es. Microsoft Excel), Aspose.Cells non può mantenere il file invariato dopo averlo caricato e risalvato, il che invalidarà la firma originale.

{{% /alert %}}

## **Come Aggiungere una Firma Digitale a un Documento Excel Già Firmato**

Il codice di esempio seguente dimostra come usare il metodo [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) per aggiungere una firma digitale a un file Excel già firmato. Verifica il [file Excel di esempio](50528280.xlsx) usato in questo esempio. Questo file è già firmato digitalmente. Verifica il [file Excel di output](50528281.xlsx) generato dal codice. Nel codice abbiamo usato il certificato demo chiamato [AsposeDemo.pfx](50528279.pfx), con password **aspose**. La schermata mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Digital Signature Example</title>
    </head>
    <body>
        <h1>Add Digital Signature to Workbook</h1>
        <p>Select an Excel file and a PFX certificate, enter the certificate password, then click "Add Digital Signature".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <br/><br/>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <label for="certPassword">Certificate Password:</label>
        <input type="password" id="certPassword" value="aspose" />
        <br/><br/>
        <button id="runExample">Add Digital Signature</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, DigitalSignature, DigitalSignatureCollection, SaveFormat, Utils } = AsposeCells;

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
            const passwordInput = document.getElementById('certPassword');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            // Read files as ArrayBuffer
            const excelFile = fileInput.files[0];
            const certFile = certInput.files[0];
            const certPassword = passwordInput.value;

            const excelArrayBuffer = await excelFile.arrayBuffer();
            const certArrayBuffer = await certFile.arrayBuffer();

            // Instantiate Workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(excelArrayBuffer));

            // Create the digital signature collection
            const dsCollection = new DigitalSignatureCollection();

            // Create new digital signature and add it in digital signature collection
            // Using certificate bytes (Uint8Array), password, comment and signing date
            const signature = new DigitalSignature(new Uint8Array(certArrayBuffer), certPassword, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
            dsCollection.add(signature);

            // Add digital signature collection inside the workbook
            workbook.addDigitalSignature(dsCollection);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignedByCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Digitally Signed Excel File';

            // Dispose the workbook
            workbook.dispose();

            resultDiv.innerHTML = '<p style="color: green;">Digital signature added successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
