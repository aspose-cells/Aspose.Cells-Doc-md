---
title: Exporter le certificat VBA vers un fichier ou un flux avec JavaScript via C++
linktitle: Exporter le certificat VBA dans un fichier ou un flux
type: docs
weight: 90
url: /fr/javascript-cpp/export-vba-certificate-to-file-or-stream/
description: Apprenez comment exporter un certificat numérique VBA vers un fichier ou un flux en utilisant Aspose.Cells for JavaScript via C++. Accédez aux données brutes des certificats numériques VBA.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter un certificat numérique VBA vers un flux tel qu'un fichier ou un flux de mémoire. Vous pouvez accéder aux données brutes du certificat numérique VBA en utilisant la propriété [**VbaProject.certRawData**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#certRawData--).

{{% /alert %}}

## **Exporter le certificat VBA vers un fichier ou un flux en JavaScript**

Veuillez consulter le code d'exemple suivant qui enregistre les données brutes du certificat VBA dans un fichier. Vous pouvez télécharger le [fichier Excel d'exemple utilisé dans ce code](5115031.xlsm) à partir du lien fourni.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract VBA Project Certificate</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve bytes data of Digital Certificate of VBA Project
            const certBytes = workbook.vbaProject.certRawData;

            // Convert to Uint8Array and create a Blob for download
            const certUint8 = Uint8Array.from(certBytes);
            const blob = new Blob([certUint8]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Cert_out_';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Certificate';

            document.getElementById('result').innerHTML = '<p style="color: green;">Certificate extracted successfully! Click the download link to save the certificate.</p>';
        });
    </script>
</html>
```
