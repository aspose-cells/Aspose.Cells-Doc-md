---
title: Ajouter un champ calculé dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/javascript-cpp/add-calculated-field-in-pivot-table/
description: Comment ajouter un champ calculé dans un tableau croisé dynamique avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, bibliothèque JavaScript Excel, ajout d’un champ calculé dans un tableau croisé dynamique en utilisant la bibliothèque JavaScript Excel.
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un tableau croisé dynamique basé sur des données connues, vous constatez que les données qui s'y trouvent ne correspondent pas à ce que vous souhaitez. Les données que vous souhaitez sont la combinaison de ces données d'origine. Par exemple, vous devez ajouter, soustraire, multiplier et diviser les données d'origine avant de les vouloir. À ce moment-là, vous devez construire un champ calculé et définir la formule correspondante pour le calcul. Ensuite, effectuez des statistiques et d'autres opérations sur le champ calculé. 

## **Comment ajouter un champ calculé dans un tableau croisé dynamique dans Excel**
Insérer un champ calculé dans un tableau croisé dynamique dans Excel, suivez ces étapes :

1. Sélectionnez le tableau croisé dynamique auquel vous souhaitez ajouter un champ calculé. 
2. Accédez à l'onglet Analyse du tableau croisé dynamique dans le ruban.
3. Cliquez sur "Champs, éléments et ensembles" puis sélectionnez "Champ calculé" dans le menu déroulant.
4. Dans le champ "Nom", entrez un nom pour le champ calculé.
5. Dans le champ "Formule", entrez la formule du calcul que vous souhaitez effectuer en utilisant les noms de champ appropriés du tableau croisé dynamique et les opérateurs mathématiques. 
<br>
<img src="1.png" width=80% />
6. Cliquez sur "OK" pour créer le champ calculé.
7. Le nouveau champ calculé apparaîtra dans la liste des champs du tableau croisé dynamique sous la section "Valeurs".
8. Faites glisser le champ calculé dans la section Valeurs du tableau croisé dynamique pour afficher les valeurs calculées.
<br>
<img src="2.png" width=80% />

## ** Comment ajouter un champ calculé dans un tableau croisé dynamique en utilisant la bibliothèque Aspose.Cells for JavaScript via C++**
Ajouter un champ calculé au fichier Excel en utilisant Aspose.Cells for JavaScript via C++. Veuillez consulter le code d'exemple suivant. Après l'exécution du code d'exemple, un tableau croisé dynamique avec un champ calculé est ajouté à la feuille de calcul.
1. Définissez les données d'origine et créez un tableau croisé dynamique. 
2. Créez le champ calculé en fonction du PivotField existant dans le tableau croisé dynamique.
3. Ajoutez le champ calculé à la zone de données. 
4. Enfin, enregistrez le classeur au format [XLSX de sortie](out.xlsx). 

## **Code d'exemple**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
