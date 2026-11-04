---
title: Formater une partie d’un tableau croisé dynamique
description: Formater une partie d’un tableau croisé dynamique dans Aspose.Cells for Python via Java en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.format, les formats étant stockés dans PivotTable.getPivotFormats() et conservés lorsque le tableau croisé dynamique est actualisé.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, Aspose.Cells for Python via Java, tableau croisé dynamique, format, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /fr/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
`PivotTable.formatAll` applique un seul style à l’ensemble du tableau croisé dynamique et est décrit sur la page parente. Il ne fait pas de distinction entre les étiquettes, les valeurs, les totaux ou des régions particulières du rapport.  
En pratique, seule une partie d’un tableau croisé dynamique doit généralement se démarquer. Les cibles courantes comprennent les étiquettes appartenant à un champ de ligne, les cellules de valeur produites par un champ, la ligne du total général, ou un rectangle arbitraire comme les deux premières lignes d’éléments.  
Appliquer un style directement aux cellules de la feuille de calcul d’un tableau croisé dynamique n’est pas équivalent. Excel stocke la mise en forme du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les étiquettes d’un champ ou les valeurs de données, et il est ré‑résolu lorsque le tableau croisé dynamique est recalculé, actualisé ou développé. En revanche, un style écrit directement sur une cellule appartient à la position de cette cellule et n’est pas suivi par le modèle pivot.  
Aspose.Cells expose la famille complète de surcharges de `PivotTable.format` afin que les deux types de mise en forme soient disponibles :
- `format(PivotArea, Style)` ancre un style à une région sémantique construite avec `PivotArea.select` ou `PivotArea.selectField`.
- `format(CellArea, Style)` ancre un style à un rectangle de la feuille de calcul à l’intérieur du tableau croisé dynamique.
- `format(int row, int column, Style)` cible une cellule.
- `formatAll(Style)` formate l’ensemble du tableau croisé dynamique.

## **Formater une zone Pivot**
Le flux de travail basé sur les zones sémantiques est l’approche recommandée lorsqu’une mise en évidence doit suivre un champ ou une région du rapport.  
1. Créez une `PivotArea` avec `PivotArea(pivot_table)`. L’objet décrit une région sémantique appartenant à ce tableau croisé dynamique spécifique.  
1. Sélectionnez un champ par sa position indexée à partir de zéro sur un axe donné avec `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DATA_AND_LABEL` sélectionne à la fois les étiquettes et les données du champ.  
   - `PivotTableSelectionType.LABEL_ONLY` sélectionne uniquement les étiquettes du champ.  
   - `PivotTableSelectionType.DATA_ONLY` sélectionne uniquement les cellules de données du champ.  
1. Sélectionnez un champ par son nom avec `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. Lorsqu’un champ de ligne est sélectionné par son nom, la région se résout aux cellules de valeur produites par les éléments de ce champ.  
1. Créez un `Style` avec `workbook.createStyle()`, configurez sa police, sa couleur de premier plan et son motif de remplissage solide, puis transmettez le style à `PivotTable.format(area, style)`.  
1. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.getPivotFormats()`.  
1. Les formats ancrés au champ sont appliqués lorsque les données pivot sont calculées. Par conséquent, appelez `PivotTable.calculateData()` après avoir appliqué les formats afin que les styles deviennent visibles.  
L’exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux étiquettes de ligne `Fruit` avec `PivotArea.select` et `PivotTableSelectionType.LABEL_ONLY`, applique un style aux cellules de valeur générées par ce même champ de ligne avec `PivotArea.selectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient appliqués.

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
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Formater une zone de cellules du tableau croisé dynamique**
Utilisez `PivotTable.format(CellArea, Style)` lorsque la région d’intérêt est un simple rectangle de feuille de calcul plutôt qu’une région pivot sémantique.  
Une `CellArea` est décrite par les propriétés `getStartRow()`, `getStartColumn()`, `getEndRow()` et `getEndColumn()`. Les valeurs sont des coordonnées de feuille de calcul indexées à partir de zéro, et les coordonnées de fin identifient la dernière ligne et la dernière colonne incluses dans le rectangle, de sorte que la zone couvre les cellules depuis la position de départ jusqu’à la position de fin, incluses.  
Contrairement à un format ancré au champ, un format `CellArea` est appliqué aux cellules immédiatement. Un autre appel à `PivotTable.calculateData()` n’est pas nécessaire pour que le style apparaisse.  
Un rectangle `CellArea` peut contenir à la fois des cellules d’étiquettes et des cellules de valeur. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.  
L’exemple suivant formate le rectangle `E4:F5` du tableau croisé dynamique avec un style italique, bleu clair, et enregistre le classeur sans autre recalcul.

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
    CellArea,
    PivotFieldType,
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
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **Comment les zones Pivot et les zones de cellules sont mappées**
Excel stocke la mise en forme du tableau croisé dynamique sous forme d’enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu’une demande de mise en forme est traduite en zones pivot lorsqu’elle est enregistrée.  
La relation entre la `CellArea` fournie par l’utilisateur et les zones pivot stockées en interne est de plusieurs à plusieurs dans les deux sens.  
- Une `CellArea` peut produire plusieurs zones pivot. Si le rectangle couvre à la fois des cellules d’étiquettes et des cellules de valeur, il est décomposé en règles distinctes d’étiquette et de données, car le modèle pivot traite indépendamment la mise en forme des étiquettes et des données.  
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu’une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C’est pourquoi `PivotArea.getCellAreas()` renvoie une collection plutôt qu’un seul rectangle.  
Chaque opération de mise en forme effectuée via `PivotTable.format` est enregistrée dans `PivotTable.getPivotFormats()`. Chaque entrée `PivotTableFormat` expose la `PivotArea` associée et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu’une `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.  
Pour distinguer les régions stockées, chaque `PivotArea` expose les indicateurs `getOnlyLabel()` et `getOnlyData()`. L’exemple ci‑dessous formate un seul rectangle couvrant à la fois les étiquettes et les valeurs, inspecte `PivotTable.getPivotFormats()`, et affiche les coordonnées `CellArea` auxquelles chaque zone pivot stockée se résout.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
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
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Parce que les formats sont stockés sous forme de zones pivot plutôt que comme des styles de cellule ordinaires, ils survivent aux recalculs et aux actualisations. Lorsque le tableau croisé dynamique est actualisé avec `PivotTable.refreshData()`, recalculé avec `PivotTable.calculateData()`, ou enregistré puis rechargé, chaque zone pivot stockée se résout de nouveau à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez une `PivotArea` construite avec `select` ou `selectField` lorsqu’une mise en évidence doit rester attachée à un champ ou à une région sémantique lors des actualisations, et utilisez une `CellArea` lorsqu’il suffit de formater un rectangle fixe dans la disposition actuelle du tableau croisé dynamique. La surcharge `format(int row, int column, Style)` à cellule unique cible une cellule individuelle. Utilisez `formatAll`, décrit sur la page parente, lorsque l’ensemble du tableau croisé dynamique doit être reformatté d’un coup.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-java/apply-style-to-pivot-table/)
- [Ajouter des champs de lignes et de colonnes au tableau croisé dynamique](/cells/fr/python-java/pivot-table-add-row-and-column-fields/)
- [Gestion des champs de valeurs dans le tableau croisé dynamique](/cells/fr/python-java/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}