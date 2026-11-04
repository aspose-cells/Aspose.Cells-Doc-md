---
title: Teil einer PivotTable formatieren
linktitle: Teil einer PivotTable formatieren
description: Formatieren Sie einen Teil einer PivotTable in Aspose.Cells for Python via Java, indem Sie Stile auf semantische PivotArea‑Bereiche oder CellArea‑Rechtecke über PivotTable.format anwenden, wobei die Formate in PivotTable.getPivotFormats() gespeichert und beim Aktualisieren der PivotTable erhalten bleiben.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, PivotTable, Format, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /de/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
`PivotTable.formatAll` wendet einen einzelnen Stil auf die gesamte Pivot‑Tabelle an und ist auf der übergeordneten Seite beschrieben. Es unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.
In der Praxis muss in der Regel nur ein Teil einer Pivot‑Tabelle hervorgehoben werden. Häufige Ziele sind die Beschriftungen, die zu einem Zeilenfeld gehören, die Wertzellen, die von einem Feld erzeugt werden, die Gesamtsummenzeile oder ein beliebiges Rechteck, wie die ersten beiden Elementzeilen.
Das direkte Anwenden eines Stils auf die Arbeitsblattzellen einer Pivot‑Tabelle ist nicht gleichwertig. Excel speichert die Formatierung von Pivot‑Tabellen als semantische `PivotArea`‑Bereiche statt als gewöhnliche Zellenstil‑Datensätze. Ein Pivot‑Area‑Format bleibt an einem Bereich wie den Beschriftungen eines Feldes oder den Datenwerten befestigt und wird neu aufgelöst, wenn die Pivot‑Tabelle neu berechnet, aktualisiert oder erweitert wird. Ein Stil, der direkt in eine Zelle geschrieben wird, gehört hingegen zu dieser Zellposition und wird vom Pivot‑Modell nicht verfolgt.
Aspose.Cells stellt die vollständige `PivotTable.format`‑Überladungsfamilie bereit, sodass beide Arten der Formatierung verfügbar sind:
- `format(PivotArea, Style)` verankert einen Stil an einem semantischen Bereich, der mit `PivotArea.select` oder `PivotArea.selectField` erstellt wird.
- `format(CellArea, Style)` verankert einen Stil an einem Arbeitsblattrechteck innerhalb der Pivot‑Tabelle.
- `format(int row, int column, Style)` richtet sich an eine einzelne Zelle.
- `formatAll(Style)` formatiert die gesamte Pivot‑Tabelle.

## **Pivot‑Area formatieren**
Der semantische Bereichs‑Workflow ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Bereich des Berichts folgen muss.
1. Erstellen Sie ein `PivotArea` mit `PivotArea(pivot_table)`. Das Objekt beschreibt einen semantischen Bereich, der zu dieser speziellen Pivot‑Tabelle gehört.
2. Wählen Sie ein Feld anhand seiner nullbasierten Position auf einer bestimmten Achse mit `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` aus.
   - `PivotTableSelectionType.DATA_AND_LABEL` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.
   - `PivotTableSelectionType.LABEL_ONLY` wählt nur die Beschriftungen des Feldes aus.
   - `PivotTableSelectionType.DATA_ONLY` wählt nur die Datenzellen des Feldes aus.
3. Wählen Sie ein Feld nach Namen mit `PivotArea.selectField(PivotFieldType axisType, String fieldName)` aus. Wenn ein Zeilenfeld nach Namen ausgewählt wird, löst sich der Bereich zu den Wertzellen, die durch die Elemente dieses Feldes erzeugt werden.
4. Erstellen Sie ein `Style` mit `workbook.createStyle()`, konfigurieren Sie dessen Schriftart, Vordergrundfarbe und ein durchgängiges Hintergrundmuster und übergeben Sie den Stil an `PivotTable.format(area, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.getPivotFormats()` hinzu.
6. Feldverankerte Formate werden gemalt, wenn die Pivot‑Daten berechnet werden. Rufen Sie daher nach dem Anwenden der Formate `PivotTable.calculateData()` auf, damit die Stile sichtbar werden.
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für den Obstverkauf, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.select` und `PivotTableSelectionType.LABEL_ONLY`, formatiert die durch dasselbe Zeilenfeld erzeugten Wertzellen mit `PivotArea.selectField` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

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

## **Ein CellArea der PivotTable formatieren**
Verwenden Sie `PivotTable.format(CellArea, Style)`, wenn der interessierende Bereich ein einfaches Arbeitsblattrechteck und kein semantischer Pivot‑Bereich ist.
`CellArea` wird durch die Eigenschaften `getStartRow()`, `getStartColumn()`, `getEndRow()` und `getEndColumn()` beschrieben. Die Werte sind nullbasierte Arbeitsblattkoordinaten, und die Endkoordinaten geben die letzte Zeile und Spalte an, die im Rechteck enthalten sind, sodass der Bereich die Zellen von der Startposition bis zur Endposition einschließt.
Im Gegensatz zu einem feldverankerten Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `PivotTable.calculateData()` ist nicht erforderlich, damit der Stil erscheint.
Ein `CellArea`‑Rechteck kann sowohl Beschriftungszellen als auch Wertzellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.
Das folgende Beispiel formatiert das Rechteck `E4:F5` der Pivot‑Tabelle mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe ohne weitere Neuberechnung.

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

## **Wie Pivot‑Bereiche und Cell‑Bereiche abgebildet werden**
Excel speichert die Formatierung von Pivot‑Tabellen als `pivotArea`‑Datensätze und nicht als gewöhnliche Arbeitsblatt‑Zellenstil‑Datensätze. Das gleiche Modell wird von Aspose.Cells verwendet, sodass ein Formatierungsantrag bei der Aufzeichnung in Pivot‑Bereiche übersetzt wird.
Die Beziehung zwischen dem vom Benutzer bereitgestellten `CellArea` und den intern gespeicherten Pivot‑Bereichen ist in beiden Richtungen viele‑zu‑viele.
- Ein `CellArea` kann mehrere Pivot‑Bereiche erzeugen. Wenn das Rechteck sowohl Beschriftungszellen als auch Wertzellen umfasst, wird es in separate Beschriftungs‑ und Datenregeln aufgeteilt, weil das Pivot‑Modell Beschriftungsformatierung und Datenformatierung unabhängig behandelt.
- Ein Pivot‑Bereich kann sich in mehrere separate `CellArea`‑Instanzen auflösen. Ein semantischer Bereich wie eine Gesamtsummenzeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Deshalb gibt `PivotArea.getCellAreas()` eine Sammlung zurück und nicht ein einzelnes Rechteck.
Jeder über `PivotTable.format` durchgeführte Formatierungsvorgang wird in `PivotTable.getPivotFormats()` aufgezeichnet. Jeder `PivotTableFormat`‑Eintrag stellt das zugehörige `PivotArea` und den darauf angewendeten `Style` dar. Die `PivotArea`‑Überladung fügt pro Aufruf genau einen Eintrag hinzu, während ein `CellArea`, das unterschiedliche semantische Regionen enthält, mehrere Einträge hinzufügen kann.
Um die gespeicherten Regionen zu unterscheiden, stellt jedes `PivotArea` die Flags `getOnlyLabel()` und `getOnlyData()` bereit. Das nachstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, untersucht `PivotTable.getPivotFormats()` und gibt die `CellArea`‑Koordinaten aus, zu denen jeder gespeicherte Pivot‑Bereich aufgelöst wird.

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
Da die Formate als Pivot‑Bereiche und nicht als gewöhnliche Zellenstile gespeichert werden, überstehen sie Neuberechnungen und Aktualisierungen. Wenn die Pivot‑Tabelle mit `PivotTable.refreshData()` aktualisiert, mit `PivotTable.calculateData()` neu berechnet oder gespeichert und wieder geladen wird, löst sich jeder gespeicherte Pivot‑Bereich erneut zur aktuellen Position seines Bereichs auf und sein Stil wird erneut angewendet.
{{% /alert %}}

Verwenden Sie ein mit `select` oder `selectField` aufgebautes `PivotArea`, wenn eine Hervorhebung über Aktualisierungen hinweg an ein Feld oder einen semantischen Bereich angehängt bleiben muss, und verwenden Sie ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Pivot‑Tabellen‑Layout ausreichend ist. Die Einzelzellen‑`format(int row, int column, Style)`‑Überladung richtet sich an eine einzelne Zelle. Verwenden Sie `formatAll`, das auf der übergeordneten Seite beschrieben wird, wenn die gesamte Pivot‑Tabelle auf einmal neu formatiert werden soll.

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/python-java/apply-style-to-pivot-table/)
- [Pivot‑Tabellen‑Zeilen- und Spaltenfelder hinzufügen](/cells/de/python-java/pivot-table-add-row-and-column-fields/)
- [Wertefelder in Pivot‑Tabelle verwalten](/cells/de/python-java/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}