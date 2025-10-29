---
title: Chiffrer et déchiffrer les fichiers ODS avec JavaScript via C++
linktitle: Crypter et décrypter les fichiers ODS
type: docs
weight: 10
url: /fr/javascript-cpp/encrypt-and-decrypt-ods-files/
description: Protéger par mot de passe et chiffrer les fichiers ODS en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}
OpenOffice.org est une suite bureautique complète qui supporte la protection par mot de passe et le chiffrement de fichiers. Cependant, un fichier ODS chiffré peut uniquement être ouvert par OpenOffice après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS chiffré et pourrait afficher des messages d’avertissement. Les options de chiffrement ne sont pas applicables aux fichiers ODS contrairement à d’autres types de fichiers. 
Aspose.Cells vous permet de chiffrer et déchiffrer des fichiers ODS. Les fichiers ODS déchiffrés peuvent être ouverts dans Excel et OpenOffice.
{{% /alert %}}

## **Chiffrer avec OpenOffice Calc**
1. Sélectionnez **Enregistrer sous** et cliquez sur la case **Enregistrer avec mot de passe**.
1. Cliquez sur le bouton **Enregistrer**.
1. Saisissez votre mot de passe souhaité dans les champs **Entrer le mot de passe pour ouvrir** et **Confirmer le mot de passe** dans la fenêtre Définir le mot de passe qui s'ouvre. 
1. Cliquez sur le bouton **OK** pour enregistrer le fichier.

## **Chiffrer un fichier ODS avec Aspose.Cells for JavaScript via C++**
Pour chiffrer un fichier ODS, chargez le fichier et définissez la valeur [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) sur le mot de passe réel avant de l'enregistrer. Le fichier ODS chiffré en sortie peut être ouvert dans OpenOffice uniquement.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect ODS File</title>
    </head>
    <body>
        <h1>Protect ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Protect and Download ODS</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded ODS file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file (converted from getSettings().setPassword -> settings.password)
            workbook.settings.password = "1234";

            // Saving the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File protected successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

## **Déchiffrer un fichier ODS avec Aspose.Cells for JavaScript via C++**
Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--). Une fois le fichier chargé, mettez la chaîne [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) à null.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Decrypt ODS Example</title>
    </head>
    <body>
        <h1>Decrypt ODS Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open an encrypted ODS file with load options
            const loadOptions = new LoadOptions(LoadFormat.Ods);

            // Set original password
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null (remove password from settings)
            workbook.settings.password = null;

            // Save the decrypted ODS file and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Decryption completed successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
