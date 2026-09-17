---
title: Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for Python via .NET hinzufügen
linktitle: Filterfelder zu einer Pivot-Tabelle
description: Lernen Sie, wie Sie mit Aspose.Cells for Python via .NET Filterfelder in Pivot-Tabellen hinzufügen und konfigurieren, einschließlich des Hinzufügens von Filterfeldern, Einzelauswahl-Filterung und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, Python via .NET, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/python-net/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine übergeordnete Komfort-API oder über die untergeordnete `page_fields`-Sammlung hinzufügen. Sie können den Filter im Einzelnauswahlmodus betreiben, ihn löschen, um alle Filterelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, damit Benutzer über die Kontrollkästchen-Benutzeroberfläche in Excel mehrere Filterelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**
Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Body anzeigt. Endbenutzer sehen es als Dropdown-Liste am oberen Rand einer gerenderten Pivot-Tabelle in Excel. Durch die Auswahl eines der verfügbaren Filterelemente wird der Pivot-Body neu aufgebaut, sodass nur die Datensätze zusammengefasst werden, die zu diesem Filterelement gehören. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.PAGE` statt als `PivotFieldType.ROW`, `PivotFieldType.COLUMN` oder `PivotFieldType.DATA` registriert wird.

## **Hinzufügen eines Filterfelds**

### Hinzufügen eines Filterfelds mit add_field_to_area
Das folgende Beispiel erstellt einen kleinen Fruit/Jahr/Betrag-Datensatz, platziert eine Pivot-Tabelle an Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```python
import aspose.cells as ac
# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
# Set up the header row
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Populate 9 rows of sample data: Fruit, Year, Amount
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
# Add a pivot table anchored at cell E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")
# Refresh and calculate the pivot table data
pivot_table.calculate_data()
# Save the workbook
workbook.save("pageFieldSample.xlsx")
```

### Hinzufügen eines Filterfelds mit page_fields.add
Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.page_fields.add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die endgültige Registrierung im Filterbereich wird durch den Aufruf der untergeordneten API ersetzt.

```python
import aspose.cells as ac
# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data). Below we obtain the Year PivotField from the
#   BaseFields collection and pass it to PageFields.Add — the
#   low-level alternative to AddFieldToArea. The result is
#   functionally identical to Scenario 1a.
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
# Headers
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")
# Sample data (9 rows)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)
# Add pivot table at E3 covering A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]
# Fruit -> Row, Amount -> Data (Year will go to Page below)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Low-level approach: grab the existing Year PivotField from BaseFields
# and register it in the Page area via PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)
# Refresh so the new page field is reflected in the saved workbook
pivot_table.calculate_data()
workbook.save("output.xlsx")
```

## **Einzelnauswahl-Filterung (Ein Filterelement anzeigen)**
Beim standardmäßigen Einzelnauswahlverhalten wird das Filterfeld als einfache Dropdown-Liste dargestellt, und die `PivotField.current_page_item`-Ganzzahl wählt aus, welches Filterelement den Pivot-Body steuert. Durch Zuweisen eines bestimmten Index wird genau dieses eine Element ausgewählt; durch Zuweisen des speziellen Sentinel-Werts `0x7FFD` (Dezimal 32765) wird der Filter gelöscht, sodass alle Filterelemente auf einmal zusammengefasst werden. Die Einzelnauswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Alle Elemente anzeigen
Das Setzen von `current_page_item` auf den magischen Wert `0x7FFD` entspricht dem Löschen des Filters: Der Pivot-Body fasst jedes Filterelement zusammen, als ob kein Filter angewendet worden wäre.

```python
import aspose.cells as ac
# Create a new workbook
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
# Populate Fruit/Year/Amount data
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
# Create pivot table at E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]
# Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")
pivot_table.calculate_data()
# Clear the page filter so every item in the page field is visible.
# 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
# equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot_table.page_fields[0].current_page_item = 0x7FFD
workbook.save("output.xlsx")
```

### Ein bestimmtes Element anzeigen
Das Setzen von `current_page_item` auf einen realen Index wählt genau dieses eine Filterelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```python
import aspose.cells as ac
# Create workbook
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Add sample data (Fruit/Year/Amount)
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
# Add pivot table at E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
# Add fields: Fruit→Row, Amount→Data, Year→Page
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")
# Page-field-specific operations
pivot_table.page_fields[0].current_page_item = 1  # 1 = second item in sorted order (e.g. "2021")
# Refresh and calculate pivot table
pivot_table.calculate_data()
workbook.save("output.xlsx")
```

## **Mehrfachauswahl-Filterung**
Die Mehrfachauswahl-Filterung verwandelt das Filter-Dropdown in eine Kontrollkästchenliste und ermöglicht es dem Endbenutzer, mehrere Filterelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.is_multiple_item_selection_allowed` muss auf `True` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.is_hidden`, welche Elemente in der Kontrollkästchenliste angezeigt werden, sodass Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

```python
import aspose.cells as ac
# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data, Year→Page via AddFieldToArea).
#   Below we apply multi-select filtering on the page field.
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Sample data: Fruit | Year | Amount
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
# — Enable multi-select on the page field
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True
# Part A — select ALL items (make every item visible)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False
# Part B — select only specific items by source value
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True
pivot_table.calculate_data()
workbook.save("output.xlsx")
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.is_hidden` **muss mindestens ein `PivotItem` sichtbar bleiben** (`is_hidden == False`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder rendert eine leere Pivot-Tabelle. Überprüfen Sie immer, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollte ich verwenden?**
Die folgende Tabelle fasst zusammen, wann Sie welche API und welchen Modus verwenden sollten, damit Sie die richtige Kombination auswählen können, ohne jedes Szenario im Detail lesen zu müssen.
| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Filterfeld nach Quellspaltennamen hinzufügen (am häufigsten) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | High-Level, einzeilig. Verwenden Sie dies, es sei denn, Sie benötigen eine `PivotField`-Referenz. |
| Filterfeld hinzufügen, wenn Sie bereits ein `PivotField`-Objekt haben | `PivotTable.page_fields.add(PivotField)` | n/a | Verwenden Sie dies, wenn das Feldobjekt woanders erhalten wurde oder wiederverwendet werden muss. |
| Auf ein einzelnes Filterelement filtern (Standardmodus) | `PivotField.current_page_item` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste. |
| Alle Elemente anzeigen / Filter löschen | `PivotField.current_page_item` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (Dezimal 32765) ist der Sentinel-Wert für „alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.is_multiple_item_selection_allowed` | auf `True` setzen | Erforderlich, bevor `is_hidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste ausblenden / anzeigen | `PivotItem.is_hidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`is_hidden == False`). |

{{% alert color="primary" %}}
Denken Sie immer an die Sichtbarkeitseinschränkung, wenn Sie die Mehrfachauswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere Pivot-Tabelle. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Computer zuverlässig geöffnet.
{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}