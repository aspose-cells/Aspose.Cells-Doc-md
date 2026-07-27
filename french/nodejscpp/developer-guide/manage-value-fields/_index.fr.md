---
title: Champs de valeur dans Aspose.Cells for Node.js via C++
linktitle: Champs de valeur dans Aspose.Cells for Node.js via C++
description: Apprenez à ajouter des champs de base à la zone de données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.Function et à placer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js, C++, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Somme, Moyenne
type: docs
weight: 230
url: /fr/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les champs de valeur constituent le cœur de chaque tableau croisé dynamique : ce sont les agrégats numériques qui résument les données sources. Dans Aspose.Cells for Node.js via C++, la zone de données d'un tableau croisé dynamique est remplie en y ajoutant des champs de base via `PivotTable.addFieldToArea`, et chaque champ placé dans cette zone peut disposer de sa propre fonction de synthèse. Lorsque deux champs de données ou plus existent, Aspose.Cells expose un champ d'agrégat spécial, `PivotTable.ValuesField`, qui peut être placé sur l'axe Ligne ou Colonne en tant que champ de base, vous offrant un contrôle plus fin sur l'affichage des champs de valeur dans la disposition.

## Ajout d'un champ à la zone de données

L'ajout d'un champ de base à la zone de données (zone de valeurs) constitue la première étape pour façonner la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.addFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.Data` ainsi que le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.DataFields`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est résumée avec `ConsolidationFunction.Sum`, tandis qu'une colonne non numérique utilise par défaut `Count`.

## Modification de la fonction de synthèse

Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `Function` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même accesseur `Function` vous permet de basculer entre les agrégats disponibles, notamment `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` et `Varp`.

{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat ; la colonne source ne change pas.
{{% /alert %}}

Vous pouvez donc conserver un champ de données en tant que `Sum` tout en ajoutant un second champ de données ciblant la même colonne source mais utilisant `Count` ou `Average`, le tout dans un seul tableau croisé dynamique.

## Placement des champs de valeur sur l'axe Ligne ou Colonne

Lorsqu'un tableau croisé dynamique contient deux champs de données ou plus, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.ValuesField`. Ce champ virtuel représente l'agrégat de chaque champ de données présent dans la zone de données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ croisé dynamique de base, ce qui est utile pour disposer plusieurs mesures côte à côte.

{{% alert color="primary" %}}
`PivotTable.ValuesField` ne fonctionne pas s'il n'y a aucun champ de valeur ou s'il n'y en a qu'un seul.
{{% /alert %}}

Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque fonctionnalité décrite ci-dessus en s'appuyant sur la même structure de tableau croisé dynamique.

## Scénario 1 — Glissement d'un champ de base dans la zone Valeurs

Ce scénario montre comment placer un seul champ de base (`Amount`) dans la zone de données d'un tableau croisé dynamique existant. La structure partagée du tableau croisé dynamique place `Category` et `Item` sur l'axe Ligne et `Year` sur l'axe Colonne. Après l'opération, `Amount` apparaît dans la zone de données et est calculé comme la `Sum` de `Amount` par défaut.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// En-têtes dans A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Lignes de données A2:D9 utilisant des boucles imbriquées avec branchement sur j
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i === 1 || i === 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i === 3 || i === 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i === 5 || i === 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i === 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i === 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i === 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i === 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i === 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i === 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i === 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// Ajouter un tableau croisé dynamique à F3 avec le nom PivotTable1
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Disposition du tableau croisé dynamique : Category et Item sur Ligne, Year sur Colonne, Amount comme champ de données
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Scénario 2 — Modification de la fonction de synthèse

Ce scénario part de la même structure de tableau croisé dynamique que le scénario 1, mais ajoute deux fois le champ `Amount` à la zone de données. Les deux champs de données font référence à la même colonne source ; cependant, le second champ est modifié à l'aide de l'accesseur `PivotField.Function` afin qu'il devienne `Count` au lieu de la valeur par défaut `Sum`.

<!-- CODE_BLOCK:1:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice so that pivotTable.getDataFields().getCount() equals 2. Retrieve the second data field via pivotTable.getDataFields().get(1) and assign countField.setFunction(ConsolidationFunction.Count) to change its summary function from the default Sum to Count; the first data field remains Sum of Amount. Demonstrate that the Function setter can also be assigned ConsolidationFunction.Average, Max, Min, etc. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_function.xlsx"). -->

## Scénario 3 — Placement des champs de valeur sur l'axe Ligne ou Colonne

Avec deux champs de données en place, `PivotTable.ValuesField` devient utilisable. Ce scénario fait glisser ce champ virtuel d'agrégat dans la zone Colonne afin que chaque mesure présente dans la zone de données apparaisse comme son propre bloc de colonnes à côté de `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

Ensemble, ces trois scénarios couvrent tous les aspects de la manipulation des champs de valeur dans Aspose.Cells for Node.js via C++, depuis un seul champ de données avec la valeur par défaut `Sum` jusqu'à un tableau croisé dynamique multi-mesures dans lequel le champ virtuel `ValuesField` contrôle la disposition sur l'axe Ligne ou Colonne.

## Articles connexes

- [Champs Ligne et Colonne d'un tableau croisé dynamique dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/row-and-column-fields/)
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}