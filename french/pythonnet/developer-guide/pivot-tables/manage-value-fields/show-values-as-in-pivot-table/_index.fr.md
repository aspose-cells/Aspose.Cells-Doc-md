---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Afficher les valeurs des champs de données du tableau croisé dynamique en pourcentage du total, en différence avec un élément de base, en totaux cumuls, en classements, et plus encore avec Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, tableau croisé dynamique, afficher les valeurs comme, format d'affichage des données, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /fr/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l’aide d’une fonction d’agrégation telle que `SUM` ou `COUNT`.  
La fonctionnalité **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un classement — afin de réaliser une analyse comparative sans formules d’assistance ni colonnes calculées.  
Les utilisations typiques comprennent l’analyse de parts du total, y compris les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulé en utilisant un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un élément de référence à l’aide de la différence ou de la différence en pourcentage par rapport à un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for Python via .NET, `PivotFieldDataDisplayFormat` sélectionne le calcul secondaire. La propriété en lecture seule `PivotField.show_values_setting` renvoie un objet `PivotShowValuesSetting`, dont les propriétés modifiables `calculation_type`, `base_field_index`, `base_item_position_type` et `base_item_index` configurent le comportement ; la méthode pratique `PivotField.show_values_as(...)` applique les mêmes quatre paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu à partir de `PivotTable.data_fields`.

## **Membres de l’énumération PivotFieldDataDisplayFormat**
Le champ de données conserve sa fonction d’agrégation, telle que `SUM` ou `COUNT`, tandis que Show Values As transforme uniquement la manière dont la valeur agrégée est affichée.  
En plus d’écrire directement les propriétés de `PivotShowValuesSetting` (voir la section précédente), une méthode pratique en un appel applique la même configuration :

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `display_format` | Le calcul secondaire `PivotFieldDataDisplayFormat` à appliquer. | Toujours. |
| `base_field` | Indice basé sur zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ de ligne auquel appartient l’élément de base). | Uniquement pour les six formats relatifs à une base ci-dessous (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`) ; ignoré par tout autre format. |
| `base_item_position_type` | Comment l’élément de base est choisi par rapport à l’élément actuel : `PivotItemPositionType.PREVIOUS`, `.NEXT` ou `.CUSTOM`. | Uniquement pour les trois formats à élément de base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) ; ignoré par tout autre format. |
| `base_item` | Indice basé sur zéro de l’élément de base. | Uniquement lorsque `base_item_position_type` est `CUSTOM` (l’indice d’élément sélectionne l’élément de base exact) ; ignoré pour `PREVIOUS` / `NEXT` et par tout format non‑base — passer `0`. |

| Type de calcul | Comportement | Paramètres de l’élément de base |
| --- | --- | --- |
| `NORMAL` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DIFFERENCE_FROM` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` uniquement avec `CUSTOM`) |
| `PERCENTAGE_OF` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` uniquement avec `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Affiche la valeur comme le pourcentage de différence par rapport à la valeur d’un élément de base dans un champ de base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` uniquement avec `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `base_field` (le champ dont l’ordre des éléments conduit à l’accumulation) |
| `PERCENTAGE_OF_ROW` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PERCENTAGE_OF_COLUMN` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PERCENTAGE_OF_TOTAL` | Affiche la valeur comme un pourcentage du total général. | — |
| `INDEX` | Affiche la valeur à l’aide de la formule d’index Excel ((valeur * total général) / (total de ligne * total de colonne)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Affiche la valeur comme un pourcentage du total de la ligne parent (pour les champs de ligne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Affiche la valeur comme un pourcentage du total de la colonne parent (pour les champs de colonne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Affiche la valeur comme un pourcentage de son total parent. | `baseField` (le champ parent servant de référence) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `base_field` (le champ d’accumulation) |
| `RANK_SMALLEST_TO_LARGEST` | Classe la valeur du plus petit (1) au plus grand. | — |
| `RANK_LARGEST_TO_SMALLEST` | Classe la valeur du plus grand (1) au plus petit. | — |

{{% alert color="primary" %}}
`show_values_as(...)` écrit les propriétés `PivotShowValuesSetting` (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`) — la méthode et l’objet de propriété sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.show_values_as` avec `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont donc lus comme des proportions de l’ensemble du jeu de résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il n’a donc besoin d’aucun champ de base ni d’élément de base — les arguments finaux (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sont des espaces réservés que le format ignore, comme indiqué dans le tableau des paramètres ci‑dessus.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Obtenir et configurer PivotField.show_values_setting**
Lire la configuration actuelle via `PivotField.show_values_setting` : la propriété en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les quatre propriétés décrivent le calcul Show Values As actif. Pour modifier la configuration, appelez la méthode `PivotField.show_values_as` — elle écrit les quatre paramètres en un seul appel, ainsi vous n’avez jamais besoin d’affecter les propriétés une par une.  
L’objet `PivotShowValuesSetting` expose les quatre propriétés écrites par `show_values_as` :
- `calculation_type` sélectionne le calcul secondaire `PivotFieldDataDisplayFormat`.
- `base_field_index` indique l’indice basé sur zéro du champ de base parmi les champs pivot. Il est utilisé par les formats relatifs à une base.
- `base_item_position_type` détermine la position de l’élément de base par rapport à l’élément actuel et accepte `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` ou `PivotItemPositionType.CUSTOM`.
- `base_item_index` indique l’indice basé sur zéro de l’élément de base et est utilisé lorsque `base_item_position_type` est `CUSTOM`.
Après avoir appelé `show_values_as`, appelez à nouveau `PivotTable.calculate_data()` afin que le corps du tableau croisé dynamique soit recalculé et réaffiché avec la configuration mise à jour.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Articles associés**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/python-net/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/python-net/refresh-pivot-table/)
- [Application d’un style au tableau croisé dynamique](/cells/fr/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}