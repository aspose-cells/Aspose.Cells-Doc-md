---
title: Geler les volets de la feuille Excel avec JavaScript via C++
linktitle: Geler les volets
type: docs
weight: 190
url: /fr/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: Dans cet article, vous apprendrez comment geler les volets des feuilles Excel de manière programmatique en utilisant Aspose.Cells for JavaScript via C++.
keywords: Geler les volets, Geler la fenêtre.
---

## **Introduction**  

Dans cet article, nous verrons comment geler les volets. Lorsque vous avez une grande quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille vers le bas. Et chaque enregistrement contient de nombreuses données. Vous pouvez geler les volets pour voir cette partie gelée même lorsque le reste des données est en cours de défilement. Vous pouvez facilement voir les en-têtes dans les premières lignes ou les premières colonnes. Geler et dégeler les volets ne modifient que la vue des données, sans changer les données elles-mêmes.  

## **Dans Excel**  

**![Geler les volets dans Excel](Freeze-panes.png)**  

1. Si vous souhaitez geler les volets, geler les lignes et les colonnes, sélectionnez d'abord une cellule (par exemple B2).  
2. Cliquez sur Affichage > Fenêtres figées.  
3. Dans le menu déroulant, cliquez sur Geler les volets.  
4. Si vous faites défiler vers le bas ou vers la droite, la première ligne et la première colonne restent figées.  

**![Fenêtres figées](Frozen-Panes.png)**  

 Comme vous pouvez le voir, la première ligne et la colonne A sont gelées, la deuxième ligne est la ligne 32 et la deuxième colonne visible est D.  

 Geler les volets vous permet de voir vos grandes données sans suivre les étiquettes de ligne ou de colonne.  

## **Geler les volets avec Aspose.Cells for JavaScript via C++**  
Il est simple de geler les volets avec Aspose.Cells for JavaScript via C++. Veuillez utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) pour geler les volets sur la cellule sélectionnée.  
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.  
2. Geler les volets avec la méthode Worksheet.freezePanes()  
3. Enregistrez le fichier.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

Fichier Excel source [exemple joint](Freeze.xlsx).
