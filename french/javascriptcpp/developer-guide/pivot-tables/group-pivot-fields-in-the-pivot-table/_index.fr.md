---
title: Regrouper les champs Pivot dans le Tableau Croisé Dynamique
linktitle: Regrouper les champs Pivot dans le Tableau Croisé Dynamique
description: Apprenez à regrouper les champs pivot de ligne et de colonne d’un tableau croisé dynamique en périodes de dates telles que les mois et les trimestres ainsi qu’en plages numériques à l’aide de PivotField.group et PivotFieldGroupOptions dans Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, tableau croisé dynamique, regroupement de champ pivot, PivotField.group, PivotFieldGroupOptions, regroupement de dates, regroupement de nombres, mois, trimestres, plage numérique, JavaScript via C++
type: docs
weight: 80
url: /fr/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement des champs pivot est utile lorsqu’un champ de ligne ou de colonne d’un tableau croisé dynamique contient de nombreux éléments distincts, comme un champ de date avec des centaines de dates ou un champ numérique avec de nombreuses valeurs éparses. Le regroupement écrase ces éléments en sections significatives : dates en mois, trimestres et années, et nombres en plages telles que 0‑1, 2‑3, 4‑5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells fournit cette capacité via la méthode `PivotField.group()` (regroupement automatique par type de données) et `PivotField.group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement de dates agrège les dates individuelles en périodes plus grandes, comme les jours, les mois, les trimestres et les années, et crée une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances dans le temps deviennent visibles d’un coup d’œil, et chaque niveau de période devient son propre champ pivot dans la zone de lignes ou de colonnes du tableau croisé dynamique.
- Le regroupement n’est disponible que pour les champs placés dans la zone ROW ou COLUMN d’un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d’abord l’ajouter à la zone de lignes ou de colonnes du tableau croisé dynamique.

## **Regrouper automatiquement les champs Pivot**
La surcharge sans paramètre de `PivotField.group()` examine le type de données du champ et le regroupe automatiquement. Un champ qui ne contient que des dates (et des valeurs vides) est regroupé par mois. Un champ qui ne contient que des nombres (et des valeurs vides) est regroupé en plages numériques à l’aide d’un intervalle automatique.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Regrouper les champs Pivot avec des options personnalisées**
La classe `PivotFieldGroupOptions` propose une configuration de regroupement personnalisée. Pour les champs de date, définissez `startDate`, `endDate` et `groupTypes`. Pour les champs numériques, définissez `startNumber`, `endNumber` et `interval`. La propriété `newPivotField` contrôle si le regroupement crée de nouveaux champs pivot à côté de l’original (voir la section Remarque à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L’exemple suivant regroupe le champ de ligne de date du tableau croisé dynamique d’exemple par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d’exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique et enregistre le résultat regroupé. La capture d’écran montre l’effet : le champ de ligne de date est maintenant regroupé par trimestres et mois.  
Notez que l’ordre des valeurs dans `options.groupTypes` est ignoré. Quel que soit l’ordre dans lequel les types de groupe sont listés, les champs regroupés s’affichent toujours de la plus grande période à la plus petite : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.groupTypes`, mais les trimestres apparaissent comme niveau externe et les mois comme niveau interne.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d’exemple est initialement un champ de données (valeur). Comme seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d’abord `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` pour déplacer `FieldTwo` vers la zone des lignes, rafraîchit le tableau croisé dynamique, puis regroupe le champ numérique en plages 0‑1, 2‑3 et 4‑5 en utilisant `startNumber = 0`, `endNumber = 5` et `interval = 2`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Remarque**

{{% alert color="primary" %}}
- Les surcharges de la méthode `PivotField.groupBy()` sont obsolètes et ont été supprimées de l’API. `PivotField.group()` et `PivotField.group(PivotFieldGroupOptions)` les remplacent.
- Dans Microsoft Excel, le regroupement d’un champ numérique **REMPLACE** le champ pivot original par les plages regroupées, tandis que le regroupement d’un champ de date crée de **NOUVEAUX** champs pivot (un par niveau de groupe, par exemple Trimestres et Mois) à côté du champ original. À partir d’Aspose.Cells 26.10, les méthodes `PivotField.group()` adoptent le même comportement qu’Excel. La propriété `PivotFieldGroupOptions.newPivotField` existe pour la compatibilité avec les versions antérieures : elle vaut `false` par défaut pour le regroupement numérique et `true` pour le regroupement date‑heure ; définissez‑la sur `false` si vous souhaitez que le regroupement de dates remplace le champ pivot original au lieu de créer de nouveaux champs.
- La propriété `PivotFieldGroupOptions.interval` n’a d’effet que pour le regroupement numérique et pour le regroupement de dates par jour (par exemple, regrouper les dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles associés**
- [Ajouter des champs de ligne et de colonne dans le Tableau Croisé Dynamique](/cells/fr/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrer les Tableaux Croisés Dynamiques par libellé ou valeur](/cells/fr/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans le Tableau Croisé Dynamique](/cells/fr/javascript-cpp/add-page-field-in-pivot-table/)
- [Appliquer un style au Tableau Croisé Dynamique](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)
- [Actualiser le Tableau Croisé Dynamique](/cells/fr/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}