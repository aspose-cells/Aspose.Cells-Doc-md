---
title: Vérifier le mot de passe des fichiers cryptés avec JavaScript via C++
linktitle: Vérifier le mot de passe des fichiers chiffrés
type: docs
weight: 10
url: /fr/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Vérifier le mot de passe des fichiers Excel cryptés (xlsx, xlsb, xls, xlsm) et Open Office (ODS) en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Si des fichiers Excel (xlsx, xlsb, xls, xlsm) et Open Office (ODS) sont verrouillés par mot de passe, Aspose supporte une vérification simple du mot de passe sans parser les données spécifiques des fichiers.  
{{% /alert %}}  

## **Vérifiez le mot de passe du fichier chiffré**  

 Pour vérifier le mot de passe du fichier crypté, Aspose.Cells for JavaScript via C++ fournit la méthode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). Cette méthode accepte deux paramètres, le flux de fichier et le mot de passe à vérifier.  
Le code d'exemple suivant démontre l'utilisation de la méthode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) pour vérifier si le mot de passe fourni est valide ou non.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```
