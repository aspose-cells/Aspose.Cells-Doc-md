---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Affichez les valeurs des champs de données du tableau croisé dynamique en pourcentage du total, une différence par rapport à un élément de base, des totaux cumulatifs, des classements, et plus encore avec Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs comme, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /fr/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l’aide d’une fonction d’agrégation telle que `SUM` ou `COUNT`. La fonctionnalité **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un classement — ce qui permet d’effectuer une analyse comparative sans formules d’assistance ni colonnes calculées.  
Les utilisations typiques comprennent l’analyse de parts du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulatif à l’aide d’un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un élément de référence en utilisant la différence ou la différence en pourcentage par rapport à un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for Python via .NET, l’énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. La propriété en lecture seule `PivotField.show_values_setting` renvoie un objet `PivotShowValuesSetting`, dont les propriétés modifiables `show_values_as`, `base_field_index` et `base_item_index` configurent le comportement ; la méthode de commodité `PivotField.show_values_as(...)` applique les mêmes paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu à partir de `PivotTable.data_fields`.

## **Membres de l’énumération PivotShowValuesAsType**
Le champ de données conserve sa fonction d’agrégation, telle que `SUM` ou `COUNT`, tandis que Show Values As ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’écrire directement les propriétés de `PivotShowValuesSetting` (voir la section précédente), une méthode de commodité en un appel applique la même configuration. Elle se présente sous deux formes — l’une adressant le champ de base et l’autre l’élément de base par indice, l’autre par nom :

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `show_values_as_type` | Le calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `base_field` | Indice zéro‑base du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ de ligne auquel appartient l’élément de base), ou — dans la forme par nom — le nom du champ de base. | Les huit formats relatifs à la base ci‑dessus (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`) ; passez `0` (ou `None` dans la forme par nom) pour tous les autres formats. |
| `base_item` | Indice zéro‑base de l’élément de base, avec deux sentinelles : `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) sélectionne l’élément précédent et `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) l’élément suivant. La forme par nom prend la légende de l’élément de base, et `None` lorsque le format sélectionné ne nécessite aucun élément de base. | Seuls les trois formats relatifs à l’élément de base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) évaluent l’élément de base ; les cinq formats relatifs au champ (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, les deux classements) l’ignorent — passez `0` ou `None`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `NORMAL` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DIFFERENCE_FROM` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `base_field` + `base_item` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PERCENTAGE_OF` | Affiche la valeur en pourcentage de la valeur d’un élément de base dans un champ de base. | `base_field` + `base_item` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PERCENTAGE_DIFFERENCE_FROM` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `base_field` + `base_item` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `RUNNING_TOTAL_IN` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `base_field` (le champ dont l’ordre des éléments conduit à l’accumulation) |
| `PERCENTAGE_OF_ROW` | Affiche la valeur en pourcentage du total de la ligne. | — |
| `PERCENTAGE_OF_COLUMN` | Affiche la valeur en pourcentage du total de la colonne. | — |
| `PERCENTAGE_OF_TOTAL` | Affiche la valeur en pourcentage du total général. | — |
| `INDEX` | Affiche la valeur en utilisant la formule d’index Excel ((valeur * total général) / (total ligne * total colonne)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Affiche la valeur en pourcentage du total de sa ligne parente (pour les champs de ligne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Affiche la valeur en pourcentage du total de sa colonne parente (pour les champs de colonne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Affiche la valeur en pourcentage de son total parent. | `base_field` (le champ parent dont le total sert de référence) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Affiche la valeur en pourcentage d’un total cumulé dans un champ de base. | `base_field` (le champ d’accumulation) |
| `RANK_SMALLEST_TO_LARGEST` | Classe la valeur du plus petit (1) au plus grand. | `base_field` (le champ dont les éléments définissent le domaine de classement) |
| `RANK_LARGEST_TO_SMALLEST` | Classe la valeur du plus grand (1) au plus petit. | `base_field` (le champ dont les éléments définissent le domaine de classement) |

{{% alert color="primary" %}}
`show_values_as(...)` écrit les propriétés de `PivotShowValuesSetting` (`show_values_as`, `base_field_index`, `base_item_index`) — la méthode et l’objet de propriété sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.show_values_as` avec `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont ainsi exprimés en proportions de l’ensemble complet des résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni élément de base — les arguments suivants (`0`, `0`) sont des espaces réservés que le format ignore, comme le précise le tableau des paramètres ci‑dessus.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
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
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Obtenir et configurer PivotField.show_values_setting**
Lisez la configuration actuelle via `PivotField.show_values_setting` : la propriété en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les propriétés décrivent le calcul Show Values As actif. Pour modifier la configuration, appelez la méthode `PivotField.show_values_as` — elle écrit tous les paramètres en un seul appel, vous n’avez jamais besoin d’assigner les propriétés une par une.  
L’objet `PivotShowValuesSetting` expose l’état que `show_values_as` écrit :
- `show_values_as` sélectionne le calcul secondaire `PivotShowValuesAsType`.
- `base_field_index` spécifie l’indice zéro‑base du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à la base.
- `base_item_index` spécifie l’élément de base : un indice zéro‑base d’un élément pivot spécifique, ou l’une des deux sentinelles — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) pour l’élément précédent, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) pour l’élément suivant. Il est utilisé par les formats relatifs à l’élément de base.
- `base_field_name` et `base_item_caption` sont des vues en lecture seule qui indiquent respectivement le nom du champ de base résolu et la légende de l’élément de base ; par exemple, après avoir sélectionné la sentinelle d’élément précédent, `base_item_caption` renvoie `(previous)`.
Après avoir appelé `show_values_as`, appelez à nouveau `PivotTable.calculate_data()` afin que le corps du tableau croisé dynamique soit recalculé et rendu avec la configuration mise à jour.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Articles associés**
- [Gestion des champs de valeurs dans le tableau croisé dynamique](/cells/fr/python-net/manage-value-fields/)
- [Actualiser le tableau croisé dynamique](/cells/fr/python-net/refresh-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}