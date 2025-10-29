---
title: Signer numériquement un projet de code VBA avec un certificat en utilisant JavaScript via C++
linktitle: Signer numériquement un projet de code VBA avec un certificat
type: docs
weight: 110
url: /fr/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Apprenez comment signer numériquement un projet de code VBA avec un certificat en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Vous pouvez signer numériquement votre projet de code VBA avec Aspose.Cells en utilisant sa méthode [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-). Suivez ces étapes pour vérifier si votre fichier Excel est signé numériquement avec un certificat.

- Cliquez sur **Visual Basic** dans l'onglet **Développeur** pour ouvrir **l'EDI VBA (Environnement de Développement Intégré Visual Basic pour Applications)**
- Cliquez sur **Outils** > **Signatures numériques...** dans **l'EDI VBA (Environnement de Développement Intégré Visual Basic pour Applications)**

et il montrera le **Formulaire de Signature Numérique** indiquant si le document est signé numériquement avec un certificat ou non.

{{% /alert %}} 

## **Signer numériquement un projet de code VBA avec un certificat en JavaScript**

Le code d'exemple suivant illustre comment utiliser la méthode [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-). Voici les fichiers d'entrée et de sortie du code d'exemple. Vous pouvez utiliser n'importe quel fichier Excel et tout certificat pour tester ce code.

- [Fichier Excel source](5115028.xlsm) utilisé dans le code d'exemple.
- [Fichier pfx de l'exemple](5115039.pfx) pour créer une signature numérique. Veuillez l'installer sur votre ordinateur pour exécuter ce code. Son mot de passe est 1234.
- [Fichier Excel de sortie](5115029.xlsm) généré par le code d'exemple.

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
