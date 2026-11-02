---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Afficher les valeurs des champs de données d'un tableau croisé dynamique sous forme de pourcentage du total, de différence par rapport à un élément de base, de totaux cumulatifs, de classements, etc. avec Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs comme, format d'affichage des données, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /fr/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l’aide d’une fonction d’agrégation telle que `SUM` ou `COUNT`. La fonctionnalité **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un classement — afin que vous puissiez effectuer une analyse comparative sans formules auxiliaires ni colonnes calculées.  
Les utilisations typiques incluent l’analyse de **la** part du total, y compris les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulatif à l’aide d’un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un élément de référence en utilisant la différence ou la différence en pourcentage d’un élément de base ; et le classement des valeurs du plus petit au plus grand ou inversement.  
Dans Aspose.Cells for Node.js via Java, `PivotFieldDataDisplayFormat` sélectionne le calcul secondaire. La méthode en lecture seule `PivotField.getShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`. Ses méthodes `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` et `setBaseItemIndex()` configurent le comportement ; la méthode de convenance `PivotField.showValuesAs(...)` applique les mêmes quatre paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu via `PivotTable.getDataFields()`.

## **Membres de l’énumération PivotFieldDataDisplayFormat**
Le champ de données conserve sa fonction d’agrégation, telle que SUM ou COUNT, tandis que **Show Values As** ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’écrire directement les paramètres de `PivotShowValuesSetting` (voir la dernière section), une méthode de convenance en un seul appel applique la même configuration :

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| Paramètre | Signification | Quand c’est requis |
| --- | --- | --- |
| `displayFormat` | Le calcul secondaire `PivotFieldDataDisplayFormat` à appliquer. | Toujours. |
| `baseField` | Indice zéro‑base du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ de ligne auquel appartient l’élément de base). | Uniquement pour les six formats relatifs à une base ci-dessous (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`) ; ignoré par tout autre format. |
| `baseItemPositionType` | Mode de sélection de l’élément de base par rapport à l’élément actuel : `PivotItemPositionType.PREVIOUS`, `.NEXT` ou `.CUSTOM`. | Uniquement pour les trois formats à élément de base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) ; ignoré par tout autre format. |
| `baseItem` | Indice zéro‑base de l’élément de base. | Uniquement lorsque `baseItemPositionType` est `CUSTOM` (l’indice sélectionne l’élément de base exact) ; ignoré pour `PREVIOUS` / `NEXT` et par tout format non‑base — passer `0`. |

| Type de calcul | Comportement | Paramètres d’élément de base |
| --- | --- | --- |
| `NORMAL` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DIFFERENCE_FROM` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` uniquement avec `CUSTOM`) |
| `PERCENTAGE_OF` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` uniquement avec `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` uniquement avec `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments entraîne l’accumulation) |
| `PERCENTAGE_OF_ROW` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PERCENTAGE_OF_COLUMN` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PERCENTAGE_OF_TOTAL` | Affiche la valeur comme un pourcentage du total général. | — |
| `INDEX` | Affiche la valeur en utilisant la formule d’index Excel ((valeur × total général) / (total ligne × total colonne)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Affiche la valeur comme un pourcentage du total de la ligne parente (pour les champs de ligne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Affiche la valeur comme un pourcentage du total de la colonne parente (pour les champs de colonne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Affiche la valeur comme un pourcentage du total du parent. | `baseField` (le champ parent servant de référence) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RANK_SMALLEST_TO_LARGEST` | Classe la valeur du plus petit (1) au plus grand. | — |
| `RANK_LARGEST_TO_SMALLEST` | Classe la valeur du plus grand (1) au plus petit. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` écrit les paramètres de `PivotShowValuesSetting` (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()`, et `setBaseItemIndex()`) — la méthode et l’objet de paramètres sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base de la boîte de dialogue **Show Values As** d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.showValuesAs()` avec `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont donc interprétés comme des proportions de l’ensemble du jeu de résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni aucun élément de base ; les arguments supplémentaires (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sont des espaces réservés que le format ignore, comme l’indique le tableau des paramètres ci‑dessus.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtenir et configurer PivotField.getShowValuesSetting()**
Lisez la configuration actuelle via `PivotField.getShowValuesSetting()` : la méthode en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les quatre paramètres décrivent le calcul **Show Values As** actif. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs()` — elle écrit les quatre paramètres en un seul appel, de sorte que vous n’avez jamais à les affecter individuellement.  
L’objet `PivotShowValuesSetting` expose les quatre paramètres que `showValuesAs()` écrit :
- `getCalculationType()` / `setCalculationType()` sélectionne le calcul secondaire `PivotFieldDataDisplayFormat`.  
- `getBaseFieldIndex()` / `setBaseFieldIndex()` spécifie l’indice zéro‑base du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à une base.  
- `getBaseItemPositionType()` / `setBaseItemPositionType()` détermine comment l’élément de base est positionné par rapport à l’élément actuel et accepte `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` ou `PivotItemPositionType.CUSTOM`.  
- `getBaseItemIndex()` / `setBaseItemIndex()` spécifie l’indice zéro‑base de l’élément de base et est utilisé lorsque `getBaseItemPositionType()` est `CUSTOM`.  
Après avoir appelé `showValuesAs()`, appelez à nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et rendu avec la nouvelle configuration.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articles connexes**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/nodejs-java/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/nodejs-java/refresh-pivot-table/)
- [Application du style au tableau croisé dynamique](/cells/fr/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}