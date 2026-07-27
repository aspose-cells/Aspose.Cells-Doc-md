---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for Node.js via C++
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Node.js via C++ mithilfe der Pivot-Refresh-API ab v26.7+ aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Node.js via C++, Pivot-Tabelle, Aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells stellt eine abgestufte Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen PivotTable. Ab **Aspose.Cells for Node.js via C++ v26.7** ist die Legacy-Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}
## Einführung
Das Aktualisieren einer PivotTable ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine abgestufte Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Diese Kette zu verstehen, ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, die Datenbankabfrage oder der Konsolidierungsbereich, in dem die Rohwerte gespeichert sind.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede PivotTable wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Anzeigeobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *ausschließlich* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Zellen** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.
Ein besonders wichtiges Konzept ist der **freigegebene Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert jede abhängige `PivotTable` auf einmal.
{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotCache.Refresh()`** — lädt Quelle → Cache neu UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.CalculateData()`** — berechnet die Anzeige einer einzigen `PivotTable` aus bereits im Cache befindlichen Daten neu, ohne Round-Trip zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblattzellen als Quelldaten, sodass der Quelltyp `Sheet` ist und die Aktualisierungsvorgänge wie beschrieben funktionieren.
## Erforderliche Importe
Alle JavaScript-Beispiele in diesem Artikel gehen davon aus, dass das Modul Aspose.Cells for Node.js via C++ geladen wurde und sich die Pivot-Typen im Namespace `Aspose.Cells.Pivot` befinden. Eine typische Einrichtung ist:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (oder Zugriff über `AsposeCells.Pivot.PivotFieldType`)
## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet anschließend jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, vollständige Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, erstellt eine PivotTable, ändert einige Quellwerte und verwendet anschließend `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Schreibe die Kopfzeile in die Zellen A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Schreibe Datenzeilen in die Zellen A2:C9 (8 Zeilen mit Obst-Daten für 2020 und 2021)
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

// Weise die Pivot-Felder zu: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
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
## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – beispielsweise, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht verwandt sind und nicht angefasst werden sollten. Für diesen Fall stellt Aspose.Cells `Worksheet.RefreshPivotTables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.
Dies ist selektiver als `Workbook.RefreshAll()`: nur die Pivot-Tabellen auf dem Zielarbeitsblatt werden aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.
Das folgende Beispiel füllt dieselben Fruit/Year/Amount-Quelldaten, fügt eine PivotTable auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert anschließend nur die Pivot-Tabellen auf diesem Arbeitsblatt.
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
## Eine einzelne PivotTable aktualisieren
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne PivotTable wünschen, bietet Ihnen die cache-basierte API zwei Möglichkeiten. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Anzeige-/Layouteinstellungen der PivotTable selbst.
### Quelldaten geändert — Verwenden Sie `PivotCache.Refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.PivotCache.Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache und berechnet anschließend jede `PivotTable` neu, die von diesem Cache abhängt.
{{% alert color="primary" %}}
Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.Refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufgebaut sind – nicht nur diejenige, die Sie referenzieren. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.
{{% /alert %}}
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten mit freigegebenem Cache zu demonstrieren, ändert einige Quellwerte und aktualisiert anschließend über eine Cache-Referenz.
```javascript
const AsposeCells = require("aspose.cells");

// Erstelle eine neue Arbeitsmappe und greife auf das erste Arbeitsblatt zu
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Schreibe die Kopfzeile: Frucht / Jahr / Betrag
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

// Füge eine ZWEITE Pivot-Tabelle "Pivot2" hinzu, verankert an E15, unter Verwendung desselben Quellbereichs A1:C9
// Sowohl Pivot1 als auch Pivot2 teilen sich einen einzelnen PivotCache, da der Quellbereich identisch ist.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Weise dieselben Felder für Pivot2 zu
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Ändere mehrere Betragszellenwerte in den Quelldaten, um eine Datenänderung zu simulieren
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
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Anzeige- oder Layouteinstellungen der PivotTable geändert wurden (zum Beispiel wurde ein Feld in einen anderen Bereich verschoben oder eine Einstellung „Beim Öffnen aktualisieren" umgeschaltet), ist es nicht erforderlich, einen Round-Trip zur Datenquelle durchzuführen. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.
Dies vermeidet den unnötigen Quellabruf und ist deutlich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.
Das folgende Beispiel ändert eine Nicht-Quelleigenschaft der PivotTable und ruft anschließend `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.
```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Schreibt die Kopfzeile Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Schreibt 8 Datenzeilen (Zeilen 2-9, passend zum Quellbereich A1:C9)
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

// Fügt eine Pivot-Tabelle namens "Pivot1" an der Zielzelle E3 hinzu, mit Quelle A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Weist die Felder zu: Fruit als Zeile, Year als Spalte, Amount als Daten
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// Ändert eine Anzeige-/Layout-Eigenschaft — dies ist eine reine Darstellungsänderung,
// daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu aus den
// bereits im PivotCache enthaltenen Daten. Da sich die Quelldaten nicht geändert haben,
// erfolgt kein Roundtrip zur Quelle — nur die zwischengespeicherten Werte werden in die
// Arbeitsblattzellen neu berechnet.
pivotTable.calculateData();

// Speichert die Arbeitsmappe auf der Festplatte
workbook.save("output.xlsx");
```
## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen
Eine Arbeitsmappe enthält häufig viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache aufbauen. Um sie aufzulisten – beispielsweise vor der Durchführung einer Batch-Aktualisierung oder um die Auswirkungen des freigegebenen Caches zu diagnostizieren – verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.
Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen oder einfach die von `GetPivotTables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin erscheinen.
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und listet anschließend die Pivot-Tabellen des Caches auf.
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
## Migration von der veralteten Methode `PivotTable.RefreshData()`
Vor Aspose.Cells for Node.js via C++ v26.7 bestand die Standardmethode zum Aktualisieren einer Pivot-Tabelle darin, `PivotTable.RefreshData()` für jede PivotTable einzeln aufzurufen. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der `RefreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft bei jedem Aufruf Daten erneut aus der Quelle ab, selbst wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten gemeinsam genutzten Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt der wiederholte Aufruf von `RefreshData()` pro PivotTable dazu, dass derselbe Cache immer wieder erneut abgerufen wird, was sehr langsam ist.
Die empfohlenen Ersetzungen sind:
- **ALLE Pivot-Tabellen in der Arbeitsmappe aktualisieren** → verwenden Sie `workbook.refreshAll();`
- **Einige davon aktualisieren** → verwenden Sie `pivotTable.PivotCache.Refresh();` für einen Cache. Da der Cache freigegeben ist, aktualisiert dieser einzige Aufruf jede PivotTable, die auf diesem Cache aufbaut. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Ansicht/das Layout der PivotTable hat sich geändert** → verwenden Sie `pivotTable.CalculateData();` um aus dem vorhandenen Cache ohne Round-Trip zur Quelle neu zu rendern.
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die sich einen einzigen Cache teilen.
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

// --- Die erste Pivot-Tabelle (Pivot1) an der Zielzelle E3 hinzufügen ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Die ZWEITE Pivot-Tabelle (Pivot2) auf demselben Quellbereich hinzufügen ---
// Sowohl Pivot1 als auch Pivot2 teilen sich EINEN zugrundeliegenden PivotCache.
// Genau dies ist das Szenario, in dem der alte RefreshData()-Ansatz pro
// Tabelle ineffizient wird: Das Aktualisieren einer Tabelle ruft den gesamten
// gemeinsamen Cache erneut ab, sodass N Aktualisierungen N teure Abrufe
// verursachen.
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
// pivotTable1.RefreshData();  // ruft erneut aus der Quelle ab, aktualisiert den gesamten Cache
// pivotTable2.RefreshData();  // ruft ERNEUT ab — der Cache ist bereits aktuell!
// Jeder Aufruf baut den gemeinsamen Cache neu auf, also N Tabellen = N redundante Abrufe.

// --- NEUES Muster ab v26.7: Den Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
// Ein einziger Aufruf von PivotCache.Refresh() holt die geänderten Werte in den
// gemeinsamen Cache UND berechnet die Anzeige JEDER Pivot-Tabelle neu, die darauf
// verweist. Da Pivot1 und Pivot2 einen PivotCache gemeinsam nutzen, aktualisiert
// dieser eine Aufruf beide Tabellen — kein zweiter Quell-Roundtrip ist erforderlich.
pivotTable1.getPivotCache().refresh();

// CalculateData() rendert nur die Anzeige einer Pivot-Tabelle (Daten + Stil) aus den
// bereits im Cache vorhandenen Daten neu — es greift NICHT auf die Quelle zu.
// Wir rufen es hier auf Pivot2 nur auf, um die API zu demonstrieren: Nachdem der Cache
// einmal aktualisiert wurde, kann jede abhängige Tabelle neu gerendert werden, ohne
// zur Quelle zurückzugehen. Verwenden Sie CalculateData() eigenständig, wenn nur die
// Ansichts-/Layout-Einstellungen der Pivot-Tabelle geändert wurden und der Cache aktuell ist.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und gibt an, wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.RefreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.PivotCache.Refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem freigegebenen Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Round-Trip zur Quelle. |
| Alle Pivot-Tabellen auf einem freigegebenen Cache auflisten | `pivotCache.GetPivotTables()` | Vor der Massenaktualisierung zur Aufzählung verwenden. |
In der Praxis sind die cache-basierten APIs der veralteten Methode `RefreshData()` pro Tabelle vorzuziehen. Sie kennen freigegebene Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.
## Verwandte Artikel
- [Einfügen eines Bildes in eine Zelle](/cells/de/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/nodejs-cpp/dbf/)
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Sparklines in Aspose.Cells for Node.js via C++](/cells/de/nodejs-cpp/sparkline/)
{{< app/cells/assistant language="javascript" >}}