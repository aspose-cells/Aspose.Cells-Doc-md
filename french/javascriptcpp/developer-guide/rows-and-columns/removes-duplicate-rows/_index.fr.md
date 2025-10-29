---
title: Supprimer les lignes en double dans une feuille de calcul avec JavaScript via C++
linktitle: Supprimer les lignes en double dans une feuille de calcul
type: docs
weight: 370
url: /fr/javascript-cpp/remove-duplicate-rows-in-a-worksheet/
description: Apprenez comment supprimer les lignes en double dans une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++ et sélectionnez des colonnes spécifiques pour vérifier les doublons.
---

Supprimer les doublons est l'une des nombreuses fonctionnalités utiles de Microsoft Excel. Elle permet aux utilisateurs de supprimer les lignes en double dans une feuille de calcul, et vous pouvez choisir quelles colonnes vérifier pour les doublons.

Aspose.Cells for JavaScript via C++ fournit la méthode `Cells.removeDuplicates()` à cet effet. Vous pouvez également définir `startRow`, `startColumn`, `endRow` et `endColumn` pour spécifier la plage de colonnes à vérifier pour les doublons.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[removeduplicates.xlsx](removeduplicates.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Duplicates Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Remove Duplicate (converted getters to properties)
            book.worksheets.get(0).cells.removeDuplicates(0, 0, 5, 3);

            // Save result and provide download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'removeduplicates-result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            resultDiv.innerHTML = '<p style="color: green;">Duplicates removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
