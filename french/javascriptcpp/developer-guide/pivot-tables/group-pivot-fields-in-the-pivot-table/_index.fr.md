---
title: Regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique
type: docs
weight: 80
url: /fr/javascript-cpp/group-pivot-fields-in-the-pivot-table/
description: Comment grouper les champs de pivot dans le tableau croisé dynamique avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, bibliothèque JavaScript Excel, Comment grouper les champs de pivot dans le tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++ Bibliothèque Excel.
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de regrouper les champs de synthèse du tableau croisé dynamique. Lorsqu'il y a une grande quantité de données liées à un champ de synthèse, il est souvent utile de les regrouper en sections. Aspose.Cells for JavaScript via C++ offre également cette fonctionnalité en utilisant la méthode [**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-).

## **Comment regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716818.xlsx) et effectue un groupement sur le premier champ de tableau croisé dynamique en utilisant la méthode [**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-). Ensuite, il actualise et calcule les données du tableau croisé dynamique et enregistre le classeur sous le nom de [fichier Excel de sortie](64716817.xlsx). La capture d'écran montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le premier champ de tableau croisé dynamique est maintenant regroupé par mois et par trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Example</title>
    </head>
    <body>
        <h1>Group Pivot Fields in PivotTable</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotGroupByType } = AsposeCells;

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

            // Load workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the second worksheet
            const ws = wb.worksheets.get(1);

            // Access the pivot table
            const pt = ws.pivotTables.get(0);

            // Specify the start and end date time
            const dtStart = new Date(2008, 1, 1);
            const dtEnd = new Date(2008, 9, 5);

            // Specify the group type list, we want to group by months and quarters
            const groupTypeList = [PivotGroupByType.Months, PivotGroupByType.Quarters];

            // Apply the grouping on first pivot field
            const field = pt.rowFields.get(0);
            field.groupBy(dtStart, dtEnd, groupTypeList, 1, true);

            // Refresh and calculate pivot table
            pt.refreshDataFlag = true;
            pt.refreshData();
            pt.calculateData();
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGroupPivotFieldsInPivotTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
