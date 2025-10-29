---
title: Crypter et décrypter des fichiers Excel avec JavaScript via C++
linktitle: Chiffrer et déchiffrer les fichiers Excel
type: docs
weight: 10
url: /fr/javascript-cpp/encrypt-and-decrypt-excel-files/
description: Comment crypter et décrypter des fichiers Excel en utilisant JavaScript via C++. Verrouiller et déverrouiller des fichiers Excel.
---

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) vous permet de chiffrer et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques (CSP), un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est 'Compatible avec Office 97/2000' ou 'Chiffrement faible (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. Cela est considéré comme un chiffrement faible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient également des CSP qui offrent des types de chiffrement forts, par exemple le 'Fournisseur cryptographique fort Microsoft'. Pour vous donner une idée, un chiffrement de 128 bits est ce que les banques utilisent pour chiffrer la connexion avec leurs systèmes de banque en ligne.  

Aspose.Cells vous permet de chiffrer et de protéger par mot de passe des fichiers Microsoft Excel avec le type de chiffrement de votre choix.  
{{% /alert %}}  

## **Utilisation de Microsoft Excel**  

Pour définir les paramètres de chiffrement de fichier dans Microsoft Excel (ici Microsoft Excel 2003) :  

1. Dans le menu **Outils**, sélectionnez **Options**. Une boîte de dialogue apparaîtra.  
 2. Sélectionnez l'onglet **Sécurité**.  
 3. Entrez un mot de passe et cliquez sur **Avancé**  
 4. Choisissez le type de chiffrement et confirmez le mot de passe.  

## **Crypter un fichier Excel avec Aspose.Cells for JavaScript via C++**  

L'exemple suivant montre comment crypter et protéger par mot de passe un fichier Excel à l'aide de l'API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Encrypt Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded excel file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify XOR encryption type.
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.XOR, keyLength: 40 };

            // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.StrongCryptographicProvider, keyLength: 128 };

            // Password protect the file.
            workbook.settings.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook encrypted and ready for download.</p>';
        });
    </script>
</html>
```  

### ** Spécification de l'option Mot de passe pour modification**  

L'exemple suivant montre comment définir l'option **Mot de passe pour modifier** de Microsoft Excel pour un fichier existant à l'aide de l'API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Password To Modify Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set the password for modification.
            workbook.settings.writeProtection.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyPasswordToModifyOption.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password-to-modify set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


## **Décrypter un fichier Excel avec Aspose.Cells for JavaScript via C++**  
Il est très facile d'ouvrir un fichier Excel protégé par mot de passe et de le décrypter en utilisant l'API Aspose.Cells comme indiqué dans le code suivant :  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Excel and Remove Password</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Prepare load options with password to open encrypted file
            const loadOptions = new LoadOptions();
            loadOptions.password = "password";

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Remove password from workbook settings
            workbook.settings.password = null;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            // Use original filename with suffix to indicate password removed
            const originalName = file.name || 'output.xlsx';
            const baseName = originalName.replace(/(\.xls[xm]?|\.csv)$/i, '') || 'output';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unlocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unlocked Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password removed successfully! Click the download link to get the unlocked file.</p>';
        });
    </script>
</html>
```  


## **Sujets avancés**  
- [Chiffrer et déchiffrer des fichiers ODS](/cells/fr/javascript-cpp/encrypt-and-decrypt-ods-files/)  
- [Définition du type de chiffrement fort](/cells/fr/javascript-cpp/setting-strong-encryption-type/)  
- [Spécifier l'auteur lors de la protection en écriture du classeur](/cells/fr/javascript-cpp/specify-author-while-write-protecting-workbook/)  
- [Vérifier le mot de passe des fichiers chiffrés](/cells/fr/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/)
