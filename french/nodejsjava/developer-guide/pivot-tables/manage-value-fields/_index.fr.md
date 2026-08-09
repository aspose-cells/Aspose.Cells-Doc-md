---
title: Champs de valeur dans Aspose.Cells for Node.js via Java
linktitle: Champs de valeur dans Aspose.Cells for Node.js via Java
description: Apprenez à ajouter des champs de base à la zone de données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.Function, et à tracer le champ de valeur sur l'axe des Lignes ou des Colonnes dans Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /fr/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les champs de valeur constituent le cœur de chaque tableau croisé dynamique, ce sont les agrégats numériques qui résument les données sources. Dans Aspose.Cells for Node.js via Java, la zone de données d'un tableau croisé dynamique est alimentée en y ajoutant des champs de base via `PivotTable.addFieldToArea`, et chaque champ placé dans cette zone peut disposer de sa propre fonction de synthèse. Lorsque deux champs de données ou plus existent, Aspose.Cells expose un champ agrégé spécial, `PivotTable.getValuesField()`, qui peut être tracé sur l'axe des Lignes ou des Colonnes en tant que champ de base, vous offrant un contrôle plus fin sur l'apparence des champs de valeur dans la disposition.
## Ajout d'un champ à la zone de données
L'ajout d'un champ de base à la zone de données (valeurs) constitue la première étape pour définir la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.addFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.DATA` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.getDataFields()`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est résumée avec `ConsolidationFunction.SUM`, tandis qu'une colonne non numérique utilise `COUNT` par défaut.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Modification de la fonction de synthèse
Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `getFunction()` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `setFunction()` permet de basculer entre les agrégats disponibles, notamment `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` et `VARP`.
{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat, la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc conserver un champ de données en tant que `SUM` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `COUNT` ou `AVERAGE`, le tout dans un seul tableau croisé dynamique.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## Tracé des champs de valeur sur l'axe des Lignes ou des Colonnes
Lorsqu'un tableau croisé dynamique contient deux champs de données ou plus, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.getValuesField()`. Ce champ virtuel représente l'agrégat de chaque champ de données qui se trouve dans la zone de données. Vous pouvez le faire glisser dans la zone des Lignes ou des Colonnes en tant que champ de base du tableau croisé dynamique, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` ne fonctionne pas s'il n'y a aucun champ de valeur ou s'il n'y en a qu'un seul.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque fonctionnalité décrite ci-dessus sur la même structure de tableau croisé dynamique.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
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