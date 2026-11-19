---
title: Utiliser la fonctionnalité « Afficher les valeurs sous forme de » dans un tableau croisé dynamique
linktitle: Utiliser la fonctionnalité « Afficher les valeurs sous forme de » dans un tableau croisé dynamique
description: Affichez les valeurs des champs de données d'un tableau croisé dynamique sous forme de pourcentage du total général, d'écart par rapport à un élément de base, de totaux cumulés, de rangs et bien d'autres avec Aspose.Cells for .NET.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs sous forme de, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /fr/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l'aide d'une fonction d'agrégation telle que `Sum` ou `Count`. La fonctionnalité **Afficher les valeurs sous forme de** d'Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, un écart par rapport à un élément de base choisi ou un rang — ce qui permet d'effectuer des analyses comparatives sans formules auxiliaires ni colonnes calculées.
Les utilisations typiques comprennent l'analyse de la répartition du total, notamment les pourcentages du total d'une ligne, du total d'une colonne ou du total général ; l'établissement de rapports cumulés à l'aide d'un total cumulé dans un champ de période ; l'analyse des écarts par rapport à un élément de référence, à l'aide des calculs d'écart par rapport à un élément de base et d'écart en pourcentage par rapport à un élément de base ; et le classement des valeurs de la plus petite à la plus grande ou de la plus grande à la plus petite.
Dans Aspose.Cells for .NET, l'énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. La propriété en lecture seule `PivotField.ShowValuesSetting` renvoie un objet `PivotShowValuesSetting`, dont les propriétés accessibles en écriture `ShowValuesAs`, `BaseFieldIndex` et `BaseItemIndex` configurent le comportement ; la méthode pratique `PivotField.ShowValuesAs(...)` applique la même configuration en un seul appel. Appliquez cette configuration à un champ de données ou de valeurs obtenu à partir de `PivotTable.DataFields`.

## **Membres de l'énumération PivotShowValuesAsType**
Le champ de données conserve sa fonction d'agrégation, telle que `Sum` ou `Count`, tandis que la fonctionnalité **Afficher les valeurs sous forme de** ne modifie que la manière dont la valeur agrégée est affichée.
Outre l'écriture directe des propriétés `PivotShowValuesSetting` (voir la dernière section), une méthode pratique permet d'appliquer la même configuration en un seul appel. Elle propose deux surcharges : l'une désigne le champ de base et l'élément de base par index, l'autre par nom :

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `showValuesAsType` | Le type de calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `baseField` | Index du champ de base parmi les champs de base du tableau croisé dynamique, numéroté à partir de zéro (par exemple, l'index du champ de ligne auquel appartient l'élément de base), ou, dans la surcharge qui prend des chaînes, le nom du champ de base. | Les huit formats qui utilisent un champ de base ci-dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`) ; transmettez `0` (ou `null` dans la surcharge qui prend des chaînes) pour tous les autres formats. |
| `baseItem` | Index de l'élément de base, numéroté à partir de zéro, avec deux valeurs sentinelles : `PivotShowValuesSetting.PreviousPivotItem` (-1) sélectionne l'élément précédent et `PivotShowValuesSetting.NextPivotItem` (-2) l'élément suivant. La surcharge qui prend des chaînes utilise plutôt la légende de l'élément de base, ou `null` lorsque le format sélectionné n'a besoin d'aucun élément de base. | Seuls les trois formats qui utilisent un élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) prennent cet élément en compte ; les cinq formats qui utilisent un champ (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, les deux classements) ne l'utilisent pas — transmettez `0` ou `null`. |

| Type de calcul | Comportement | Paramètres liés à l'élément de base |
| --- | --- | --- |
| `Normal` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DifferenceFrom` | Affiche la valeur sous forme d'écart par rapport à la valeur d'un élément de base dans un champ de base. | `baseField` + `baseItem` (des index ou des légendes, ou une valeur sentinelle pour l'élément précédent ou suivant) |
| `PercentageOf` | Affiche la valeur sous forme de pourcentage de la valeur d'un élément de base dans un champ de base. | `baseField` + `baseItem` (des index ou des légendes, ou une valeur sentinelle pour l'élément précédent ou suivant) |
| `PercentageDifferenceFrom` | Affiche la valeur sous forme d'écart en pourcentage par rapport à la valeur d'un élément de base dans un champ de base. | `baseField` + `baseItem` (des index ou des légendes, ou une valeur sentinelle pour l'élément précédent ou suivant) |
| `RunningTotalIn` | Affiche la valeur sous forme de total cumulé pour les éléments successifs d'un champ de base. | `baseField` (le champ dont l'ordre des éléments pilote l'accumulation) |
| `PercentageOfRow` | Affiche la valeur sous forme de pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur sous forme de pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur sous forme de pourcentage du total général. | — |
| `Index` | Affiche la valeur à l'aide de la formule d'index d'Excel ((valeur * total général) / (total de la ligne * total de la colonne)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur sous forme de pourcentage du total de sa ligne parente (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur sous forme de pourcentage du total de sa colonne parente (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur sous forme de pourcentage du total de son champ parent. | `baseField` (le champ parent dont le total sert de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur sous forme de pourcentage d'un total cumulé dans un champ de base. | `baseField` (le champ d'accumulation) |
| `RankSmallestToLargest` | Attribue à la valeur un rang allant de la plus petite (1) à la plus grande. | `baseField` (le champ dont les éléments définissent la portée du classement) |
| `RankLargestToSmallest` | Attribue à la valeur un rang allant de la plus grande (1) à la plus petite. | `baseField` (le champ dont les éléments définissent la portée du classement) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` écrit l'état `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex`, `BaseItemIndex`) — la méthode et l'objet `PivotShowValuesSetting` sont deux moyens de configurer le même état, à l'image des sélecteurs de champ de base et d'élément de base dans la boîte de dialogue Afficher les valeurs sous forme de d'Excel.
{{% /alert %}}

## **Afficher les valeurs sous forme de pourcentage du total**
Appelez la méthode `PivotField.ShowValuesAs` avec `PivotShowValuesAsType.PercentageOfTotal` pour afficher chaque cellule des champs de données, y compris le total général, sous forme de pourcentage du total général. Les valeurs affichées représentent donc la part de chaque élément dans le jeu de résultats complet. Ce format utilise uniquement le total général comme référence ; il ne nécessite donc ni champ de base ni élément de base — les arguments de fin (`0`, `0`) sont des valeurs de remplissage ignorées par le format, comme l'indique le tableau des paramètres ci-dessus.

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtenir et configurer PivotField.ShowValuesSetting**
Lisez la configuration actuelle au moyen de `PivotField.ShowValuesSetting` : la propriété en lecture seule renvoie l'objet `PivotShowValuesSetting` du champ, dont les propriétés décrivent le calcul actif dans le cadre de la fonctionnalité **Afficher les valeurs sous forme de**. Pour modifier la configuration, appelez la méthode `PivotField.ShowValuesAs` — elle écrit tous les paramètres en un seul appel ; il n'est donc jamais nécessaire d'affecter les propriétés une à une.
L'objet `PivotShowValuesSetting` expose l'état écrit par `ShowValuesAs` :
- `ShowValuesAs` sélectionne le calcul secondaire `PivotShowValuesAsType`.
- `BaseFieldIndex` spécifie l'index du champ de base parmi les champs du tableau croisé dynamique, numéroté à partir de zéro. Il est utilisé par les formats qui utilisent un champ de base.
- `BaseItemIndex` spécifie l'élément de base : un index d'un élément spécifique du tableau croisé dynamique, numéroté à partir de zéro, ou l'une des deux valeurs sentinelles — `PivotShowValuesSetting.PreviousPivotItem` (-1) pour l'élément précédent, `PivotShowValuesSetting.NextPivotItem` (-2) pour l'élément suivant. Il est utilisé par les formats qui utilisent un élément de base.
- `BaseFieldName` et `BaseItemCaption` sont des propriétés en lecture seule qui exposent le nom du champ de base et la légende de l'élément de base après résolution ; par exemple, après avoir sélectionné la valeur sentinelle correspondant à l'élément précédent, `BaseItemCaption` retourne `(previous)`.
Après avoir appelé `ShowValuesAs`, appelez à nouveau `PivotTable.CalculateData()` afin que le corps du tableau croisé dynamique soit recalculé et régénéré avec la configuration mise à jour.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articles connexes**
- [Gestion des champs de valeur dans un tableau croisé dynamique](/cells/fr/net/manage-value-fields/)
- [Utilisation des formats d'affichage des données de DataField dans un tableau croisé dynamique](/cells/fr/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Actualisation d'un tableau croisé dynamique](/cells/fr/net/refresh-pivot-table/)
- [Application d'un style à un tableau croisé dynamique](/cells/fr/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}