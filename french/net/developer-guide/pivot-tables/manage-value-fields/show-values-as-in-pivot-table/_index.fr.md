---
title: Afficher les valeurs comme dans un tableau croisé dynamique
linktitle: Afficher les valeurs comme
description: Afficher les valeurs des champs de données d’un tableau croisé dynamique sous forme de pourcentage du total, de différence par rapport à un élément de base, de totaux cumulés, de classements et plus encore avec Aspose.Cells for .NET.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs comme, format d’affichage des données, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /fr/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique agrège généralement chaque champ de données avec une fonction d’agrégation telle que `Sum` ou `Count`. La fonctionnalité **Afficher les valeurs comme** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi, ou un classement — ce qui permet d’effectuer des analyses comparatives sans formules auxiliaires ni colonnes calculées.  
Les utilisations typiques comprennent l’analyse de la part du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; les rapports cumulatifs à l’aide d’un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un repère à l’aide d’une différence ou d’une différence en pourcentage par rapport à un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for .NET, `PivotFieldDataDisplayFormat` sélectionne le calcul secondaire. La propriété en lecture seule `PivotField.ShowValuesSetting` renvoie un objet `PivotShowValuesSetting`, dont les propriétés modifiables `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType` et `BaseItemIndex` configurent le comportement ; la méthode pratique `PivotField.ShowValuesAs(...)` applique les mêmes quatre paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu via `PivotTable.DataFields`.

## **Membres d'énumération PivotFieldDataDisplayFormat**
Le champ de données conserve sa fonction d’agrégation, telle que Sum ou Count, tandis que **Afficher les valeurs comme** ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’écrire directement les propriétés `PivotShowValuesSetting` (voir la dernière section), une méthode pratique à appel unique applique la même configuration :

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `displayFormat` | Le calcul secondaire `PivotFieldDataDisplayFormat` à appliquer. | Toujours. |
| `baseField` | Indice zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ de ligne auquel appartient l’élément de base). | Uniquement pour les six formats relatifs à une base ci-dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`) ; ignoré par tout autre format. |
| `baseItemPositionType` | Mode de sélection de l’élément de base par rapport à l’élément actuel : `PivotItemPositionType.Previous`, `.Next` ou `.Custom`. | Uniquement pour les trois formats à élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) ; ignoré par tout autre format. |
| `baseItem` | Indice zéro de l’élément de base. | Uniquement lorsque `baseItemPositionType` est `Custom` (l’indice de l’élément désigne l’élément de base exact) ; ignoré pour `Previous` / `Next` et par tout format qui ne repose pas sur un élément de base — passer `0`. |

| Type de calcul | Comportement | Paramètres de l’élément de base |
| --- | --- | --- |
| `Normal` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (défaut). | — |
| `DifferenceFrom` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageOf` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageDifferenceFrom` | Affiche la valeur comme le pourcentage de différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `RunningTotalIn` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments pilote l’accumulation) |
| `PercentageOfRow` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur comme un pourcentage du total général. | — |
| `Index` | Affiche la valeur en utilisant la formule d’index Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur comme un pourcentage du total de la ligne parente (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur comme un pourcentage du total de la colonne parente (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur comme un pourcentage de son total parent. | `baseField` (le champ parent servant de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RankSmallestToLargest` | Classe la valeur du plus petit (1) au plus grand. | — |
| `RankLargestToSmallest` | Classe la valeur du plus grand (1) au plus petit. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` écrit les propriétés `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — la méthode et l’objet de propriété sont deux façons de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue **Afficher les valeurs comme** d’Excel.
{{% /alert %}}

## **Afficher les valeurs comme pourcentage du total**
Appelez la méthode `PivotField.ShowValuesAs` avec `PivotFieldDataDisplayFormat.PercentageOfTotal` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont donc présentés comme des proportions de l’ensemble du jeu de résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ ou élément de base ; les arguments supplémentaires (`0`, `PivotItemPositionType.Previous`, `0`) sont des espaces réservés que le format ignore, comme indiqué dans le tableau des paramètres ci‑dessus.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtenir et configurer PivotField.ShowValuesSetting**
Lisez la configuration actuelle via `PivotField.ShowValuesSetting` : la propriété en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les quatre propriétés décrivent le calcul **Afficher les valeurs comme** actif. Pour modifier la configuration, appelez la méthode `PivotField.ShowValuesAs` — elle écrit les quatre paramètres en un seul appel, de sorte que vous n’avez jamais à affecter chaque propriété séparément.  
L’objet `PivotShowValuesSetting` expose les quatre propriétés que `ShowValuesAs` écrit :
- `CalculationType` sélectionne le calcul secondaire `PivotFieldDataDisplayFormat`.
- `BaseFieldIndex` indique l’indice zéro du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à une base.
- `BaseItemPositionType` détermine comment l’élément de base est positionné par rapport à l’élément actuel et accepte `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` ou `PivotItemPositionType.Custom`.
- `BaseItemIndex` indique l’indice zéro de l’élément de base et est utilisé lorsque `BaseItemPositionType` est `Custom`.  
Après avoir appelé `ShowValuesAs`, appelez à nouveau `PivotTable.CalculateData()` afin que le corps du tableau croisé dynamique soit recalculé et rendu avec la nouvelle configuration.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articles associés**
- [Gestion des champs de valeurs dans le tableau croisé dynamique](/cells/fr/net/manage-value-fields/)
- [Travail avec les formats d’affichage des données du DataField dans le tableau croisé dynamique](/cells/fr/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Actualisation du tableau croisé dynamique](/cells/fr/net/refresh-pivot-table/)
- [Application du style au tableau croisé dynamique](/cells/fr/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}