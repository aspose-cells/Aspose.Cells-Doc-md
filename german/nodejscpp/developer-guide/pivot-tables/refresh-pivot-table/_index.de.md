---
title: PivotTables und PivotCaches in Aspose.Cells for Node.js via C++ aktualisieren
linktitle: PivotTables und PivotCaches
description: Erfahren Sie, wie Sie PivotTables in Aspose.Cells for Node.js via C++ mit der Aktualisierungs-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables anhand praxisnaher Codebeispiele.
keywords: Aspose.Cells, Node.js via C++, PivotTable, aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet eine mehrstufige Aktualisierungs-API, mit der Sie Pivot-Daten in vier unterschiedlichen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen PivotTable. Ab **Aspose.Cells for Node.js via C++ v26.7** ist die ältere Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren, cacheorientierten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Introduction
Das Aktualisieren einer PivotTable ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrstufige Datenkette, die die ursprünglichen Quelldaten mit den im Arbeitsblatt dargestellten Werten verbindet. Das Verständnis dieser Kette ist entscheidend, um für jede Situation die richtige Aktualisierungs-API auszuwählen.
Die Datenkette besteht aus vier Ebenen:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, die Datenbankabfrage oder den Konsolidierungsbereich, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — die Momentaufnahme der Quelldaten im Arbeitsspeicher. Jede PivotTable basiert auf einem `PivotCache`; dort werden alle Daten erfasst und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Formatierungen rendert.

{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quellentypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen gespeichert sind. Externe Quellen (Datenbanken, externe Verbindungen usw.) können über die Cache-API derzeit noch nicht aktualisiert werden.
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.calculateData()`** — berechnet die Anzeige einer einzelnen `PivotTable` anhand bereits zwischengespeicherter Daten neu, ohne Round-Trip zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Zellen des Arbeitsblatts als Quelldaten. Daher ist der Quellentyp `Sheet`, und die Aktualisierungsoperationen verhalten sich wie beschrieben.
{{% /alert %}}

## Quick Start
Wenn Sie lediglich den kürzestmöglichen Code benötigen, um alle PivotTables in der Arbeitsmappe zu aktualisieren, genügt ein einziger Aufruf:

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Alles Weitere in diesem Artikel erläutert, wann Sie stattdessen eine API mit kleinerem Geltungsbereich auswählen sollten.

## Required Imports
Bei allen JavaScript-Beispielen in diesem Artikel wird vorausgesetzt, dass das Modul Aspose.Cells for Node.js via C++ geladen wurde und die Pivot-Typen im Namespace `Aspose.Cells.Pivot` liegen. Ein typischer Setup lautet:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (alternativ kann über `AsposeCells.Pivot.PivotFieldType` darauf zugegriffen werden)

## Refresh All Pivot Tables in the Workbook
Wenn alle PivotCaches und PivotTables in der Arbeitsmappe die aktuellen Quelldaten wiedergeben sollen, ist `Workbook.refreshAll()` die einfachste und umfassendste Aktualisierungs-API. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – jeder `PivotCache` wird aus seiner Quelle aktualisiert, und anschließend wird jede abhängige `PivotTable` neu berechnet. Dieses Vorgehen wird für allgemeine Aktualisierungen des gesamten Dokuments empfohlen, wenn die Performance keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quelldatenbereich für Fruit, Year und Amount, fügt eine PivotTable hinzu, ändert einige Quellwerte und bringt anschließend mit `refreshAll()` alles in einem einzigen Aufruf auf den neuesten Stand.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
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
Wenn Sie nur die PivotTables auf einem bestimmten Arbeitsblatt aktualisieren müssen – beispielsweise, weil die PivotTables auf anderen Arbeitsblättern nicht relevant sind und nicht verändert werden sollen –, bietet Aspose.Cells mit `Worksheet.refreshPivotTables()` eine API, die auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Wenn Sie eine einzelne PivotTable differenziert steuern müssen, bietet die cachebasierte API zwei Optionen. Die Auswahl hängt davon ab, ob sich die zugrunde liegenden Quelldaten oder lediglich die Ansichts- bzw. Layouteinstellungen der PivotTable geändert haben.

### Source Data Changed — Use `PivotCache.refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist `pivotTable.PivotCache.refresh()` der richtige Einstiegspunkt. Dieser Aufruf liest die Quelldaten erneut in den PivotCache ein und berechnet anschließend jede `PivotTable` neu, die von diesem PivotCache abhängt.

### Only View/Layout Changed — Use `calculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansicht oder das Layout der PivotTable geändert wurde – beispielsweise, wenn ein Feld in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet wurde –, ist kein Round-Trip zur Datenquelle erforderlich. Der PivotCache enthält bereits die richtigen Daten; nur die dargestellte PivotTable muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine Eigenschaft der PivotTable, die nicht die Datenquelle betrifft, und ruft anschließend `calculateData()` auf, um sie aus dem vorhandenen PivotCache neu zu rendern.

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
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
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Eine Arbeitsmappe enthält häufig viele PivotTables, die alle auf demselben PivotCache basieren. Um sie aufzulisten – beispielsweise vor einer Stapelaktualisierung oder zur Diagnose der Auswirkungen eines gemeinsam genutzten PivotCaches –, verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Sammlung aller PivotTables zurück, die vom angegebenen PivotCache abhängen.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Vor Aspose.Cells for Node.js via C++ v26.7 bestand die Standardmethode zum Aktualisieren einer PivotTable darin, `PivotTable.RefreshData()` für jede PivotTable einzeln aufzurufen. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cacheorientierten APIs ersetzt werden.
Der tabellenweise Einsatz von `RefreshData()` ist in realen Arbeitsmappen aus zwei Gründen problematisch:
- Die Methode ruft bei *jedem* Aufruf die Daten aus der Quelle erneut ab, selbst wenn sich die Quelle nicht geändert hat.
Empfohlene Alternativen sind:
Das folgende Beispiel veranschaulicht das neue, effiziente Muster für Arbeitsmappen mit mehreren PivotTables, die einen einzelnen PivotCache gemeinsam nutzen.

## Which Refresh API Should I Use?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs und die empfohlene Auswahl zusammen.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; umfasst alle PivotCaches und PivotTables. |
| Nur PivotTables auf einem einzelnen Arbeitsblatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen PivotCache geändert | `pivotTable.PivotCache.refresh()` | Aktualisiert ALLE PivotTables, die diesen gemeinsam genutzten PivotCache verwenden. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.calculateData()` | Vermeidet unnötige Round-Trips zur Quelle. |
| Alle PivotTables mit einem gemeinsam genutzten PivotCache auflisten | `pivotCache.getPivotTables()` | Vor Massenaktualisierungen zur Aufzählung verwenden. |
In der Praxis sollten cachebasierte APIs der veralteten tabellenweisen Methode `RefreshData()` vorgezogen werden. Sie berücksichtigen gemeinsam genutzte PivotCaches, vermeiden redundante Quellenabfragen und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## Common Pitfalls
- **Vergessen der Aktualisierung vor dem Speichern.** Eine PivotTable schreibt ihre dargestellten Werte nur dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.refresh()` (oder `Workbook.refreshAll()`) vor `Workbook.save()` auf. Andernfalls enthält die gespeicherte Datei weiterhin die alten aggregierten Werte.
- **Aufruf der veralteten Methode `RefreshData()` für jede Tabelle.** Ab v26.7 ist `PivotTable.RefreshData()` als veraltet markiert und ruft bei jedem Aufruf die Quelle erneut ab. Bei mehreren PivotTables, die einen PivotCache gemeinsam nutzen, bedeutet dies N redundante Quellenabfragen. Ersetzen Sie dies durch einen einzigen Aufruf von `PivotCache.refresh()`, gefolgt von `calculateData()` für jede Tabelle.
- **Aktualisierung bei ausschließlich geändertem Layout.** Wenn Sie nur die Ansicht einer PivotTable geändert haben (Spaltenreihenfolge, `ConsolidationFunction` usw.), ohne die Quelldaten zu ändern, ist `PivotCache.refresh()` unnötig und langsam. Rufen Sie `pivotTable.calculateData()` auf, um die PivotTable aus dem vorhandenen PivotCache neu zu rendern.
- **Externe Quelle wird von `PivotCache.refresh()` nicht unterstützt.** Wenn die Quelle der PivotTable aus einer externen Verbindung stammt (Datenbank, OLAP-Cube usw.), kann sie in v26.7 nicht mit `PivotCache.refresh()` aktualisiert werden. Derzeit werden nur die Quellentypen `Sheet` und `Consolidation` unterstützt. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder erstellen Sie den PivotCache aus der Quelle neu.

{{< app/cells/assistant language="nodejs-cpp" >}}