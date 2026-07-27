---
title: Filterfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
linktitle: Filterfelder hinzufügen
description: Erfahren Sie, wie Sie Filterfelder in PivotTables mit Aspose.Cells for Python via Java hinzufügen und konfigurieren, einschließlich Hinzufügen von Filterfeldern, Einzel-Auswahl-Filterung und Mehrfach-Auswahl-Filterung.
keywords: Aspose.Cells, Python, Java, PivotTable, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in PivotTables. Sie können ein Filterfeld über eine komfortable High-Level-API oder über die Low-Level-Sammlung `page_fields` hinzufügen, und Sie können den Filter im Einzel-Auswahl-Modus steuern, ihn zurücksetzen, um alle Seitenelemente anzuzeigen, oder das Feld auf Mehrfach-Auswahl umschalten, sodass Benutzer über die Kontrollkästchen-Benutzeroberfläche in Excel mehrere Seitenelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**

Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Bereich anzeigt. Endbenutzer sehen es als Dropdown am oberen Rand einer gerenderten Pivot-Tabelle in Excel, und die Auswahl eines der verfügbaren Seitenelemente baut den Pivot-Bereich neu auf, sodass nur die zu diesem Seitenelement gehörenden Datensätze zusammengefasst werden. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.PAGE` registriert wird, anstatt als `PivotFieldType.ROW`, `PivotFieldType.COLUMN` oder `PivotFieldType.DATA`.

Ein Filterfeld kann in zwei Verhaltensweisen arbeiten. Im Standardverhalten **Einzelauswahl** ist jeweils nur ein Seitenelement sichtbar, sodass der Pivot-Bereich genau eine Teilmenge zusammenfasst. Im Verhalten **Mehrfachauswahl** zeigt das Feld eine Kontrollkästchenliste, und der Pivot-Bereich fasst die Vereinigungsmenge aller markierten Seitenelemente zusammen. Dasselbe Quellfeld kann zwischen diesen Verhaltensweisen hin und her verschoben werden, indem eine einzelne Eigenschaft umgeschaltet wird.

Aspose.Cells for Python via Java stellt zwei gleichwertige Möglichkeiten bereit, um ein Filterfeld zu registrieren. Die High-Level-API ist `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`, die den Namen der Quellspalte übernimmt und das Feld in einem einzigen Aufruf hinzufügt. Die Low-Level-API ist `PivotTable.page_fields.add(PivotField)`, die verwendet wird, wenn Sie bereits eine `PivotField`-Referenz besitzen und dieselbe Feldinstanz dem Filterbereich hinzufügen möchten. Beide APIs füllen am Ende dieselbe `page_fields`-Sammlung, und der Rest dieses Artikels zeigt, wie Sie zwischen ihnen wählen und wie Sie jeden Filtermodus steuern.

## **Hinzufügen eines Filterfelds**

Es gibt zwei Möglichkeiten, ein Pivot-Feld im Filterbereich zu registrieren. Der High-Level-Aufruf übernimmt den Namen der Quellspalte als Zeichenkette und ist der häufigste Weg. Der Low-Level-Aufruf akzeptiert eine vorhandene `PivotField`-Instanz und ist praktisch, wenn dieselbe Feldinstanz in mehreren Pivot-Bereichen wiederverwendet werden muss. Beide Aufrufe platzieren das Feld in `PivotTable.page_fields`, woraufhin es als Dropdown für die Seite am oberen Rand der gerenderten Pivot-Tabelle erscheint.

### Hinzufügen eines Filterfelds mit add_field_to_area

Das folgende Beispiel erstellt einen kleinen Datensatz mit Frucht / Jahr / Betrag, platziert eine PivotTable an Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Erstellen einer neuen Arbeitsmappe
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Kopfzeile einrichten
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 Zeilen Beispieldaten einfügen: Frucht, Jahr, Betrag
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Pivot-Tabelle hinzufügen, verankert an Zelle E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Felder ihren Bereichen hinzufügen: Frucht als Zeile, Betrag als Daten, Jahr als Seitenfeld
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Pivot-Tabellen-Daten aktualisieren und berechnen
pivotTable.refreshData()
pivotTable.calculateData()

# Arbeitsmappe speichern
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### Hinzufügen eines Filterfelds mit page_fields.add

Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.page_fields.add` übergeben. Die PivotTable und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die endgültige Registrierung im Filterbereich wird durch den Low-Level-API-Aufruf ersetzt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
#   Szenario 1a (Obst/Jahr/Betrag-Daten, Pivot bei E3, Obst→Zeile,
#   Betrag→Daten) erstellt. Unten rufen wir das Jahr-PivotField aus der
#   BaseFields-Sammlung ab und übergeben es an PageFields.Add — die
#   Low-Level-Alternative zu AddFieldToArea. Das Ergebnis ist
#   funktional identisch mit Szenario 1a.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Kopfzeilen
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Beispieldaten (9 Zeilen)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# Pivot-Tabelle bei E3 hinzufügen, die A1:C10 abdeckt
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Obst -> Zeile, Betrag -> Daten (Jahr wird unten zur Seite hinzugefügt)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Low-Level-Ansatz: das vorhandene Jahr-PivotField aus BaseFields holen
# und im Seitenbereich über PageFields.Add(PivotField) registrieren.
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Einzel-Auswahl-Filterung (Anzeigen eines Seitenelements)**

Im Standardverhalten der Einzelauswahl wird das Filterfeld als einzelnes Dropdown dargestellt, und der ganzzahlige Wert `PivotField.current_page_item` wählt aus, welches Seitenelement den Pivot-Bereich steuert. Durch Zuweisen eines bestimmten Index wird dieses eine Element ausgewählt; durch Zuweisen des speziellen Sentinelwerts `0x7FFD` (Dezimal 32765) wird der Filter zurückgesetzt, sodass alle Seitenelemente gleichzeitig zusammengefasst werden. Die Einzelauswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente

Das Setzen von `current_page_item` auf den magischen Wert `0x7FFD` entspricht dem Zurücksetzen des Filters: Der Pivot-Bereich fasst alle Seitenelemente zusammen, als ob kein Filter angewendet wäre.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Erstellen Sie eine neue Arbeitsmappe
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Daten für Fruit/Year/Amount einfügen
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# Pivot-Tabelle bei E3 erstellen
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Pivot-Felder konfigurieren: Fruit→Zeile, Amount→Daten, Year→Seite
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.refreshData()
pivotTable.calculateData()

# Den Seitenfilter löschen, damit jeder Eintrag im Seitenfeld sichtbar ist.
# 0x7FFD (dezimal 32765) ist der spezielle Sentinel-Wert, der „alle Einträge" bedeutet —
# entspricht der Auswahl von „(Alle)" im Dropdown-Menü des Seitenfelds in Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Anzeigen eines bestimmten Elements

Das Setzen von `current_page_item` auf einen realen Index wählt genau dieses eine Seitenelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Arbeitsmappe erstellen
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Beispieldaten hinzufügen (Frucht/Jahr/Betrag)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# Pivot-Tabelle bei E3 hinzufügen
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Felder hinzufügen: Frucht→Zeile, Betrag→Daten, Jahr→Seite
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Seitenfeld-spezifische Operationen
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = zweites Element in sortierter Reihenfolge (z. B. "2021")

# Pivot-Tabelle aktualisieren und berechnen
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Mehrfach-Auswahl-Filterung**

Die Mehrfach-Auswahl-Filterung verwandelt das Seiten-Dropdown in eine Kontrollkästchenliste und ermöglicht es dem Endbenutzer, mehrere Seitenelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.is_multiple_item_selection_allowed` muss auf `True` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.is_hidden`, welche Elemente in der Kontrollkästchenliste erscheinen, sodass Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente in eine Whitelist aufnehmen können.

Der folgende Code aktiviert die Mehrfachauswahl für dasselbe Year-Filterfeld, das in Szenario 1a erstellt wurde, und zeigt dann zwei Muster: Teil A deckt alle Seitenelemente auf, indem `is_hidden` für jeden Eintrag auf `False` belassen wird, während Teil B nur die von Ihnen gewählten Quellwerte in eine Whitelist aufnimmt und alles andere durch einen `switch (pivot_items[i].get_string_value())`-Block ausblendet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
#   Szenario 1a (Frucht/Jahr/Betrag-Daten, Pivot bei E3, Frucht→Zeile,
#   Betrag→Daten, Jahr→Seite über AddFieldToArea) erstellt.
#   Unten wenden wir die Mehrfachauswahl-Filterung auf das Seitenfeld an.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Beispieldaten: Frucht | Jahr | Betrag
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Mehrfachauswahl auf dem Seitenfeld aktivieren
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Teil A — ALLE Elemente auswählen (jedes Element sichtbar machen)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Teil B — nur bestimmte Elemente nach Quellwert auswählen
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Hinweis:** Bei Verwendung der Mehrfach-Auswahl-Filterung über `PivotItem.is_hidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`is_hidden == False`). Wenn jedes Element ausgeblendet ist, stürzt Excel beim Öffnen der Datei entweder ab oder rendert eine leere PivotTable. Überprüfen Sie immer, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollten verwendet werden?**

Die folgende Tabelle fasst zusammen, wann jede API und jeder Modus verwendet werden sollte, damit Sie die richtige Kombination wählen können, ohne jedes Szenario im Detail lesen zu müssen.

| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Hinzufügen eines Filterfelds über den Namen der Quellspalte (am häufigsten) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | High-Level, einzeilig. Verwenden Sie dies, es sei denn, Sie benötigen eine `PivotField`-Referenz. |
| Hinzufügen eines Filterfelds, wenn Sie bereits ein `PivotField`-Objekt besitzen | `PivotTable.page_fields.add(PivotField)` | n/a | Verwenden Sie dies, wenn das Feldobjekt anderswo bezogen wurde oder wiederverwendet werden muss. |
| Filtern auf ein einzelnes Seitenelement (Standardmodus) | `PivotField.current_page_item` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Filter zurücksetzen | `PivotField.current_page_item` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (Dezimal 32765) ist der Sentinelwert für „alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.is_multiple_item_selection_allowed` | auf `True` setzen | Erforderlich, bevor `is_hidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste ein-/ausblenden | `PivotItem.is_hidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`is_hidden == False`). |

{{% alert color="primary" %}}
Denken Sie immer an die Sichtbarkeitseinschränkung, wenn Sie die Mehrfach-Auswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere PivotTable. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Rechner zuverlässig geöffnet.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}