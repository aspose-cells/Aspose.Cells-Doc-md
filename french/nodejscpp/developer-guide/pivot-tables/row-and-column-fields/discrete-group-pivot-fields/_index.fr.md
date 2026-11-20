---
title: Regroupement discret des éléments de champ de tableau croisé dynamique
linktitle: Regroupement discret
description: Apprenez comment regrouper les éléments de champ de tableau croisé dynamique dans des groupes nommés personnalisés comme fruits et légumes en utilisant DiscreteGroupItem et PivotFieldGroupOptions.DiscreteGroupItems dans Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, tableau croisé dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regrouper les éléments de tableau croisé dynamique, groupes personnalisés, PivotField.Group, Node.js, tableau croisé dynamique Excel
type: docs
weight: 90
url: /fr/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique rassemble les éléments par type de données, comme les dates en mois et trimestres ou les nombres en plages. Le regroupement discret résout le problème opposé, en rassemblant des éléments spécifiques et non liés dans des groupes nommés personnalisés, par exemple les produits en fruits et légumes, les magasins en régions, ou les comptes en zones. Aspose.Cells for Node.js via C++ fournit le regroupement discret via la classe `DiscreteGroupItem` et la propriété `PivotFieldGroupOptions.discreteGroupItems`.
- `DiscreteGroupItem` est un nom de groupe ainsi que les éléments qui y appartiennent. Les éléments peuvent être identifiés de deux manières, par leurs noms (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) ou par leurs positions indexées à zéro dans les données source (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Les deux formes produisent le même résultat.
- Le regroupement discret est appliqué à un champ dans la zone de ligne ou de colonne du tableau croisé dynamique en transmettant les options à `pivotField.group(pivotFieldGroupOptions)`.

## **Regrouper les éléments de champ de tableau croisé dynamique par noms d’éléments**
L’exemple suivant crée une petite liste de ventes (produit, date et montant), crée un tableau croisé dynamique à partir de celle‑ci avec `product` dans la zone de lignes, `date` dans la zone de colonnes et `amount` dans la zone de données, puis définit deux groupes personnalisés par noms d’éléments, fruits (grape, cherry) et légumes (carrot, potato). Le résultat montre une disposition de lignes à deux niveaux, le nom du groupe étant le niveau externe et les éléments d’origine imbriqués en dessous, de sorte que les tendances puissent être lues par groupe personnalisé et par élément.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Après `calculateData()`, la zone de lignes du tableau croisé dynamique affiche les fruits (grape 50, cherry 80) et les légumes (carrot 60, potato 70) avec le total général de 260, et les étiquettes de colonnes conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regrouper les éléments de champ de tableau croisé dynamique par indices d’éléments**
Lorsque les noms des éléments sont longs ou localisés, le deuxième constructeur de `DiscreteGroupItem` identifie les éléments par leur indice. Les indices sont des positions indexées à zéro des éléments dans l’ordre où ils apparaissent dans les données source, et non pas dans l’ordre alphabétique. Dans les données d’exemple ci‑dessus, grape est l’élément 0, carrot l’élément 1, potato l’élément 2 et cherry l’élément 3, ainsi fruit correspond à `{ 0, 3 }` et vegetable à `{ 1, 2 }`. Le résultat est identique à l’exemple basé sur les noms.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont pas affectés à aucun groupe personnalisé ne sont pas perdus. Ils restent dans le tableau croisé dynamique au même niveau que les groupes personnalisés, chacun sous forme d’une entrée à un seul élément. Dans l’exemple ci‑dessus, la définition du seul groupe fruit laisse carrot et potato dans la zone de lignes en tant qu’entrées autonomes à côté du groupe fruit.
- La propriété `PivotFieldGroupOptions.newPivotField` contrôle la disposition du regroupement discret. Elle vaut true par défaut, ce qui ajoute le champ groupé comme un nouveau champ externe à côté du champ original, produisant la disposition à deux niveaux illustrée ci‑dessus (`rowFields` passe à 2). Réglez‑la sur false pour remplacer le champ original, la zone de lignes affichera alors un seul niveau contenant uniquement les noms de groupes avec leurs valeurs agrégées, fruit 130 (50 + 80) et vegetable 130 (60 + 70).
- Les constructeurs basés sur les noms et sur les indices de `DiscreteGroupItem` peuvent être mélangés au sein du même tableau `PivotFieldGroupOptions.discreteGroupItems`.
{{% /alert %}}

## **Articles connexes**
- [Regrouper les champs de tableau croisé dynamique](/cells/fr/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne dans le tableau croisé dynamique](/cells/fr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)
- [Rafraîchir le tableau croisé dynamique](/cells/fr/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}