---
title: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for Node.js via Java
linktitle: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for Node.js via Java
description: Apprenez à ajouter des champs de base aux zones de ligne et de colonne d'un tableau croisé dynamique et à contrôler les sous-totaux des champs de tableau croisé dynamique à l'aide de PivotField.setSubtotals dans Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, tableau croisé dynamique, champ de ligne, champ de colonne, PivotField, setSubtotals, PivotFieldSubtotalType, sous-totaux
type: docs
weight: 220
url: /fr/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajouter un champ à la zone de ligne ou de colonne**
La méthode `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` déplace un champ de base des données sources vers l'une des quatre zones du tableau croisé dynamique. L'argument `fieldType` accepte l'une des valeurs `PivotFieldType` suivantes.
- `ROW` — champs placés verticalement à gauche
- `COLUMN` — champs placés horizontalement en haut
- `DATA` — champs dont les valeurs sont agrégées
- `PAGE` — champs utilisés comme filtres de rapport
L'ordre d'imbrication des champs est important. L'ajout de `Category` à la zone de ligne, suivi de celui de `Item`, produit un tableau croisé dynamique dont le regroupement extérieur est `Category` et le regroupement intérieur est `Item`. Si vous inversez l'ordre, la hiérarchie est inversée.

## **Sous-totaux des champs de tableau croisé dynamique**
La méthode `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` détermine les lignes de sous-total qui s'affichent pour un champ de tableau croisé dynamique. Chaque appel active ou désactive un seul type de sous-total indépendamment des autres. Lorsque vous transmettez `shown = true`, le sous-total s'affiche, tandis que `shown = false` le masque. Comme chaque appel n'affecte qu'un seul type, vous pouvez appeler la méthode plusieurs fois avec différentes valeurs `subtotalType` afin de définir un sous-ensemble personnalisé de sous-totaux.
L'énumération `PivotFieldSubtotalType` définit les types de sous-total disponibles.
- `AUTOMATIC` — Aspose.Cells choisit la sélection par défaut (généralement `SUM` pour les champs numériques)
- `NONE` — supprime toutes les lignes de sous-total
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Les sous-totaux ne s'affichent que si la zone de ligne (ou la zone de colonne) contient au moins deux champs de tableau croisé dynamique. Un seul champ ne permet pas de définir un sous-total significatif ; les appels `setSubtotals` n'ont donc aucun effet visible dans ce cas. Cet article place deux champs de ligne (`Category` au niveau supérieur, `Item` au niveau inférieur) dans chaque exemple afin que le sous-total marquant la fin de chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**
Si vous n'effectuez aucun appel à `setSubtotals`, Aspose.Cells applique la sélection `AUTOMATIC` aux champs numériques. L'exemple suivant confirme explicitement ce comportement en appelant `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` sur le champ de ligne `Category` du niveau supérieur.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Scénario 2 — Suppression de tous les sous-totaux (Aucun)**
L'appel à `setSubtotals(PivotFieldSubtotalType.NONE, true)` supprime toutes les lignes de sous-total du tableau croisé dynamique, ne laissant que les lignes de champ et le total général au bas du tableau. Cette option est utile lorsque vous souhaitez obtenir les données groupées brutes, sans aucune ligne de synthèse.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Scénario 3 — Sous-ensemble de sous-totaux personnalisé (Somme + Moyenne)**
Vous pouvez définir plusieurs types de sous-total. Chaque appel à `setSubtotals` porte indépendamment sur un seul type. Appeler la méthode deux fois — une fois avec `SUM` et une fois avec `AVERAGE` — permet d'obtenir un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Récapitulatif**
Les trois scénarios ne diffèrent que par un seul point : les appels à `setSubtotals`. Tout le reste — le jeu de données, les champs et les zones auxquelles ils sont affectés — est identique, ce qui rend les dispositions directement comparables.
- **Placement des champs.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` déplace une colonne source vers une région. Dans une même région, l’ordre des appels détermine l’ordre d’affichage, de sorte que le premier appel devient le groupe le plus externe. Les sous-totaux nécessitent deux champs ou plus dans la même région : avec un seul champ, il n’y a rien entre les groupes sur lequel calculer un sous-total.
- **Scénario 1 — sous-totaux automatiques.** Ne pas appeler `setSubtotals` laisse le choix à Excel, qui applique son sous-total par défaut aux champs numériques. Appeler `setSubtotals` avec `AsposeCells.PivotFieldSubtotalType.AUTOMATIC` enregistre explicitement ce choix au lieu de le laisser implicite.
- **Scénario 2 — absence de sous-totaux.** `setSubtotals` avec `AsposeCells.PivotFieldSubtotalType.NONE` désactive le sous-total par défaut, de sorte que le tableau croisé conserve les lignes de champ et le total général, mais supprime les lignes de sous-total qu’Excel insérerait autrement entre elles.
- **Scénario 3 — un sous-ensemble choisi.** Chaque appel active ou désactive précisément un type de sous-total, et les appels s’accumulent plutôt qu’ils ne s’annulent les uns les autres. Appeler `setSubtotals` une fois avec `AsposeCells.PivotFieldSubtotalType.SUM` et une fois avec `AsposeCells.PivotFieldSubtotalType.AVERAGE` laisse donc les deux activés, et le tableau croisé affiche un sous-total « Somme », un sous-total « Moyenne » et un total général.

{{% alert color="primary" %}}
Rien dans la gestion des sous-totaux n’est spécifique à la région des lignes. Les mêmes appels à `setSubtotals` appliqués à un champ extrait de `PivotTable.ColumnFields` produisent les mêmes trois dispositions sur l’axe des colonnes, car le paramètre appartient au champ croisé, et non à l’axe sur lequel il est placé.
{{% /alert %}}

## **Articles connexes**
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/nodejs-java/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}