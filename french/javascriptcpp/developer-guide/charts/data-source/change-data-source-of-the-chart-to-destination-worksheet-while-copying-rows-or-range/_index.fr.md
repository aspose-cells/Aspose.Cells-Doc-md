---
title: Modifier la source de données du graphique vers la feuille de destination lors de la copie de lignes ou de plages avec JavaScript via C++
linktitle: Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage
description: Apprenez comment changer la source de données d’un graphique vers une feuille de destination lors de la copie de lignes ou d’une plage dans Aspose.Cells for JavaScript via C++. Ce guide montre comment mettre à jour la plage de données du graphique et la lier à la feuille de destination.
keywords: Aspose.Cells for JavaScript via C++, visualisation, source de données, feuille de destination, lignes, plage, copie, mise à jour, plage de données, liaison.
type: docs
weight: 440
url: /fr/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Scénarios d'utilisation possibles**

Lorsque vous copiez des lignes ou une plage contenant des graphiques vers une nouvelle feuille, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est `=Sheet1!$A$1:$B$4`, alors après la copie, la source de données restera la même, c’est-à-dire `=Sheet1!$A$1:$B$4`. Elle continue de faire référence à l’ancienne feuille, c'est-à-dire Sheet1. Ce comportement est également celui de Microsoft Excel. Mais si vous souhaitez qu’elle fasse référence à la nouvelle feuille de destination, utilisez la propriété [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) et définissez-la sur **true** lors de l’appel de la méthode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-). Maintenant, si votre feuille de destination est DestSheet, la source de données de votre graphique passera de `=Sheet1!$A$1:$B$4` à `=DestSheet!$A$1:$B$4`.

## **Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage**

Le code d'exemple suivant explique l'utilisation de la propriété [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) lors de la copie de lignes ou de plages contenant des graphiques vers une nouvelle feuille. Le code utilise le [fichier Excel d'exemple](5113699.xlsx) et génère le [fichier Excel de sortie](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
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

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
