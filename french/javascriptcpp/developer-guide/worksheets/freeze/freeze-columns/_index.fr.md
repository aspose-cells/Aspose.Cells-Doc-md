---
title: Geler la ou les premières colonnes de la feuille Excel avec JavaScript via C++
linktitle: Geler les colonnes
type: docs
weight: 190
url: /fr/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: Apprenez à figer les colonnes de gauche des feuilles Excel de manière programmatique en utilisant Aspose.Cells for JavaScript via C++.
keywords: Fixer les colonnes de gauche, Fixer la ou les premières colonnes, Verrouiller la ou les colonnes
---

## **Introduction**  

Dans cet article, nous apprendrons comment geler la(les) colonne(s) de gauche. Lorsqu'une ligne contient une grande quantité de données, vous pourriez ne pas voir les colonnes de gauche lorsque vous faites défiler horizontalement la feuille. Vous pouvez geler et verrouiller la(les) première(s) colonne(s) afin de voir cette partie figée même lorsque le reste des données défile. Il est facile de voir les en-têtes dans les colonnes de gauche.  

## **Geler les colonnes dans Excel**  

**![Geler la ou les premières colonnes dans Excel](freeze-columns.png)**  

1. Si vous souhaitez fixer la ou les colonnes de gauche, sélectionnez d'abord la colonne sous la colonne qui doit être figée.
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Geler la première colonne.
4. Si vous faites défiler vers le bas, la première colonne reste toujours visible à gauche.

**![Colonne figée](frozen-columns.png)**  

Comme vous pouvez le voir, la première colonne est gelée, et cette colonne reste toujours verrouillée en haut de la vue lorsque vous faites défiler horizontalement.

Figer les colonnes vous permet de voir vos longues données sans aucune difficulté à suivre la première colonne.

## **Figer les colonnes avec Aspose.Cells for JavaScript via C++**  
Il est simple de figer la ou les premières colonnes avec Aspose.Cells for JavaScript via C++.  
Veuillez utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) pour figer la ou les colonnes à la colonne sélectionnée.  
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figez la première colonne avec la méthode Worksheet.freezePanes().
3. Enregistrez le fichier.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
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

Fichier Excel source [exemple joint](Freeze.xlsx).
