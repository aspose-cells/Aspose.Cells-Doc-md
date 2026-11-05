---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for Python via Java – ancrer une règle à la région de données avec applyTo et une portée PivotConditionFormatScopeType, ou définir la cible avec addCellArea et getPivotAreas, puis associer les règles et les styles via getFormatConditions().addCondition.
keywords: Aspose.Cells for Python via Java, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /fr/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques – une région `PivotArea` ou `CellArea` est appliquée une fois et conserve son style, quelles que soient les valeurs. La mise en forme conditionnelle est la contrepartie basée sur des règles – mettre en évidence chaque montant supérieur à 200, ombrer la moitié centrale, ou signaler les éléments les moins bien classés – et la mise en évidence suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou actualisé.  
Dans Aspose.Cells, la mise en forme conditionnelle d’un tableau croisé dynamique se trouve dans la collection `PivotTable.getConditionalFormats()` . Chaque entrée est un `PivotConditionalFormat` qui répond à deux questions de manière indépendante :
- **Où la règle s'applique-t-elle ?** La région cible est définie soit via `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)`, qui reproduit le sélecteur de portée de l’interface Excel, soit via `PivotConditionalFormat.addCellArea(CellArea)` et la collection `PivotConditionalFormat.getPivotAreas()`, qui nomment explicitement la région.  
- **Quel est le test de la règle ?** Une ou plusieurs conditions sont ajoutées à `PivotConditionalFormat.getFormatConditions()` avec `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, et chaque condition possède son propre `Style`.

{{% alert color="primary" %}}
Ne pas appeler `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ou `FormatConditionCollection.addArea(CellArea)` sur l’objet `PivotConditionalFormat.getFormatConditions()` d’un format conditionnel pivot. Ces deux surcharges sont héritées de l’API de mise en forme conditionnelle ordinaire de la feuille de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques – la zone de cellules n’est jamais convertie en zone pivot, la demande est donc ignorée silencieusement. Définissez toujours la région sur le `PivotConditionalFormat` lui‑même (`applyTo`, `addCellArea` ou `getPivotAreas()`) et ajoutez la règle avec l’une des surcharges `addCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (méthode de l'interface Excel)**
La première façon positionne la règle comme le fait l’interface utilisateur d’Excel. Une cellule du tableau croisé dynamique est identifiée par ses coordonnées de feuille de calcul basées sur zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu’où la règle doit s’étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.DATA` – toutes les cellules de valeur générées par le tableau croisé dynamique, y compris les totaux généraux.  
- `PivotConditionFormatScopeType.FIELD` – les cellules de valeur qui appartiennent au champ identifié par la cellule, excluant les totaux généraux. La cellule doit être une cellule de champ, telle qu’une étiquette de champ de ligne ; passer une cellule de valeur génère une exception.  
- `PivotConditionFormatScopeType.SELECTION` – uniquement les cellules de valeur à l’intersection sélectionnée par la cellule, généralement une seule cellule de valeur.
L’exemple ci‑dessous crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche se trouve en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `DATA`, et met en évidence chaque montant supérieur à 200 en blanc gras sur fond rouge. Avec les valeurs Pomme 220, Banane 330, Cerise 200 et le total général 750, la règle colore F4, F5 et F7 – la région résolue est toute la colonne de données F4 : F7, et seules les cellules dont la valeur satisfait la règle s’illuminent.

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
    Color,
    BackgroundType,
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Tableau croisé dynamique avec son coin supérieur gauche en E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Ancrer le format conditionnel à F4 (ligne 3, colonne 5) avec la portée Données
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Règle - mettre en évidence les montants supérieurs à 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

Ancrer la même règle à l’étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `FIELD` la résout en F4 : F6 – la même colonne de données sans la ligne du total général – car la portée décrit maintenant le champ `Fruit` plutôt que l’ensemble de la zone de valeurs. La portée `SELECTION` ancrée en F4 se résout uniquement à F4.

## **Définir la région manuellement**
La seconde méthode ignore le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec addCellArea()**
`addCellArea(CellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont basées sur zéro, et la région correspond exactement au rectangle indiqué – aucune expansion vers la colonne de données et aucune logique de total général. Utilisez‑la lorsque les cellules d’intérêt forment un rectangle fixe connu de la mise en page actuelle du tableau croisé dynamique.

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
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Cibler le rectangle F4:F6 (les cellules de valeur sans le total général)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Règle - italique sur jaune clair pour les montants entre 150 et 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **Une région pivot sémantique avec getPivotAreas()**
La collection `getPivotAreas()` reprend le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `PivotArea.select(...)` ou `PivotArea.selectField(...)`, puis ajoutez‑le avec `getPivotAreas().addPivotArea(PivotArea)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lors du rafraîchissement du tableau croisé dynamique et du déplacement de la mise en page. La surcharge `getPivotAreas().add(PivotArea)` compile toujours mais est marquée obsolète – privilégiez `addPivotArea`.

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
    Color,
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Attacher la règle au champ de données Amount en tant que région sémantique
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Règle - texte gris pour les montants inférieurs à 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `PivotTable.getConditionalFormats().add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur – rouvrir le fichier dans l’exemple ci‑dessous montre la même règle avec son type, son opérateur et sa formule intacts, et `PivotConditionalFormat.getCellAreas()` indique les mêmes régions. Les entrées qui n’ont jamais reçu de condition sont supprimées lors de l’enregistrement du classeur, de la même manière qu’Excel élimine une mise en forme conditionnelle dépourvue de règle.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# Ceci affiche :
# Formats conditionnels : 1
# Format 0 : CellValue GreaterThan formula1==200
#     lignes 4-7, colonnes 6-6        (F4:F7, la région de données résolue)
jpype.shutdownJVM()
```

## **Articles connexes**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-java/apply-style-to-pivot-table/)
- [Formater une partie du tableau croisé dynamique](/cells/fr/python-java/format-part-of-pivot-table/)
- [Top 10 Afficher ou filtrer dans le tableau croisé dynamique](/cells/fr/python-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}