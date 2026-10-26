---
title: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique avec Aspose.Cells for Node.js via C++
description: Découvrez comment ajouter des champs de base aux régions de ligne et de colonne d’un tableau croisé dynamique et contrôler les sous-totaux des champs de pivot à l’aide de PivotField.setSubtotals dans Aspose.Cells for Node.js via C++
linktitle: Champs de ligne et de colonne
keywords: Aspose.Cells, Node.js, C++, tableau croisé dynamique, champ de ligne, champ de colonne, PivotField, SetSubtotals, PivotFieldSubtotalType, sous-totaux
type: docs
weight: 220
url: /fr/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajouter un champ à la région de ligne ou de colonne**
La méthode `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` déplace un champ de base des données source vers l’une des quatre régions du tableau croisé dynamique. L’argument `fieldType` accepte l’une des valeurs `PivotFieldType` suivantes.
- `Row` — champs placés verticalement à gauche
- `Column` — champs placés horizontalement en haut
- `Data` — champs dont les valeurs sont agrégées
- `Page` — champs utilisés comme filtres de rapport
L’ordre d’imbrication des champs est important. L’ajout de `Category` à la région de ligne, puis de `Item`, produit un tableau croisé dynamique dont le regroupement externe est `Category` et le regroupement interne est `Item`. L’inversion de l’ordre inverse la hiérarchie.

## **Sous-totaux des champs de pivot**
La méthode `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` contrôle les lignes de sous-total qui apparaissent pour un champ de pivot. Chaque appel active ou désactive indépendamment un seul type de sous-total. La transmission de `shown = true` affiche le sous-total, tandis que `shown = false` le masque. Comme chaque appel n’affecte qu’un seul type, l’appel de la méthode à plusieurs reprises avec différentes valeurs de `subtotalType` permet de définir un sous-ensemble personnalisé de sous-totaux.
L’énumération `PivotFieldSubtotalType` définit les types de sous-total disponibles.
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
Les sous-totaux ne sont affichés que si la région de ligne (ou la région de colonne) contient au moins deux champs de pivot. Un champ unique ne permet pas de calculer un sous-total pertinent entre des groupes ; dans ce cas, les appels à `setSubtotals` n’ont donc aucun effet visible. Le présent article place par conséquent deux champs de ligne (`Category` externe, `Item` interne) dans chaque exemple, afin que la limite de sous-total entre chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**
Lorsque vous n’appelez pas `setSubtotals`, Aspose.Cells applique la sélection `Automatic` aux champs numériques. L’exemple suivant confirme explicitement ce comportement en appelant `setSubtotals(PivotFieldSubtotalType.Automatic, true)` sur le champ de ligne externe `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
L’appel à `setSubtotals(PivotFieldSubtotalType.None, true)` supprime toutes les lignes de sous-total du tableau croisé dynamique, ne laissant que les lignes de champ et le total général au bas de celui-ci. Cette approche est utile lorsque vous souhaitez obtenir les données groupées brutes sans aucune ligne de résumé.

```javascript
const AsposeCells = require("aspose.cells.node");
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
const pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
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
Vous n’êtes pas limité à un seul type de sous-total. Chaque appel à `setSubtotals` agit indépendamment sur un type. Par conséquent, l’appel de la méthode deux fois — une fois avec `Sum` et une fois avec `Average` — produit un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
Les trois scénarios ne diffèrent que par les appels à `setSubtotals`. Tout le reste — le jeu de données, les champs et les zones auxquelles ils sont assignés — est identique, ce qui rend les dispositions directement comparables.
- **Placer les champs.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` déplace une colonne source vers une région. Dans une même région, l’ordre des appels détermine l’ordre d’affichage, de sorte que le premier appel devient le groupe le plus externe. Les sous-totaux nécessitent deux champs ou plus dans la même région : avec un seul champ, il n’y a rien entre les groupes sur lequel effectuer un sous-total.
- **Scénario 1 — sous-totaux automatiques.** Ne pas appeler `setSubtotals` laisse le choix à Excel, qui applique son sous-total par défaut aux champs numériques. Appeler `setSubtotals` avec `AsposeCells.PivotFieldSubtotalType.Automatic` enregistre explicitement ce choix au lieu de le laisser implicite.
- **Scénario 2 — pas de sous-totaux.** `setSubtotals` avec `AsposeCells.PivotFieldSubtotalType.None` désactive le sous-total par défaut, de sorte que le tableau croisé conserve les lignes de champ et le total général, mais supprime les lignes de sous-total qu’Excel insérerait normalement entre elles.
- **Scénario 3 — un sous-ensemble choisi.** Chaque appel active ou désactive précisément un type de sous-total, et les appels s’accumulent plutôt qu’ils ne s’annulent les uns les autres. Appeler `setSubtotals` une fois avec `AsposeCells.PivotFieldSubtotalType.Sum` et une fois avec `AsposeCells.PivotFieldSubtotalType.Average` laisse donc les deux activés, et le tableau croisé affiche un sous-total de Somme, un sous-total de Moyenne et un total général.

{{% alert color="primary" %}}
Rien concernant les sous-totaux n’est spécifique à la région des lignes. Les mêmes appels à `setSubtotals` sur un champ provenant de `PivotTable.ColumnFields` produisent les mêmes trois dispositions sur l’axe des colonnes, car le paramètre appartient au champ croisé et non à l’axe sur lequel il est placé.
{{% /alert %}}

## **Articles associés**
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}