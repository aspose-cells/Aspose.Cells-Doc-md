---
title: Regroupement discret des éléments de champ pivot
description: Apprenez à regrouper les éléments de champ pivot en groupes personnalisés portant un nom, tels que les fruits et les légumes, à l’aide de DiscreteGroupItem et PivotFieldGroupOptions.DiscreteGroupItems dans Aspose.Cells for .NET.
linktitle: Regroupement discret
keywords: Aspose.Cells, Tableau Croisé Dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regroupement des éléments de champ pivot, groupes personnalisés, PivotField.Group, C#, Tableau Croisé Dynamique Excel
type: docs
weight: 90
url: /fr/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique collecte les éléments par type de données, par exemple les dates en mois et trimestres ou les nombres en plages. Le regroupement discret résout le problème inverse : regrouper des éléments spécifiques et non apparentés en groupes personnalisés portant un nom, par exemple des produits en fruits et légumes, des magasins en régions ou des comptes en zones. Aspose.Cells fournit le regroupement discret au moyen de la classe `DiscreteGroupItem` et de la propriété `PivotFieldGroupOptions.DiscreteGroupItems`.
- Un `DiscreteGroupItem` est composé d’un nom de groupe et des éléments qui lui appartiennent. Les éléments peuvent être identifiés de deux manières, par leur nom (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) ou par leur position à base zéro dans les données source (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Les deux formes produisent le même résultat.
- Le regroupement discret est appliqué à un champ situé dans la zone de lignes ou de colonnes du Tableau Croisé Dynamique en transmettant les options à `PivotField.Group(PivotFieldGroupOptions)`.

## **Regrouper les éléments de champ pivot par nom d’élément**
L’exemple suivant construit une petite liste de ventes (produit, date et montant), crée un Tableau Croisé Dynamique à partir de celle-ci avec `product` dans la zone de lignes, `date` dans la zone de colonnes et `amount` dans la zone de données, puis définit deux groupes personnalisés par nom d’élément, `fruit` (`grape`, `cherry`) et `vegetables` (`carrot`, `potato`). Le résultat affiche une disposition des lignes à deux niveaux, avec le nom du groupe au niveau extérieur et les éléments d’origine imbriqués au-dessous, afin de permettre la lecture des tendances par groupe personnalisé et par élément.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

Après `CalculateData()`, la zone de lignes du Tableau Croisé Dynamique affiche `fruit` (`grape` 50, `cherry` 80) et `vegetable` (`carrot` 60, `potato` 70), avec un total général de 260, tandis que les libellés de colonnes conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regrouper les éléments de champ pivot par index d’élément**
Lorsque les noms d’éléments sont longs ou localisés, le second constructeur de `DiscreteGroupItem` identifie les éléments par index. Les index correspondent aux positions à base zéro des éléments dans l’ordre dans lequel ils apparaissent dans les données source, et non à l’ordre alphabétique. Dans les données d’exemple ci-dessus, `grape` est l’élément 0, `carrot` est l’élément 1, `potato` est l’élément 2 et `cherry` est l’élément 3. Le groupe `fruit` correspond donc à `{ 0, 3 }` et le groupe `vegetable` à `{ 1, 2 }`. Le résultat est identique à celui de l’exemple fondé sur les noms.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont affectés à aucun groupe personnalisé ne sont pas perdus. Ils restent dans le Tableau Croisé Dynamique au même niveau que les groupes personnalisés, chacun constituant une entrée distincte composée d’un seul élément. Dans l’exemple ci-dessus, la définition du seul groupe `fruit` laisse `carrot` et `potato` dans la zone de lignes sous forme d’entrées autonomes à côté du groupe `fruit`.
- La propriété `PivotFieldGroupOptions.NewPivotField` contrôle la disposition du regroupement discret. Sa valeur par défaut est `true`, ce qui ajoute le champ regroupé comme nouveau champ extérieur à côté du champ d’origine et produit la disposition à deux niveaux illustrée ci-dessus (`RowFields` passe à 2). Définissez-la sur `false` pour remplacer le champ d’origine. La zone de lignes affiche alors un seul niveau contenant uniquement les noms des groupes et leurs valeurs agrégées, soit `fruit` 130 (50 + 80) et `vegetable` 130 (60 + 70).
- Les constructeurs de `DiscreteGroupItem` fondés sur les noms et sur les index peuvent être combinés dans le même tableau `DiscreteGroupItems`.
{{% /alert %}}

## **Articles connexes**
- [Regrouper les champs pivot dans le Tableau Croisé Dynamique](/cells/fr/net/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne dans un Tableau Croisé Dynamique](/cells/fr/net/pivot-table-add-row-and-column-fields/)
- [Filtrer les Tableaux Croisés Dynamiques par libellé ou valeur](/cells/fr/net/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style au Tableau Croisé Dynamique](/cells/fr/net/apply-style-to-pivot-table/)
- [Actualiser le Tableau Croisé Dynamique](/cells/fr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}