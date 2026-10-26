---
title: Modifier la disposition des champs de page dans un Tableau Croisé Dynamique
linktitle: Modifier la disposition des champs de page dans un Tableau Croisé Dynamique
description: Apprendre à contrôler la disposition de la zone des champs de page dans un Tableau Croisé Dynamique à l’aide d’Aspose.Cells for Node.js via C++, notamment en définissant l’ordre d’affichage, le nombre de champs avant le retour à la ligne et l’ordre des champs de page en haut du Tableau Croisé Dynamique.
keywords: Aspose.Cells, bibliothèque Node.js via C++, tableur, Tableau Croisé Dynamique, champ de page, ordre des champs de page, nombre de champs de page avant le retour à la ligne, déplacement d’un champ de page
type: docs
weight: 191
url: /fr/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Cet article est la suite de la rubrique **Ajouter un champ de page dans un Tableau Croisé Dynamique**. Il illustre comment contrôler la disposition de la zone des champs de page — le bandeau de contrôles de filtre situé en haut d’un Tableau Croisé Dynamique — y compris l’ordre d’affichage, le nombre de champs avant le retour à la ligne et le réordonnancement des champs.
{{% /alert %}}

## **Introduction**
Un Tableau Croisé Dynamique dans Microsoft Excel expose une **zone de champs de page** dédiée, située au-dessus du corps des lignes, des colonnes et des données du tableau. Cette zone est affichée sous la forme d’un bandeau de contrôles de filtre déroulants (un par champ de page). Les utilisateurs finaux cliquent sur ces contrôles pour filtrer le Tableau Croisé Dynamique selon des critères tels que l’année ou la région. Aspose.Cells for Node.js via C++ modélise cette zone par la collection `pivotTable.pageFields` et expose trois propriétés qui contrôlent sa disposition visuelle :
- `pivotTable.pageFieldOrder` (une valeur `Aspose.Cells.PrintOrderType`) détermine si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous*.
- `pivotTable.pageFieldWrapCount` définit le nombre de champs de page à placer par ligne ou colonne avant le retour à la ligne.
- `pivotTable.pageFields.move(currIndex, destIndex)` réordonne les champs de page sans modifier le mode d’ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données commun, afin de pouvoir comparer les dispositions obtenues.

## **Source Data**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Les huit lignes sont renseignées dans chaque exemple de code et dans le même ordre, de sorte que les données source ne varient jamais entre les scénarios — seules les propriétés de disposition des champs de page changent.

## **Example 1: Over Then Down**
Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) pour qu’ils apparaissent **côte à côte sur une seule ligne** en haut du Tableau Croisé Dynamique. Nous affectons `Fruit` à l’axe des lignes, plaçons `Year` en premier et `Region` en second sur l’axe des pages (l’ordre des appels `addFieldToArea` détermine l’index de départ), ajoutons `Amount` (`Sum`) comme champ de données, puis définissons `pageFieldOrder` sur `PrintOrderType.OverThenDown` et `pageFieldWrapCount = 2`. Avec `OverThenDown` et une valeur de 2 pour le nombre de champs avant le retour à la ligne, les deux champs de page sont disposés horizontalement, côte à côte sur une seule ligne en haut du Tableau Croisé Dynamique. Le bandeau occupe donc une ligne et deux colonnes.

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
const path = require("path");
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}
let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();
let pivotDataSheet = worksheets.add("PivotData");
let pivotDataCells = pivotDataSheet.getCells();
// Headers (row 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// Row 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// Row 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// Row 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// Row 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// Row 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// Row 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// Row 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// Row 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// Add PivotTableReport sheet
let pivotTableSheet = worksheets.add("PivotTableReport");
let pivotTables = pivotTableSheet.getPivotTables();
// Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
let pivotTable = pivotTables.add("PivotData!A1:D9", 0, 0);
// Add fields
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);
// Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
// Refresh and calculate
pivotTable.calculateData();
// Save
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Example 2: Down Then Over**
Dans cet exemple, nous plaçons `Fruit` sur l’axe des lignes, `Year` et `Region` sur l’axe des pages (avec `Year` en premier), et `Amount` (`Sum`) comme champ de données — exactement comme dans l’exemple 1. Nous définissons ensuite `pageFieldOrder` sur `PrintOrderType.DownThenOver` et `pageFieldWrapCount` sur `2`. Avec `DownThenOver` et une valeur de 2 pour le nombre de champs avant le retour à la ligne, les deux champs de page sont empilés verticalement — `Year` au-dessus et `Region` juste en dessous — pour former une seule colonne en haut du Tableau Croisé Dynamique. Le bandeau occupe donc deux lignes et une seule colonne, contrairement à l’exemple 1.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReport = workbook.getWorksheets().add("PivotTableReport");
const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
const pivotTable = pivotReport.getPivotTables().add("PivotData!A1:D9", 0, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**
Dans le troisième scénario, nous conservons ce jeu de données et cette répartition des champs, définissons une disposition neutre (`OverThenDown` avec une valeur de `2` pour le nombre de champs avant le retour à la ligne), puis illustrons l’opération `pageFields.move`. L’appel `move(0, 1)` déplace le champ de page situé à l’index 0 (`Year`) vers la position 1, tandis que le champ de page qui occupait la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` est le second. Le mode de retour à la ligne et le mode d’ordre restent inchangés. Le bandeau est donc toujours affiché horizontalement, côte à côte — seul l’ordre des deux listes déroulantes a été inversé.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
const pivotSheet = workbook.getWorksheets().add("PivotTableReport");
const pivotTable = pivotSheet.getPivotTables().add("PivotData!A1:D9", 2, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Related Articles**
- [Ajouter un champ de page dans un Tableau Croisé Dynamique](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/) — la page parente qui présente l’ajout de champs de page à un Tableau Croisé Dynamique.
- [Champs de ligne et de colonne dans un Tableau Croisé Dynamique](/cells/fr/nodejs-cpp/row-and-column-fields/) — explique l’affectation de champs aux axes des lignes et des colonnes en complément du travail sur l’axe des pages présenté ici.
- [Gérer les champs de valeur dans un Tableau Croisé Dynamique](/cells/fr/nodejs-cpp/manage-value-fields/) — décrit comment configurer la zone des données (valeurs), y compris l’agrégation `Sum` utilisée dans cet article.
- [Actualiser un Tableau Croisé Dynamique](/cells/fr/nodejs-cpp/refresh-pivot-table/) — explique `refreshData` et `calculateData`, qui sont nécessaires après le réordonnancement des champs de page.
- [Appliquer un style à un Tableau Croisé Dynamique](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/) — montre comment mettre en forme le Tableau Croisé Dynamique rendu après la disposition du bandeau de champs de page.

{{< app/cells/assistant language="nodejs-cpp" >}}