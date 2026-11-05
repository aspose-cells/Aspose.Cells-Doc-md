---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for Python via .NET – ancrer une règle à la région de données avec la méthode apply_to et une portée PivotConditionFormatScopeType, ou définir la cible avec add_cell_area et pivot_areas, puis lier les règles et les styles via format_conditions.add_condition.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /fr/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques — une région `PivotArea` ou `CellArea` est appliquée une fois et conserve son style quels que soient les valeurs. La mise en forme conditionnelle est la contrepartie pilotée par des règles — mettre en évidence chaque montant supérieur à 200, ombrer les cinquante pour cent du milieu, ou signaler les éléments les moins bien classés — et la mise en évidence suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou rafraîchi.  
Dans Aspose.Cells, la mise en forme conditionnelle d’un tableau croisé dynamique réside dans la collection `pivot_table.conditional_formats`. Chaque entrée est un `PivotConditionalFormat` qui répond indépendamment à deux questions :
- **Où la règle s'applique-t-elle ?** La région cible est définie soit via `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)`, qui reproduit le sélecteur de portée de l’interface utilisateur Excel, soit via `add_cell_area(cell_area: CellArea)` et la collection `pivot_areas`, qui nomment explicitement la région.
- **Que teste la règle ?** Une ou plusieurs conditions sont ajoutées à `format_conditions` avec `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)`, chaque condition portant son propre `style`.

{{% alert color="primary" %}}
Ne pas appeler `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` ou `format_conditions.add_area(cell_area: CellArea)` sur l’objet `format_conditions` d’un format conditionnel de pivot. Ces deux surcharges sont héritées de l’API de mise en forme conditionnelle ordinaire des feuilles de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques — la zone de cellules n’est jamais convertie en zone de pivot, la requête est donc ignorée silencieusement. Définissez toujours la région sur le `pivot_conditional_format` lui‑même (`apply_to`, `add_cell_area` ou `pivot_areas`) et ajoutez la règle avec l’une des surcharges `add_condition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (méthode de l'interface Excel)**
La première méthode place la règle comme le fait l’interface utilisateur d’Excel. Une cellule du tableau croisé dynamique est identifiée par ses coordonnées de feuille de calcul indexées à zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu’où la règle doit s’étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.DATA` — toutes les cellules de valeur que le tableau croisé dynamique produit, y compris les totaux généraux.
- `PivotConditionFormatScopeType.FIELD` — les cellules de valeur qui appartiennent au champ identifié par la cellule, en excluant les totaux généraux. La cellule doit être une cellule de champ, telle qu’une étiquette de champ de ligne ; passer une cellule de valeur déclenche une exception.
- `PivotConditionFormatScopeType.SELECTION` — uniquement les cellules de valeur à l’intersection sélectionnée par la cellule, généralement une seule cellule de valeur.
L’exemple ci‑dessous crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche se trouve en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `PivotConditionFormatScopeType.DATA`, et met en évidence chaque montant supérieur à 200 en blanc gras sur rouge. Avec les valeurs **Apple** 220, **Banana** 330, **Cherry** 200 et le total général 750, la règle colore F4, F5 et F7 — la région résolue est toute la colonne de données F4 : F7, et seules les cellules dont la valeur satisfait la règle s’illuminent.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Tableau croisé dynamique avec son coin supérieur gauche en E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Ancre le format conditionnel à F4 (ligne 3, colonne 5) avec la portée Data
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Règle - mettre en évidence les montants supérieurs à 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

Ancrer la même règle à l’étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `PivotConditionFormatScopeType.FIELD` résout à F4 : F6 au lieu de F4 : F7 — la même colonne de données sans la ligne du total général — car la portée décrit maintenant le champ **Fruit** plutôt que l’ensemble de la zone de valeurs. La portée `PivotConditionFormatScopeType.SELECTION` ancrée à F4 ne résout qu’à F4.

## **Définir la région manuellement**
La deuxième méthode évite le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec add_cell_area**
`add_cell_area(cell_area: CellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul indexées à zéro, et la région correspond exactement au rectangle indiqué — aucune extension vers la colonne de données et aucune logique de total général. Utilisez‑la lorsque les cellules d’intérêt constituent un rectangle fixe connu de la mise en page actuelle du tableau croisé dynamique.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Cibler le rectangle F4:F6 (les cellules de valeur sans le total général)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Règle - italique sur jaune clair pour les montants entre 150 et 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **Une région pivot sémantique avec pivot_areas**
`pivot_areas` utilise le même modèle de région sémantique que la page sœur pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `select` ou `select_field`, puis ajoutez‑le avec `pivot_areas.add_pivot_area(pivot_area)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est rafraîchi et que la disposition change. La surcharge `pivot_areas.add(pivot_area)` compile encore mais est marquée comme obsolète — privilégiez `add_pivot_area`.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Attacher la règle au champ de données Amount en tant que région sémantique
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Règle - texte gris pour les montants inférieurs à 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `pivot_table.conditional_formats.add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur — la réouverture du fichier dans l’exemple ci‑dessous montre la même règle avec son type, son opérateur et sa formule intacts, et `get_cell_areas()` indique les mêmes régions. Les entrées qui n’ont jamais reçu de condition sont supprimées lors de l’enregistrement du classeur, de la même manière qu’Excel élimine une mise en forme conditionnelle dépourvue de règle.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# Ceci affiche :
# Formats conditionnels : 1
# Format 0 : CellValue GreaterThan formula1==200
#     lignes 4-7, colonnes 6-6        (F4:F7, la région de données résolues)
```

## **Articles connexes**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Formater une partie du tableau croisé dynamique](/cells/fr/python-net/format-part-of-pivot-table/)
- [Afficher ou filtrer le top 10 dans le tableau croisé dynamique](/cells/fr/python-net/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}