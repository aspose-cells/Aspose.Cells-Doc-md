---
title: Modifier la disposition des champs de page dans un tableau croisé dynamique
linktitle: Modifier la disposition des champs de page dans un tableau croisé dynamique
description: Découvrez comment contrôler la disposition de la zone des champs de page dans un tableau croisé dynamique à l’aide d’Aspose.Cells for JavaScript via C++, notamment pour définir l’ordre d’affichage, le nombre de champs de page avant le retour à la ligne et l’ordre des champs de page en haut du tableau croisé dynamique.
keywords: Aspose.Cells for JavaScript via C++, tableur, tableau croisé dynamique, champ de page, ordre des champs de page, nombre de champs de page avant le retour à la ligne, déplacer un champ de page
type: docs
weight: 191
url: /fr/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Cet article est la suite de l’article **Ajouter un champ de page dans un tableau croisé dynamique**. Il montre comment contrôler la disposition de la zone des champs de page — la bande de contrôles de filtre déroulants située en haut d’un tableau croisé dynamique — y compris l’ordre d’affichage, le nombre de champs de page avant le retour à la ligne et le réordonnancement des champs de page.
{{% /alert %}}

## **Introduction**
Un tableau croisé dynamique dans Microsoft Excel met à disposition une **zone de champs de page** dédiée, située au-dessus du corps du tableau, qui regroupe les lignes, les colonnes et les données. Cette zone s’affiche sous la forme d’une bande de contrôles de filtre déroulants (un contrôle par champ de page). Les utilisateurs finaux cliquent sur ces contrôles pour filtrer le tableau croisé dynamique selon des critères tels que l’année ou la région. Aspose.Cells modélise cette zone via la collection `pivotTable.pageFields` et expose trois propriétés qui contrôlent sa disposition visuelle :
- `pivotTable.pageFieldOrder` (une valeur `Aspose.Cells.PrintOrderType`) détermine si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous*.
- `pivotTable.pageFieldWrapCount` définit le nombre de champs de page à placer par ligne ou par colonne avant le retour à la ligne.
- `pivotTable.pageFields.move(currIndex, destIndex)` réordonne les champs de page sans modifier le mode d’ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un même jeu de données, afin de comparer côte à côte les dispositions obtenues.

## **Données source**
| Fruit  | Année | Région | Montant |
|--------|-------|--------|---------|
| Pomme  | 2022  | Nord   | 150     |
| Pomme  | 2023  | Nord   | 180     |
| Banane | 2022  | Sud    | 120     |
| Banane | 2023  | Sud    | 140     |
| Cerise | 2022  | Est    | 200     |
| Cerise | 2023  | Est    | 220     |
| Raisin | 2022  | Ouest  | 90      |
| Raisin | 2023  | Ouest  | 110     |
Les huit lignes sont renseignées dans chaque exemple de code, dans le même ordre. Les données source ne varient donc pas entre les scénarios — seules les propriétés de disposition des champs de page changent.

## **Exemple 1 : `OverThenDown`**
Dans le premier scénario, vous configurez les deux champs de page (`Year`, `Region`) afin qu’ils apparaissent **côte à côte dans une seule ligne** en haut du tableau croisé dynamique. Vous affectez `Fruit` à l’axe des lignes, placez `Year` en première position et `Region` en deuxième position sur l’axe des pages (l’ordre des appels à `addFieldToArea` détermine l’index initial), ajoutez `Amount` (`Sum`) comme champ de données, puis définissez `pivotTable.pageFieldOrder` à la valeur `PrintOrderType.OverThenDown` avec `pivotTable.pageFieldWrapCount = 2`. Avec `OverThenDown` et un nombre de champs de page de 2, les deux champs de page sont disposés horizontalement, côte à côte, dans une seule ligne en haut du tableau croisé dynamique. La bande occupe donc une ligne sur deux colonnes.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // En-têtes (ligne 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // Ligne 1 : Apple, 2022, North, 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // Ligne 2 : Apple, 2023, North, 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // Ligne 3 : Banana, 2022, South, 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // Ligne 4 : Banana, 2023, South, 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // Ligne 5 : Cherry, 2022, East, 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // Ligne 6 : Cherry, 2023, East, 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // Ligne 7 : Grape, 2022, West, 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // Ligne 8 : Grape, 2023, West, 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // Ajouter la feuille PivotTableReport
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // Créer un tableau croisé dynamique basé sur PivotData!A1:D9 et placé en A1 sur PivotTableReport
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Ajouter des champs
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Année
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Région
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Montant
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // Configurer la disposition de la zone des champs de page : placer les champs de page de gauche à droite en premier, puis passer à la ligne suivante après chaque groupe de 2
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // Actualiser et calculer
            pivotTable.calculateData();
            // Enregistrer
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Exemple 2 : `DownThenOver`**
Dans cet exemple, vous placez `Fruit` sur l’axe des lignes, `Year` et `Region` sur l’axe des pages (avec `Year` en premier), et `Amount` (`Sum`) comme champ de données — exactement comme dans l’exemple 1. Vous définissez ensuite `pivotTable.pageFieldOrder` à la valeur `PrintOrderType.DownThenOver` et `pivotTable.pageFieldWrapCount` à la valeur `2`. Avec `DownThenOver` et un nombre de champs de page de 2, les deux champs de page sont empilés verticalement — `Year` en haut, `Region` juste en dessous — et forment une seule colonne en haut du tableau croisé dynamique. La bande occupe donc deux lignes sur une seule colonne, contrairement à l’exemple 1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Exemple 3 : Déplacer un champ de page**
Dans le troisième scénario, vous conservez ce jeu de données et cette répartition des champs, puis définissez une disposition neutre (`OverThenDown` avec un nombre de champs de page de `2`). Le scénario illustre ensuite l’opération `pivotTable.pageFields.move`. L’appel `move(0, 1)` déplace le champ de page situé à l’index 0 (`Year`) vers la position 1, et le champ de page qui occupait la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` le second. Le mode d’ordre et le nombre de champs de page avant le retour à la ligne restent inchangés. La bande est donc toujours affichée horizontalement, avec les contrôles côte à côte — seul l’ordre des deux listes déroulantes a été inversé.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Articles connexes**
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/javascript-cpp/add-page-field-in-pivot-table/) — la page mère qui présente l’ajout de champs de page à un tableau croisé dynamique.
- [Gérer les champs de valeur dans un tableau croisé dynamique](/cells/fr/javascript-cpp/manage-value-fields/) — explique comment configurer la zone des données (valeurs), notamment l’agrégation `Sum` utilisée dans cet article.
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/javascript-cpp/apply-style-to-pivot-table/) — montre comment mettre en forme le tableau croisé dynamique après avoir défini la disposition de la bande de champs de page.

{{< app/cells/assistant language="javascript-cpp" >}}