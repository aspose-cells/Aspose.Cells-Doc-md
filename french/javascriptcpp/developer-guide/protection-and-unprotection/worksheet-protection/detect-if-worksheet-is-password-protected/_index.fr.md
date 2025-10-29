---
title: Détecter si une feuille de calcul est protégée par mot de passe avec JavaScript via C++
linktitle: Détecter si la feuille de calcul est protégée par mot de passe
type: docs
weight: 360
url: /fr/javascript-cpp/detect-if-worksheet-is-password-protected/
description: Apprenez comment détecter si une feuille de calcul est protégée par mot de passe en utilisant Aspose.Cells for JavaScript via C++. 
keywords: Détecter la protection par mot de passe de la feuille de calcul JavaScript via C++, vérifier si la feuille de calcul est protégée par mot de passe JavaScript via C++, Aspose.Cells for JavaScript via C++
---

{{% alert color="primary" %}}

Il est possible de protéger séparément les classeurs et les feuilles de calcul. Par exemple, un classeur peut contenir une ou plusieurs feuilles protégées par mot de passe, cependant, le classeur lui-même peut ou non être protégé. Les API Aspose.Cells offrent les moyens de détecter si une feuille donnée est protégée par mot de passe ou non. Cet article démontre l'utilisation de Aspose.Cells for JavaScript via API C++ pour atteindre le même résultat.

{{% /alert %}}

Aspose.Cells for JavaScript via C++ a exposé la propriété [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) pour détecter si une feuille est protégée par mot de passe ou non. La propriété de type booléen [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) retourne **true** si [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) est protégé par mot de passe et **false** sinon.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```
