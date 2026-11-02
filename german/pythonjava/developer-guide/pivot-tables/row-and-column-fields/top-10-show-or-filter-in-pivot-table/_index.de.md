---
title: Top 10 in PivotTables anzeigen oder filtern
linktitle: Top 10 in PivotTables anzeigen oder filtern
description: Erfahren Sie, wie Sie mit Aspose.Cells for Python via Java in einer PivotTable nur die obersten oder untersten Elemente eines PivotTable-Felds anzeigen. Dieser Artikel behandelt die Methode top10AutoShow für Excel 97-2003, das Lesen von Optionen mit Top10AutoShowSettings und den Top-10-Filter für Excel 2007-365 über filterTop10.
keywords: Aspose.Cells for Python via Java, PivotTable, Top 10, automatische Anzeige, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /de/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die alle Elemente eines Zeilenfelds auflistet, kann bei Dutzenden von Elementen schwer lesbar sein. Ein Top-10-Bericht behält nur die obersten oder untersten Elemente bei und eignet sich daher genau für Ranking-Berichte – etwa für „die 5 umsatzstärksten Produkte“ oder „die 3 Regionen mit der niedrigsten Verkaufsanzahl“. Aspose.Cells unterstützt zwei Mechanismen dafür, die den beiden Generationen von Microsoft Excel entsprechen.
- **AutoShow für Excel 97-2003** – die Methode `PivotField.top10AutoShow()`. Dies ist die klassische Einstellung „Obere/untere N Elemente anzeigen“, die direkt im PivotTable-Feld gespeichert wird. Sie funktioniert in allen Excel-Versionen, ob alt oder neu, da sie Bestandteil des ursprünglichen PivotTable-Formats ist.
- **Top-10-Filter für Excel 2007-365** – die Methode `PivotField.filterTop10()`. Dies ist der moderne Top-10-Wertfilter, der im Feldmenü unter Wertfiltern zu finden ist. Er wird in einem `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und unterstützt eine Rangfolge basierend auf der Anzahl der Elemente oder einem Prozentsatz.

## **Top 10 in Excel 97-2003 anzeigen (top10AutoShow)**
Die klassische AutoShow-Funktion wird mit einem einzigen Aufruf von `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` konfiguriert:
- `isAutoShow` – aktiviert oder deaktiviert die AutoShow-Einstellung für das Feld.
- `isTop` – `True` behält die obersten Elemente bei („Oben“), `False` die untersten („Unten“).
- `count` – die Anzahl der beizubehaltenden Elemente, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `rankBy` – der nullbasierte Index des **Datenfelds**, dessen Werte für die Rangfolge der Elemente maßgeblich sind. Geben Sie -1 an, um die Elemente nach dem Feld selbst zu rangieren.
Die Rangfolge kann durch ein Wertfeld oder durch das Feld selbst bestimmt werden. Zwei naheliegende Varianten werden nachstehend gezeigt.

### **Rangfolge nach einem Wertfeld**
Ordnen Sie die Elemente des Zeilenfelds anhand eines herkömmlichen Wertfelds wie „Summe der Verkäufe“ an. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die zwei Sportarten mit den höchsten Verkaufswerten. `rankBy` ist 0, da „Summe der Verkäufe“ das Datenfeld mit Index 0 ist.

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
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Rangfolge nach dem Feld selbst**
Ein Feld kann auch anhand seiner eigenen Werte rangiert werden – geben Sie -1 als `rankBy` an. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Das folgende Beispiel zeigt die drei am niedrigsten rangierten Sportarten. Beim Speichern dieser Einstellung wird das Attribut `rankBy` aus dem XML der PivotTable weggelassen, da -1 der Standardwert des Formats ist. `Top10AutoShowSettings.getRankBy()` liest anschließend den Wert -1 zurück.

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
# Die unteren 3 Elemente anzeigen, die nach dem Feld selbst rangsortiert sind (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Aktuelle Optionen lesen (Top10AutoShowSettings)**
Die Methode `PivotField.getTop10AutoShowSettings()` liefert ein `PivotFieldTop10AutoShowSettings`-Objekt zurück, das die aktuell im Feld gespeicherten AutoShow-Optionen enthält. Verwenden Sie es, um zu prüfen, wie die Elemente in einer vorhandenen oder aus einer Datei geladenen Arbeitsmappe beziehungsweise in einer gerade konfigurierten PivotTable dargestellt werden.

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

Die vier Eigenschaften entsprechen den klassischen AutoShow-Attributen, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), sodass die zurückgelesenen Werte von jeder Excel-Version berücksichtigt werden.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten Zugriffsmethoden von `PivotField` – `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` und `getAutoShowField()` – sind als veraltet markiert. Verwenden Sie stattdessen das `Top10AutoShowSettings`-Objekt. Die Zuordnung lautet: `PivotField.isAutoShow()` entspricht `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` entspricht `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` entspricht `Top10AutoShowSettings.getAutoShowCount()` und `PivotField.getAutoShowField()` entspricht `Top10AutoShowSettings.getRankBy()`. Die Methode `top10AutoShow()` selbst ist die unterstützte Methode zum Ändern der Einstellungen.
- `top10AutoShow` funktioniert mit Zeilen- und Spaltenfeldern. Ein Feld, das ausschließlich im Seitenbereich (Filterbereich) liegt, kann auf diese Weise nicht rangiert werden, da seine Elemente nicht im PivotTable-Körper angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (filterTop10)**
Moderne Excel-Versionen stellen Top 10 als Wertfilter im Feldmenü (Wertfilter, Top 10...) bereit. Aspose.Cells bildet dies mit der Methode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` ab, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` – der nullbasierte Index des Datenfelds, dessen aggregierte Werte für die Rangfolge der Elemente maßgeblich sind.
- `type` – legt fest, wie `itemCount` zu interpretieren ist. `PivotFilterType.COUNT` behält eine feste Anzahl von Elementen bei (Option „Elemente“ im Dialog). `PivotFilterType.PERCENT` behält einen bestimmten Prozentsatz der Elemente bei; `itemCount` ist dabei selbst der Prozentsatz, 30 bedeutet also die obersten 30 Prozent. `PivotFilterType.SUM` bestimmt die Rangfolge anhand der kumulierten Summe der Werte.
- `isTop` – `True` für „Oben“, `False` für „Unten“.
- `itemCount` – der Wert N in „Top N“; seine Einheit hängt von `type` ab.

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
    # Top-10-Filter — die beiden höchsten Elemente nach „Summe der Verkäufe“ beibehalten (Datenfeldindex 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # Für einen prozentbasierten Filter stattdessen die oberen 30 Prozent der Elemente beibehalten:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` und `filterTop10` sind zwei getrennte Funktionen. AutoShow schreibt den klassischen Attributsatz `autoShow` in das PivotTable-Feld und wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `filterTop10` schreibt einen modernen `PivotFilter`-Eintrag, der Excel 2007 oder eine neuere Version erfordert. Wird eine Arbeitsmappe in einer älteren Excel-Version geöffnet, zeigt die PivotTable mit dem modernen Filter standardmäßig alle Elemente an. Für Dokumente, die mit älteren Tools verarbeitet werden müssen, ist `top10AutoShow` vorzuziehen; für moderne Arbeitsmappen ist `filterTop10` vorzuziehen, da der Filter mit den anderen Wertfiltern kombiniert werden kann.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTables nach Bezeichnung oder Wert filtern](/cells/de/python-java/filter-by-label-or-value-of-pivot-table/)
- [Zeilen- und Spaltenfelder zu einer PivotTable hinzufügen](/cells/de/python-java/pivot-table-add-row-and-column-fields/)
- [PivotTable-Felder in der PivotTable gruppieren](/cells/de/python-java/group-pivot-fields-in-the-pivot-table/)
- [PivotTable aktualisieren](/cells/de/python-java/refresh-pivot-table/)
- [Seitenfeld zur PivotTable hinzufügen](/cells/de/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}