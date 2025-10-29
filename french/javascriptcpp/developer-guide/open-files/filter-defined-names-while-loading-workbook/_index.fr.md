---
title: Filtrer les noms définis lors du chargement du classeur avec JavaScript via C++
linktitle: Filtrer les noms définis lors du chargement du classeur
type: docs
weight: 50
url: /fr/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells permet de filtrer ou de supprimer les noms définis présents dans le classeur. Veuillez utiliser [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) pour charger les noms définis et [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) pour les supprimer lors du chargement du classeur. À noter, en supprimant les noms définis, les formules dans le classeur pourraient ne plus fonctionner.

## **Filtrer les noms définis lors du chargement du classeur**

Le code d’exemple suivant charge le [fichier Excel exemple](61767860.xlsx) qui contient une formule en cellule **C1** incluant des noms définis, c’est-à-dire *=SUM(MyName1, MyName2)*. Comme nous utilisons [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) pour supprimer les noms définis lors du chargement du classeur, la formule en cellule C1 dans le [fichier Excel de sortie](61767861.xlsx) est cassée et affiche *#NAME?*. Voir la capture d’écran suivante illustrant l’effet du code sur le fichier Excel d’exemple.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
