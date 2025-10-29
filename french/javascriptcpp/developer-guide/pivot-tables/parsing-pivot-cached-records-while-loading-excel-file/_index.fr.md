---
title: Analyse des enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel
type: docs
weight: 70
url: /fr/javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Scénarios d'utilisation possibles**

Lorsque vous créez un tableau croisé dynamique, Microsoft Excel prend une copie des données sources et les enregistre dans le cache du tableau croisé dynamique. Le cache du tableau croisé dynamique est conservé dans la mémoire de Microsoft Excel. Vous ne pouvez pas le voir, mais ce sont les données auxquelles le tableau croisé dynamique fait référence lorsque vous construisez votre tableau croisé dynamique ou modifiez une sélection de filtre ou déplacez des lignes/colonnes. Cela permet à Microsoft Excel de réagir très rapidement aux modifications du tableau croisé dynamique, mais cela peut également doubler la taille de votre fichier. Après tout, le cache du tableau croisé dynamique est simplement une copie de vos données sources, il est donc logique que la taille de votre fichier puisse être potentiellement doublée.

Lorsque vous chargez votre fichier Excel dans l'objet Workbook, vous pouvez décider si vous souhaitez également charger les enregistrements du cache Pivot ou non, en utilisant la propriété [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). La valeur par défaut de cette propriété est **false**. Si le cache Pivot est assez volumineux, cela peut améliorer les performances. Mais si vous souhaitez également charger les enregistrements du cache Pivot, vous devez définir cette propriété sur **true**.

## **Analyse des enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel**

Le code d'exemple suivant explique l'utilisation de la propriété [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). Il charge le [fichier Excel d'exemple](61767773.xlsx) tout en analysant les enregistrements du cache pivot, puis il rafraîchit le tableau croisé dynamique et l'enregistre sous le nom de [fichier Excel de sortie](61767774.xlsx).

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Parsing Pivot Cached Records While Loading Example</title>
    </head>
    <body>
        <h1>Parsing Pivot Cached Records While Loading Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options
            const options = new LoadOptions();
            // Set ParsingPivotCachedRecords true, default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag false
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
