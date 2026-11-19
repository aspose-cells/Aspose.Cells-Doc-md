---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Afficher les valeurs des champs de données d’un tableau croisé dynamique en pourcentage du total, en différence par rapport à un élément de base, en totaux cumulatifs, en classements, et plus encore avec Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, tableau croisé dynamique, afficher les valeurs comme, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /fr/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données avec une fonction d’agrégation telle que `SUM` ou `COUNT`. La fonctionnalité **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi, ou un classement — vous permettant d’effectuer une analyse comparative sans formules auxiliaires ni colonnes calculées. Les utilisations typiques incluent l’analyse de **la** part du total, y compris les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulé en utilisant un total cumulé dans un champ de période ; l’analyse de variance par rapport à un élément de référence en utilisant la différence ou la différence en pourcentage par rapport à un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit. Dans Aspose.Cells for Node.js via C++, l’énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. L’accesseur en lecture seule `PivotField.getShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`, dont les méthodes `setShowValuesAs()`, `setBaseFieldIndex()` et `setBaseItemIndex()` configurent le comportement ; la méthode pratique `PivotField.showValuesAs(...)` applique les mêmes paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu via `PivotTable.getDataFields()`.

## **Membres de l'énumération PivotShowValuesAsType**
Le champ de données conserve sa fonction d’agrégation, telle que SUM ou COUNT, tandis que **Show Values As** ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’écrire directement les paramètres `PivotShowValuesSetting` (voir la dernière section), une méthode pratique en un appel applique la même configuration. Elle existe sous deux formes — une adressant le champ de base et l’élément de base par index, l’autre par nom :

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `showValuesAsType` | Le calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `baseField` | Index à base zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l'index du champ de ligne auquel appartient l'élément de base), ou — sous forme de nom — le nom du champ de base. | Les huit formats relatifs au champ de base ci‑dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`) ; passez `0` (ou `null` sous forme de nom) pour tout autre format. |
| `baseItem` | Index à base zéro de l'élément de base, avec deux sentinelles : -1 sélectionne l'élément précédent et -2 l'élément suivant (la liaison Node.js via C++ n'exporte pas les constantes nommées — passez les valeurs littérales). La forme nom utilise la légende de l'élément de base à la place, et `null` lorsque le format sélectionné ne nécessite pas d'élément de base. | Seuls les trois formats relatifs à l'élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) évaluent l'élément de base ; les cinq formats relatifs au champ (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, les deux classements) l'ignorent — passez `0` ou `null`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `Normal` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (défaut). | — |
| `DifferenceFrom` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un index ou une légende, ou la sentinelle précédente/suivante) |
| `PercentageOf` | Affiche la valeur en pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un index ou une légende, ou la sentinelle précédente/suivante) |
| `PercentageDifferenceFrom` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un index ou une légende, ou la sentinelle précédente/suivante) |
| `RunningTotalIn` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments entraîne l’accumulation) |
| `PercentageOfRow` | Affiche la valeur en pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur en pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur en pourcentage du total général. | — |
| `Index` | Affiche la valeur en utilisant la formule d’index Excel ((valeur * total général) / (total de ligne * total de colonne)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur en pourcentage du total de sa ligne parente (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur en pourcentage du total de sa colonne parente (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur en pourcentage de son total parent. | `baseField` (le champ parent dont le total sert de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur en pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RankSmallestToLargest` | Classe la valeur du plus petit (1) au plus grand. | `baseField` (le champ dont les éléments définissent le périmètre du classement) |
| `RankLargestToSmallest` | Classe la valeur du plus grand (1) au plus petit. | `baseField` (le champ dont les éléments définissent le périmètre du classement) |

{{% alert color="primary" %}}
`showValuesAs(...)` écrit les paramètres `PivotShowValuesSetting` (`getShowValuesAs()`/`setShowValuesAs()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, et `getBaseItemIndex()`/`setBaseItemIndex()`) — la méthode et l’objet de propriété sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans le dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.showValuesAs()` avec `PivotShowValuesAsType.PercentageOfTotal` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont donc lus comme des proportions de l’ensemble complet des résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni aucun élément de base — les arguments de fin (`0`, `0`) sont des espaces réservés que le format ignore, comme le indique le tableau des paramètres ci‑dessus.

```javascript
const AsposeCells = require("aspose.cells.node");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtenir et configurer PivotField.getShowValuesSetting()**
Lisez la configuration actuelle via `PivotField.getShowValuesSetting()` : l’accesseur en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les paramètres décrivent le calcul **Show Values As** actif. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs()` — elle écrit tous les paramètres en un seul appel, vous n’avez donc jamais besoin de les définir un par un.  
L’objet `PivotShowValuesSetting` expose l’état que `showValuesAs()` écrit :
- `getShowValuesAs()` et `setShowValuesAs()` sélectionnent le calcul secondaire `PivotShowValuesAsType`.
- `getBaseFieldIndex()` et `setBaseFieldIndex()` spécifient l’index à base zéro du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs au champ de base.
- `getBaseItemIndex()` et `setBaseItemIndex()` spécifient l’élément de base : un index à base zéro d’un élément pivot spécifique, ou l’une des deux valeurs sentinelles — -1 pour l’élément précédent, -2 pour l’élément suivant (la liaison n’exporte pas les constantes nommées). Il est utilisé par les formats relatifs à l’élément de base.
- `getBaseFieldName()` et `getBaseItemCaption()` sont des vues en lecture seule qui renvoient le nom du champ de base résolu et la légende de l’élément de base ; par exemple, après avoir sélectionné la sentinelle d’élément précédent, `getBaseItemCaption()` renvoie `(previous)`.
Après avoir appelé `showValuesAs()`, appelez de nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et réaffiché avec la nouvelle configuration.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articles associés**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/nodejs-cpp/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/nodejs-cpp/refresh-pivot-table/)
- [Application du style au tableau croisé dynamique](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}