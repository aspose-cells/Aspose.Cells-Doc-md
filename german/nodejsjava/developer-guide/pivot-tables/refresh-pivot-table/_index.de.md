---
title: PivotTables und PivotCaches in Aspose.Cells for Node.js via Java aktualisieren
linktitle: PivotTables und PivotCaches
description: Erfahren Sie, wie Sie mit der PivotTable-Aktualisierungs-API v26.7+ PivotTables in Aspose.Cells for Node.js via Java aktualisieren. Dieser Artikel behandelt refreshAll, refreshPivotTables, PivotCache.refresh, calculateData und getPivotTables anhand praktischer Codebeispiele.
keywords: Aspose.Cells, Node.js, Java, PivotTable, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet eine mehrstufige Aktualisierungs-API, mit der Sie die Daten einer PivotTable auf vier verschiedenen Ebenen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen PivotTable. Ab **Aspose.Cells for Node.js via Java v26.7** ist die bisherige Methode `PivotTable.RefreshData()` als obsolet markiert und sollte durch die effizienteren, cachebasierten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Einführung
Das Aktualisieren einer PivotTable ist selten nur ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrstufige Datenkette, die die ursprünglichen Quelldaten mit den im Arbeitsblatt dargestellten Werten verbindet. Das Verständnis dieser Kette ist entscheidend, um in jeder Situation die geeignete Aktualisierungs-API auszuwählen.
Die vierstufige Datenkette besteht aus Folgendem:
1. **Datenquelle** – die ursprünglichen Arbeitsblattbereiche, die Datenbankabfrage oder der Konsolidierungsbereich, in denen die Rohwerte gespeichert sind.
2. **PivotCache** – die Momentaufnahme der Quelldaten im Arbeitsspeicher. Jede PivotTable basiert auf einem `PivotCache`; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** – das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- and Filterfelder definiert. Eine `PivotTable` liest *ausschließlich* aus ihrem `PivotCache` und niemals direkt aus der Datenquelle.
4. **Cells** – die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Formatierungen schreibt.

{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Daten des Caches stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen gespeichert sind. Externe Quellen wie Datenbanken oder externe Verbindungen lassen sich über die Cache-API noch nicht aktualisieren.
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.calculateData()`** – berechnet die Anzeige einer einzelnen `PivotTable` anhand bereits zwischengespeicherter Daten neu, ohne einen erneuten Zugriff auf die Datenquelle.
Alle Szenarien in diesem Artikel verwenden Zellen eines Arbeitsblatts als Quelldaten. Der Quelltyp ist daher `Sheet`, und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
{{% /alert %}}

## Schnellstart
Wenn Sie lediglich den kürzestmöglichen Code benötigen, um alle PivotTables in der Arbeitsmappe zu aktualisieren, genügt ein einzelner Aufruf:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Alle weiteren Informationen in diesem Artikel erläutern, wann Sie stattdessen eine API mit engerem Geltungsbereich wählen sollten.

## Erforderliche Imports
- `const aspose = require('aspose.cells');`
- Oder für einzelne Imports: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Alle PivotTables in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder PivotCache und jede PivotTable in der Arbeitsmappe die aktuellen Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe, aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet anschließend jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine Aktualisierungen des gesamten Dokuments, wenn die Performance keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich für Fruit/Year/Amount sowie einer PivotTable, ändert einige Quellwerte und aktualisiert anschließend mit `refreshAll()` alle Komponenten in einem einzigen Aufruf.

```javascript
const AsposeCells = require("aspose.cells");
// Erstelle eine neue Arbeitsmappe
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Schreibe die Kopfzeile in die Zellen A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Schreibe Datenzeilen in die Zellen A2:C9 (8 Zeilen mit Obst-Daten über 2020 und 2021)
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
// Füge eine Pivot-Tabelle hinzu: Quellbereich "A1:C9", Zielzelle "E3"
const pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Weise Pivot-Felder zu: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Ändere mehrere Amount-Werte in den Quelldaten, um Änderungen zu simulieren
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Aktualisiere jede Pivot-Tabelle / jeden Pivot-Cache in der Arbeitsmappe
workbook.refreshAll();
// Speichere die Arbeitsmappe
workbook.save("output.xlsx");
```

## Alle PivotTables in einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die PivotTables in einem bestimmten Arbeitsblatt aktualisieren – beispielsweise, wenn die PivotTables in anderen Arbeitsblättern unabhängig sind und nicht verändert werden sollen. Aspose.Cells bietet dafür `Worksheet.refreshPivotTables()`, eine API, die auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Eine einzelne PivotTable aktualisieren
Wenn Sie eine einzelne PivotTable detailliert steuern möchten, bietet Ihnen die cachebasierte API zwei Möglichkeiten. Die Auswahl hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder lediglich die Ansichts- bzw. Layouteinstellungen der PivotTable selbst.

### Quelldaten wurden geändert – `PivotCache.refresh()` verwenden
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist `pivotTable.PivotCache.refresh()` der richtige Einstiegspunkt. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet anschließend jede `PivotTable` neu, die von diesem Cache abhängt.

### Nur Ansicht/Layout wurde geändert – `calculateData()` verwenden
Wenn sich die Quelldaten *nicht* geändert haben, sondern lediglich die Ansicht oder das Layout der PivotTable wurden – beispielsweise wurde ein Feld in einen anderen Bereich verschoben oder die Einstellung zum Aktualisieren beim Öffnen geändert –, ist kein erneuter Zugriff auf die Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die Anzeige der PivotTable muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine Eigenschaft der PivotTable, die nicht zur Datenquelle gehört, und ruft anschließend `calculateData()` auf, um sie aus dem vorhandenen Cache neu darzustellen.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Kopfzeile mit "Obst / Jahr / Betrag" schreiben
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 8 Datenzeilen schreiben (Zeilen 2-9, passend zum Quellbereich A1:C9)
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
// Pivot-Tabelle mit dem Namen hinzufügen, platziert in Zielzelle E3, Datenquelle A1:C9
var pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Felder zuweisen: Fruit zu Zeile, Year zu Spalte, Amount zu Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Eine Ansichts-/Layout-Eigenschaft ändern – dies ist eine reine Darstellungsänderung,
// daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) aus den
// bereits im PivotCache gespeicherten Daten neu. Da sich die Quelldaten nicht geändert haben,
// erfolgt kein Round-Trip zur Quelle – nur die zwischengespeicherten Werte werden neu
// in die Arbeitsblattzellen berechnet.
pivotTable.calculateData();
// Arbeitsbuch auf der Festplatte speichern
workbook.save("output.xlsx");
```

Eine Arbeitsmappe enthält häufig viele PivotTables, die alle auf einem gemeinsamen Cache basieren. Um sie aufzulisten – beispielsweise vor einer Massenaktualisierung oder zur Diagnose der Auswirkungen eines gemeinsamen Caches –, verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Auflistung aller `PivotTable`-Instanzen zurück, die vom angegebenen Cache abhängen.

## Migrieren von der obsoleten `PivotTable.RefreshData()`
Vor Aspose.Cells for Node.js via Java v26.7 bestand die Standardmethode zum Aktualisieren einer PivotTable darin, `PivotTable.RefreshData()` für jede PivotTable einzeln aufzurufen. Ab v26.7 ist diese Methode als **obsolet** markiert und sollte durch die oben beschriebenen cachebasierten APIs ersetzt werden.
Es gibt zwei Gründe, warum der tabellenweise Einsatz von `RefreshData()` in Arbeitsmappen aus der Praxis problematisch ist:
- Die Methode ruft die Daten jedes Mal erneut aus der Quelle ab, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersatzmethoden sind die cachebasierten APIs.
Das folgende Beispiel veranschaulicht das neue effiziente Muster für Arbeitsmappen mit mehreren PivotTables, die einen gemeinsamen Cache verwenden.

## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann die jeweilige API verwendet werden sollte.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; umfasst alle Caches und PivotTables. |
| Nur PivotTables in einem einzelnen Arbeitsblatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Die Quelldaten eines Caches wurden geändert | `pivotTable.PivotCache.refresh()` | Aktualisiert ALLE PivotTables, die auf diesem gemeinsamen Cache basieren. |
| Nur die Ansichts-/Layouteinstellungen wurden geändert | `pivotTable.calculateData()` | Vermeidet den unnötigen erneuten Zugriff auf die Datenquelle. |
| Alle PivotTables in einem gemeinsamen Cache auflisten | `pivotCache.getPivotTables()` | Zur Auflistung vor einer Massenaktualisierung verwenden. |
In der Praxis sollten Sie den cachebasierten APIs gegenüber der obsoleten tabellenweisen Methode `RefreshData()` den Vorzug geben. Sie berücksichtigen gemeinsame Caches, vermeiden redundante Datenabrufe aus der Quelle und ermöglichen es Ihnen, den kleinstmöglichen Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## Häufige Fehler
- **Vergessen des Aktualisierens vor dem Speichern.** Eine PivotTable schreibt ihre dargestellten Werte erst dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wurde. Wenn Sie Quellzellen ändern, rufen Sie vor `Workbook.save()` `PivotCache.refresh()` oder `Workbook.refreshAll()` auf; andernfalls enthält die gespeicherte Datei weiterhin die alten aggregierten Werte.
- **Aufruf der obsoleten Methode `RefreshData()` für jede Tabelle.** In v26.7 ist `PivotTable.RefreshData()` als obsolet markiert und lädt die Quelldaten bei jedem Aufruf erneut aus der Quelle. Bei mehreren PivotTables, die einen gemeinsamen Cache verwenden, bedeutet dies N redundante Abrufe der Quelldaten. Verwenden Sie stattdessen einen einzigen Aufruf von `PivotCache.refresh()` mit anschließendem `calculateData()` pro Tabelle.
- **Aktualisierung, obwohl nur das Layout geändert wurde.** Wenn Sie lediglich die Ansicht einer PivotTable geändert haben – etwa die Spaltenreihenfolge oder `ConsolidationFunction` –, ohne die Quelldaten zu bearbeiten, ist `PivotCache.refresh()` unnötig und langsam. Rufen Sie `pivotTable.calculateData()` auf, um die PivotTable aus dem vorhandenen Cache neu darzustellen.
- **`PivotCache.refresh()` unterstützt keine externe Quelle.** Wenn die Datenquelle der PivotTable aus einer externen Verbindung stammt – einer Datenbank, einem OLAP-Cube oder einem ähnlichen System –, kann `PivotCache.refresh()` sie in v26.7 nicht aktualisieren. Die Methode unterstützt derzeit nur die Quelltypen `Sheet` und `Consolidation`. Öffnen Sie die Arbeitsmappe bei externen Quellen erneut oder erstellen Sie den Cache aus der Quelle neu.

{{< app/cells/assistant language="nodejs-java" >}}