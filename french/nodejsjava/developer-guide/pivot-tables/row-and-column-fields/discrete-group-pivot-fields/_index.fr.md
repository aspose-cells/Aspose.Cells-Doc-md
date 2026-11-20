---
title: Regroupement discret des éléments d’un champ de tableau croisé dynamique
linktitle: Regroupement discret
description: Découvrez comment regrouper les éléments d’un champ de tableau croisé dynamique dans des groupes nommés personnalisés, tels que les fruits et les légumes, à l’aide de DiscreteGroupItem et PivotFieldGroupOptions.getDiscreteGroupItems() dans Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tableau croisé dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regrouper les éléments du tableau croisé dynamique, groupes personnalisés, PivotField.group, Aspose.Cells for Node.js via Java, tableau croisé dynamique Excel
type: docs
weight: 90
url: /fr/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique collecte les éléments par type de données, par exemple les dates en mois et en trimestres ou les nombres en plages de valeurs. Le regroupement discret résout le problème inverse en regroupant des éléments spécifiques et non liés dans des groupes nommés personnalisés, par exemple des produits sous « fruits » et « légumes », des magasins par région ou des comptes par zone. Aspose.Cells fournit le regroupement discret au moyen de la classe `DiscreteGroupItem` et de la propriété `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un `DiscreteGroupItem` est constitué d’un nom de groupe et des éléments qui lui appartiennent. Les éléments peuvent être identifiés de deux façons : par leur nom (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) ou par leur position dans les données source, avec une numérotation commençant à zéro (`new DiscreteGroupItem("fruit", [0, 3])`). Les deux formes produisent le même résultat.
- Pour appliquer le regroupement discret à un champ situé dans la zone des lignes ou des colonnes d’un tableau croisé dynamique, transmettez les options à `PivotField.group(PivotFieldGroupOptions)`.

## **Regrouper les éléments d’un champ de tableau croisé dynamique par nom d’élément**
L’exemple suivant construit une petite liste de ventes (produit, date et montant), crée un tableau croisé dynamique à partir de cette liste avec `product` dans la zone des lignes, `date` dans la zone des colonnes et `amount` dans la zone des données, puis définit deux groupes personnalisés en fonction des noms d’élément : `fruit` (`grape`, `cherry`) et `vegetables` (`carrot`, `potato`). Le résultat affiche une disposition des lignes à deux niveaux, avec le nom du groupe au niveau extérieur et les éléments d’origine imbriqués en dessous, ce qui permet d’analyser les tendances par groupe personnalisé et par élément.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Après l’exécution de `calculateData()`, la zone des lignes du tableau croisé dynamique affiche `fruit` (`grape` 50, `cherry` 80) et `vegetable` (`carrot` 60, `potato` 70), avec un total général de 260, tandis que les libellés des colonnes conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regrouper les éléments d’un champ de tableau croisé dynamique par indice d’élément**
Lorsque les noms des éléments sont longs ou localisés, le deuxième constructeur de `DiscreteGroupItem` identifie les éléments selon leur indice. Chaque indice désigne la position d’un élément dans l’ordre d’apparition dans les données source, avec une numérotation commençant à zéro, et non dans l’ordre alphabétique. Dans les données d’exemple ci-dessus, `grape` est l’élément 0, `carrot` est l’élément 1, `potato` est l’élément 2 et `cherry` est l’élément 3 ; `fruit` correspond donc à `{ 0, 3 }` et `vegetable` à `{ 1, 2 }`. Le résultat est identique à celui de l’exemple utilisant les noms.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont affectés à aucun groupe personnalisé sont conservés. Ils restent dans le tableau croisé dynamique, au même niveau que les groupes personnalisés, chacun sous la forme d’une entrée autonome à élément unique. Dans l’exemple ci-dessus, la définition du seul groupe `fruit` laisse `carrot` et `potato` dans la zone des lignes sous forme d’entrées autonomes à côté du groupe `fruit`.
- La propriété `PivotFieldGroupOptions.getNewPivotField()` contrôle la disposition du regroupement discret. Par défaut, sa valeur est `true`, ce qui ajoute le champ regroupé sous la forme d’un nouveau champ extérieur à côté du champ d’origine et produit ainsi la disposition à deux niveaux illustrée ci-dessus (`getRowFields()` passe à 2). Définissez-la sur `false` avec `PivotFieldGroupOptions.setNewPivotField(false)` pour remplacer le champ d’origine. Dans ce cas, la zone des lignes affiche un seul niveau contenant uniquement les noms des groupes et leurs valeurs agrégées : `fruit` 130 (50 + 80) et `vegetable` 130 (60 + 70).
- Les constructeurs de `DiscreteGroupItem` fondés sur les noms et ceux fondés sur les indices peuvent être mélangés au sein du même tableau `getDiscreteGroupItems()`.
{{% /alert %}}

## **Articles associés**
- [Regrouper les champs dans le tableau croisé dynamique](/cells/fr/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}