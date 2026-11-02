---
title: Top 10 in einer PivotTable anzeigen oder filtern
linktitle: Top 10 in einer PivotTable anzeigen oder filtern
description: Erfahren Sie, wie Sie mit Aspose.Cells for Python via .NET in einem PivotTable-Feld nur die höchst- oder niedrigstplatzierten Elemente anzeigen. Dieser Artikel behandelt die Methode top_10_auto_show für Excel 97-2003, das Lesen von Optionen mithilfe von top_10_auto_show_settings und den Top-10-Filter für Excel 2007-365 mithilfe von filter_top10.
keywords: Aspose.Cells, Python über .NET, PivotTable, Top 10, AutoShow, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /de/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwer lesbar sein, wenn das Feld Dutzende Elemente enthält. Ein Top-10-Bericht behält nur die höchst- oder niedrigstplatzierten Elemente bei – das ist genau der Zweck von Rankingberichten, beispielsweise „die 5 umsatzstärksten Produkte“ oder „die 3 Regionen mit der niedrigsten Verkaufsanzahl“. Aspose.Cells unterstützt zwei Mechanismen, die den beiden Generationen von Microsoft Excel entsprechen.
- **Excel 97-2003 AutoShow** – die Methode `PivotField.top_10_auto_show()`. Dies ist die klassische Einstellung „N höchste/niedrigste Elemente anzeigen“, die direkt am PivotTable-Feld gespeichert ist. Sie funktioniert in jeder Excel-Version, ob alt oder neu, da sie Teil des ursprünglichen PivotTable-Formats ist.
- **Excel 2007-365 Top-10-Filter** – die Methode `PivotField.filter_top10()`. Dies ist der moderne Top-10-Wertfilter, der im Feldmenü unter „Wertfilter“ zu finden ist. Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und unterstützt eine Rangfolge nach Elementanzahl und Prozentsatz.

## **Top 10 in Excel 97-2003 anzeigen (top_10_auto_show)**
Das klassische AutoShow wird mit einem einzigen Aufruf von `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)` konfiguriert:
- `is_auto_show` – aktiviert oder deaktiviert die AutoShow-Einstellung für das Feld.
- `is_top` – `True` behält die höchstplatzierten Elemente bei (Oben), `False` die niedrigstplatzierten (Unten).
- `count` – die Anzahl der beizubehaltenden Elemente, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `rank_by` – der nullbasierte Index des **Datenfelds**, dessen Werte die Rangfolge der Elemente bestimmen. Geben Sie -1 an, um die Elemente nach dem Feld selbst einzustufen.
Die Rangfolge kann anhand eines Wertfelds oder des Felds selbst ermittelt werden. Im Folgenden werden zwei naheliegende Varianten gezeigt.

### **Nach einem Wertfeld einstufen**
Ordnen Sie die Elemente des Zeilenfelds anhand eines gewöhnlichen Wertfelds wie `Sum of Sales` ein. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die 2 Sportarten mit den höchsten `Sales`-Werten. `rank_by` ist 0, weil `Sum of Sales` das Datenfeld mit dem Index 0 ist.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Die 2 besten Elemente anzeigen, sortiert nach "Sum of Sales" (Datenfeldindex 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Nach dem Feld selbst einstufen**
Ein Feld kann auch anhand seiner eigenen Werte eingestuft werden – geben Sie -1 als `rank_by` an. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Das folgende Beispiel zeigt die 3 Sportarten am unteren Ende, eingestuft anhand des Feldes selbst. Wird diese Einstellung gespeichert, wird das Attribut `rank_by` aus dem XML der PivotTable weggelassen, da -1 der Standardwert des Formats ist, und `top_10_auto_show_settings.rank_by` liest den Wert -1 zurück.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Aktuelle Optionen lesen (top_10_auto_show_settings)**
Die Eigenschaft `PivotField.top_10_auto_show_settings` gibt ein `PivotFieldTop10AutoShowSettings`-Objekt zurück, das die derzeit im Feld gespeicherten AutoShow-Optionen zugänglich macht. Verwenden Sie es, um zu prüfen, wie eine vorhandene Arbeitsmappe oder eine gerade konfigurierte PivotTable ihre Elemente darstellt. Dies gilt auch für Arbeitsmappen, die aus einer Datei geladen wurden.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

Die vier Eigenschaften bilden die klassischen AutoShow-Attribute ab, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Somit sind die zurückgelesenen Werte dieselben, die von jeder Excel-Version berücksichtigt werden.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten `PivotField`-Eigenschaften `is_auto_show`, `is_ascend_show`, `auto_show_count` und `auto_show_field` sind als veraltet markiert. Verwenden Sie stattdessen das Objekt `top_10_auto_show_settings`: `is_auto_show` wird zu `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` wird zu `top_10_auto_show_settings.is_top`, `auto_show_count` wird zu `top_10_auto_show_settings.auto_show_count` und `auto_show_field` wird zu `top_10_auto_show_settings.rank_by`. Die Methode `top_10_auto_show()` selbst ist die unterstützte Vorgehensweise zum Ändern der Einstellungen.
- `top_10_auto_show` funktioniert mit Zeilen- und Spaltenfeldern. Ein Feld, das ausschließlich im Seitenbereich (Filterbereich) liegt, kann auf diese Weise nicht eingestuft werden, da seine Elemente nicht im PivotTable-Körper angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (filter_top10)**
Moderne Excel-Versionen stellen Top 10 im Feldmenü als Wertfilter bereit („Wertfilter“, „Top 10 …“). Aspose.Cells bildet dies mit der Methode `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)` ab, die den erstellten `PivotFilter` zurückgibt:
- `value_field_index` – der nullbasierte Index des Datenfelds, dessen aggregierte Werte die Rangfolge der Elemente bestimmen.
- `type` – legt fest, was `item_count` bedeutet. `PivotFilterType.COUNT` behält eine feste Anzahl von Elementen bei (die Option „Elemente“ im Dialog). `PivotFilterType.PERCENT` behält einen Prozentsatz der Elemente bei, sodass `item_count` selbst der Prozentsatz ist – 30 behält die oberen 30 % der Elemente bei. `PivotFilterType.SUM` erstellt die Rangfolge nach kumuliertem Wertanteil.
- `is_top` – `True` für Oben, `False` für Unten.
- `item_count` – der N-Wert in einer Top-N-Auswahl; die Einheit hängt von `type` ab.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Top-10-Filter — die 2 obersten Elemente nach "Sum of Sales" beibehalten (Datenfeldindex 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# Für einen prozentualen Filter stattdessen die obersten 30 Prozent der Elemente beibehalten:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` und `filter_top10` sind zwei separate Funktionen. AutoShow schreibt den klassischen `autoShow`-Attributsatz am PivotTable-Feld und wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `filter_top10` schreibt einen modernen `PivotFilter`-Eintrag, der Excel 2007 oder eine neuere Version erfordert. Wird eine Arbeitsmappe in einer älteren Excel-Version geöffnet, zeigt die PivotTable bei Verwendung des modernen Filters alle Elemente an. Für Dokumente, die über ältere Tools hin und zurück verarbeitet werden müssen, ist `top_10_auto_show` vorzuziehen; für moderne Arbeitsmappen sollte `filter_top10` verwendet werden, da es sich mit den übrigen Wertfiltern kombinieren lässt.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/python-net/filter-by-label-or-value-of-pivot-table/)
- [Zeilen- und Spaltenfelder zu PivotTables hinzufügen](/cells/de/python-net/pivot-table-add-row-and-column-fields/)
- [PivotTable-Felder in der PivotTable gruppieren](/cells/de/python-net/group-pivot-fields-in-the-pivot-table/)
- [PivotTable aktualisieren](/cells/de/python-net/refresh-pivot-table/)
- [Seitenfeld zur PivotTable hinzufügen](/cells/de/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}