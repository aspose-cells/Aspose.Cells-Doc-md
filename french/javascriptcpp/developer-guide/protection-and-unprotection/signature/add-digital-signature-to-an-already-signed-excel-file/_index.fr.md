---
title: Ajouter une signature numérique à un fichier Excel déjà signé avec JavaScript via C++
linktitle: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Cet article décrit comment ajouter une signature numérique à un fichier Excel déjà signé en utilisant JavaScript avec Aspose.Cells for JavaScript via C++.
keywords: Ajouter une signature numérique à un fichier Excel déjà signé, comment ajouter une signature numérique à un document Excel déjà signé en utilisant JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for JavaScript via C++ fournit la méthode [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) que vous pouvez utiliser pour ajouter une signature numérique à un fichier Excel déjà signé.

{{% alert color="primary" %}}

Veuillez noter qu'en ajoutant une signature numérique à un document Excel déjà signé, si le document original est un document généré par Aspose.Cells, cela fonctionne bien. Mais si le document original est généré par d'autres moteurs (par exemple Microsoft Excel, etc.), Aspose.Cells ne peut pas conserver le fichier identique après le chargement et la sauvegarde, ce qui rendra la signature d'origine invalide.

{{% /alert %}}

## **Comment ajouter une signature numérique à un fichier Excel déjà signé**

Le code d'exemple suivant montre comment utiliser la méthode [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) pour ajouter une signature numérique à un fichier Excel déjà signé. Veuillez vérifier le [fichier Excel d'exemple](50528280.xlsx) utilisé dans ce code. Ce fichier est déjà signé numériquement. Vérifiez le [fichier Excel de sortie](50528281.xlsx) généré par le code. Nous avons utilisé le certificat de démonstration nommé [AsposeDemo.pfx](50528279.pfx), qui a un mot de passe **aspose**. La capture d'écran montre l'effet du code d'exemple sur le fichier Excel de référence après exécution.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Code d'exemple**

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
