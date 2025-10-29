---
title: Obtenir l identifiant unique de la feuille de calcul avec JavaScript via C++
linktitle: Obtenir l identifiant unique de la feuille de calcul
type: docs
weight: 190
url: /fr/javascript-cpp/get-worksheet-unique-id/
description: Cet article montre comment obtenir l identifiant unique d une feuille Excel en utilisant la bibliothèque JavaScript et l API C++ de manière programmée.
keywords: identifiant unique feuille Excel JavaScript via C++, identifiant unique feuille JavaScript via C++
---

## **Obtenir l'identifiant unique de la feuille de calcul**

Aspose.Cells for JavaScript via C++ offre la capacité d'obtenir l'identifiant unique d'une feuille en utilisant la propriété [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--). Le code suivant démontre l'utilisation de la propriété [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--) pour afficher l'identifiant unique d'une feuille. Le code utilise ce [fichier Excel d'exemple](105480213.xlsx).

### Code source

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Worksheet Unique Id Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Unique Id
            const uniqueId = worksheet.uniqueId;
            console.log("Unique Id: " + uniqueId);

            document.getElementById('result').innerHTML = '<p style="color: green;">Unique Id: ' + uniqueId + '</p>';
        });
    </script>
</html>
```
