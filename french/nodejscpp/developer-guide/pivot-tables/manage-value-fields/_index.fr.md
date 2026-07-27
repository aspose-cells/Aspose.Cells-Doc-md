---
title: Gérer les champs de valeur d'un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Champs de valeur
description: Apprenez à ajouter des champs de base à la zone de données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.Function et à tracer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js via C++, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /fr/nodejs-cpp/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Ajout d'un champ à la zone de données
L'ajout d'un champ de base à la zone de données (valeur) est la première étape pour définir la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.addFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.Data` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.getDataFields()`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est synthétisée avec `ConsolidationFunction.Sum`, tandis qu'une colonne non numérique utilise `Count` par défaut.
## Modification de la fonction de synthèse
Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `getFunction()` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `setFunction()` vous permet de basculer entre les agrégats disponibles, notamment `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` et `Varp`.
{{% alert color="primary" %}}
La modification de la fonction de synthèse affecte uniquement l'agrégat, la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc laisser un champ de données avec `Sum` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `Count` ou `Average`, le tout dans un seul tableau croisé dynamique.
## Tracer les champs de valeur sur l'axe Ligne ou Colonne
Lorsqu'un tableau croisé dynamique contient au moins deux champs de données, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.getValuesField`. Ce champ virtuel représente l'agrégat de chaque champ de données présent dans la zone de données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ de base du tableau croisé dynamique, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` ne fonctionne pas s'il n'y a aucun champ de valeur ou seulement un.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque capacité décrite ci-dessus par rapport à la même structure de tableau croisé dynamique.
## Scénario 1 — Glisser un champ de base dans la zone Valeur
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

// Disposition du tableau croisé : Category et Item en ligne, Year en colonne, Amount comme champ de données
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## Scénario 2 — Modification de la fonction de synthèse
Ce scénario part de la même structure de tableau croisé dynamique que dans le scénario 1, mais ajoute le champ `Amount` deux fois à la zone de données. Les deux champs de données font référence à la même colonne source, cependant le second champ est redéfini à l'aide du setter `setFunction()` pour qu'il devienne `Count` au lieu du `Sum` par défaut.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
 worksheet.getCells().get(i, j).putValue(items[i - 1]);
 }
 else if (j == 2)
 {
 let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
 worksheet.getCells().get(i, j).putValue(years[i - 1]);
 }
 else
 {
 let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
 worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();

workbook.save("output_function.xlsx");
```
## Scénario 3 — Tracer les champs de valeur sur l'axe Ligne ou Colonne
Avec deux champs de données en place, `PivotTable.getValuesField()` devient utilisable. Ce scénario fait glisser ce champ virtuel d'agrégat sur la zone Colonne afin que chaque mesure de la zone de données apparaisse comme son propre bloc de colonnes à côté de `Year`.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

let categories = ["Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable"];
let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
let amounts = [100, 150, 80, 90, 50, 60, 40, 45];

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.getCells().get(i, j).putValue(categories[i - 1]);
 else if (j == 1) worksheet.getCells().get(i, j).putValue(items[i - 1]);
 else if (j == 2) worksheet.getCells().get(i, j).putValue(years[i - 1]);
 else worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField().getName());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

{{< app/cells/assistant language="javascript" >}}
