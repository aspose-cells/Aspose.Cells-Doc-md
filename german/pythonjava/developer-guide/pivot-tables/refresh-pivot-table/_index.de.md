---
title: PivotTables und Pivot-Caches in Aspose.Cells for Python via Java aktualisieren
linktitle: PivotTables und Pivot-Caches
description: Erfahren Sie, wie Sie PivotTables in Aspose.Cells for Python via Java mithilfe der API zur Pivot-Aktualisierung ab Version v26.7 aktualisieren. Dieser Artikel behandelt refreshAll, refreshPivotTables, PivotCache.refresh, calculateData und getPivotTables anhand praktischer Codebeispiele.
keywords: Aspose.Cells, Python via Java, PivotTable, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt eine mehrstufige Aktualisierungs-API bereit, mit der Sie Pivot-Daten auf vier verschiedenen Ebenen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen PivotTable. Ab **Aspose.Cells for Python via Java v26.7** ist die bisherige Methode `PivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren APIs mit Cache-Unterstützung ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Introduction
Das Aktualisieren einer PivotTable besteht selten aus einem einzigen Vorgang. Hinter den Kulissen verwaltet Aspose.Cells eine mehrstufige Datenkette, die die ursprünglichen Quelldaten mit den im Arbeitsblatt dargestellten Werten verbindet. Das Verständnis dieser Kette ist entscheidend, um für jede Situation die richtige Aktualisierungs-API auszuwählen.
Die vierstufige Datenkette umfasst:
1. **Datenquelle** – die ursprünglichen Arbeitsblattbereiche, die Datenbankabfrage oder den Konsolidierungsbereich, in denen die Rohwerte gespeichert sind.
2. **PivotCache** – die Momentaufnahme der Quelldaten im Arbeitsspeicher. Jede PivotTable basiert auf einem `PivotCache`; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** – das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *ausschließlich* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** – die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Formatierungen rendert.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Seit v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`SHEET`** und **`CONSOLIDATION`** – also Daten, die in Arbeitsblattbereichen gespeichert sind. Externe Quellen wie Datenbanken oder externe Verbindungen können über die Cache-API noch nicht aktualisiert werden.
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.calculateData()`** – berechnet die Anzeige einer einzelnen PivotTable anhand bereits zwischengespeicherter Daten neu, ohne die Datenquelle erneut abzufragen.
Alle Szenarien in diesem Artikel verwenden Zellen eines Arbeitsblatts als Quelldaten. Der Quelltyp ist daher `SHEET`, und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
{{% /alert %}}

## Quick Start
Wenn Sie lediglich den kürzestmöglichen Code benötigen, um alle PivotTables in der Arbeitsmappe zu aktualisieren, genügt ein einzelner Aufruf:

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

Alles Weitere in diesem Artikel erläutert, wann Sie stattdessen eine API mit engerem Geltungsbereich wählen sollten.

## Required Imports
Alle Python-Beispiele in diesem Artikel verwenden die folgenden Imports, da die Pivot-Typen im Namespace `aspose.cells.pivot` liegen:
- `import jpype`
- `import aspose.cells as cells`
Das Modul `jpype` initialisiert die JVM, während `aspose.cells` die in diesem Artikel verwendeten Typen für Arbeitsmappen, Arbeitsblätter, Zellen und PivotTables bereitstellt.

## Refresh All Pivot Tables in the Workbook
Wenn Sie sicherstellen möchten, dass jeder Pivot-Cache und jede PivotTable in der Arbeitsmappe die aktuellen Quelldaten widerspiegelt, ist `Workbook.refreshAll()` die einfachste und umfassendste API. Ein einzelner Aufruf durchläuft die gesamte Arbeitsmappe, aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet anschließend jede abhängige `PivotTable` neu. Dies ist die empfohlene Vorgehensweise für allgemeine Aktualisierungen des gesamten Dokuments, wenn die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich für Fruit/Year/Amount, erzeugt eine PivotTable, ändert einige Quellwerte und bringt anschließend mit einem einzigen Aufruf von `refreshAll()` alles auf den neuesten Stand.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
Manchmal müssen Sie nur die PivotTables in einem bestimmten Arbeitsblatt aktualisieren, beispielsweise wenn die PivotTables in anderen Arbeitsblättern nachweislich nicht damit zusammenhängen und nicht verändert werden dürfen. Aspose.Cells bietet dafür `Worksheet.refreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh a Single Pivot Table
Wenn Sie für eine einzelne PivotTable eine detaillierte Kontrolle benötigen, bietet die cachebasierte API zwei Optionen. Die Wahl hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder lediglich die Ansicht beziehungsweise das Layout der PivotTable.

### Source Data Changed — Use `PivotCache.refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist `pivotTable.getPivotCache().refresh()` der richtige Einstiegspunkt. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet anschließend jede `PivotTable` neu, die von diesem Cache abhängt.

### Only View/Layout Changed — Use `calculateData()`
Wenn sich die Quelldaten *nicht* geändert haben und lediglich die Ansicht oder das Layout der PivotTable geändert wurde, beispielsweise durch das Verschieben eines Felds in einen anderen Bereich oder das Ändern einer Einstellung zur Aktualisierung beim Öffnen, ist kein erneuter Abruf aus der Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte PivotTable muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine Eigenschaft der PivotTable, die nicht zur Quelle gehört, und ruft anschließend `calculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Eine Arbeitsmappe enthält häufig mehrere PivotTables, die alle auf einem gemeinsamen Cache basieren. Um sie aufzulisten, beispielsweise vor einer Massenaktualisierung oder zur Diagnose der Auswirkungen eines gemeinsam genutzten Caches, verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Auflistung aller `PivotTable`-Instanzen zurück, die vom angegebenen Cache abhängen.

## Migrating from the Obsolete `PivotTable.refreshData()`
Vor Aspose.Cells for Python via Java v26.7 wurde eine PivotTable üblicherweise aktualisiert, indem `PivotTable.refreshData()` für jede PivotTable einzeln aufgerufen wurde. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen APIs mit Cache-Unterstützung ersetzt werden.
Es gibt zwei Gründe, warum der Ansatz, `refreshData()` pro Tabelle aufzurufen, bei Arbeitsmappen aus der Praxis problematisch ist:
- Bei jedem Aufruf werden die Daten erneut aus der Quelle abgerufen, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind:
Das folgende Beispiel veranschaulicht das neue, effiziente Muster für Arbeitsmappen mit mehreren PivotTables, die einen gemeinsamen Cache verwenden.

## Which Refresh API Should I Use?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann die jeweilige API verwendet werden sollte.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; umfasst alle Caches und Tabellen. |
| Nur PivotTables in einem einzelnen Arbeitsblatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE PivotTables, die auf diesem gemeinsam genutzten Cache basieren. |
| Nur Ansicht oder Layout geändert | `pivotTable.calculateData()` | Vermeidet einen unnötigen erneuten Abruf aus der Quelle. |
| Alle PivotTables in einem gemeinsam genutzten Cache auflisten | `pivotCache.getPivotTables()` | Vor einer Massenaktualisierung zum Auflisten verwenden. |
In der Praxis sollten Sie cachebasierte APIs der veralteten Variante `refreshData()` pro Tabelle vorziehen. Sie berücksichtigen gemeinsam genutzte Caches, vermeiden redundante Datenabrufe aus der Quelle und ermöglichen es Ihnen, den kleinstmöglichen Umfang zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## Common Pitfalls
- **Aktualisierung vor dem Speichern vergessen.** Eine PivotTable schreibt ihre gerenderten Werte nur dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wurde. Wenn Sie Quellzellen ändern, müssen Sie `PivotCache.refresh()` oder `Workbook.refreshAll()` vor `Workbook.save()` aufrufen. Andernfalls enthält die gespeicherte Datei weiterhin die alten aggregierten Werte.
- **Aufruf der veralteten `RefreshData()` pro Tabelle.** In v26.7 ist `PivotTable.RefreshData()` als veraltet markiert und ruft bei jedem Aufruf die Quelle erneut ab. Bei mehreren PivotTables mit einem gemeinsamen Cache bedeutet dies N redundante Datenabrufe aus der Quelle. Ersetzen Sie dies durch einen einzigen Aufruf von `PivotCache.refresh()` mit anschließendem `calculateData()` pro Tabelle.
- **Aktualisierung, obwohl sich nur das Layout geändert hat.** Wenn Sie lediglich die Ansicht einer PivotTable geändert haben, etwa die Spaltenreihenfolge oder `ConsolidationFunction`, ohne die Quelldaten zu ändern, ist `PivotCache.refresh()` nicht erforderlich und langsam. Rufen Sie stattdessen `pivotTable.calculateData()` auf, um die PivotTable aus dem vorhandenen Cache neu zu rendern.
- **Externe Quelle wird von `PivotCache.refresh()` nicht unterstützt.** Wenn die Quelle der PivotTable aus einer externen Verbindung wie einer Datenbank oder einem OLAP-Cube stammt, kann `PivotCache.refresh()` sie in v26.7 nicht aktualisieren. Die API unterstützt derzeit nur die Quelltypen `Sheet` und `Consolidation`. Öffnen Sie die Arbeitsmappe bei externen Quellen erneut oder bauen Sie den Cache aus der Quelle neu auf.

{{< app/cells/assistant language="python" >}}