---
title: Teil einer Pivot-Tabelle formatieren
linktitle: Teil einer Pivot-Tabelle formatieren
description: Formatieren Sie einen Teil einer Pivot-Tabelle in Aspose.Cells for Python via .NET, indem Sie Stile auf semantische PivotArea‑Regionen oder CellArea‑Rechtecke über PivotTable.format anwenden; die Formate werden in PivotTable.pivot_formats gespeichert und bleiben erhalten, wenn die Pivot‑Tabelle aktualisiert wird.
keywords: Aspose.Cells for Python via .NET, Pivot-Tabelle, Format, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /de/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
`PivotTable.format_all` wendet einen einzelnen Stil auf die gesamte Pivot-Tabelle an und wird auf der übergeordneten Seite behandelt. Es unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.
In der Praxis muss in der Regel nur ein Teil einer Pivot-Tabelle hervorgehoben werden. Häufige Zielbereiche umfassen die Beschriftungen eines Zeilenfeldes, die von einem Feld erzeugten Wertezellen, die Gesamtsummenzeile oder ein beliebiges Rechteck, etwa die ersten beiden Elementzeilen.
Das direkte Anwenden eines Stils auf die Arbeitsblattzellen einer Pivot-Tabelle ist nicht äquivalent. Excel speichert die Pivot-Tabellenformatierung als semantische `PivotArea`‑Regionen und nicht als gewöhnliche Zellstil‑Einträge. Ein Pivot‑Area‑Format bleibt an einer Region wie den Beschriftungen eines Feldes oder den Datenwerten befestigt und wird neu zugeordnet, wenn die Pivot‑Tabelle neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebener Stil gehört hingegen zu dieser Zellposition und wird vom Pivot‑Modell nicht nachverfolgt.
Aspose.Cells stellt die komplette Überladungsfamilie von `PivotTable.format` bereit, sodass beide Arten der Formatierung verfügbar sind:
- `format(PivotArea, Style)` verankert einen Stil in einer semantischen Region, die mit `PivotArea.select` oder `PivotArea.select_field` erstellt wird.
- `format(CellArea, Style)` verankert einen Stil in einem Arbeitsblatt‑Rechteck innerhalb der Pivot‑Tabelle.
- `format(int row, int column, Style)` zielt auf eine einzelne Zelle ab.
- `format_all(Style)` formatiert die gesamte Pivot‑Tabelle.

## **Eine Pivot‑Area formatieren**
1. Erstellen Sie ein `PivotArea` mit `PivotArea(pivot_table)`. Das Objekt beschreibt eine semantische Region, die zu dieser bestimmten Pivot‑Tabelle gehört.
2. Wählen Sie ein Feld über seine nullbasierte Position auf einer gegebenen Achse mit `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.
   - `PivotTableSelectionType.LABEL_ONLY` wählt nur die Beschriftungen des Feldes aus.
   - `PivotTableSelectionType.DATA_ONLY` wählt nur die Datenzellen des Feldes aus.
3. Wählen Sie ein Feld nach Namen mit `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. Wird ein Zeilenfeld nach Namen ausgewählt, wird die Region zu den Wertezellen aufgelöst, die durch die Elemente dieses Feldes erzeugt werden.
4. Erstellen Sie ein `Style` mit `Workbook.create_style()`, konfigurieren Sie dessen Schriftart, Vordergrundfarbe und ein einfarbiges Hintergrundmuster und übergeben Sie den Stil an `PivotTable.format(area, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.pivot_formats` hinzu.
6. Feldgebundene Formate werden angewendet, wenn die Pivot‑Daten berechnet werden. Rufen Sie daher nach dem Anwenden der Formate `PivotTable.calculate_data()` auf, damit die Stile sichtbar werden.
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für Obstverkäufe, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.select` und `PivotTableSelectionType.LABEL_ONLY`, formatiert die durch dasselbe Zeilenfeld erzeugten Wertezellen mit `PivotArea.select_field` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

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

## **Cell‑Area der Pivot‑Tabelle formatieren**
Verwenden Sie `PivotTable.format(CellArea, Style)`, wenn der interessierende Bereich ein einfaches Arbeitsblatt‑Rechteck und keine semantische Pivot‑Region ist.
Ein `CellArea` wird durch die Eigenschaften `start_row`, `start_column`, `end_row` und `end_column` beschrieben. Die Werte sind nullbasierte Arbeitsblattkoordinaten, und die Endkoordinaten geben die letzte Zeile und Spalte an, die im Rechteck enthalten sind, sodass die Fläche die Zellen von der Startposition bis zur Endposition (einschließlich) abdeckt.
Im Gegensatz zu einem feldgebundenen Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `calculate_data()` ist nicht erforderlich, damit der Stil sichtbar wird.
Ein `CellArea`‑Rechteck kann sowohl Beschriftungszellen als auch Wertezellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.
Das folgende Beispiel formatiert das Rechteck `E4:F5` der Pivot‑Tabelle mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe ohne weitere Neuberechnung.

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

## **Wie Pivot‑Areas und Cell‑Areas zugeordnet werden**
Excel speichert die Pivot‑Tabellenformatierung als `pivotArea`‑Datensätze und nicht als gewöhnliche Arbeitsblatt‑Zellstil‑Datensätze. Das gleiche Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanfrage beim Speichern in Pivot‑Areas übersetzt wird.
Die Beziehung zwischen dem vom Benutzer bereitgestellten `CellArea` und den intern gespeicherten Pivot‑Areas ist in beiden Richtungen viele‑zu‑viele.
- Ein `CellArea` kann mehrere Pivot‑Areas erzeugen. Wenn das Rechteck sowohl Beschriftungs‑ als auch Werte‑zellen umfasst, wird es in separate Beschriftungs‑ und Daten‑Regeln zerlegt, da das Pivot‑Modell Beschriftungs‑ und Datenformatierung unabhängig behandelt.
- Eine Pivot‑Area kann zu mehreren disjunkten `CellArea`‑Instanzen aufgelöst werden. Eine semantische Region wie eine Gesamtsummenzeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Deshalb gibt `PivotArea.get_cell_areas()` eine Sammlung zurück statt eines einzelnen Rechtecks.
Jeder über `PivotTable.format` ausgeführte Formatierungsvorgang wird in `PivotTable.pivot_formats` gespeichert. Jeder `PivotTableFormat`‑Eintrag enthält die zugehörige `PivotArea` und den darauf angewendeten `Style`. Die `PivotArea`‑Überladung fügt pro Aufruf genau einen Eintrag hinzu, während ein `CellArea`, das verschiedene semantische Regionen enthält, mehrere Einträge hinzufügen kann.
Um die gespeicherten Regionen zu unterscheiden, stellt jede `PivotArea` die Flags `only_label` und `only_data` bereit. Das nachstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, untersucht `PivotTable.pivot_formats` und gibt die `CellArea`‑Koordinaten aus, zu denen jede gespeicherte Pivot‑Area aufgelöst wird.

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
Da die Formate als Pivot‑Areas und nicht als gewöhnliche Zellstile gespeichert werden, überstehen sie eine Neuberechnung und Aktualisierung. Wenn die Pivot‑Tabelle mit `PivotTable.refresh_data` aktualisiert, mit `calculate_data` neu berechnet oder gespeichert und erneut geladen wird, löst jede gespeicherte Pivot‑Area ihre aktuelle Position erneut auf und ihr Stil wird wieder angewendet.
{{% /alert %}}

Verwenden Sie ein `PivotArea`, das mit `select` oder `select_field` erstellt wurde, wenn eine Hervorhebung über Aktualisierungen hinweg an ein Feld oder eine semantische Region gebunden bleiben muss, und verwenden Sie ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Pivot‑Tabellen‑Layout ausreichend ist. Die Einzel‑Zell‑Überladung `format(int row, int column, Style)` richtet sich an eine einzelne Zelle. Nutzen Sie `format_all`, das auf der übergeordneten Seite beschrieben wird, wenn die gesamte Pivot‑Tabelle auf einmal neu formatiert werden soll.

## **Verwandte Artikel**
- [Stil auf Pivot-Tabelle anwenden](/cells/de/python-net/apply-style-to-pivot-table/)
- [Pivot-Tabellenzeilen- und -spaltenfelder hinzufügen](/cells/de/python-net/pivot-table-add-row-and-column-fields/)
- [Wertefelder in Pivot-Tabelle verwalten](/cells/de/python-net/manage-value-fields/)
- [Pivot-Tabelle aktualisieren](/cells/de/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}