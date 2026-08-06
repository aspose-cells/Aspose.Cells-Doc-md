---
title: Modifier la disposition des champs de page dans un tableau croisé dynamique
linktitle: Modifier la disposition des champs de page dans un tableau croisé dynamique
description: Apprenez à contrôler la disposition de la zone des champs de page dans un tableau croisé dynamique à l'aide d'Aspose.Cells for .NET, y compris la définition de l'ordre d'affichage, du nombre de champs par ligne et de l'ordre des champs de page en haut du tableau croisé dynamique.
keywords: Aspose.Cells, bibliothèque .NET, feuille de calcul, tableau croisé dynamique, champ de page, ordre des champs de page, nombre de champs de page par ligne, déplacer un champ de page
type: docs
weight: 191
url: /fr/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Cet article fait suite au sujet **Ajouter un champ de page dans un tableau croisé dynamique**. Il montre comment contrôler la disposition de la zone des champs de page, c'est-à-dire la bande de contrôles de filtre située en haut d'un tableau croisé dynamique, y compris l'ordre d'affichage, le nombre de champs par ligne et la réorganisation des champs.

{{% /alert %}}

## **Introduction**

Un tableau croisé dynamique dans Microsoft Excel expose une **zone de champs de page** dédiée qui se trouve au-dessus du corps des lignes/colonnes/données du tableau. Cette zone est rendue sous la forme d'une bande de contrôles déroulants de filtrage (un par champ de page) ; ce sont eux sur lesquels les utilisateurs finaux cliquent pour découper le tableau croisé dynamique selon des critères tels que l'année ou la région. Aspose.Cells modélise cette zone via la collection `PivotTable.PageFields` et expose trois propriétés qui contrôlent la disposition visuelle de la bande :

- `PivotTable.PageFieldOrder` (une valeur `Aspose.Cells.PrintOrderType`) décide si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous*.
- `PivotTable.PageFieldWrapCount` définit combien de champs de page sont placés par ligne ou par colonne avant le retour à la ligne.
- `PivotTable.PageFields.Move(currIndex, destIndex)` réorganise les champs de page sans changer le mode d'ordre.

Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données partagé, afin que vous puissiez comparer les dispositions obtenues côte à côte.

## **Données sources**

Les trois exemples ci-dessous chargent ces huit lignes de données de ventes dans une feuille de calcul nommée `PivotData`. Les données contiennent deux candidats aux champs de page (`Year`, `Region`), un candidat au champ de ligne (`Fruit`) et une mesure (`Amount`), ce qui rend la bande des champs de page intéressante à examiner.

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

Les huit lignes sont renseignées dans chaque exemple de code, dans un ordre identique, de sorte que les données sources ne diffèrent jamais d'un scénario à l'autre ; seules les propriétés de disposition des champs de page changent.

## **Exemple 1 : D'abord horizontalement, puis verticalement**

Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) pour qu'ils apparaissent **côte à côte sur une seule ligne** en haut du tableau croisé dynamique. Nous assignons `Fruit` à l'axe des lignes, plaçons `Year` en premier et `Region` en second sur l'axe des pages (l'ordre des appels `AddFieldToArea` détermine l'indice de départ), ajoutons `Amount` (Somme) comme champ de données, puis définissons `PageFieldOrder` sur `PrintOrderType.OverThenDown` avec `PageFieldWrapCount = 2`. Avec `OverThenDown` et un nombre de champs par ligne de 2, les deux champs de page sont disposés horizontalement côte à côte sur une seule ligne en haut du tableau croisé dynamique, de sorte que la bande occupe une ligne d'une largeur de deux.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// En-têtes (ligne 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// Ligne 1 : Pomme, 2022, Nord, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Ligne 2 : Pomme, 2023, Nord, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Ligne 3 : Banane, 2022, Sud, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Ligne 4 : Banane, 2023, Sud, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Ligne 5 : Cerise, 2022, Est, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Ligne 6 : Cerise, 2023, Est, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Ligne 7 : Raisin, 2022, Ouest, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Ligne 8 : Raisin, 2023, Ouest, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// Ajouter la feuille PivotTableReport
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// Créer un tableau croisé dynamique à partir de PivotData!A1:D9 placé en A1 sur PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Ajouter des champs
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Fruit
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Année
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Région
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Montant
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Configurer la disposition de la zone des champs de page : placer les champs de page horizontalement d'abord, revenir à la ligne tous les 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Actualiser et calculer
pivotTable.CalculateData();

// Enregistrer
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Exemple 2 : D'abord verticalement, puis horizontalement**

Dans cet exemple, nous plaçons `Fruit` sur l'axe des lignes, `Year` et `Region` sur l'axe des pages (avec `Year` en premier) et `Amount` (Somme) comme champ de données, exactement comme dans l'exemple 1. Nous définissons ensuite `PageFieldOrder` sur `PrintOrderType.DownThenOver` et `PageFieldWrapCount` sur `2`. Avec `DownThenOver` et un nombre de champs par ligne de 2, les deux champs de page sont empilés verticalement : `Year` en haut, `Region` directement en dessous, formant une seule colonne en haut du tableau croisé dynamique. La bande occupe donc deux lignes d'une largeur de un, contrairement à l'exemple 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Exemple 3 : Déplacer un champ de page**

Dans le troisième scénario, nous conservons ce jeu de données et cette allocation des champs, définissons une disposition neutre (`OverThenDown` avec un nombre de champs par ligne de `2`), puis démontrons l'opération `PageFields.Move`. L'appel `Move(0, 1)` déplace le champ de page à l'indice 0 (`Year`) à la position 1, et le champ de page qui était à la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` est le second. Le mode d'ordre et le nombre de champs par ligne restent inchangés, donc la bande est toujours rendue horizontalement côte à côte ; seul l'ordre des deux listes déroulantes a été permuté.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **Articles connexes**

- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/net/add-page-field-in-pivot-table/) — la page parente qui présente comment ajouter des champs de page à un tableau croisé dynamique.
- [Champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/net/pivot-table-add-row-and-column-fields/) — couvre l'affectation des champs aux axes des lignes et des colonnes, en complément du travail sur l'axe des pages présenté ici.
- [Gérer les champs de valeur dans un tableau croisé dynamique](/cells/fr/net/manage-value-fields/) — décrit comment configurer la zone des données (valeurs), y compris l'agrégation `Sum` utilisée dans cet article.
- [Actualiser un tableau croisé dynamique](/cells/fr/net/refresh-pivot-table/) — explique `RefreshData` et `CalculateData`, qui sont requis après la réorganisation des champs de page.
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/net/apply-style-to-pivot-table/) — montre comment mettre en forme le tableau croisé dynamique rendu une fois que la bande des champs de page a été disposée.

{{< app/cells/assistant language="csharp" >}}