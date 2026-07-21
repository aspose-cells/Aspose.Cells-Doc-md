---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for Node.js via C++
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Node.js via C++ mit der v26.7+ Pivot-Aktualisierungs-API aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Node.js via C++, Pivot-Tabelle, Aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells bietet eine mehrschichtige Aktualisierungs-API, mit der Sie Pivot-Daten in vier verschiedenen Bereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Node.js via C++ v26.7** ist die Legacy-Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren, cache-fähigen APIs ersetzt werden, die in diesem Artikel beschrieben werden.

{{% /alert %}}

## Einführung

Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den im Arbeitsblatt angezeigten Werten verbindet. Diese Kette zu verstehen, ist der Schlüssel zur Wahl der richtigen Aktualisierungs-API für jede Situation.

Die vierschichtige Datenkette ist:

1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Werte- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

Ein besonders wichtiges Konzept ist der **geteilte Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert sofort jede abhängige `PivotTable`.

{{% alert color="primary" %}}

`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.

{{% /alert %}}

Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:

- **`PivotCache.Refresh()`** — lädt die Quelle neu in den Cache UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.CalculateData()`** — berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Rückgriff auf die Datenquelle.

Alle Szenarien in diesem Artikel verwenden Arbeitsblattzellen als Quelldaten, daher ist der Quelltyp `Sheet`, und die Aktualisierungsvorgänge verhalten sich wie beschrieben.

## Erforderliche Importe

Alle JavaScript-Beispiele in diesem Artikel setzen voraus, dass das Modul Aspose.Cells for Node.js via C++ geladen wurde und die Pivot-Typen im Namespace `Aspose.Cells.Pivot` verfügbar sind. Eine typische Konfiguration ist:

- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (oder Zugriff über `AsposeCells.Pivot.PivotFieldType`)

## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren

Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die aktuellsten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, dokumentenweite Aktualisierungen, bei denen die Leistung keine Rolle spielt.

Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich Fruit/Year/Amount, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Schreibe die Kopfzeile in die Zellen A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Schreibe Datenzeilen in die Zellen A2:C9 (8 Zeilen mit Fruchtdaten für 2020 und 2021)
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

// Füge eine Pivot-Tabelle hinzu: Quellbereich „A1:C9", Zielzelle „E3", Name „Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Weise Pivot-Felder zu: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Ändere mehrere Amount-Werte in den Quelldaten, um Änderungen zu simulieren
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Aktualisiere jede Pivot-Tabelle / jeden Pivot-Cache in der Arbeitsmappe
workbook.refreshAll();

// Speichere die Arbeitsmappe
workbook.save("output.xlsx");
```

## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren

Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – zum Beispiel, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht in Beziehung stehen und nicht angefasst werden sollten. Für diesen Fall stellt Aspose.Cells `Worksheet.RefreshPivotTables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

Dies ist selektiver als `Workbook.RefreshAll()`: Nur die Pivot-Tabellen auf dem Zielarbeitsblatt werden aktualisiert, Pivot-Tabellen auf anderen Arbeitsblättern bleiben unberührt.

Das folgende Beispiel füllt die gleichen Quelldaten Fruit/Year/Amount, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.

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

## Eine einzelne Pivot-Tabelle aktualisieren

Wenn Sie eine feinkörnige Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrundeliegenden Quelldaten oder nur die Ansichts-/Layout-Einstellungen der Pivot-Tabelle selbst.

### Quelldaten geändert — Verwenden Sie `PivotCache.Refresh()`

Wenn sich die zugrundeliegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.PivotCache.Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

{{% alert color="primary" %}}

Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.Refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufgebaut sind – nicht nur die, auf die Sie verweisen. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.

{{% /alert %}}

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten des geteilten Caches zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.

```javascript
const AsposeCells = require("aspose.cells");

// Erstelle eine neue Arbeitsmappe und greife auf das erste Arbeitsblatt zu
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Schreibe die Kopfzeile: Obst / Jahr / Menge
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Schreibe ungefähr 9 Datenzeilen (Traube / Blaubeere / Kiwi / Kirsche über 2020-2021)
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Füge die erste Pivot-Tabelle "Pivot1" hinzu, verankert an Zelle E3, Quellbereich A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Weise Felder für Pivot1 zu
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Füge eine ZWEITE Pivot-Tabelle "Pivot2" hinzu, verankert an E15, mit demselben Quellbereich A1:C9
// Sowohl Pivot1 als auch Pivot2 teilen sich einen einzelnen PivotCache, da der Quellbereich identisch ist.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Weise dieselben Felder für Pivot2 zu
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Ändere mehrere Mengen-Zellenwerte in den Quelldaten, um eine Datenänderung zu simulieren
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Aktualisiere den geteilten PivotCache.
// Da Pivot1 und Pivot2 denselben PivotCache teilen, aktualisiert dieser einzelne Aufruf
// BEIDE Pivot-Tabellen (Daten + Stil) aus der aktualisierten Quelle.
pivotTable1.getPivotCache().refresh();

// Speichere die Arbeitsmappe
workbook.save("output.xlsx");
```

### Nur Ansicht/Layout geändert — Verwenden Sie `CalculateData()`

Wenn sich die Quelldaten *nicht* geändert haben, aber nur die Ansichts- oder Layout-Einstellungen der Pivot-Tabelle geändert wurden (zum Beispiel wurde ein Feld in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet), ist kein Round-Trip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.

Dies vermeidet den unnötigen Quellabruf und ist erheblich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.

Das folgende Beispiel ändert eine nicht quellbezogene Eigenschaft der Pivot-Tabelle und ruft dann `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Kopfzeile mit Fruit / Year / Amount schreiben
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

// Eine Pivot-Tabelle namens "Pivot1" hinzufügen, platziert in der Zielzelle E3, mit Quelle aus A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Felder zuweisen: Fruit zur Zeile, Year zur Spalte, Amount zu den Daten
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// Eine Ansichts-/Layout-Eigenschaft ändern – dies ist eine rein darstellungsbezogene Änderung,
// daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu,
// aus den bereits im PivotCache gehaltenen Daten. Da sich die Quelldaten nicht geändert haben,
// wird kein Roundtrip zur Quelle durchgeführt – nur die zwischengespeicherten Werte werden neu
// in die Arbeitsblattzellen berechnet.
pivotTable.calculateData();

// Arbeitsmappe auf der Festplatte speichern
workbook.save("output.xlsx");
```

## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem einzigen geteilten Cache aufsetzen. Um sie aufzulisten – zum Beispiel vor einer Batch-Aktualisierung oder um die Auswirkungen des geteilten Caches zu diagnostizieren – verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die vom angegebenen Cache abhängt.

Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen oder einfach die von `GetPivotTables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin erscheinen.

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und listet dann die Pivot-Tabellen des Caches auf.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migration von der veralteten `PivotTable.RefreshData()`

Vor Aspose.Cells for Node.js via C++ v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.RefreshData()` auf jeder Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-fähigen APIs ersetzt werden.

Es gibt zwei Gründe, warum der Ansatz mit `RefreshData()` pro Tabelle in realen Arbeitsmappen problematisch ist:

- Er ruft die Daten *jedes Mal* erneut aus der Quelle ab, auch wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten geteilten Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt der wiederholte Aufruf von `RefreshData()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder erneut abgerufen wird, was sehr langsam ist.

Die empfohlenen Ersetzungen sind:

- **Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren** → verwenden Sie `workbook.refreshAll();`
- **Einige davon aktualisieren** → verwenden Sie `pivotTable.PivotCache.Refresh();` für einen Cache. Da der Cache geteilt wird, aktualisiert dieser einzige Aufruf jede Pivot-Tabelle, die auf diesem Cache aufbaut. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Pivot-Layout wurde geändert** → verwenden Sie `pivotTable.CalculateData();`, um aus dem vorhandenen Cache ohne Quell-Round-Trip neu zu rendern.

Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Quelldaten aufbauen: Frucht / Jahr / Betrag (Kopfzeile + 9 Zeilen) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Erste Pivot-Tabelle (Pivot1) an der Zielzelle E3 hinzufügen ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- ZWEITE Pivot-Tabelle (Pivot2) auf DENSELBEN Quellbereich hinzufügen ---
// Sowohl Pivot1 als auch Pivot2 teilen sich EINEN zugrundeliegenden PivotCache.
// Genau dies ist das Szenario, in dem der alte pro-Tabellen RefreshData()-
// Ansatz ineffizient wird: Das Aktualisieren einer Tabelle ruft den gesamten
// gemeinsam genutzten Cache erneut ab, sodass das Aktualisieren von N Tabellen
// denselben teuren Abruf N-mal durchführt.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Mehrere Betragswerte in den Quelldaten ändern ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- VERALTETES Muster (vor 26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // ruft erneut von der Quelle ab und aktualisiert den gesamten Cache
// pivotTable2.RefreshData();  // ruft ERNEUT ab — der Cache ist bereits frisch!
// Jeder Aufruf baut den gemeinsam genutzten Cache neu auf, also N Tabellen = N redundante Abrufe.

// --- NEUES Muster ab v26.7: Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
// Ein einziger Aufruf von PivotCache.Refresh() holt die geänderten Werte in den
// gemeinsam genutzten Cache UND berechnet die Anzeige JEDER Pivot-Tabelle neu,
// die darauf verweist. Da sich Pivot1 und Pivot2 einen PivotCache teilen,
// aktualisiert dieser eine Aufruf beide Tabellen — kein zweiter Quellzugriff nötig.
pivotTable1.getPivotCache().refresh();

// CalculateData() rendert nur die Anzeige einer Pivot-Tabelle (Daten + Stil)
// aus den bereits im Cache vorhandenen Daten neu — es greift NICHT auf die
// Quelle zu. Wir rufen es hier nur auf, um die API zu demonstrieren: Nachdem
// der Cache einmal aktualisiert wurde, kann jede abhängige Tabelle neu gerendert
// werden, ohne zur Quelle zurückzugehen. Verwenden Sie CalculateData() eigenständig,
// wenn sich nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle geändert haben
// und der Cache aktuell ist.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Welche Aktualisierungs-API sollte ich verwenden?

Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und gibt an, wann jede zu wählen ist.

| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.RefreshPivotTables()` | Beschränkt auf ein Arbeitsblatt. |
| Quelldaten für einen Cache geändert | `pivotTable.PivotCache.Refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem geteilten Cache. |
| Nur Ansichts-/Layout-Einstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Quell-Round-Trip. |
| Alle Pivot-Tabellen auf einem geteilten Cache auflisten | `pivotCache.GetPivotTables()` | Zum Auflisten vor einer Massenaktualisierung verwenden. |

In der Praxis bevorzugen Sie die cache-basierten APIs gegenüber der veralteten `RefreshData()` pro Tabelle. Sie kennen geteilte Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

{{< app/cells/assistant language="javascript" >}}