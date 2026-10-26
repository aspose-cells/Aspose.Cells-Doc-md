---
title: Pivot-Tabellen und Pivot-Caches in Aspose.Cells for Python via .NET aktualisieren
linktitle: Pivot-Tabellen und Pivot-Caches
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Python via .NET mit der Pivot-Refresh-API ab v26.7 aktualisieren können. Dieser Artikel behandelt refresh_all, _refresh_pivot_tables, PivotCache.refresh, _calculate_data und _get_pivot_tables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Python via .NET, Pivot-Tabelle, Aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet eine mehrstufige Aktualisierungs-API, mit der Sie Pivot-Daten in vier verschiedenen Bereichen neu laden können — von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Python via .NET v26.7** ist die Legacy-Methode `PivotTable.refresh_data()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Introduction
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — die In-Memory-Momentaufnahme der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

{{% alert color="primary" %}}
`PivotCache.source_type` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** — also Daten, die in Arbeitsblattbereichen liegen. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.calculate_data()`** — berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Round-Trip zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, daher ist der Quelltyp `Sheet` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
{{% /alert %}}

## Quick Start
Wenn Sie nur den kürzestmöglichen Code benötigen, der jede Pivot-Tabelle in der Arbeitsmappe aktualisiert, reicht ein einziger Aufruf aus:

```python
import aspose.cells as ac

workbook = ac.Workbook("input.xlsx")
workbook.refresh_all()
workbook.save("output.xlsx")
```

Alles andere in diesem Artikel erklärt, wann Sie stattdessen eine engere API wählen sollten.

## Required Imports
Alle Python-Beispiele in diesem Artikel beginnen mit den folgenden drei Import-Anweisungen, da die Pivot-Typen im Namespace `aspose.cells.pivot` leben:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Refresh All Pivot Tables in the Workbook
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refresh_all()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe — aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, vollständige Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Jahr/Betrag-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refresh_all()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write header row into cells A1:C1
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(50)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(60)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(70)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(80)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(90)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(100)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(110)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(120)
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.cells.get("C2").put_value(55)
worksheet.cells.get("C5").put_value(85)
worksheet.cells.get("C9").put_value(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refresh_all()
# Save the workbook
workbook.save("output.xlsx")
```

## Refresh All Pivot Tables on a Single Worksheet
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — zum Beispiel, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht verwandt sind und nicht angefasst werden sollten. Für diesen Fall bietet Aspose.Cells `Worksheet.refresh_pivot_tables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2021)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2021)
worksheet.cells.get("C5").put_value(120)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(180)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2020)
worksheet.cells.get("C7").put_value(130)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(220)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2020)
worksheet.cells.get("C9").put_value(140)
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
worksheet.cells.get("C2").put_value(300)
worksheet.cells.get("C5").put_value(250)
worksheet.cells.get("C9").put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Refresh a Single Pivot Table
Wenn Sie eine feinkörnige Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrundeliegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.

### Source Data Changed — Use `PivotCache.refresh()`
Wenn sich die zugrundeliegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivot_table.pivot_cache.refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

### Only View/Layout Changed — Use `calculate_data()`
Wenn sich die Quelldaten *nicht* geändert haben, aber nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (zum Beispiel wurde ein Feld in einen anderen Bereich verschoben oder eine Einstellung für "Beim Öffnen aktualisieren" umgeschaltet), ist kein Round-Trip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivot_table.calculate_data()` die richtige Wahl.
Das folgende Beispiel ändert eine Nicht-Quell-Eigenschaft der Pivot-Tabelle und ruft dann `calculate_data()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write Fruit / Year / Amount header row
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(150)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(250)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(350)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(450)
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivot_table.refresh_data_on_opening_file = False
# calculate_data() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivot_table.calculate_data()
# Save the workbook to disk
workbook.save("output.xlsx")
```

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsamen Cache sitzen. Um sie aufzulisten — zum Beispiel vor einer Stapelaktualisierung oder um die Auswirkungen des gemeinsamen Caches zu diagnostizieren — verwenden Sie `PivotCache.get_pivot_tables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.

## Migrating from the Obsolete `PivotTable.refresh_data()`
Vor Aspose.Cells for Python via .NET v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.refresh_data()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der Ansatz `refresh_data()` pro Tabelle in realen Arbeitsmappen problematisch ist:
- Es ruft die Daten bei jedem Aufruf *erneut* aus der Quelle ab, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind:
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.

## Which Refresh API Should I Use?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refresh_all()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.refresh_pivot_tables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivot_table.pivot_cache.refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsamen Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivot_table.calculate_data()` | Überspringt unnötigen Quell-Round-Trip. |
| Alle Pivot-Tabellen auf einem gemeinsamen Cache auflisten | `pivot_cache.get_pivot_tables()` | Zur Auflistung vor Massenaktualisierungen verwenden. |
In der Praxis sind die cache-basierten APIs dem veralteten `refresh_data()` pro Tabelle vorzuziehen. Sie kennen gemeinsame Caches, vermeiden redundante Quellabfragen und ermöglichen es Ihnen, den kleinsten Bereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## Common Pitfalls
- **Vergessen, vor dem Speichern zu aktualisieren.** Eine Pivot-Tabelle schreibt ihre gerenderten Werte nur dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.refresh()` (oder `Workbook.refresh_all()`) vor `Workbook.save()` auf, da die gespeicherte Datei sonst noch die alten aggregierten Werte enthält.
- **Aufruf der veralteten `refresh_data()` pro Tabelle.** In v26.7 ist `PivotTable.refresh_data()` als veraltet markiert und ruft die Quelle bei jedem Aufruf erneut ab. Bei mehreren Pivot-Tabellen, die einen Cache gemeinsam nutzen, bedeutet dies N redundante Quellabfragen. Ersetzen Sie dies durch ein einzelnes `PivotCache.refresh()`, gefolgt von `calculate_data()` pro Tabelle.
- **Aktualisierung bei nur geändertem Layout.** Wenn Sie nur die Ansicht einer Pivot-Tabelle geändert haben (Spaltenreihenfolge, `ConsolidationFunction` usw.), ohne Quelldaten zu berühren, ist `PivotCache.refresh()` unnötig und langsam. Rufen Sie `pivotTable.calculate_data()` auf, um aus dem vorhandenen Cache neu zu rendern.
- **Externe Quelle wird von `PivotCache.refresh()` nicht unterstützt.** Wenn die Quelle der Pivot-Tabelle aus einer externen Verbindung stammt (Datenbank, OLAP-Cube usw.), kann `PivotCache.refresh()` sie in v26.7 nicht aktualisieren — es unterstützt derzeit nur die Quelltypen `Sheet` und `Consolidation`. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder erstellen Sie den Cache aus der Quelle neu.

{{< app/cells/assistant language="python-net" >}}