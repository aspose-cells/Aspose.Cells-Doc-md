---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for Node.js via Java
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Node.js via Java mit der v26.7+ Pivot-Refresh-API aktualisieren können. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables anhand praktischer Codebeispiele.
keywords: Aspose.Cells, Node.js, Java, Pivot-Tabelle, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells bietet eine mehrschichtige Aktualisierungs-API, mit der Sie Pivot-Daten in vier verschiedenen Bereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Aspose.Cells for Node.js via Java v26.7** ist die Legacy-Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.

{{% /alert %}}

## Einführung

Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.

Die vierschichtige Datenkette ist:

1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte leben.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

Ein besonders wichtiges Konzept ist der **gemeinsam genutzte Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert sofort jede abhängige `PivotTable`.

{{% alert color="primary" %}}

`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.

{{% /alert %}}

Aufgrund dieser Kette gibt es zwei grundlegende Aktualisierungspfade in Aspose.Cells:

- **`PivotCache.Refresh()`** — lädt Quelle → Cache neu UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.CalculateData()`** — berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne einen Round-Trip zur Datenquelle.

Alle Szenarien in diesem Artikel verwenden Arbeitsblattzellen als Quelldaten, sodass der Quelltyp `Sheet` ist und sich die Aktualisierungsvorgänge wie beschrieben verhalten.

## Erforderliche Importe

Alle JavaScript-Beispiele in diesem Artikel benötigen das Aspose.Cells for Node.js via Java-Modul. Die Pivot-Typen befinden sich im Namespace `Aspose.Cells.Pivot`, der Teil desselben Moduls ist:

- `const aspose = require('aspose.cells');`
- Oder für bestimmte Importe: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren

Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einzelner Aufruf durchläuft die gesamte Arbeitsmappe – er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, vollständige Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.

Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```javascript
const AsposeCells = require("aspose.cells");

// Eine neue Arbeitsmappe erstellen
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Kopfzeile in die Zellen A1:C1 schreiben
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Obstdaten für 2020 und 2021)
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

// Eine Pivot-Tabelle hinzufügen: Quellbereich "A1:C9", Zielzelle "E3", Name "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot-Felder zuweisen: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Mehrere Amount-Werte in den Quelldaten ändern, um Änderungen zu simulieren
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Alle Pivot-Tabellen / Pivot-Caches in der Arbeitsmappe aktualisieren
workbook.refreshAll();

// Die Arbeitsmappe speichern
workbook.save("output.xlsx");
```

## Alle Pivot-Tabellen in einem einzelnen Arbeitsblatt aktualisieren

Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – zum Beispiel, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht verwandt sind und nicht angefasst werden sollten. Für diesen Fall bietet Aspose.Cells `Worksheet.RefreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

Dies ist selektiver als `Workbook.RefreshAll()`: Nur die Pivot-Tabellen auf dem Zielarbeitsblatt werden aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.

Das folgende Beispiel füllt die gleichen Fruit/Year/Amount-Quelldaten, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.

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

Wenn Sie eine feinkörnige Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrundeliegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.

### Quelldaten geändert — Verwenden Sie `PivotCache.Refresh()`

Wenn sich die zugrundeliegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.PivotCache.Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

{{% alert color="primary" %}}

Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.Refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufgebaut sind – nicht nur die, auf die Sie verweisen. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.

{{% /alert %}}

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten des gemeinsam genutzten Caches zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.

```javascript
const AsposeCells = require("aspose.cells");

// Erstellen Sie eine neue Arbeitsmappe und greifen Sie auf das erste Arbeitsblatt zu
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Schreiben Sie die Kopfzeile: Frucht / Jahr / Betrag
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Schreiben Sie ungefähr 9 Datenzeilen (Traube / Blaubeere / Kiwi / Kirsche über 2020-2021)
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

// Fügen Sie die erste Pivot-Tabelle "Pivot1" hinzu, verankert an Zelle E3, Quellbereich A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Felder für Pivot1 zuweisen
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Fügen Sie eine ZWEITE Pivot-Tabelle "Pivot2" hinzu, verankert an E15, unter Verwendung des GLEICHEN Quellbereichs A1:C9
// Sowohl Pivot1 als auch Pivot2 teilen sich einen einzigen PivotCache, da der Quellbereich identisch ist.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Weisen Sie die gleichen Felder für Pivot2 zu
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Ändern Sie mehrere Betragszellenwerte in den Quelldaten, um eine Datenänderung zu simulieren
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Aktualisieren Sie den gemeinsam genutzten PivotCache.
// Da Pivot1 und Pivot2 denselben PivotCache teilen, aktualisiert dieser einzelne Aufruf BEIDE Pivot-Tabellen (Daten + Stil) aus der aktualisierten Quelle.
pivotTable1.getPivotCache().refresh();

// Speichern Sie die Arbeitsmappe
workbook.save("output.xlsx");
```

### Nur Ansicht/Layout geändert — Verwenden Sie `CalculateData()`

Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (z. B. wurde ein Feld in einen anderen Bereich verschoben oder eine Beim-Öffnen-aktualisieren-Einstellung umgeschaltet), ist kein Round-Trip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.

Dies vermeidet den unnötigen Quellabruf und ist deutlich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.

Das folgende Beispiel ändert eine Nicht-Quell-Eigenschaft der Pivot-Tabelle und ruft dann `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Kopfzeile Fruit / Year / Amount schreiben
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

// Eine Pivot-Tabelle namens "Pivot1" an der Zielzelle E3 hinzufügen, mit Quelle A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Felder zuweisen: Fruit zur Zeile, Year zur Spalte, Amount zu den Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Eine Ansichts-/Layout-Eigenschaft ändern — dies ist eine reine Darstellungsänderung,
// daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu,
// ausgehend von den bereits im PivotCache gehaltenen Daten. Da sich die Quelldaten
// nicht geändert haben, erfolgt kein Roundtrip zur Quelle — nur die zwischengespeicherten
// Werte werden in die Arbeitsblattzellen neu berechnet.
pivotTable.calculateData();

// Arbeitsmappe auf der Festplatte speichern
workbook.save("output.xlsx");
```

## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache aufbauen. Um sie aufzulisten – z. B. vor einer Stapelaktualisierung oder zur Diagnose der Auswirkungen des gemeinsam genutzten Caches – verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.

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
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

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

Vor Aspose.Cells for Aspose.Cells for Node.js via Java v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.RefreshData()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.

Es gibt zwei Gründe, warum der `RefreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:

- Es ruft Daten *jedes Mal* aus der Quelle erneut ab, wenn es aufgerufen wird, auch wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten gemeinsam genutzten Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt der wiederholte Aufruf von `RefreshData()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder neu abgerufen wird, was sehr langsam ist.

Die empfohlenen Ersetzungen sind:

- **ALLE Pivot-Tabellen in der Arbeitsmappe aktualisieren** → verwenden Sie `workbook.refreshAll();`
- **Einige davon aktualisieren** → verwenden Sie `pivotTable.getPivotCache().refresh();` für einen Cache. Da der Cache gemeinsam genutzt wird, aktualisiert dieser einzelne Aufruf jede Pivot-Tabelle, die auf diesem Cache aufbaut. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivotTable.calculateData();`, um aus dem vorhandenen Cache neu zu rendern, ohne einen Quell-Round-Trip.

Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Quellendaten aufbauen: Frucht / Jahr / Betrag (Kopfzeile + 9 Zeilen) ---
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

// --- Erste Pivot-Tabelle (Pivot1) an Zielzelle E3 hinzufügen ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- ZWEITE Pivot-Tabelle (Pivot2) am GLEICHEN Quellbereich hinzufügen ---
// Sowohl Pivot1 als auch Pivot2 teilen sich EINEN zugrundeliegenden PivotCache.
// Dies ist genau das Szenario, in dem der Legacy-Ansatz pro Tabelle RefreshData()
// ineffizient wird: Das Aktualisieren einer Tabelle ruft den gesamten
// gemeinsam genutzten Cache erneut ab, sodass N Tabellen N unnötige Abrufe verursachen.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Mehrere Betragswerte in den Quelldaten ändern ---
sheet.getCells().get("C2").putValue(5000);   // Traube 2020
sheet.getCells().get("C5").putValue(7500);   // Kirsche 2020
sheet.getCells().get("C9").putValue(9500);   // Kirsche 2021

// --- VERALTETES Muster (vor 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // ruft erneut von der Quelle ab, aktualisiert den gesamten Cache
// pivotTable2.refreshData();  // ruft ERNEUT ab — der Cache ist bereits frisch!
// Jeder Aufruf baut den gemeinsamen Cache neu auf, also N Tabellen = N redundante Abrufe.

// --- NEUES Muster ab v26.7: Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
// Ein einziger Aufruf von PivotCache.Refresh() holt die geänderten Werte in den gemeinsamen
// Cache UND berechnet die Anzeige JEDER Pivot-Tabelle neu, die darauf verweist.
// Da Pivot1 und Pivot2 einen PivotCache gemeinsam nutzen, aktualisiert dieser
// einzelne Aufruf beide Tabellen — kein zweiter Quellzugriff ist erforderlich.
pivotTable1.getPivotCache().refresh();

// CalculateData() rendert nur die Anzeige einer Pivot-Tabelle neu (Daten + Stil)
// aus den bereits im Cache enthaltenen Daten — es greift NICHT auf die Quelle zu.
// Wir rufen es hier nur auf, um die API zu demonstrieren: nachdem der Cache
// einmal aktualisiert wurde, kann jede abhängige Tabelle neu gerendert werden,
// ohne auf die Quelle zurückzugreifen. Verwenden Sie CalculateData() eigenständig,
// wenn sich nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle geändert haben und der Cache aktuell ist.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Welche Aktualisierungs-API sollte ich verwenden?

Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann welche zu wählen ist.

| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.RefreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.PivotCache.Refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsam genutzten Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Quell-Round-Trip. |
| Alle Pivot-Tabellen auf einem gemeinsam genutzten Cache auflisten | `pivotCache.GetPivotTables()` | Vor einer Massenaktualisierung zum Aufzählen verwenden. |

In der Praxis bevorzugen Sie die cache-basierten APIs gegenüber der veralteten `RefreshData()` pro Tabelle. Sie kennen gemeinsam genutzte Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Bereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

{{< app/cells/assistant language="javascript" >}}