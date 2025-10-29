---
title: Effacer le filtre dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/javascript-cpp/clear-filter-in-pivot-table/
description: Comment effacer le filtre de pivot spécifique dans le champ de pivot avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, bibliothèque JavaScript Excel, effacer le filtre de pivot dans le tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++ Excel Library.
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un tableau croisé dynamique avec des données connues et que vous souhaitez filtrer le tableau croisé dynamique, vous devez apprendre et utiliser le filtre. Cela peut vous aider à filtrer efficacement les données que vous souhaitez. En utilisant l’API Aspose.Cells for JavaScript via C++, vous pouvez manipuler le filtre sur les valeurs des champs dans les tableaux croisés dynamiques. 

## **Comment effacer le filtre dans le tableau croisé dynamique dans Excel**
Effacer le filtre dans le tableau croisé dynamique dans Excel, suivez ces étapes :

1. Sélectionnez le tableau croisé dynamique que vous souhaitez effacer. 
2. Cliquez sur la flèche déroulante pour le filtre que vous souhaitez effacer dans le tableau croisé dynamique.
3. Sélectionnez "Effacer le filtre" dans le menu déroulant.
<img src="1.png" width=80% />
4. Si vous souhaitez effacer tous les filtres du tableau croisé dynamique, vous pouvez également cliquer sur le bouton "Effacer les filtres" dans l'onglet Analyser le tableau croisé dynamique dans le ruban d'Excel.
<img src="2.png" width=80% />

## **Comment effacer le filtre dans le tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++**
Effacer le filtre dans le tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++. Veuillez consulter le code d'exemple suivant. 
1. Définir les données et créer un tableau croisé dynamique basé sur celles-ci. 
2. Ajouter un filtre sur le champ de ligne du tableau croisé dynamique. 
3. Enregistrer le classeur au format [XLSX de sortie](out_add.xlsx). Après l'exécution du code d'exemple, un tableau croisé dynamique avec un filtre top10 est ajouté à la feuille de calcul. 
4. Effacer le filtre sur un champ pivotant spécifique. Après l'exécution du code pour effacer le filtre, le filtre sur le champ pivotant spécifique sera effacé. Veuillez vérifier le [XLSX de sortie](out_delete.xlsx).

## **Code d'exemple**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkAdd" style="display: none; margin-right: 10px;">Download Pivot Added File</a>
            <a id="downloadLinkDelete" style="display: none;">Download Pivot Filter Cleared File</a>
        </div>
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
            document.getElementById('result').innerHTML = '<p>Running example...</p>';

            // Create a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("A6");
            cell.value = "Guava";
            cell = cells.get("A7");
            cell.value = "Carambola";
            cell = cells.get("A8");
            cell.value = "Banana";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("B6");
            cell.value = 5;
            cell = cells.get("B7");
            cell.value = 2;
            cell = cells.get("B8");
            cell.value = 20;

            // Adding a PivotTable to the worksheet
            const i = ws.pivotTables.add("=A1:B8", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Count");
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;

            const field = pivotTable.rowFields.get(0);
            field.isAutoSort = true;
            field.isAscendSort = false;
            field.autoSortField = 0;

            // Add top10 filter
            const index = pivotTable.pivotFilters.add(field.baseIndex, AsposeCells.PivotFilterType.Count);
            const filter = pivotTable.pivotFilters.get(index);
            filter.autoFilter.filterTop10(0, true, false, 5);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after adding pivot/filter
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLinkAdd = document.getElementById('downloadLinkAdd');
            downloadLinkAdd.href = URL.createObjectURL(blob);
            downloadLinkAdd.download = 'out_add.xlsx';
            downloadLinkAdd.style.display = 'inline-block';
            downloadLinkAdd.textContent = 'Download out_add.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created and top10 filter applied. Download the file with pivot added.</p>';

            // Clear PivotFilter from the specific PivotField
            pivotTable.pivotFilters.clearFilter(field.baseIndex);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after clearing filter
            const outputData2 = workbook.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLinkDelete = document.getElementById('downloadLinkDelete');
            downloadLinkDelete.href = URL.createObjectURL(blob2);
            downloadLinkDelete.download = 'out_delete.xlsx';
            downloadLinkDelete.style.display = 'inline-block';
            downloadLinkDelete.textContent = 'Download out_delete.xlsx';

            document.getElementById('result').innerHTML += '<p style="color: green;">Pivot filter cleared and data recalculated. Download the file with filter removed.</p>';
        });
    </script>
</html>
```
