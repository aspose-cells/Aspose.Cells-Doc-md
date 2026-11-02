---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Afficher les valeurs des champs de données d’un tableau croisé dynamique en pourcentage du total, en différence d’un élément de base, en totaux cumulatifs, en classements et plus encore avec Aspose.Cells for Java.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs comme, format d’affichage des données, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /fr/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données avec une fonction d'agrégation telle que `Sum` ou `Count`. La fonctionnalité **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi, ou un classement — vous permettant d’effectuer une analyse comparative sans formules auxiliaires ni colonnes calculées.  
Les utilisations typiques incluent l’analyse de **la** part du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; le **rapport** cumulatif en utilisant un total cumulé dans un champ de période ; l’analyse de variance par rapport à un élément de référence en utilisant la différence ou la différence en pourcentage par rapport à un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for Java, `PivotFieldDataDisplayFormat` sélectionne le calcul secondaire. Le getter en lecture seule `PivotField.getShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`, dont les méthodes `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` et `setBaseItemIndex(...)` configurent le comportement ; la méthode de commodité `PivotField.showValuesAs(...)` applique les mêmes quatre paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu via `PivotTable.getDataFields()`.

## **Membres de l'énumération PivotFieldDataDisplayFormat**
Le champ de données conserve sa fonction d'agrégation, telle que Sum ou Count, tandis que Show Values As ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’utiliser directement les accesseurs de `PivotShowValuesSetting` (voir la section précédente), une méthode de commodité en un appel applique la même configuration :

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `displayFormat` | Le calcul secondaire `PivotFieldDataDisplayFormat` à appliquer. | Toujours. |
| `baseField` | Indice basé sur zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ ligne auquel appartient l’élément de base). | Uniquement pour les six formats relatifs à une base ci-dessous (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`) ; ignoré par tout autre format. |
| `baseItemPositionType` | Comment l’élément de base est choisi par rapport à l’élément actuel : `PivotItemPositionType.PREVIOUS`, `NEXT` ou `CUSTOM`. | Uniquement pour les trois formats à élément de base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) ; ignoré par tout autre format. |
| `baseItem` | Indice basé sur zéro de l’élément de base. | Seulement lorsque `baseItemPositionType` est `CUSTOM` (l’indice de l’élément choisit exactement l’élément de base) ; ignoré pour `PREVIOUS` / `NEXT` et pour tout format non‑base — passez `0`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `NORMAL` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DIFFERENCE_FROM` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` uniquement avec `CUSTOM`) |
| `PERCENTAGE_OF` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` uniquement avec `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` uniquement avec `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments pilote l’accumulation) |
| `PERCENTAGE_OF_ROW` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PERCENTAGE_OF_COLUMN` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PERCENTAGE_OF_TOTAL` | Affiche la valeur comme un pourcentage du total général. | — |
| `INDEX` | Affiche la valeur en utilisant la formule d’index Excel ((valeur * total général) / (total ligne * total colonne)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Affiche la valeur comme un pourcentage du total de la ligne parente (pour les champs de ligne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Affiche la valeur comme un pourcentage du total de la colonne parente (pour les champs de colonne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Affiche la valeur comme un pourcentage de son total parent. | `baseField` (le champ parent servant de référence) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RANK_SMALLEST_TO_LARGEST` | Classe la valeur du plus petit (1) au plus grand. | — |
| `RANK_LARGEST_TO_SMALLEST` | Classe la valeur du plus grand (1) au plus petit. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` définit les valeurs de `PivotShowValuesSetting` via `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` et `setBaseItemIndex(...)` — la méthode et l’objet de propriété sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.showValuesAs(...)` avec `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` pour convertir chaque cellule du champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont donc exprimés en proportions de l’ensemble complet des résultats. Ce format compare chaque valeur uniquement au total général, il n’a donc besoin d’aucun champ de base ni **d**élément de base — les arguments supplémentaires (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sont des espaces réservés que le format ignore, comme indiqué dans le tableau des paramètres ci‑dessus.

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
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtenir et configurer PivotField.getShowValuesSetting**
Lisez la configuration actuelle via `PivotField.getShowValuesSetting()` : le getter en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les quatre propriétés décrivent le calcul Show Values As actif. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs(...)` — elle écrit les quatre paramètres en un seul appel, vous n’avez donc jamais besoin de définir chaque propriété séparément.  
L’objet `PivotShowValuesSetting` expose les quatre propriétés que `showValuesAs(...)` écrit :
- `getCalculationType()` / `setCalculationType(...)` sélectionne le calcul secondaire `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` spécifie l’indice basé sur zéro du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à une base.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` détermine comment l’élément de base est positionné par rapport à l’élément actuel et accepte `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` ou `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` spécifie l’indice basé sur zéro de l’élément de base et est utilisé lorsque `BaseItemPositionType` est `CUSTOM`.
Après avoir appelé `showValuesAs(...)`, appelez de nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et réaffiché avec la configuration mise à jour.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Articles associés**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/java/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/java/refresh-pivot-table/)
- [Application du style au tableau croisé dynamique](/cells/fr/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}