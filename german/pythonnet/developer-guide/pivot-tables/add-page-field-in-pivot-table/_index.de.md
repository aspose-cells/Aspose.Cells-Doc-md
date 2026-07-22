---
title: Seitenfelder in Pivot-Tabellen
linktitle: Seitenfelder in Pivot-Tabellen
description: Erfahren Sie, wie Sie mit Aspose.Cells for Python via .NET Seitenfelder in Pivot-Tabellen hinzufügen und konfigurieren, einschließlich des Hinzufügens von Seitenfeldern, Einzelauswahl-Filterung und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, Python via .NET, Pivot-Tabelle, Seitenfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/python-net/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Seitenfeldern in Pivot-Tabellen. Sie können ein Seitenfeld über eine komfortable High-Level-API oder über die Low-Level-Sammlung `page_fields` hinzufügen, und Sie können den Seitenfilter im Einzelauswahl-Modus steuern, ihn löschen, um alle Seitenelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, sodass Benutzer mehrere Seitenelemente gleichzeitig über die Checkbox-Benutzeroberfläche in Excel auswählen können.
{{% /alert %}}

## **Einführung**

Ein Seitenfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Bereich anzeigt. Endbenutzer sehen es als Dropdown-Liste am oberen Rand einer gerenderten Pivot-Tabelle in Excel. Die Auswahl eines der verfügbaren Seitenelemente baut den Pivot-Bereich neu auf, sodass nur die Datensätze zusammengefasst werden, die zu diesem Seitenelement gehören. Ein Pivot-Feld wird zu einem Seitenfeld, wenn es als `PivotFieldType.PAGE` registriert wird, anstatt als `PivotFieldType.ROW`, `PivotFieldType.COLUMN` oder `PivotFieldType.DATA`.

Ein Seitenfeld kann in zwei Verhaltensweisen arbeiten. Im Standardverhalten **Einzelauswahl** ist jeweils nur ein Seitenelement sichtbar, sodass der Pivot-Bereich genau eine Teilmenge zusammenfasst. Im Verhalten **Mehrfachauswahl** zeigt das Feld eine Checkbox-Liste an, und der Pivot-Bereich fasst die Vereinigung aller markierten Seitenelemente zusammen. Dasselbe Quellfeld kann zwischen diesen Verhaltensweisen hin- und hergeschaltet werden, indem eine einzige Eigenschaft umgeschaltet wird.

Aspose.Cells for Python via .NET bietet zwei gleichwertige Möglichkeiten, ein Seitenfeld zu registrieren. Die High-Level-API ist `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")`, die den Namen der Quellspalte übernimmt und das Feld in einem einzigen Aufruf hinzufügt. Die Low-Level-API ist `PivotTable.page_fields.add(PivotField)`, die verwendet wird, wenn Sie bereits eine Referenz auf ein `PivotField` besitzen und dieselbe Feldinstanz zum Seitenbereich hinzufügen möchten. Beide APIs füllen letztlich dieselbe Sammlung `page_fields`, und der Rest dieses Artikels zeigt, wie Sie zwischen ihnen wählen und wie Sie jeden Filtermodus steuern.

## **Hinzufügen eines Seitenfelds**

Es gibt zwei Möglichkeiten, ein Pivot-Feld im Seitenbereich zu registrieren. Der High-Level-Aufruf nimmt den Namen der Quellspalte als Zeichenkette entgegen und ist der häufigste Weg. Der Low-Level-Aufruf akzeptiert eine vorhandene `PivotField`-Instanz und ist praktisch, wenn dasselbe Feldobjekt in mehreren Pivot-Bereichen wiederverwendet werden muss. Beide Aufrufe platzieren das Feld in `PivotTable.page_fields`, wonach es als Seiten-Dropdown am oberen Rand der gerenderten Pivot-Tabelle erscheint.

### Hinzufügen eines Seitenfelds mit add_field_to_area

Das folgende Beispiel erstellt einen kleinen Datensatz mit Fruit / Year / Amount, platziert eine Pivot-Tabelle in Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Seitenbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```python
import aspose.cells as ac

# Erstelle eine neue Arbeitsmappe
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Richte die Kopfzeile ein
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Befülle 9 Zeilen mit Beispieldaten: Frucht, Jahr, Betrag
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# Füge eine Pivot-Tabelle hinzu, verankert an Zelle E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Füge Felder zu ihren Bereichen hinzu: Frucht als Zeile, Betrag als Daten, Jahr als Seitenfeld
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Aktualisiere und berechne die Pivot-Tabellen-Daten
pivot_table.refresh_data()
pivot_table.calculate_data()

# Speichere die Arbeitsmappe
workbook.save("pageFieldSample.xlsx")
```

### Hinzufügen eines Seitenfelds mit page_fields.add

Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.page_fields.add` übergeben. Die Pivot-Tabelle und das Seitenfeld werden genau wie im vorherigen Szenario konstruiert; nur die abschließende Registrierung im Seitenbereich wird durch den Low-Level-API-Aufruf ersetzt.

```python
import aspose.cells as ac

# — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
#   Szenario 1a (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit→Zeile,
#   Amount→Daten) erstellt. Im Folgenden holen wir das Year-PivotField
#   aus der BaseFields-Sammlung und übergeben es an PageFields.Add —
#   die Low-Level-Alternative zu AddFieldToArea. Das Ergebnis ist
#   funktional identisch mit Szenario 1a.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Kopfzeilen
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# Beispieldaten (9 Zeilen)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# Pivot-Tabelle bei E3 hinzufügen, die A1:C10 abdeckt
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Fruit -> Zeile, Amount -> Daten (Year wird unten zur Seite hinzugefügt)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Low-Level-Ansatz: das vorhandene Year-PivotField aus BaseFields holen
# und über PageFields.Add(PivotField) im Seitenbereich registrieren.
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Einzelauswahl-Filterung (Anzeigen eines Seitenelements)**

Im Standardverhalten der Einzelauswahl wird das Seitenfeld als einfaches Dropdown dargestellt, und die Ganzzahl `PivotField.current_page_item` wählt aus, welches Seitenelement den Pivot-Bereich steuert. Das Zuweisen eines bestimmten Index wählt dieses eine Element aus; das Zuweisen des speziellen Sentinel-Werts `0x7FFD` (Dezimal 32765) löscht den Filter, sodass alle Seitenelemente gleichzeitig zusammengefasst werden. Die Einzelauswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente

Das Setzen von `current_page_item` auf den magischen Wert `0x7FFD` entspricht dem Löschen des Seitenfilters: Der Pivot-Bereich fasst alle Seitenelemente zusammen, als wäre kein Filter angewendet worden.

```python
import aspose.cells as ac

# Erstellen einer neuen Arbeitsmappe
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Befüllen der Daten Fruit/Year/Amount
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# Pivot-Tabelle an E3 erstellen
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Pivot-Felder konfigurieren: Fruit→Zeile, Amount→Daten, Year→Seite
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.refresh_data()
pivot_table.calculate_data()

# Den Seitenfilter löschen, damit jedes Element im Seitenfeld sichtbar ist.
# 0x7FFD (dezimal 32765) ist der spezielle Sentinel-Wert, der "alle Elemente" bedeutet —
# entspricht der Auswahl von "(Alle)" im Dropdown-Feld der Excel-Seite.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### Anzeigen eines bestimmten Elements

Das Setzen von `current_page_item` auf einen echten Index wählt nur dieses eine Seitenelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Seitenfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```python
import aspose.cells as ac

# Arbeitsmappe erstellen
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Beispieldaten hinzufügen (Frucht/Jahr/Betrag)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# Pivot-Tabelle bei E3 hinzufügen
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Felder hinzufügen: Frucht→Zeile, Betrag→Daten, Jahr→Seite
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Seitenfeld-spezifische Operationen
pivot_table.page_fields[0].current_page_item = 1  # 1 = zweites Element in sortierter Reihenfolge (z. B. "2021")

# Pivot-Tabelle aktualisieren und berechnen
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Mehrfachauswahl-Filterung**

Die Mehrfachauswahl-Filterung verwandelt das Seiten-Dropdown in eine Checkbox-Liste und ermöglicht es dem Endbenutzer, mehrere Seitenelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.is_multiple_item_selection_allowed` muss auf `True` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.is_hidden`, welche Elemente in der Checkbox-Liste erscheinen, sodass Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

Der folgende Code aktiviert die Mehrfachauswahl für dasselbe Year-Seitenfeld, das in Szenario 1a erstellt wurde, und zeigt dann zwei Muster: Teil A zeigt jedes Seitenelement an, indem `is_hidden` für jeden Eintrag auf `False` belassen wird, während Teil B nur die von Ihnen gewählten Quellwerte auf eine Whitelist setzt und alles andere durch einen `if` / `elif`-Block ausblendet, der `pivot_items[i].get_string_value()` prüft.

```python
import aspose.cells as ac

# — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
#   Szenario 1a (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit→Row,
#   Amount→Data, Year→Page über AddFieldToArea) erstellt.
#   Unten wenden wir die Mehrfachauswahl-Filterung auf das Seitenfeld an.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Beispieldaten: Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — Mehrfachauswahl auf dem Seitenfeld aktivieren
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Teil A — ALLE Elemente auswählen (jedes Element sichtbar machen)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Teil B — nur bestimmte Elemente nach Quellwert auswählen
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.is_hidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`is_hidden == False`). Wenn jedes Element ausgeblendet ist, stürzt Excel beim Öffnen der Datei entweder ab oder rendert eine leere Pivot-Tabelle. Stellen Sie immer sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollten verwendet werden?**

Die folgende Tabelle fasst zusammen, wann welche API und welcher Modus verwendet werden sollte, damit Sie die richtige Kombination wählen können, ohne jedes Szenario im Detail lesen zu müssen.

| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Seitenfeld nach Quellspaltennamen hinzufügen (häufigster Fall) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | High-Level, einzeilig. Verwenden Sie dies, es sei denn, Sie benötigen eine `PivotField`-Referenz. |
| Seitenfeld hinzufügen, wenn Sie bereits ein `PivotField`-Objekt haben | `PivotTable.page_fields.add(PivotField)` | n/a | Verwenden Sie dies, wenn das Feldobjekt woanders erhalten wurde oder wiederverwendet werden muss. |
| Nach einem einzelnen Seitenelement filtern (Standardmodus) | `PivotField.current_page_item` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Seitenfilter löschen | `PivotField.current_page_item` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (Dezimal 32765) ist der Sentinel für "alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.is_multiple_item_selection_allowed` | auf `True` setzen | Erforderlich, bevor `is_hidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahl-Liste ausblenden / anzeigen | `PivotItem.is_hidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`is_hidden == False`). |

{{% alert color="primary" %}}
Denken Sie immer an die Sichtbarkeitsbedingung, wenn Sie die Mehrfachauswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Seitenfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere Pivot-Tabelle. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Rechner zuverlässig geöffnet.
{{% /alert %}}


{{< app/cells/assistant language="python" >}}