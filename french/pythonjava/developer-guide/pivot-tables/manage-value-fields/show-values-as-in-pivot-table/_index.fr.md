---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Affichez les valeurs du champ de données du tableau croisé dynamique en pourcentage du total, une différence par rapport à un élément de base, des totaux cumulés, des rangs, et plus avec Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs comme, format d'affichage des données, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /fr/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique agrège habituellement chaque champ de données avec une fonction d’agrégation telle que `Sum` ou `Count`. La fonction **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi, ou un rang — ce qui permet d’effectuer des analyses comparatives sans formules auxiliaires ni colonnes calculées.  
Les utilisations typiques comprennent l’analyse de **la** part du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulatif en utilisant un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un élément de référence à l’aide de la différence ou de la différence en pourcentage d’un élément de base ; et le classement des valeurs du plus petit au plus grand ou inversement.  
Dans Aspose.Cells for Python via Java, `PivotFieldDataDisplayFormat` sélectionne le calcul secondaire. La méthode en lecture seule `PivotField.getShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`, dont les méthodes modifiables `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` et `setBaseItemIndex` configurent le comportement ; la méthode de commodité `PivotField.showValuesAs(...)` applique les mêmes quatre paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu via `PivotTable.getDataFields()`.

## **Membres de l’énumération PivotFieldDataDisplayFormat**
Le champ de données conserve sa fonction d’agrégation, comme Sum ou Count, tandis que Show Values As ne transforme que la façon dont la valeur agrégée est affichée.  
En plus de définir directement les propriétés de `PivotShowValuesSetting` (voir la section suivante), une méthode de commodité en un seul appel applique la même configuration :

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `displayFormat` | Le calcul secondaire `PivotFieldDataDisplayFormat` à appliquer. | Toujours. |
| `baseField` | Index zéro‑based du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’index du champ de ligne auquel appartient l’élément de base). | Uniquement pour les six formats relatifs à une base ci-dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`) ; ignoré par tout autre format. |
| `baseItemPositionType` | Mode de sélection de l’élément de base par rapport à l’élément courant : `PivotItemPositionType.Previous`, `.Next` ou `.Custom`. | Uniquement pour les trois formats à élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) ; ignoré par tout autre format. |
| `baseItem` | Index zéro‑based de l’élément de base. | Uniquement lorsque `baseItemPositionType` est `Custom` (l’index désigne l’élément de base exact) ; ignoré pour `Previous`/`Next` et par tout format non‑base — passez `0`. |

| Type de calcul | Comportement | Paramètres de l’élément de base |
| --- | --- | --- |
| `Normal` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DifferenceFrom` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageOf` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageDifferenceFrom` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `RunningTotalIn` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments pilote l’accumulation) |
| `PercentageOfRow` | Affiche la valeur comme pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur comme pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur comme pourcentage du total général. | — |
| `Index` | Affiche la valeur en utilisant la formule d’index d’Excel ((valeur * total général) / (total ligne * total colonne)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur comme pourcentage du total de la ligne parent (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur comme pourcentage du total de la colonne parent (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur comme pourcentage de son total parent. | `baseField` (le champ parent servant de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur comme pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RankSmallestToLargest` | Classe la valeur du plus petit (1) au plus grand. | — |
| `RankLargestToSmallest` | Classe la valeur du plus grand (1) au plus petit. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` écrit les valeurs de `PivotShowValuesSetting` via `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` et `setBaseItemIndex` — la méthode et l’objet de paramètres sont deux façons de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.showValuesAs` avec `PivotFieldDataDisplayFormat.PercentageOfTotal` pour convertir chaque cellule du champ de données, y compris le total général, en sa part du total général. Les nombres affichés représentent donc des proportions de l’ensemble du jeu de résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni élément de base — les arguments supplémentaires (`0`, `PivotItemPositionType.Previous`, `0`) sont des espaces réservés que le format ignore, comme indiqué dans le tableau des paramètres ci‑dessus.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Obtenir et configurer PivotField.getShowValuesSetting()**
Lisez la configuration actuelle via `PivotField.getShowValuesSetting()` : la méthode en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les quatre propriétés décrivent le calcul Show Values As actif. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs` — elle écrit les quatre paramètres en un seul appel, de sorte que vous n’avez jamais besoin d’assigner les propriétés individuellement.  
L’objet `PivotShowValuesSetting` expose les quatre propriétés que `showValuesAs` écrit :
- `getCalculationType()` renvoie le calcul secondaire `PivotFieldDataDisplayFormat`, tandis que `setCalculationType(...)` le modifie.
- `getBaseFieldIndex()` et `setBaseFieldIndex(...)` spécifient l’index zéro‑based du champ de base au sein des champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à une base.
- `getBaseItemPositionType()` et `setBaseItemPositionType(...)` déterminent comment l’élément de base est positionné par rapport à l’élément courant et acceptent `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` ou `PivotItemPositionType.Custom`.
- `getBaseItemIndex()` et `setBaseItemIndex(...)` spécifient l’index zéro‑based de l’élément de base et sont utilisés lorsque `BaseItemPositionType` vaut `Custom`.
Après avoir appelé `showValuesAs`, appelez de nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et rendu avec la configuration mise à jour.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Articles associés**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/python-java/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}