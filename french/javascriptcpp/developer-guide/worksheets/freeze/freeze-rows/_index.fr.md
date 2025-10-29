---
title: Figer la ou les premières lignes de la feuille Excel avec JavaScript via C++
linktitle: Geler les lignes
type: docs
weight: 190
url: /fr/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: Dans cet article, vous apprendrez comment figer les lignes du haut des feuilles Excel de manière programmatique en utilisant la bibliothèque JavaScript avec l API C++.
keywords: Figer les lignes du haut, figer la première ligne JavaScript via C++.
---

## **Introduction**

Dans cet article, nous apprendrons comment figer la ou les lignes supérieures. Lorsque vous avez une grande quantité de données sous une en-tête commune, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille vers le bas. Vous pouvez figer la ou les lignes supérieures pour voir cette partie figée même lorsque le reste des données est défilé. Vous pouvez facilement voir les en-têtes dans les lignes supérieures.

## **Figer les rangées dans Excel**

**![Figer la rangée(s) supérieure(s) dans Excel](Freeze-Rows.png)**

1. Si vous souhaitez figer la ou les premières lignes, sélectionnez d'abord la ligne sous celle qui doit être figée.
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Figer la rangée supérieure.
4. Si vous faites défiler vers le bas, la première ligne reste toujours en vue en haut.

**![Ligne figée](Frozen-Row.png)**

Comme vous pouvez le voir, la première ligne est figée ; la première ligne reste toujours en haut de la vue lorsque vous faites défiler vers le bas.

Figer les lignes vous permet de voir vos grandes données sans suivre l’étiquette de la ligne.

## **Figer la ou les lignes avec Aspose.Cells for JavaScript via C++**
Il est simple de figer la ou les lignes avec Aspose.Cells for JavaScript via C++. 
Veuillez utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) pour figer la ou les lignes à la ligne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figer la première ligne avec la méthode Worksheet.freezePanes().
3. Enregistrez le fichier.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Fichier Excel source d'exemple joint [échantillon](../Freeze.xlsx).
