---
title: Définir un type de chiffrement fort avec JavaScript via C++
linktitle: Définition du type de chiffrement fort
type: docs
weight: 60
url: /fr/javascript-cpp/setting-strong-encryption-type/
description: Apprendre comment définir des types de chiffrement forts pour les fichiers Excel en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) vous permet de chiffrer et protéger par mot de passe des feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques. Un fournisseur de services cryptographiques (ou CSP) est un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est "Office 97/2000 Compatible". Il s'agit d'un CSP avec plusieurs problèmes de sécurité connus. Les feuilles de calcul sécurisées avec le type de chiffrement "chiffrement faible (XOR)" ou avec le type de chiffrement "Office 97/2000 Compatible" peuvent être facilement crackées.

Pour résoudre ce problème, utilisez l'un des types de chiffrement forts fournis par Microsoft Excel. Vous pouvez modifier le type de chiffrement pour utiliser le CSP le plus fort disponible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise, par exemple, 'Fournisseur cryptographique Microsoft fort'.

Vous pouvez également chiffrer et protéger par mot de passe des fichiers Excel avec un type de chiffrement fort en utilisant l'API Aspose.Cells.

{{% /alert %}}  
## **Application du chiffrement avec Microsoft Excel**  
Pour implémenter le chiffrement de fichier dans Microsoft Excel (par exemple 2007) :

1. Dans le menu **Outils**, sélectionnez **Options**.  
1. Sélectionnez l'onglet **Sécurité**.  
1. Entrez une valeur pour le champ **Mot de passe pour ouvrir**.  
1. Cliquez sur **Avancé**.  
1. Choisissez le type de chiffrement et confirmez le mot de passe.  

## **Application du chiffrement avec Aspose.Cells**  
Les exemples de code ci-dessous appliquent un chiffrement fort sur un fichier et définissent un mot de passe.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Encrypt Workbook</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            workbook.encryptionOptions = [AsposeCells.EncryptionType.StrongCryptographicProvider, 128];
            workbook.settings.password = "1234";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```
