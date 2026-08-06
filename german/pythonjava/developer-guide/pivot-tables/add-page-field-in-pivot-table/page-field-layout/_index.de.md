---
title: Layout des Seitenfelds in der Pivot-Tabelle ändern
linktitle: Layout des Seitenfelds in der Pivot-Tabelle ändern
description: Erfahren Sie, wie Sie das Layout des Seitenfeldbereichs in einer Pivot-Tabelle mit Aspose.Cells for Python via Java steuern können, einschließlich der Einstellung der Anzeigereihenfolge, der Umbruchanzahl und der Feldreihenfolge der Seitenfelder am oberen Rand der Pivot-Tabelle.
keywords: Aspose.Cells for Python via Java, Python-Java-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Seitenfeld, Reihenfolge der Seitenfelder, Umbruchanzahl der Seitenfelder, Seitenfeld verschieben
type: docs
weight: 191
url: /de/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Dieser Artikel ist eine Fortsetzung des Themas **Seitenfeld in Pivot-Tabelle hinzufügen**. Er zeigt, wie Sie das Layout des Seitenfeldbereichs — den Streifen mit Filtersteuerelementen am oberen Rand einer Pivot-Tabelle — steuern können, einschließlich Anzeigereihenfolge, Umbruchanzahl und Feldneuanordnung.
{{% /alert %}}
## **Einführung**
Eine Pivot-Tabelle in Microsoft Excel enthält einen dedizierten **Seitenfeldbereich**, der oberhalb des Zeilen-/Spalten-/Datenkörpers der Tabelle liegt. Dieser Bereich wird als Streifen mit Dropdown-Filtersteuerelementen (eines pro Seitenfeld) dargestellt und wird von Endbenutzern angeklickt, um die Pivot-Tabelle nach Kriterien wie Jahr oder Region zu filtern. Aspose.Cells for Python via Java modelliert diesen Bereich über die Sammlung `pivot_table.page_fields` und stellt drei Eigenschaften bereit, die steuern, wie der Streifen visuell angeordnet wird:
- `pivot_table.page_field_order` (ein `Aspose.Cells.PrintOrderType`-Wert) legt fest, ob zusätzliche Seitenfelder *neben* den vorhandenen oder *unterhalb* davon platziert werden.
- `pivot_table.page_field_wrap_count` legt fest, wie viele Seitenfelder pro Zeile oder Spalte vor dem Umbruch platziert werden.
- `pivot_table.page_fields.move(curr_index, dest_index)` ordnet die Seitenfelder neu, ohne den Anordnungsmodus zu ändern.
Dieser Artikel führt durch drei Codebeispiele, die jede dieser Operationen an einem gemeinsamen Datensatz demonstrieren, damit Sie die resultierenden Layouts direkt vergleichen können.
## **Quelldaten**
Alle drei folgenden Beispiele laden diese acht Zeilen Verkaufsdaten in ein Arbeitsblatt namens `PivotData`. Die Daten enthalten zwei Seitenfeldkandidaten (`Year`, `Region`), einen Zeilenfeldkandidaten (`Fruit`) und ein Maß (`Amount`), wodurch der Seitenfeldstreifen sinnvoll zu prüfen ist.
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
Alle acht Zeilen werden in jedem Codebeispiel in identischer Reihenfolge gefüllt, sodass sich die Quelldaten zwischen den Szenarien nie unterscheiden — nur die Layouteigenschaften der Seitenfelder weichen ab.
## **Beispiel 1: Zuerst horizontal, dann vertikal**
Im ersten Szenario konfigurieren wir die beiden Seitenfelder (`Year`, `Region`), sodass sie **nebeneinander in einer einzelnen Zeile** am oberen Rand der Pivot-Tabelle erscheinen. Wir weisen `Fruit` der Zeilenachse zu, platzieren `Year` zuerst und `Region` an zweiter Stelle auf der Seitenachse (die Reihenfolge der `add_field_to_area`-Aufrufe bestimmt den Startindex), fügen `Amount` (Summe) als Datenfeld hinzu und setzen dann `page_field_order` auf `PrintOrderType.OVER_THEN_DOWN` mit `page_field_wrap_count = 2`. Mit `OVER_THEN_DOWN` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder horizontal nebeneinander in einer einzelnen Zeile am oberen Rand der Pivot-Tabelle angeordnet, sodass der Streifen eine Zeile mit Breite zwei einnimmt.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# Kopfzeilen (Zeile 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# Zeile 1: Apfel, 2022, Nord, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# Zeile 2: Apfel, 2023, Nord, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# Zeile 3: Banane, 2022, Süd, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# Zeile 4: Banane, 2023, Süd, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# Zeile 5: Kirsche, 2022, Ost, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# Zeile 6: Kirsche, 2023, Ost, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# Zeile 7: Traube, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# Zeile 8: Traube, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# PivotTableReport-Blatt hinzufügen
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# Pivot-Tabelle erstellen, die aus PivotData!A1:D9 stammt und bei A1 auf PivotTableReport platziert wird
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Felder hinzufügen
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Frucht
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # Jahr
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Betrag
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# Layout des Seitenfeldbereichs konfigurieren: Seitenfelder zuerst horizontal anordnen, nach jeweils 2 umbrechen
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# Aktualisieren und berechnen
pivotTable.calculateData()

# Speichern
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **Beispiel 2: Zuerst vertikal, dann horizontal**
In diesem Beispiel platzieren wir `Fruit` auf der Zeilenachse, `Year` und `Region` auf der Seitenachse (mit `Year` zuerst) und `Amount` (Summe) als Datenfeld — genau wie in Beispiel 1. Dann setzen wir `page_field_order` auf `PrintOrderType.DOWN_THEN_OVER` und `page_field_wrap_count` auf `2`. Mit `DOWN_THEN_OVER` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder vertikal gestapelt — `Year` oben, `Region` direkt darunter — und bilden eine einzelne Spalte am oberen Rand der Pivot-Tabelle. Der Streifen nimmt daher zwei Zeilen mit Breite eins ein, im Gegensatz zu Beispiel 1.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```
## **Beispiel 3: Ein Seitenfeld verschieben**
Im dritten Szenario behalten wir diesen Datensatz und diese Feldzuordnung bei, legen ein neutrales Layout fest (`OVER_THEN_DOWN` mit Umbruchanzahl `2`) und demonstrieren dann die `page_fields.move`-Operation. Der Aufruf `move(0, 1)` verschiebt das Seitenfeld an Index 0 (`Year`) an Position 1, und das Seitenfeld, das sich an Position 1 befand (`Region`), rückt auf Position 0. Nach diesem Aufruf ist `Region` das erste Seitenfeld und `Year` das zweite. Umbruch und Anordnungsmodus bleiben unverändert, sodass der Streifen weiterhin horizontal nebeneinander dargestellt wird — nur die Reihenfolge der beiden Dropdowns wurde vertauscht.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```
## **Verwandte Artikel**
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/python-java/add-page-field-in-pivot-table/) — die übergeordnete Seite, die vorstellt, wie Seitenfelder zu einer Pivot-Tabelle hinzugefügt werden.
- [Zeilen- und Spaltenfelder in Pivot-Tabelle](/cells/de/python-java/row-and-column-fields/) — behandelt die Zuweisung von Feldern zu Zeilen- und Spaltenachsen und ergänzt die hier gezeigten Seitenachsenarbeiten.
- [Wertfelder in Pivot-Tabelle verwalten](/cells/de/python-java/manage-value-fields/) — beschreibt, wie der Daten- (Wert-)Bereich konfiguriert wird, einschließlich der in diesem Artikel verwendeten `SUM`-Aggregation.
- [Pivot-Tabelle aktualisieren](/cells/de/python-java/refresh-pivot-table/) — erklärt `refresh_data` und `calculate_data`, die nach dem Neuordnen der Seitenfelder erforderlich sind.
- [Stil auf Pivot-Tabelle anwenden](/cells/de/python-java/apply-style-to-pivot-table/) — zeigt, wie die gerenderte Pivot-Tabelle formatiert wird, nachdem der Seitenfeldstreifen angeordnet wurde.
{{< app/cells/assistant language="python" >}}