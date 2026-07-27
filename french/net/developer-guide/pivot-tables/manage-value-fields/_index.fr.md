---
title: Gérer les champs de valeur d'un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Champs de valeur
description: Apprenez à ajouter des champs de base à la zone de données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.Function et à tracer le champ de valeur sur l'axe des lignes ou des colonnes dans Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /fr/net/pivot-table-manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Ajout d'un champ à la zone de données
L'ajout d'un champ de base à la zone de données (valeur) constitue la première étape pour définir la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.AddFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.Data` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.DataFields`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est résumée avec `ConsolidationFunction.Sum`, tandis qu'une colonne non numérique utilise par défaut `Count`.
## Modification de la fonction de synthèse
Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `Function` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même accesseur `Function` vous permet de basculer entre les agrégats disponibles, notamment `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` et `Varp`.
{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat ; la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc laisser un champ de données en tant que `Sum` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `Count` ou `Average`, le tout dans un seul tableau croisé dynamique.
## Traçage des champs de valeur sur l'axe des lignes ou des colonnes
Lorsqu'un tableau croisé dynamique contient au moins deux champs de données, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.ValuesField`. Ce champ virtuel représente l'agrégat de chaque champ de données présent dans la zone de données. Vous pouvez le faire glisser dans la zone des lignes ou des colonnes en tant que champ croisé dynamique de base, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.ValuesField` ne fonctionne pas s'il n'y a aucun ou un seul champ de valeur.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque capacité décrite ci-dessus par rapport à la même structure de tableau croisé dynamique.
## Scénario 1 — Glisser un champ de base dans la zone des valeurs
Ce scénario montre comment placer un seul champ de base (`Amount`) dans la zone de données d'un tableau croisé dynamique existant. La structure partagée du tableau croisé dynamique place `Category` et `Item` sur l'axe des lignes et `Year` sur l'axe des colonnes. Après l'opération, `Amount` apparaît dans la zone de données et est calculé comme la `Sum` de `Amount` par défaut.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// En-têtes dans A1:D1
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// Lignes de données A2:D9 utilisant des boucles imbriquées avec branchement sur j
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.Cells[i, j].PutValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.Cells[i, j].PutValue("Apple");
 else if (i == 3 || i == 4) worksheet.Cells[i, j].PutValue("Banana");
 else if (i == 5 || i == 6) worksheet.Cells[i, j].PutValue("Carrot");
 else worksheet.Cells[i, j].PutValue("Daikon");
 break;
 case 2:
 worksheet.Cells[i, j].PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.Cells[i, j].PutValue(100);
 else if (i == 2) worksheet.Cells[i, j].PutValue(150);
 else if (i == 3) worksheet.Cells[i, j].PutValue(80);
 else if (i == 4) worksheet.Cells[i, j].PutValue(90);
 else if (i == 5) worksheet.Cells[i, j].PutValue(50);
 else if (i == 6) worksheet.Cells[i, j].PutValue(60);
 else if (i == 7) worksheet.Cells[i, j].PutValue(40);
 else worksheet.Cells[i, j].PutValue(45);
 break;
 }
 }
}

// Ajouter un tableau croisé dynamique à F3 avec le nom PivotTable1
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Mise en page du tableau croisé : Catégorie et Article sur Ligne, Année sur Colonne, Montant comme champ de données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```
## Scénario 2 — Modification de la fonction de synthèse
Ce scénario part de la même structure de tableau croisé dynamique que le scénario 1, mais ajoute deux fois le champ `Amount` à la zone de données. Les deux champs de données font référence à la même colonne source, cependant le second champ est modifié à l'aide de l'accesseur `PivotField.Function` afin qu'il devienne `Count` au lieu du `Sum` par défaut.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.Cells[i, j].PutValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
 worksheet.Cells[i, j].PutValue(items[i - 1]);
 }
 else if (j == 2)
 {
 int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
 worksheet.Cells[i, j].PutValue(years[i - 1]);
 }
 else
 {
 int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };
 worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");

pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;

pivotTable.CalculateData();

workbook.Save("output_function.xlsx");
```
## Scénario 3 — Tracer les champs de valeur sur l'axe des lignes ou des colonnes
Avec deux champs de données en place, `PivotTable.ValuesField` devient utilisable. Ce scénario fait glisser ce champ virtuel agrégé sur la zone des colonnes afin que chaque mesure de la zone de données apparaisse comme son propre bloc de colonnes à côté de `Year`.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

string[] categories = { "Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable" };
string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.Cells[i, j].PutValue(categories[i - 1]);
 else if (j == 1) worksheet.Cells[i, j].PutValue(items[i - 1]);
 else if (j == 2) worksheet.Cells[i, j].PutValue(years[i - 1]);
 else worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.DataFields[1].Function = ConsolidationFunction.Count;

pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);

pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```
## Articles connexes
- [Champs de lignes et de colonnes du tableau croisé dynamique dans Aspose.Cells for .NET](/cells/fr/net/row-and-column-fields/)
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/net/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
