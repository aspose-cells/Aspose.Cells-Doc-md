---
title: Afficher les valeurs sous forme dans un tableau croisé dynamique
linktitle: Afficher les valeurs sous forme dans un tableau croisé dynamique
description: Affichez les valeurs des champs de données d'un tableau croisé dynamique sous forme de pourcentage du total, de différence par rapport à un élément de base, de totaux cumulés, de rangs et d'autres modes, à l'aide d'Aspose.Cells for Java.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs sous forme, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /fr/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l'aide d'une fonction d'agrégation telle que `Sum` ou `Count`. La fonctionnalité **Afficher les valeurs sous forme** d'Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un rang — afin de permettre une analyse comparative sans formules auxiliaires ni colonnes calculées.
Les utilisations courantes comprennent l'analyse de la part dans le total, notamment les pourcentages du total d'une ligne, du total d'une colonne ou du total général ; les rapports cumulés utilisant un total cumulé dans un champ de période ; l'analyse des écarts par rapport à un élément de référence à l'aide de la différence par rapport à un élément de base ou du pourcentage de différence par rapport à un élément de base ; et le classement des valeurs, de la plus petite à la plus grande ou de la plus grande à la plus petite.
Dans Aspose.Cells for Java, l'énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. L'accesseur en lecture seule `PivotField.getShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`, dont les méthodes `setShowValuesAs(...)`, `setBaseFieldIndex(...)` et `setBaseItemIndex(...)` configurent le comportement ; la méthode utilitaire `PivotField.showValuesAs(...)` applique la même configuration en un seul appel. Appliquez cette configuration à un champ de données ou de valeur récupéré à partir de `PivotTable.getDataFields()`.

## **Membres de l'énumération PivotShowValuesAsType**
Le champ de données conserve sa fonction d'agrégation, telle que `Sum` ou `Count`, tandis que la fonctionnalité **Afficher les valeurs sous forme** modifie uniquement la manière dont la valeur agrégée est affichée.
En plus de l'utilisation directe des méthodes de définition de `PivotShowValuesSetting` (voir la dernière section), une méthode utilitaire permet d'appliquer la même configuration en un seul appel. Elle propose deux surcharges : l'une identifiant le champ de base et l'élément de base par index, l'autre par nom :

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `showValuesAsType` | Le calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `baseField` | Index, commençant à zéro, du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l'index du champ de ligne auquel appartient l'élément de base) ou, dans la surcharge `String`, le nom du champ de base. | Requis pour les huit formats relatifs à la base ci-dessous (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`) ; transmettez `0` (ou `null` dans la surcharge `String`) pour tous les autres formats. |
| `baseItem` | Index, commençant à zéro, de l'élément de base, avec deux valeurs sentinelles : `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) sélectionne l'élément précédent et `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) l'élément suivant. La surcharge `String` prend à la place le libellé de l'élément de base, ou `null` lorsque le format sélectionné ne nécessite aucun élément de base. | Nécessaire uniquement pour les trois formats relatifs à l'élément de base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`), qui évaluent l'élément de base ; les cinq formats relatifs au champ (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, les deux formats de classement) l'ignorent — transmettez `0` ou `null`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `NORMAL` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DIFFERENCE_FROM` | Affiche la valeur sous forme de différence par rapport à la valeur d'un élément de base dans un champ de base. | `baseField` + `baseItem` (un index ou un libellé, ou la valeur sentinelle de l'élément précédent ou suivant) |
| `PERCENTAGE_OF` | Affiche la valeur sous forme de pourcentage de la valeur d'un élément de base dans un champ de base. | `baseField` + `baseItem` (un index ou un libellé, ou la valeur sentinelle de l'élément précédent ou suivant) |
| `PERCENTAGE_DIFFERENCE_FROM` | Affiche la valeur sous forme de pourcentage de différence par rapport à la valeur d'un élément de base dans un champ de base. | `baseField` + `baseItem` (un index ou un libellé, ou la valeur sentinelle de l'élément précédent ou suivant) |
| `RUNNING_TOTAL_IN` | Affiche la valeur sous forme de total cumulé pour les éléments successifs d'un champ de base. | `baseField` (le champ dont l'ordre des éléments détermine l'accumulation) |
| `PERCENTAGE_OF_ROW` | Affiche la valeur sous forme de pourcentage du total de la ligne. | — |
| `PERCENTAGE_OF_COLUMN` | Affiche la valeur sous forme de pourcentage du total de la colonne. | — |
| `PERCENTAGE_OF_TOTAL` | Affiche la valeur sous forme de pourcentage du total général. | — |
| `INDEX` | Affiche la valeur à l'aide de la formule d'index d'Excel ((valeur * total général) / (total de la ligne * total de la colonne)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Affiche la valeur sous forme de pourcentage du total de sa ligne parente (pour les champs de ligne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Affiche la valeur sous forme de pourcentage du total de sa colonne parente (pour les champs de colonne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Affiche la valeur sous forme de pourcentage de son total parent. | `baseField` (le champ parent dont le total sert de référence) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Affiche la valeur sous forme de pourcentage d'un total cumulé dans un champ de base. | `baseField` (le champ d'accumulation) |
| `RANK_SMALLEST_TO_LARGEST` | Attribue un rang à la valeur, de la plus petite (1) à la plus grande. | `baseField` (le champ dont les éléments définissent la portée du classement) |
| `RANK_LARGEST_TO_SMALLEST` | Attribue un rang à la valeur, de la plus grande (1) à la plus petite. | `baseField` (le champ dont les éléments définissent la portée du classement) |

{{% alert color="primary" %}}
`showValuesAs(...)` définit exactement l'état de l'objet `PivotShowValuesSetting` au moyen de `setShowValuesAs(...)`, `setBaseFieldIndex(...)` et `setBaseItemIndex(...)` — la méthode et l'objet de configuration constituent deux moyens de configurer le même état, à l'image des sélecteurs de champ de base et d'élément de base dans la boîte de dialogue « Afficher les valeurs sous forme » d'Excel.
{{% /alert %}}

## **Afficher les valeurs sous forme de pourcentage du total**
Appelez la méthode `PivotField.showValuesAs(...)` avec `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` pour transformer chaque cellule du champ de données, y compris le total général, en une valeur représentant sa part du total général. Les nombres affichés sont donc exprimés sous forme de proportions de l'ensemble complet des résultats. Ce format compare chaque valeur uniquement au total général ; il ne nécessite donc ni champ de base ni élément de base — les arguments finaux (`0`, `0`) sont des valeurs de remplacement que le format ignore, comme l'indique le tableau des paramètres ci-dessus.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtenir et configurer PivotField.getShowValuesSetting**
Lisez la configuration actuelle à l'aide de `PivotField.getShowValuesSetting()` : l'accesseur en lecture seule renvoie l'objet `PivotShowValuesSetting` du champ, dont les propriétés décrivent le mode de calcul actuellement appliqué par « Afficher les valeurs sous forme ». Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs(...)` — elle applique tous les paramètres en un seul appel ; il n'est donc jamais nécessaire de définir les propriétés une à une.
L'objet `PivotShowValuesSetting` expose l'état appliqué par `showValuesAs(...)` :
- `getShowValuesAs()` / `setShowValuesAs(...)` permettent de sélectionner le calcul secondaire `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` spécifient l'index (commençant à zéro) du champ de base parmi les champs du tableau croisé dynamique. Ils sont utilisés par les formats relatifs à la base.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` spécifient l'élément de base : l'index (commençant à zéro) d'un élément précis du tableau croisé dynamique, ou l'une des deux valeurs sentinelles — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) pour l'élément précédent et `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) pour l'élément suivant. Ils sont utilisés par les formats relatifs à l'élément de base.
- `getBaseFieldName()` et `getBaseItemCaption()` fournissent, en lecture seule, le nom résolu du champ de base et le libellé résolu de l'élément de base ; par exemple, après avoir sélectionné la valeur sentinelle correspondant à l'élément précédent, `getBaseItemCaption()` renvoie `(previous)`.
Après avoir appelé `showValuesAs(...)`, appelez à nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et réaffiché avec la configuration mise à jour.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articles associés**
- [Gérer les champs de valeur dans un tableau croisé dynamique](/cells/fr/java/manage-value-fields/)
- [Actualiser un tableau croisé dynamique](/cells/fr/java/refresh-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}