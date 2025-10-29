---
title: Détecter les cellules fusionnées dans une feuille de calcul avec JavaScript via C++
linktitle: Détecter les cellules fusionnées dans une feuille de calcul
description: Apprenez comment détecter les cellules fusionnées dans une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++. Cet article vous montrera comment utiliser la bibliothèque pour identifier et manipuler les cellules fusionnées.
keywords: Aspose.Cells, Feuille de calcul, Cellules fusionnées, Détecter, Identifier, Opérer JavaScript via C++
type: docs
weight: 80
url: /fr/javascript-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Cet article fournit des informations sur la manière d'obtenir les zones de cellules fusionnées dans une feuille de calcul.

Aspose.Cells for JavaScript via C++ vous permet d'obtenir les zones de cellules fusionnées dans une feuille de calcul. Vous pouvez également les dé-fusionner (diviser). Cet article présente le code le plus simple utilisant **Aspose.Cells API** pour effectuer cette tâche.

{{% /alert %}}

Le composant fournit la méthode [**Cells.mergedAreas**](https://reference.aspose.com/cells/javascript-cpp/cells/#mergedAreas--) qui peut obtenir toutes les cellules fusionnées. L'exemple de code suivant montre comment détecter les cellules fusionnées dans une feuille de calcul.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unmerge Areas</title>
    </head>
    <body>
        <h1>Unmerge Merged Areas Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook by opening the uploaded excel file
            const wkBook = new Workbook(new Uint8Array(arrayBuffer));

            // Get a worksheet in the workbook
            const wkSheet = wkBook.worksheets.get("Sheet2");

            // Clear its contents
            wkSheet.cells.clear();

            // Get merged areas
            const areas = wkSheet.cells.mergedAreas;

            // Check if areas is null or not
            if (!areas || areas.length === 0) {
                console.warn("No merged areas to unmerge.");
                resultDiv.innerHTML = '<p style="color: orange;">No merged areas to unmerge.</p>';
                return;
            }

            // Define some variables
            let frow, fcol, erow, ecol, trows, tcols;
            // Loop through the arraylist and get each cellarea
            // To unmerge it
            for (let i = 0; i < areas.length; i++) {
                frow = areas[i].startRow;
                fcol = areas[i].startColumn;
                erow = areas[i].endRow;
                ecol = areas[i].endColumn;

                trows = erow - frow + 1;
                tcols = ecol - fcol + 1;
                wkSheet.cells.unMerge(frow, fcol, trows, tcols);
            }

            // Saving the modified Excel file and provide download link
            const outputData = wkBook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MergeTrial.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Merged areas unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
