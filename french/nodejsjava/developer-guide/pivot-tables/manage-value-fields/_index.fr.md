---
title: Gérer les champs de valeur d'un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Champs de valeur
description: Apprenez à ajouter des champs de base à la zone de données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.Function, et à tracer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Somme, Moyenne
type: docs
weight: 230
url: /fr/nodejs-java/pivot-table-manage-value-fields/
/fr/nodejs-java/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
Les champs de valeur constituent le cœur de chaque tableau croisé dynamique : ce sont les agrégats numériques qui résument les données sources. Dans Aspose.Cells for Node.js via Java, la zone de données d'un tableau croisé dynamique est remplie en y ajoutant des champs de base via `PivotTable.addFieldToArea`, et chaque champ placé dans cette zone peut disposer de sa propre fonction de synthèse. Lorsqu'au moins deux champs de données existent, Aspose.Cells expose un champ d'agrégat spécial, `PivotTable.getValuesField()`, qui peut être tracé sur l'axe Ligne ou Colonne en tant que champ de base, offrant ainsi un contrôle plus fin sur l'affichage des champs de valeur dans la disposition.
## Ajout d'un champ à la zone de données
L'ajout d'un champ de base à la zone de données (valeur) est la première étape pour définir la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.addFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.DATA` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.getDataFields()`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est synthétisée avec `ConsolidationFunction.SUM`, tandis qu'une colonne non numérique utilise par défaut `COUNT`.
## Modification de la fonction de synthèse
Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `getFunction()` renvoie une valeur de l'énumération `ConsolidationFunction`. L'accesseur `setFunction()` vous permet également de basculer entre les agrégats disponibles, notamment `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` et `VARP`.
{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat, la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc conserver un champ de données comme `SUM` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `COUNT` ou `AVERAGE`, le tout dans un seul tableau croisé dynamique.
## Tracer les champs de valeur sur l'axe Ligne ou Colonne
Lorsqu'un tableau croisé dynamique contient au moins deux champs de données, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.getValuesField()`. Ce champ virtuel représente l'agrégat de chaque champ de données présent dans la zone de données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ de tableau croisé dynamique de base, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` ne fonctionne pas s'il n'y a aucun ou un seul champ de valeur.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque capacité décrite ci-dessus par rapport à la même structure de tableau croisé dynamique.
## Scénario 1 — Glissement d'un champ de base dans la zone de valeurs
Ce scénario montre comment placer un seul champ de base (`Amount`) dans la zone de données d'un tableau croisé dynamique existant. La structure partagée du tableau croisé dynamique place `Category` et `Item` sur l'axe Ligne et `Year` sur l'axe Colonne. Après l'opération, `Amount` apparaît dans la zone de données et est calculé comme la `Somme` de `Amount` par défaut.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// En-têtes dans A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Lignes de données A2:D9 utilisant des boucles imbriquées avec un branchement sur j
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// Ajouter un tableau croisé dynamique à F3 avec le nom PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Disposition du tableau croisé dynamique : Category et Item en ligne, Year en colonne, Amount comme champ de données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## Scénario 2 — Modification de la fonction de synthèse
Ce scénario part de la même structure de tableau croisé dynamique que le scénario 1, mais ajoute le champ `Amount` deux fois dans la zone de données. Les deux champs de données référencent la même colonne source ; cependant, le second champ est remplacé à l'aide de l'accesseur `PivotField.setFunction()` afin qu'il devienne `COUNT` au lieu du `SUM` par défaut.
## Scénario 3 — Tracer les champs de valeur sur l'axe Ligne ou Colonne
Avec deux champs de données en place, `PivotTable.getValuesField()` devient utilisable. Ce scénario fait glisser ce champ virtuel d'agrégat dans la zone Colonne, de sorte que chaque mesure de la zone de données apparaisse comme son propre bloc de colonnes à côté de `Year`.
Ensemble, ces trois scénarios couvrent tous les aspects de la manipulation des champs de valeur dans Aspose.Cells for Node.js via Java, d'un seul champ de données avec le `SUM` par défaut à un tableau croisé dynamique multi-mesures dans lequel le `ValuesField` virtuel contrôle la disposition sur l'axe Ligne ou Colonne.
## Articles connexes
- [Champs de ligne et de colonne du tableau croisé dynamique dans Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/row-and-column-fields/)
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/nodejs-java/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}