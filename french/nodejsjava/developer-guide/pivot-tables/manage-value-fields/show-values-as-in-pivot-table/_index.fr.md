---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Affichez les valeurs des champs de données d’un tableau croisé dynamique sous forme de pourcentage du total, de différence par rapport à un élément de base, de totaux cumulés, de classements, et plus encore avec Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, tableau croisé dynamique, afficher les valeurs comme, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /fr/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège généralement chaque champ de données à l’aide d’une fonction d’agrégation telle que `SUM` ou `COUNT`. La fonctionnalité **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un classement—afin que vous puissiez effectuer des analyses comparatives sans formules d’assistance ni colonnes calculées.  
Les utilisations typiques comprennent l’analyse de la part du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulatif à l’aide d’un total cumulé dans un champ de période ; l’analyse de variance par rapport à un élément de référence en utilisant la différence ou la différence en pourcentage d’un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for Node.js via Java, l’énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. La méthode en lecture seule `PivotField.getShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`, dont les méthodes `setShowValuesAs()`, `setBaseFieldIndex()` et `setBaseItemIndex()` configurent le comportement ; la méthode de commodité `PivotField.showValuesAs(...)` applique les mêmes paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu via `PivotTable.getDataFields()`.

## **Membres de l'énumération PivotShowValuesAsType**
Le champ de données conserve sa fonction d’agrégation, telle que SUM ou COUNT, tandis que Show Values As ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’utiliser directement les accesseurs du `PivotShowValuesSetting` (voir la dernière section), une méthode de commodité en un appel applique la même configuration. Elle existe sous deux formes — l’une adressant le champ de base et l’autre l’élément de base par indice, l’autre par nom :

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `showValuesAsType` | Le calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `baseField` | Indice zéro‑based du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ de ligne auquel appartient l’élément de base), ou — sous forme de nom — le nom du champ de base. | Les huit formats relatifs à la base ci‑dessous (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`) ; passer `0` (ou `null` dans la forme par nom) pour tout autre format. |
| `baseItem` | Indice zéro‑based de l’élément de base, avec deux sentinelles : -1 sélectionne l’élément précédent et -2 l’élément suivant (la racine du package n’exporte pas les constantes `PivotShowValuesSetting` — utilisez les valeurs littérales). La forme par nom prend la légende de l’élément de base à la place, et `null` lorsque le format sélectionné ne nécessite aucun élément de base. | Seuls les trois formats d’élément de base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) évaluent l’élément de base ; les cinq formats relatifs au champ (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, les deux classements) l’ignorent — passer `0` ou `null`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `NORMAL` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (défaut). | — |
| `DIFFERENCE_FROM` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PERCENTAGE_OF` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PERCENTAGE_DIFFERENCE_FROM` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `RUNNING_TOTAL_IN` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments entraîne l’accumulation) |
| `PERCENTAGE_OF_ROW` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PERCENTAGE_OF_COLUMN` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PERCENTAGE_OF_TOTAL` | Affiche la valeur comme un pourcentage du total général. | — |
| `INDEX` | Affiche la valeur en utilisant la formule d’index Excel ((valeur * total général) / (total ligne * total colonne)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Affiche la valeur comme un pourcentage du total de la ligne parent (pour les champs de ligne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Affiche la valeur comme un pourcentage du total de la colonne parent (pour les champs de colonne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Affiche la valeur comme un pourcentage de son total parent. | `baseField` (le champ parent dont le total sert de référence) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RANK_SMALLEST_TO_LARGEST` | Classe la valeur du plus petit (1) au plus grand. | `baseField` (le champ dont les éléments définissent le périmètre du classement) |
| `RANK_LARGEST_TO_SMALLEST` | Classe la valeur du plus grand (1) au plus petit. | `baseField` (le champ dont les éléments définissent le périmètre du classement) |

{{% alert color="primary" %}}
`showValuesAs(...)` écrit l’état `PivotShowValuesSetting` via `setShowValuesAs()`, `setBaseFieldIndex()` et `setBaseItemIndex()` — la méthode et l’objet de propriétés sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs comme pourcentage du total**
Appelez la méthode `PivotField.showValuesAs()` avec `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés représentent donc des proportions de l’ensemble du jeu de résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni aucun élément de base — les arguments de fin (`0`, `0`) sont des espaces réservés que le format ignore, comme l’indique le tableau des paramètres ci‑dessus.

```javascript
const AsposeCells = require("aspose.cells");
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
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtenir et configurer PivotField.getShowValuesSetting()**
Lisez la configuration actuelle via `PivotField.getShowValuesSetting()` : la méthode en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les réglages décrivent le calcul Show Values As actif. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs()` — elle écrit tous les réglages en un seul appel, vous n’avez donc jamais besoin de les définir un à un.  
L’objet `PivotShowValuesSetting` expose l’état que `showValuesAs()` écrit :
- `getShowValuesAs()` / `setShowValuesAs()` sélectionne le calcul secondaire `PivotShowValuesAsType`.  
- `getBaseFieldIndex()` / `setBaseFieldIndex()` spécifie l’indice zéro‑based du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à la base.  
- `getBaseItemIndex()` / `setBaseItemIndex()` spécifie l’élément de base : un indice zéro‑based d’un élément de tableau croisé dynamique spécifique, ou l’une des deux valeurs sentinelles — -1 pour l’élément précédent, -2 pour l’élément suivant (la racine du package n’exporte pas les constantes nommées). Il est utilisé par les formats d’élément de base.  
- `getBaseFieldName()` et `getBaseItemCaption()` sont des vues en lecture seule qui rapportent respectivement le nom du champ de base résolu et la légende de l’élément de base ; par exemple, après avoir sélectionné la sentinelle d’élément précédent, `getBaseItemCaption()` renvoie `(previous)`.  
Après avoir appelé `showValuesAs()`, appelez de nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et rendu avec la configuration mise à jour.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/nodejs-java/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/nodejs-java/refresh-pivot-table/)
- [Application du style au tableau croisé dynamique](/cells/fr/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}