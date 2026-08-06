---
title: Modifier la disposition des champs de page dans un tableau croisé dynamique
linktitle: Modifier la disposition des champs de page dans un tableau croisé dynamique
description: Apprenez à contrôler la disposition de la zone des champs de page dans un tableau croisé dynamique à l'aide d'Aspose.Cells for Node.js via C++, y compris la définition de l'ordre d'affichage, du nombre de champs de page par ligne ou colonne et de l'ordre des champs de page en haut du tableau croisé dynamique.
keywords: Aspose.Cells, Node.js via C++ library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /fr/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Cet article fait suite au sujet **Ajouter un champ de page dans un tableau croisé dynamique**. Il montre comment contrôler la disposition de la zone des champs de page — la barre de contrôles de filtre située en haut d'un tableau croisé dynamique — y compris l'ordre d'affichage, le nombre de champs de page par ligne ou colonne et le réordonnancement des champs.
{{% /alert %}}
## **Introduction**
Un tableau croisé dynamique dans Microsoft Excel expose une **zone de champs de page** dédiée qui se trouve au-dessus du corps lignes/colonnes/données du tableau. Cette zone est rendue sous forme d'une barre de contrôles déroulants (un par champ de page) et c'est ce sur quoi les utilisateurs finaux cliquent pour filtrer le tableau croisé dynamique selon des critères tels que l'année ou la région. Aspose.Cells for Node.js via C++ modélise cette zone via la collection `pivotTable.pageFields` et expose trois propriétés qui contrôlent la disposition visuelle de la barre :
- `pivotTable.pageFieldOrder` (une valeur `Aspose.Cells.PrintOrderType`) décide si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous*.
- `pivotTable.pageFieldWrapCount` définit combien de champs de page sont placés par ligne ou par colonne avant d'effectuer un retour à la ligne.
- `pivotTable.pageFields.move(currIndex, destIndex)` réorganise les champs de page sans modifier le mode d'ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données partagé, afin que vous puissiez comparer les dispositions résultantes côte à côte.
## **Données source**
Les trois exemples ci-dessous chargent ces huit lignes de données de ventes dans une feuille de calcul nommée `PivotData`. Les données contiennent deux candidats aux champs de page (`Year`, `Region`), un candidat au champ de ligne (`Fruit`) et une mesure (`Amount`), ce qui rend la barre des champs de page significative à inspecter.
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
Les huit lignes sont remplies dans chaque exemple de code, dans un ordre identique, de sorte que les données source ne diffèrent jamais d'un scénario à l'autre — seules les propriétés de disposition des champs de page changent.
## **Exemple 1 : Horizontal puis vertical (Over Then Down)**
Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) pour qu'ils apparaissent **côte à côte sur une seule ligne** en haut du tableau croisé dynamique. Nous affectons `Fruit` à l'axe des lignes, plaçons `Year` en premier et `Region` en second sur l'axe des pages (l'ordre des appels `addFieldToArea` détermine l'index de départ), ajoutons `Amount` (Somme) comme champ de données, puis définissons `pageFieldOrder` sur `PrintOrderType.OverThenDown` avec `pageFieldWrapCount = 2`. Avec `OverThenDown` et un retour à la ligne après 2 champs, les deux champs de page sont disposés horizontalement côte à côte sur une seule ligne en haut du tableau croisé dynamique, de sorte que la barre occupe une ligne d'une largeur de deux.
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// En-têtes (ligne 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Ligne 1 : Pomme, 2022, Nord, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Ligne 2 : Pomme, 2023, Nord, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Ligne 3 : Banane, 2022, Sud, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Ligne 4 : Banane, 2023, Sud, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Ligne 5 : Cerise, 2022, Est, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Ligne 6 : Cerise, 2023, Est, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Ligne 7 : Raisin, 2022, Ouest, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Ligne 8 : Raisin, 2023, Ouest, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Ajouter la feuille PivotTableReport
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// Créer un tableau croisé dynamique à partir de PivotData!A1:D9 placé en A1 sur PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Ajouter des champs
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Année
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Région
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Montant
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Configurer la disposition de la zone des champs de page : placer les champs de page en travers d'abord, retourner après chaque 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Actualiser et calculer
pivotTable.calculateData();

// Enregistrer
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **Exemple 2 : Vertical puis horizontal (Down Then Over)**
Dans cet exemple, nous plaçons `Fruit` sur l'axe des lignes, `Year` et `Region` sur l'axe des pages (avec `Year` en premier), et `Amount` (Somme) comme champ de données — exactement comme dans l'exemple 1. Nous définissons ensuite `pageFieldOrder` sur `PrintOrderType.DownThenOver` et `pageFieldWrapCount` sur `2`. Avec `DownThenOver` et un retour à la ligne après 2 champs, les deux champs de page sont empilés verticalement — `Year` en haut, `Region` directement en dessous — formant une seule colonne en haut du tableau croisé dynamique. La barre occupe donc deux lignes d'une largeur de un, contrairement à l'exemple 1.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);

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

const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **Exemple 3 : Déplacer un champ de page**
Dans le troisième scénario, nous conservons ce jeu de données et cette affectation des champs, définissons une disposition neutre (`OverThenDown` avec un retour à la ligne après 2 champs), puis démontrons l'opération `pageFields.move`. L'appel `move(0, 1)` déplace le champ de page à l'index 0 (`Year`) vers la position 1, et le champ de page qui se trouvait à la position 1 (`Region`) glisse vers la position 0. Après cet appel, `Region` est le premier champ de page et `Year` est le second. Le mode de retour à la ligne et le mode d'ordre restent inchangés, donc la barre est toujours rendue horizontalement côte à côte — seul l'ordre des deux listes déroulantes a été inversé.
```javascript
const AsposeCells = require("aspose.cells");

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

const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);

const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

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
## **Articles connexes**
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/) — la page parente qui présente comment les champs de page sont ajoutés à un tableau croisé dynamique.
- [Champs de lignes et de colonnes dans un tableau croisé dynamique](/cells/fr/nodejs-cpp/row-and-column-fields/) — couvre l'affectation des champs aux axes des lignes et des colonnes, complétant le travail sur l'axe des pages présenté ici.
- [Gérer les champs de valeurs dans un tableau croisé dynamique](/cells/fr/nodejs-cpp/manage-value-fields/) — décrit comment configurer la zone des données (valeurs), y compris l'agrégation `Sum` utilisée dans cet article.
- [Actualiser un tableau croisé dynamique](/cells/fr/nodejs-cpp/refresh-pivot-table/) — explique `refreshData` et `calculateData`, qui sont requis après le réordonnancement des champs de page.
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/) — montre comment formater le tableau croisé dynamique rendu après que la barre des champs de page a été disposée.
{{< app/cells/assistant language="nodejs-cpp" >}}