---
title: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Champs de ligne et de colonne
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /fr/nodejs-cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajout d'un champ à la région de ligne ou de colonne**

La méthode `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` déplace un champ de base des données source vers l'une des quatre régions du tableau croisé dynamique. L'argument `fieldType` accepte l'une des valeurs `PivotFieldType` suivantes.

- `Row` — champs placés verticalement à gauche
- `Column` — champs placés horizontalement en haut
- `Data` — champs dont les valeurs sont agrégées
- `Page` — champs utilisés comme filtres de rapport

Après l'ajout des champs, vous pouvez y accéder via les propriétés `PivotTable.RowFields` et `PivotTable.ColumnFields`. Chaque propriété renvoie une `PivotFieldCollection`. Le champ à l'index 0 de `RowFields` est le champ de ligne le plus externe, et les indices suivants représentent les champs imbriqués à l'intérieur. La même convention d'indexation s'applique à `ColumnFields`.

L'ordre d'imbrication des champs est important. L'ajout de `Category` à la région de ligne en premier, puis de `Item`, produit un tableau croisé dynamique dont le regroupement externe est `Category` et dont le regroupement interne est `Item`. L'inversion de l'ordre inverse la hiérarchie.

## **Sous-totaux des champs croisés**

La méthode `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` contrôle quelles lignes de sous-total apparaissent pour un champ croisé. Chaque appel bascule un seul type de sous-total indépendamment. Le passage de `shown = true` affiche le sous-total, tandis que `shown = false` le masque. Comme chaque appel n'affecte qu'un seul type, l'appel de la méthode plusieurs fois avec différentes valeurs `subtotalType` permet de construire un sous-ensemble personnalisé de sous-totaux.

L'énumération `PivotFieldSubtotalType` définit les types de sous-totaux disponibles.

- `Automatic` — Aspose.Cells choisit la sélection par défaut (généralement `Sum` pour les champs numériques)
- `None` — supprime toutes les lignes de sous-total
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Les sous-totaux ne s'affichent que lorsqu'il y a deux champs croisés ou plus dans la région de ligne (ou dans la région de colonne). Un seul champ n'a rien de significatif à sous-totaliser entre les valeurs, donc les appels `SetSubtotals` n'ont aucun effet visible dans ce cas. Cet article place donc deux champs de ligne (`Category` externe, `Item` interne) dans chaque exemple afin que la limite de sous-total entre chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**

Lorsque vous n'appelez pas du tout `SetSubtotals`, Aspose.Cells applique la sélection `Automatic` aux champs numériques. L'exemple suivant confirme explicitement ce comportement en appelant `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` sur le champ de ligne `Category` externe.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Scénario 2 — Suppression de tous les sous-totaux (None)**

L'appel de `SetSubtotals(PivotFieldSubtotalType.None, true)` supprime toutes les lignes de sous-total du tableau croisé dynamique, ne laissant que les lignes de champ et le total général en bas. Ceci est utile lorsque vous souhaitez obtenir les données groupées brutes sans aucune ligne de synthèse.

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
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
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

const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Scénario 3 — Sous-ensemble personnalisé de sous-totaux (Sum + Average)**

Vous n'êtes pas limité à un seul type de sous-total. Chaque appel `SetSubtotals` opère indépendamment sur un type, donc l'appel de la méthode deux fois — une fois avec `Sum` et une fois avec `Average` — produit un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotTables = worksheet.getPivotTables();
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```
## **Récapitulatif**

Les trois scénarios ci-dessus partagent le même ensemble de données et la même structure de tableau croisé dynamique. La seule différence entre eux est l'appel `SetSubtotals` appliqué au champ de ligne `Category` externe. Rappelez-vous la règle des deux champs : un seul champ dans une région n'a rien à sous-totaliser entre les valeurs, donc placez toujours au moins deux champs dans la région de ligne ou de colonne lorsque vous souhaitez que `SetSubtotals` ait un effet visible.

## **Articles connexes**

- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
