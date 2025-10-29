---
title: Spécifier le nombre maximum de lignes pour une formule partagée avec JavaScript via C++
linktitle: Spécifier le nombre maximum de lignes de formule partagée
type: docs
weight: 40
url: /fr/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Apprenez comment spécifier le nombre maximum de lignes pour les formules partagées en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

La valeur maximale par défaut pour le nombre de lignes dans une formule partagée est 64. Elle peut être n'importe quel nombre, par exemple elle peut être 1000. La performance d'une formule partagée varie en fonction du nombre de lignes. Par conséquent, Aspose.Cells propose la propriété [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) qui peut être utilisée pour spécifier le nombre maximum de lignes de la formule partagée. La formule partagée sera divisée en plusieurs formules partagées si le total de lignes de la formule dépasse cette valeur, comme illustré dans la capture d'écran suivante.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Spécifier le nombre maximum de lignes de formule partagée**  

Le code d'exemple suivant explique l'utilisation de la propriété [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--). Il définit le nombre maximum de lignes de la formule partagée à 5, ajoute la formule partagée en D1 pour 100 lignes, puis enregistre dans [fichier Excel de sortie](61767856.xlsx). Si vous extrayez le contenu du fichier Excel de sortie et consultez *sheet1.xml*, vous verrez la formule partagée se diviser après chaque 5 lignes, comme indiqué dans la capture d'écran ci-dessus.  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
