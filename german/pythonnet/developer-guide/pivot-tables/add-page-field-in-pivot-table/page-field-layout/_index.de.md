---
title: Seitenfeldlayout in Pivot-Tabelle ändern
linktitle: Seitenfeldlayout in Pivot-Tabelle ändern
description: Erfahren Sie, wie Sie das Layout des Seitenfeldbereichs in einer Pivot-Tabelle mit Aspose.Cells for Python via .NET steuern, einschließlich der Anzeigereihenfolge, der Umbruchanzahl und der Feldreihenfolge der Seitenfelder am oberen Rand der Pivot-Tabelle.
keywords: Aspose.Cells, Python via .NET-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Seitenfeld, Seitenfeldreihenfolge, Seitenfeldumbruchanzahl, Seitenfeld verschieben
type: docs
weight: 191
url: /de/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Dieser Artikel ist eine Fortsetzung des Themas **Seitenfeld in Pivot-Tabelle hinzufügen**. Er zeigt, wie Sie das Layout des Seitenfeldbereichs steuern — die Leiste mit Filtersteuerelementen am oberen Rand einer Pivot-Tabelle — einschließlich Anzeigereihenfolge, Umbruchanzahl und Neuanordnung der Felder.
{{% /alert %}}
## **Einführung**
Eine Pivot-Tabelle in Microsoft Excel stellt einen dedizierten **Seitenfeldbereich** bereit, der oberhalb des Zeilen-/Spalten-/Datenkörpers der Tabelle liegt. Dieser Bereich wird als Leiste mit Dropdown-Filtersteuerelementen dargestellt (eines pro Seitenfeld) und ist das Element, auf das Endbenutzer klicken, um die Pivot-Tabelle nach Kriterien wie Jahr oder Region aufzuteilen. Aspose.Cells for Python via .NET modelliert diesen Bereich über die Sammlung `pivot_table.page_fields` und stellt drei Eigenschaften bereit, die steuern, wie die Leiste visuell angeordnet wird:
- `pivot_table.page_field_order` (ein `PrintOrderType`-Wert) entscheidet, ob zusätzliche Seitenfelder *neben* den vorhandenen oder *unterhalb* von ihnen platziert werden.
- `pivot_table.page_field_wrap_count` legt fest, wie viele Seitenfelder pro Zeile oder Spalte vor einem Umbruch platziert werden.
- `pivot_table.page_fields.move(curr_index, dest_index)` ordnet die Seitenfelder neu an, ohne den Reihenfolgemodus zu ändern.
Dieser Artikel führt durch drei Codebeispiele, die jede dieser Operationen an einem gemeinsamen Datensatz demonstrieren, damit Sie die resultierenden Layouts direkt nebeneinander vergleichen können.
## **Quelldaten**
Alle drei folgenden Beispiele laden diese acht Zeilen mit Verkaufsdaten in ein Arbeitsblatt namens `PivotData`. Die Daten enthalten zwei Seitenfeldkandidaten (`Year`, `Region`), einen Zeilenfeldkandidaten (`Fruit`) und eine Kennzahl (`Amount`), wodurch die Seitenfeldleiste sinnvoll zu prüfen ist.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alle acht Zeilen werden in jedem Codebeispiel in identischer Reihenfolge befüllt, sodass sich die Quelldaten zwischen den Szenarien niemals unterscheiden — nur die Layout-Eigenschaften des Seitenfelds variieren.
## **Beispiel 1: Über, dann nach unten**
Im ersten Szenario konfigurieren wir die beiden Seitenfelder (`Year`, `Region`) so, dass sie **nebeneinander in einer einzelnen Zeile** am oberen Rand der Pivot-Tabelle erscheinen. Wir weisen `Fruit` der Zeilenachse zu, platzieren `Year` zuerst und `Region` an zweiter Stelle auf der Seitenachse (die Reihenfolge der `add_field_to_area`-Aufrufe bestimmt den Startindex), fügen `Amount` (Summe) als Datenfeld hinzu und setzen dann `page_field_order` auf `PrintOrderType.OverThenDown` mit `page_field_wrap_count = 2`. Mit `OverThenDown` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder horizontal nebeneinander in einer einzelnen Zeile am oberen Rand der Pivot-Tabelle angeordnet, sodass die Leiste eine Zeile mit Breite zwei einnimmt.
```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# Kopfzeilen (Zeile 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# Zeile 1: Apple, 2022, Nord, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# Zeile 2: Apple, 2023, Nord, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# Zeile 3: Banane, 2022, Süd, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# Zeile 4: Banane, 2023, Süd, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# Zeile 5: Kirsche, 2022, Ost, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# Zeile 6: Kirsche, 2023, Ost, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# Zeile 7: Traube, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# Zeile 8: Traube, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# Arbeitsblatt "PivotTableReport" hinzufügen
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# Pivot-Tabelle erstellen mit Quelle PivotData!A1:D9, platziert bei A1 in PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Felder hinzufügen
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Frucht
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Jahr
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Betrag
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# Layout des Seitenfeldbereichs konfigurieren: Seitenfelder zuerst horizontal anordnen, nach jeweils 2 umbrechen
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# Aktualisieren und berechnen
pivot_table.calculate_data()

# Speichern
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```
## **Beispiel 2: Nach unten, dann über**
In diesem Beispiel platzieren wir `Fruit` auf der Zeilenachse, `Year` und `Region` auf der Seitenachse (wobei `Year` zuerst kommt) und `Amount` (Summe) als Datenfeld — genau wie in Beispiel 1. Anschließend setzen wir `page_field_order` auf `PrintOrderType.DownThenOver` und `page_field_wrap_count` auf `2`. Mit `DownThenOver` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder vertikal gestapelt — `Year` oben, `Region` direkt darunter — und bilden eine einzelne Spalte am oberen Rand der Pivot-Tabelle. Die Leiste nimmt daher zwei Zeilen mit Breite eins ein, im Gegensatz zu Beispiel 1.
```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```
## **Beispiel 3: Ein Seitenfeld verschieben**
Im dritten Szenario behalten wir diesen Datensatz und die Feldzuordnung bei, legen ein neutrales Layout fest (`OverThenDown` mit Umbruchanzahl `2`) und demonstrieren dann die Operation `page_fields.move`. Der Aufruf `move(0, 1)` verschiebt das Seitenfeld an Index 0 (`Year`) an Position 1, und das Seitenfeld, das sich an Position 1 befand (`Region`), rückt auf Position 0. Nach diesem Aufruf ist `Region` das erste Seitenfeld und `Year` das zweite. Der Umbruch- und Reihenfolgemodus bleiben unverändert, sodass die Leiste weiterhin horizontal nebeneinander dargestellt wird — nur die Reihenfolge der beiden Dropdowns wurde vertauscht.
```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```
## **Verwandte Artikel**
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/python-net/add-page-field-in-pivot-table/) — die übergeordnete Seite, die einführt, wie Seitenfelder zu einer Pivot-Tabelle hinzugefügt werden.
- [Zeilen- und Spaltenfelder in Pivot-Tabelle](/cells/de/python-net/row-and-column-fields/) — behandelt die Zuweisung von Feldern zu den Zeilen- und Spaltenachsen und ergänzt die hier gezeigten Arbeiten an der Seitenachse.
- [Wertfelder in Pivot-Tabelle verwalten](/cells/de/python-net/manage-value-fields/) — beschreibt, wie der Datenbereich (Wertebereich) konfiguriert wird, einschließlich der in diesem Artikel verwendeten `Sum`-Aggregation.
- [Pivot-Tabelle aktualisieren](/cells/de/python-net/refresh-pivot-table/) — erklärt `refresh_data` und `calculate_data`, die nach dem Neuordnen der Seitenfelder erforderlich sind.
- [Stil auf Pivot-Tabelle anwenden](/cells/de/python-net/apply-style-to-pivot-table/) — zeigt, wie die gerenderte Pivot-Tabelle formatiert wird, nachdem die Seitenfeldleiste angeordnet wurde.
{{< app/cells/assistant language="python-net" >}}