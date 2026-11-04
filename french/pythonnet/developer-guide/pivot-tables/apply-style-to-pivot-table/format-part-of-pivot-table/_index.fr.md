---
title: Format Part of a Pivot Table
description: Formatez une partie d'un tableau croisé dynamique dans Aspose.Cells for Python via .NET en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.format, les formats étant stockés dans PivotTable.pivot_formats et conservés lors du rafraîchissement du tableau croisé dynamique.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Python via .NET, tableau croisé dynamique, mise en forme, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /fr/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
`PivotTable.format_all` applique un seul style à l'ensemble du tableau croisé dynamique et est couvert sur la page parente. Il ne fait pas de distinction entre les étiquettes, les valeurs, les totaux ou les régions particulières du rapport.  
En pratique, seule une partie d'un tableau croisé dynamique doit généralement être mise en évidence. Les cibles courantes comprennent les étiquettes appartenant à un champ de ligne, les cellules de valeurs générées par un champ, la ligne de total général, ou un rectangle arbitraire tel que les deux premières lignes d'éléments.  
Appliquer un style directement aux cellules de la feuille de calcul d'un tableau croisé dynamique n'est pas équivalent. Excel stocke la mise en forme du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les étiquettes d'un champ ou les valeurs de données, et il est à nouveau résolu lorsque le tableau croisé dynamique est recalculé, actualisé ou développé. En revanche, un style écrit directement dans une cellule appartient à la position de cette cellule et n'est pas suivi par le modèle de tableau croisé dynamique.  
Aspose.Cells expose la famille complète de surcharges `PivotTable.format` afin que les deux types de mise en forme soient disponibles :
- `format(PivotArea, Style)` ancre un style à une région sémantique construite avec `PivotArea.select` ou `PivotArea.select_field`.
- `format(CellArea, Style)` ancre un style à un rectangle de feuille de calcul à l'intérieur du tableau croisé dynamique.
- `format(int row, int column, Style)` cible une cellule.
- `format_all(Style)` met en forme l'ensemble du tableau croisé dynamique.

## **Formater une zone Pivot**
Le flux de travail basé sur les zones sémantiques est l'approche recommandée lorsqu'une mise en évidence doit suivre un champ ou une région du rapport.
1. Créez un `PivotArea` avec `PivotArea(pivot_table)`. L'objet décrit une région sémantique qui appartient à ce tableau croisé dynamique spécifique.  
2. Sélectionnez un champ par sa position indexée à zéro sur un axe donné avec `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` sélectionne à la fois les étiquettes et les données du champ.
   - `PivotTableSelectionType.LABEL_ONLY` sélectionne uniquement les étiquettes du champ.
   - `PivotTableSelectionType.DATA_ONLY` sélectionne uniquement les cellules de données du champ.  
3. Sélectionnez un champ par son nom avec `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. Lorsqu'un champ de ligne est sélectionné par son nom, la région se résout en les cellules de valeurs générées par les éléments de ce champ.  
4. Créez un `Style` avec `Workbook.create_style()`, configurez sa police, sa couleur de premier plan et son motif de fond plein, puis transmettez le style à `PivotTable.format(area, style)`.  
5. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.pivot_formats`.  
6. Les formats ancrés au champ sont appliqués lorsque les données du tableau croisé dynamique sont calculées. Par conséquent, appelez `PivotTable.calculate_data()` après avoir appliqué les formats afin que les styles deviennent visibles.  
L'exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux étiquettes de ligne `Fruit` avec `PivotArea.select` et `PivotTableSelectionType.LABEL_ONLY`, applique un style aux cellules de valeur produites par ce même champ de ligne avec `PivotArea.select_field`, puis recalcule le tableau croisé dynamique afin que les deux styles soient appliqués.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **Formater une zone de cellules du tableau croisé dynamique**
Utilisez `PivotTable.format(CellArea, Style)` lorsque la région d'intérêt est un simple rectangle de feuille de calcul plutôt qu'une région pivot sémantique.  
Un `CellArea` est décrit par les propriétés `start_row`, `start_column`, `end_row` et `end_column`. Les valeurs sont des coordonnées de feuille de calcul indexées à zéro, et les coordonnées de fin identifient la dernière ligne et la dernière colonne incluses dans le rectangle, de sorte que la zone couvre les cellules de la position de départ jusqu'à la position de fin, inclusivement.  
Contrairement à un format ancré à un champ, un format `CellArea` est appliqué aux cellules immédiatement. Un autre appel à `calculate_data()` n'est pas nécessaire pour que le style apparaisse.  
Un rectangle `CellArea` peut contenir à la fois des cellules d'étiquettes et des cellules de valeurs. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.  
L'exemple suivant met en forme le rectangle `E4:F5` du tableau croisé dynamique avec un style italique bleu clair et enregistre le classeur sans autre recalcul.

```python
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
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **Correspondance entre les zones Pivot et les zones CellArea**
Excel stocke la mise en forme des tableaux croisés dynamiques sous forme d'enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule de feuille de calcul ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu'une demande de mise en forme est traduite en zones pivot lorsqu'elle est enregistrée.  
La relation entre le `CellArea` fourni par l'utilisateur et les zones pivot stockées en interne est de type plusieurs-à-plusieurs dans les deux sens.  
- Un `CellArea` peut produire plusieurs zones pivot. Si le rectangle englobe à la fois des cellules d'étiquettes et des cellules de valeurs, il est décomposé en règles distinctes d'étiquettes et de données, car le modèle pivot traite indépendamment la mise en forme des étiquettes et des données.  
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu'une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C'est pourquoi `PivotArea.get_cell_areas()` renvoie une collection plutôt qu'un seul rectangle.  
Chaque opération de mise en forme effectuée via `PivotTable.format` est enregistrée dans `PivotTable.pivot_formats`. Chaque entrée `PivotTableFormat` expose le `PivotArea` associé et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu'un `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.  
Pour distinguer les régions stockées, chaque `PivotArea` expose les indicateurs `only_label` et `only_data`. L'exemple ci‑dessous formate un rectangle unique couvrant à la fois les étiquettes et les valeurs, inspecte `PivotTable.pivot_formats` et affiche les coordonnées `CellArea` que chaque zone pivot stockée résout.

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
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
Parce que les formats sont stockés en tant que zones pivot plutôt qu'en tant que styles de cellule ordinaires, ils survivent aux recalculs et aux actualisations. Lorsque le tableau croisé dynamique est actualisé avec `PivotTable.refresh_data`, recalculé avec `calculate_data`, ou enregistré puis rechargé, chaque zone pivot stockée se résout de nouveau à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez un `PivotArea` construit avec `select` ou `select_field` lorsqu'une mise en évidence doit rester attachée à un champ ou à une région sémantique au travers des actualisations, et utilisez un `CellArea` lorsque le formatage d'un rectangle fixe dans la disposition actuelle du tableau croisé dynamique suffit. La surcharge `format(int row, int column, Style)` cible une cellule individuelle. Utilisez `format_all`, présenté sur la page parente, lorsque l'ensemble du tableau croisé dynamique doit être restylé en une seule fois.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Ajouter des champs de ligne et de colonne au tableau croisé dynamique](/cells/fr/python-net/pivot-table-add-row-and-column-fields/)
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/python-net/manage-value-fields/)
- [Actualiser le tableau croisé dynamique](/cells/fr/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}