---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Affichez les valeurs des champs de données du tableau croisé dynamique sous forme de pourcentage du total, de différence par rapport à un élément de base, de totaux cumulatifs, de classements et plus encore avec Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tableau croisé dynamique, afficher les valeurs comme, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /fr/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l'aide d'une fonction d'agrégation telle que `SUM` ou `COUNT`. La fonctionnalité **Afficher les valeurs comme** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un rang — afin de réaliser une analyse comparative sans formules auxiliaires ni colonnes calculées.  
Les usages typiques comprennent l’analyse de la part du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulatif à l’aide d’un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un repère grâce à la différence ou à la différence en pourcentage d’un élément de base ; et le classement des valeurs du plus petit au plus grand ou inversement.  
Dans Aspose.Cells for Python via Java, l’énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. La méthode en lecture seule `PivotField.getShowValuesSetting()` renvoie un objet `PivotShowValuesSetting`, dont les méthodes `setShowValuesAs(...)`, `setBaseFieldIndex(...)` et `setBaseItemIndex(...)` configurent le comportement ; la méthode de commodité `PivotField.showValuesAs(...)` applique les mêmes paramètres en un seul appel. Appliquez ces réglages à un champ de données ou de valeurs obtenu via `PivotTable.getDataFields()`.

## **Membres de l'énumération PivotShowValuesAsType**
Le champ de données conserve sa fonction d’agrégation, telle que `SUM` ou `COUNT`, tandis que **Afficher les valeurs comme** ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’utiliser directement les mutateurs de `PivotShowValuesSetting` (voir la dernière section), une méthode de commodité en un appel applique la même configuration. Elle se présente sous deux formes — l’une adressant le champ de base et l’élément de base par indice, l’autre par nom :

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `show_values_as_type` | Le calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `base_field` | Index zéro‑basé du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ ligne auquel appartient l’élément de base), ou — dans la forme par nom — le nom du champ de base. | Les huit formats relatifs au base ci‑dessous (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_SMALLEST_TO_LARGEST`) ; passez `0` (ou `None` dans la forme par nom) pour tout autre format. |
| `base_item` | Index zéro‑basé de l’élément de base, avec deux sentinelles : `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) sélectionne l’élément précédent et `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) l’élément suivant. La forme par nom utilise la légende de l’élément de base à la place, et `None` quand le format choisi ne nécessite aucun élément de base. | Seulement les trois formats relatifs à l’élément de base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) évaluent l’élément de base ; les cinq formats relatifs au champ (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, les deux rangs) l’ignorent — passez `0` ou `None`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `NORMAL` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DIFFERENCE_FROM` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `base_field` + `base_item` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PERCENTAGE_OF` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `base_field` + `base_item` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PERCENTAGE_DIFFERENCE_FROM` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `base_field` + `base_item` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `RUNNING_TOTAL_IN` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `base_field` (le champ dont l’ordre des éléments conduit à l’accumulation) |
| `PERCENTAGE_OF_ROW` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PERCENTAGE_OF_COLUMN` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PERCENTAGE_OF_TOTAL` | Affiche la valeur comme un pourcentage du total général. | — |
| `INDEX` | Affiche la valeur en utilisant la formule d’index Excel ((valeur * total général) / (total ligne * total colonne)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Affiche la valeur comme un pourcentage du total de la ligne parent (pour les champs de ligne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Affiche la valeur comme un pourcentage du total de la colonne parent (pour les champs de colonne imbriqués). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Affiche la valeur comme un pourcentage du total du parent. | `base_field` (le champ parent dont le total sert de référence) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `base_field` (le champ d’accumulation) |
| `RANK_SMALLEST_TO_LARGEST` | Classe la valeur du plus petit (1) au plus grand. | `base_field` (le champ dont les éléments définissent l’étendue du classement) |
| `RANK_LARGEST_TO_SMALLEST` | Classe la valeur du plus grand (1) au plus petit. | `base_field` (le champ dont les éléments définissent l’étendue du classement) |

{{% alert color="primary" %}}
`showValuesAs(...)` écrit les valeurs de `PivotShowValuesSetting` via `setShowValuesAs`, `setBaseFieldIndex` et `setBaseItemIndex` — la méthode et l’objet de paramétrage sont deux manières de configurer le même état, reproduisant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue **Afficher les valeurs comme** d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.showValuesAs` avec `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés représentent donc des proportions de l’ensemble du jeu de résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni élément de base ; les arguments supplémentaires (`0`, `0`) sont des espaces réservés que le format ignore, comme l’indique le tableau des paramètres ci‑dessus.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Obtenir et configurer PivotField.getShowValuesSetting()**
Lisez la configuration actuelle via `PivotField.getShowValuesSetting()` : la méthode en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les propriétés décrivent le calcul **Afficher les valeurs comme** actif. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs` — elle écrit tous les paramètres en un seul appel, vous n’avez donc jamais besoin de définir chaque propriété séparément.  
L’objet `PivotShowValuesSetting` expose l’état que `showValuesAs` écrit :
- `getShowValuesAs()` renvoie le calcul secondaire `PivotShowValuesAsType`, tandis que `setShowValuesAs(...)` le modifie.  
- `getBaseFieldIndex()` et `setBaseFieldIndex(...)` spécifient l’indice zéro‑basé du champ de base parmi les champs pivot. Il est utilisé par les formats relatifs au champ de base.  
- `getBaseItemIndex()` et `setBaseItemIndex(...)` spécifient l’élément de base : un indice zéro‑basé d’un élément pivot spécifique, ou l’une des deux sentinelles — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) pour l’élément précédent, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) pour l’élément suivant. Il est utilisé par les formats relatifs à l’élément de base.  
- `getBaseFieldName()` et `getBaseItemCaption()` sont des vues en lecture seule qui rapportent respectivement le nom du champ de base résolu et la légende de l’élément de base ; par exemple, après avoir sélectionné la sentinelle précédent‑élément, `getBaseItemCaption()` renvoie `(previous)`.  
Après avoir appelé `showValuesAs`, invoquez de nouveau `PivotTable.calculateData()` afin que le corps du tableau pivot soit recalculé et rendu avec la nouvelle configuration.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Articles associés**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/python-java/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}