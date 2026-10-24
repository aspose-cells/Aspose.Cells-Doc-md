---
title: Pivot-Tabellen und Pivot-Caches in Aspose.Cells for Java aktualisieren
linktitle: Pivot-Tabellen und Pivot-Caches
description: "Erfahren Sie, wie Sie mit der Pivot-Refresh-API v26.7+ Pivot-Tabellen in Aspose.Cells for Java aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables anhand praktischer Codebeispiele."
keywords: Aspose.Cells, Java, Pivot-Tabelle, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt eine mehrstufige Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Umfängen neu laden können – vom gesamten Workbook bis zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Java v26.7** ist die veraltete Methode `PivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren, cachebewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Introduction
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die die ursprünglichen Quelldaten mit den dargestellten Werten im Arbeitsblatt verbindet. Das Verständnis dieser Kette ist entscheidend, um für jede Situation die richtige Aktualisierungs-API auszuwählen.
Die vierstufige Datenkette lautet:
1. **Datenquelle** – die ursprünglichen Arbeitsblattbereiche, die Datenbankabfrage oder den Konsolidierungsbereich, in dem die Rohwerte gespeichert sind.
2. **`PivotCache`** – die In-Memory-Aufnahme der Quelldaten. Jede Pivot-Tabelle basiert auf einem `PivotCache`; hier werden alle Daten gesammelt und aggregiert.
3. **`PivotTable`** – das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **`Cells`** – die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Formatierungen darstellt.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen gespeichert sind. Externe Quellen (Datenbanken, externe Verbindungen usw.) können über die Cache-API noch nicht aktualisiert werden.
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.calculateData()`** – berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne einen Rückweg zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Zellen eines Arbeitsblatts als Quelldaten; der Quelltyp ist daher `Sheet`, und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
{{% /alert %}}

## Quick Start
Wenn Sie lediglich den kürzestmöglichen Code benötigen, der sämtliche Pivot-Tabellen in der Arbeitsmappe aktualisiert, genügt ein einziger Aufruf:

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Alles Weitere in diesem Artikel erläutert, wann Sie stattdessen eine API mit kleinerem Umfang auswählen sollten.

## Required Import Statements
Alle Java-Beispiele in diesem Artikel beginnen mit den folgenden Importanweisungen, da die Pivot-Typen im Paket `com.aspose.cells.pivot` liegen:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist `Workbook.refreshAll()` die einfachste und umfassendste API. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet anschließend jede abhängige `PivotTable` neu. Dies ist die empfohlene Vorgehensweise für allgemeine Aktualisierungen des gesamten Dokuments, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich Fruit/Year/Amount, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refreshAll()`, um alles mit einem einzigen Aufruf auf den neuesten Stand zu bringen.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – beispielsweise wenn die Pivot-Tabellen auf anderen Arbeitsblättern nachweislich nicht zusammenhängen und nicht verändert werden sollen. In diesem Fall stellt Aspose.Cells `Worksheet.refreshPivotTables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Wenn Sie eine einzelne Pivot-Tabelle detailliert kontrollieren möchten, bietet die cachebasierte API zwei Optionen. Die Wahl hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder lediglich die Ansicht-/Layout-Einstellungen der Pivot-Tabelle selbst.

### Source Data Changed — Use `PivotCache.refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.getPivotCache().refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet anschließend jede `PivotTable` neu, die von diesem Cache abhängt.

### Only View/Layout Changed — Use `calculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansicht oder die Layouteinstellungen der Pivot-Tabelle wurden – beispielsweise ein Feld in einen anderen Bereich verschoben oder die Einstellung zum Aktualisieren beim Öffnen umgeschaltet wurde –, ist kein Rückweg zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die dargestellte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine nicht quellbezogene Eigenschaft der Pivot-Tabelle und ruft dann `calculateData()` auf, um sie aus dem vorhandenen Cache neu darzustellen.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsamen Cache basieren. Um sie aufzulisten – etwa vor einer Massenaktualisierung oder zur Diagnose der Auswirkungen eines gemeinsamen Caches –, verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Sammlung aller `PivotTable` zurück, die vom angegebenen Cache abhängen.

## Migrating from the Obsolete `PivotTable.refreshData()`
Vor Aspose.Cells for Java v26.7 war der Standardweg zum Aktualisieren einer Pivot-Tabelle, `PivotTable.refreshData()` für jede Pivot-Tabelle einzeln aufzurufen. Ab v26.7 ist diese Methode als **veraltet** gekennzeichnet und sollte durch die oben beschriebenen cachebewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der Ansatz `refreshData()` pro Tabelle bei Arbeitsmappen aus der Praxis problematisch ist:
- Er ruft die Daten bei jedem Aufruf erneut aus der Quelle ab, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind:
Das folgende Beispiel zeigt das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzelnen Cache gemeinsam nutzen.

## Which Refresh API Should I Use?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann Sie welche auswählen sollten.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein einzelnes Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE Pivot-Tabellen, die diesen gemeinsamen Cache verwenden. |
| Nur Ansicht-/Layout-Einstellungen geändert | `pivotTable.calculateData()` | Überspringt den unnötigen Rückweg zur Quelle. |
| Alle Pivot-Tabellen in einem gemeinsamen Cache auflisten | `pivotCache.getPivotTables()` | Zum Auflisten vor einer Massenaktualisierung verwenden. |
In der Praxis sollten Sie cachebasierte APIs der veralteten Methode `refreshData()` pro Tabelle vorziehen. Sie berücksichtigen gemeinsame Caches, vermeiden redundante Datenabrufe aus der Quelle und ermöglichen es Ihnen, den kleinsten Umfang zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## Common Pitfalls
- **Das Aktualisieren vor dem Speichern vergessen.** Eine Pivot-Tabelle schreibt ihre dargestellten Werte erst dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.refresh()` (oder `Workbook.refreshAll()`) vor `Workbook.save()` auf; andernfalls enthält die gespeicherte Datei weiterhin die alten aggregierten Werte.
- **Die veraltete `refreshData()` pro Tabelle aufrufen.** In v26.7 ist `PivotTable.refreshData()` als veraltet markiert und ruft die Quelle bei jedem Aufruf erneut ab. Wenn mehrere Pivot-Tabellen einen Cache gemeinsam verwenden, bedeutet dies N redundante Datenabrufe aus der Quelle. Ersetzen Sie dies durch einen einzigen `PivotCache.refresh()` und anschließend `calculateData()` pro Tabelle.
- **Aktualisieren, wenn sich nur das Layout geändert hat.** Wenn Sie nur die Ansicht einer Pivot-Tabelle geändert haben (Spaltenreihenfolge, `ConsolidationFunction` usw.), ohne die Quelldaten zu berühren, ist `PivotCache.refresh()` unnötig und langsam. Rufen Sie `pivotTable.calculateData()` auf, um sie aus dem vorhandenen Cache neu darzustellen.
- **Externe Quelle wird von `PivotCache.refresh()` nicht unterstützt.** Wenn die Quelle der Pivot-Tabelle aus einer externen Verbindung stammt (Datenbank, OLAP-Cube usw.), kann `PivotCache.refresh()` sie in v26.7 nicht aktualisieren – derzeit unterstützt die Methode nur die Quelltypen `Sheet` und `Consolidation`. Bei externen Quellen müssen Sie die Arbeitsmappe erneut öffnen oder den Cache aus der Quelle neu erstellen.

{{< app/cells/assistant language="java" >}}