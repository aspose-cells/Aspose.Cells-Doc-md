---
title: Pivot-Tabellen und Pivot-Caches in Aspose.Cells for Node.js via C++ aktualisieren
linktitle: Pivot-Tabellen und Pivot-Caches
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Node.js via C++ mit der Pivot-Refresh-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Node.js via C++, Pivot-Tabelle, aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt eine mehrschichtige Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können — von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Node.js via C++ v26.7** ist die veraltete Methode `PivotTable.RefreshData()` als obsolet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Einführung
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Diese Kette zu verstehen, ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte leben.
2. **PivotCache** — der In-Memory-Schnappschuss der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansicht-Objekt, das Zeilen-, Spalten-, Werte- und Filterfelder definiert. Eine `PivotTable` liest *ausschließlich* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** — also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}

Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.CalculateData()`** — berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Rückkehr zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblattzellen als Quelldaten, daher ist der Quelltyp `Sheet` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.

## Schnellstart
Wenn Sie nur den kürzestmöglichen Code benötigen, der jede Pivot-Tabelle in der Arbeitsmappe aktualisiert, reicht ein einziger Aufruf:

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Schreibe die Kopfzeile in die Zellen A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Schreibe Datenzeilen in die Zellen A2:C9 (8 Zeilen mit Fruchtdaten über 2020 und 2021)
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
// Füge eine Pivot-Tabelle hinzu: Quellbereich "A1:C9", Zielzelle "E3", Name "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Weise Pivot-Felder zu: Fruit an Zeilen, Year an Spalten, Amount an Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Ändere mehrere Amount-Werte in den Quelldaten, um Änderungen zu simulieren
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Aktualisiere alle Pivot-Tabellen / Pivot-Caches in der Arbeitsmappe
workbook.refreshAll();
// Speichere die Arbeitsmappe
workbook.save("output.xlsx");
```

Alles andere in diesem Artikel erklärt, wann Sie stattdessen eine engere API wählen sollten.

## Erforderliche Importe
Alle JavaScript-Beispiele in diesem Artikel gehen davon aus, dass das Modul Aspose.Cells for Node.js via C++ geladen wurde und die Pivot-Typen im Namespace `Aspose.Cells.Pivot` liegen. Eine typische Einrichtung ist:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (oder Zugriff über `AsposeCells.Pivot.PivotFieldType`)

## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe — er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, vollumfängliche Aktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```javascript
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

## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — beispielsweise wenn Pivot-Tabellen auf anderen Arbeitsblättern bekanntermaßen nicht verwandt sind und nicht angefasst werden sollen. Für diesen Fall bietet Aspose.Cells `Worksheet.RefreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Kopfzeile mit Frucht / Jahr / Betrag schreiben
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
// Eine Pivot-Tabelle namens "Pivot1" hinzufügen, platziert in der Zielzelle E3, mit Quelle A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Felder zuweisen: Frucht zu Zeile, Jahr zu Spalte, Betrag zu Daten
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// Eine Ansichts-/Layout-Eigenschaft ändern — dies ist eine reine Präsentationsänderung,
// daher ist KEIN erneutes Lesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu aus den
// bereits im PivotCache gespeicherten Daten. Da sich die Quelldaten nicht geändert haben,
// wird kein Round-Trip zur Quelle durchgeführt — nur die zwischengespeicherten Werte werden neu
// in die Arbeitsblattzellen berechnet.
pivotTable.calculateData();
// Arbeitsmappe auf der Festplatte speichern
workbook.save("output.xlsx");
```

## Eine einzelne Pivot-Tabelle aktualisieren
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layout-Einstellungen der Pivot-Tabelle selbst.

### Quelldaten geändert — Verwenden Sie `PivotCache.Refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.PivotCache.Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

### Nur Ansicht/Layout geändert — Verwenden Sie `CalculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layout-Einstellungen der Pivot-Tabelle (z. B. ein Feld wurde in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen wurde umgeschaltet), ist kein Rückweg zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine Nicht-Quelle-Eigenschaft der Pivot-Tabelle und ruft dann `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.
Eine Arbeitsmappe enthält häufig viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache sitzen. Um sie aufzulisten — zum Beispiel vor einer Stapelaktualisierung oder um die Auswirkungen gemeinsam genutzter Caches zu diagnostizieren — verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.

## Migration von der obsoleten `PivotTable.RefreshData()`
Vor Aspose.Cells for Node.js via C++ v26.7 bestand die Standardmethode zum Aktualisieren einer Pivot-Tabelle darin, `PivotTable.RefreshData()` für jede Pivot-Tabelle einzeln aufzurufen. Ab v26.7 ist diese Methode als **obsolet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der Ansatz mit `RefreshData()` pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft die Daten *bei jedem* Aufruf erneut aus der Quelle ab, auch wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind:
Das folgende Beispiel demonstriert das neue effizientere Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzelnen Cache gemeinsam nutzen.

## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und wann Sie welche wählen sollten.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.RefreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.PivotCache.Refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsam genutzten Cache. |
| Nur Ansichts-/Layout-Einstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Quellrundgang. |
| Alle Pivot-Tabellen auf einem gemeinsam genutzten Cache auflisten | `pivotCache.GetPivotTables()` | Zum Auflisten vor einer Massenaktualisierung verwenden. |
In der Praxis sind die cache-basierten APIs dem obsoleten `RefreshData()` pro Tabelle vorzuziehen. Sie berücksichtigen gemeinsam genutzte Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## Häufige Fehlerquellen
- **Vergessen, vor dem Speichern zu aktualisieren.** Eine Pivot-Tabelle schreibt ihre gerenderten Werte nur dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.Refresh()` (oder `Workbook.RefreshAll()`) vor `Workbook.save()` auf, da die gespeicherte Datei sonst weiterhin die alten aggregierten Werte enthält.
- **Aufruf der obsoleten `RefreshData()` pro Tabelle.** In v26.7 ist `PivotTable.RefreshData()` als obsolet markiert und ruft die Quelle bei jedem Aufruf erneut ab. Bei mehreren Pivot-Tabellen, die einen Cache gemeinsam nutzen, bedeutet dies N redundante Quellabrufe. Ersetzen Sie dies durch einen einzigen `PivotCache.Refresh()`, gefolgt von `CalculateData()` pro Tabelle.
- **Aktualisieren, wenn sich nur das Layout geändert hat.** Wenn Sie nur die Ansicht einer Pivot-Tabelle (Spaltenreihenfolge, `ConsolidationFunction` usw.) geändert haben, ohne die Quelldaten zu berühren, ist `PivotCache.Refresh()` unnötig und langsam. Rufen Sie `pivotTable.CalculateData()` auf, um aus dem vorhandenen Cache neu zu rendern.
- **Externe Quelle wird von `PivotCache.Refresh()` nicht unterstützt.** Wenn die Quelle der Pivot-Tabelle aus einer externen Verbindung (Datenbank, OLAP-Cube usw.) stammt, kann `PivotCache.Refresh()` sie in v26.7 nicht aktualisieren — es werden derzeit nur die Quelltypen `Sheet` und `Consolidation` unterstützt. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder bauen Sie den Cache aus der Quelle neu auf.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}