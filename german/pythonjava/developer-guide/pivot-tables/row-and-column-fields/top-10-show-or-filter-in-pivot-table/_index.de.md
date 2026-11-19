---
title: Top‑10‑Anzeige oder -Filter in PivotTable
linktitle: Top‑10‑Anzeige oder -Filter in PivotTable
description: Erfahren Sie, wie Sie in Aspose.Cells for Python via Java nur die am höchsten bzw. am niedrigsten platzierten Elemente eines Pivot‑Feldes anzeigen. Dieser Artikel behandelt die Excel 97‑2003‑Methode top10AutoShow, das Auslesen von Optionen mit Top10AutoShowSettings und den Excel 2007‑365‑Top‑10‑Filter über filterTop10.
keywords: Aspose.Cells for Python via Java, PivotTable, Top‑10, Auto‑Anzeige, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /de/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwer lesbar sein, wenn das Feld Dutzende von Mitgliedern enthält. Ein Top‑10‑Bericht behält nur die am höchsten bzw. am niedrigsten platzierten Elemente, was genau das ist, was Ranglistenberichte benötigen – „die Top 5 Produkte nach Umsatz“ oder „die unteren 3 Regionen nach Verkaufszahl“. Aspose.Cells unterstützt dafür zwei Mechanismen, die zwei Generationen von Microsoft Excel entsprechen.
- **Excel 97‑2003 AutoShow** — die Methode `PivotField.top10AutoShow()`. Dies ist die klassische Einstellung „Zeige die obersten/untersten N Elemente“, die direkt im Pivot‑Feld gespeichert wird. Sie funktioniert in jeder Excel‑Version, alt und neu, da sie Teil des ursprünglichen PivotTable‑Formats ist.
- **Excel 2007‑365 Top 10‑Filter** — die Methode `PivotField.filterTop10()`. Dies ist der moderne Top‑10‑Wertfilter, der im Feldmenü unter „Wertfilter“ zu finden ist. Er wird als ein `PivotFilter`‑Objekt gespeichert, das dem Feld zugeordnet ist, und ermöglicht ein Ranking basierend auf Anzahl der Elemente oder Prozentsatz.

## **Top‑10‑Anzeige in Excel 97‑2003 (top10AutoShow)**
Die klassische Auto‑Anzeige wird mit einem einzigen Aufruf von `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` konfiguriert:
- `isAutoShow` — aktiviert oder deaktiviert die Auto‑Anzeige‑Einstellung für das Feld.
- `isTop` — `True` behält die am höchsten platzierten Elemente (Top), `False` die am niedrigsten (Bottom).
- `count` — gibt an, wie viele Elemente behalten werden sollen, z. B. 10 für einen klassischen Top‑10‑Bericht.
- `rankBy` — der nullbasierte Index des **Datenfelds**, dessen Werte die Elemente ranken. Verwenden Sie -1, um die Elemente nach dem Feld selbst zu ranken.
Das Ranking kann durch ein Werte‑Feld oder durch das Feld selbst gesteuert werden. Zwei natürliche Varianten existieren, siehe unten.

### **Ranking nach einem Werte‑Feld**
Rangieren Sie die Elemente des Zeilenfelds nach einem gewöhnlichen Werte‑Feld, z. B. Summe der Verkäufe. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt die Top 2 Sportarten nach Umsatz. `rankBy` ist 0, weil „Summe der Verkäufe“ das Datenfeld am Index 0 ist.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Ranking nach dem Feld selbst**
Ein Feld kann auch nach ihm selbst gerankt werden – übergeben Sie -1 als `rankBy`. Für diese Variante wird kein zusätzliches Datenfeld benötigt; das Feld muss lediglich im Zeilen‑ (oder Spalten‑) Bereich vorhanden sein. Das folgende Beispiel zeigt die untersten 3 Sportarten, die nach dem Feld selbst gerankt werden. Wenn diese Einstellung gespeichert wird, wird das Attribut `rankBy` aus dem PivotTable‑XML weggelassen, da -1 der Standardwert des Formats ist, und `Top10AutoShowSettings.getRankBy()` liest -1 zurück.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Aktuelle Optionen lesen (Top10AutoShowSettings)**
Die Methode `PivotField.getTop10AutoShowSettings()` gibt ein `PivotFieldTop10AutoShowSettings`‑Objekt zurück, das die derzeit im Feld gespeicherten Auto‑Anzeige‑Optionen offenlegt. Verwenden Sie es, um zu prüfen, wie eine bestehende Arbeitsmappe oder eine gerade konfigurierte PivotTable ihre Elemente darstellt – einschließlich aus Datei geladener Arbeitsmappen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

Die vier Eigenschaften entsprechen den klassischen Auto‑Anzeige‑Attributen, die in das PivotTable‑XML geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Die zurückgelesenen Werte sind also die Werte, die von jeder Excel‑Version honoriert werden.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten `PivotField`‑Accessor‑Methoden `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` und `getAutoShowField()` sind als veraltet markiert. Verwenden Sie stattdessen das Objekt `Top10AutoShowSettings`: `PivotField.isAutoShow()` wird zu `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` zu `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` zu `Top10AutoShowSettings.getAutoShowCount()` und `PivotField.getAutoShowField()` zu `Top10AutoShowSettings.getRankBy()`. Die Methode `top10AutoShow()` selbst ist der unterstützte Weg, um die Einstellungen zu ändern.
- `top10AutoShow` funktioniert mit Zeilen‑ und Spaltenfeldern. Ein Feld, das ausschließlich im Seiten‑ (Filter‑) Bereich liegt, kann nicht auf diese Weise gerankt werden, da seine Elemente nicht im Pivot‑Körper angeordnet sind.
{{% /alert %}}

## **Excel 2007‑365: Top‑10‑Filter (filterTop10)**
Moderne Excel‑Versionen stellen Top 10 als Wertfilter im Feldmenü (Wertfilter, Top 10…) bereit. Aspose.Cells modelliert dies mit der Methode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` — der nullbasierte Index des Datenfelds, dessen aggregierte Werte die Elemente ranken.
- `type` — gibt an, was `itemCount` bedeutet. `PivotFilterType.COUNT` behält eine feste Anzahl von Elementen (Option „Elemente“ im Dialog). `PivotFilterType.PERCENT` behält einen Prozentsatz der Elemente, sodass `itemCount` den Prozentsatz selbst darstellt – 30 bedeutet die obersten 30 %. `PivotFilterType.SUM` rankt nach kumulativer Wertabdeckung.
- `isTop` — `True` für Top, `False` für Bottom.
- `itemCount` — das N in Top N; die Einheit hängt von `type` ab.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` und `filterTop10` sind zwei separate Funktionen. AutoShow schreibt das klassische `autoShow`‑Attribut, das im Pivot‑Feld gesetzt wird, und wird von allen Excel‑Versionen bis Excel 97 honoriert. `filterTop10` schreibt einen modernen `PivotFilter`‑Eintrag, der Excel 2007 oder neuer erfordert. Wenn eine Arbeitsmappe in einer älteren Excel‑Version geöffnet wird, fällt eine PivotTable, die den modernen Filter verwendet, zurück und zeigt alle Elemente an. Für Dokumente, die durch alte Werkzeuge hindurchgehen müssen, bevorzugen Sie `top10AutoShow`; für moderne Arbeitsmappen bevorzugen Sie `filterTop10`, da es mit anderen Wertfiltern kombiniert werden kann.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot‑Tabellen nach Beschriftung oder Wert filtern](/cells/de/python-java/filter-by-label-or-value-of-pivot-table/)
- [Pivot‑Tabellen‑Zeilen‑ und Spaltenfelder hinzufügen](/cells/de/python-java/pivot-table-add-row-and-column-fields/)
- [Pivot‑Felder in der Pivot‑Tabelle gruppieren](/cells/de/python-java/group-pivot-fields-in-the-pivot-table/)
- [Pivot‑Tabelle aktualisieren](/cells/de/python-java/refresh-pivot-table/)
- [Seitenfeld in Pivot‑Tabelle hinzufügen](/cells/de/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}