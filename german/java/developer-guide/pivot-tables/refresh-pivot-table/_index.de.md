---
title: Pivot-Tabellen in Aspose.Cells for Java aktualisieren
linktitle: Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Java mit der Pivot-Refresh-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables anhand praktischer Codebeispiele.
keywords: Aspose.Cells, Java, Pivot-Tabelle, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet eine mehrschichtige Aktualisierungs-API, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Java v26.7** ist die alte Methode `PivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}
## Einführung
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** – die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** – der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** – das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Zellen** – die Arbeitsblatt-`Cells`, in die die `PivotTable` ihre berechneten Werte und Stile rendert.
Ein besonders wichtiges Konzept ist der **gemeinsame Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Auf einen einzelnen `PivotCache` kann von vielen Pivot-Tabellen verwiesen werden, und das Aktualisieren dieses Caches aktualisiert alle abhängigen `PivotTable`s auf einmal.
{{% alert color="primary" %}}
`PivotCache.getSourceType()` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen liegen. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotCache.refresh()`** – lädt Quelle → Cache neu UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.calculateData()`** – berechnet die Anzeige einer einzelnen `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Round-Trip zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, daher ist der Quelltyp `Sheet` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
## Erforderliche Import-Anweisungen
Alle Java-Beispiele in diesem Artikel beginnen mit den folgenden Import-Anweisungen, da die Pivot-Typen im Paket `com.aspose.cells.pivot` liegen:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`
## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refreshAll()`. Ein einzelner Aufruf durchläuft die gesamte Arbeitsmappe – er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, vollständige Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.
```java
import java.lang.System;
import com.aspose.cells.Workbook;
import com.aspose.cells.pivot.*;

// Eine neue Arbeitsmappe erstellen
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Kopfzeile in die Zellen A1:C1 schreiben
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Fruchtdaten für 2020 und 2021)
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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot-Felder zuweisen: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Mehrere Amount-Werte in den Quelldaten ändern, um Änderungen zu simulieren
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Jede Pivot-Tabelle / jeden Pivot-Cache in der Arbeitsmappe aktualisieren
workbook.refreshAll();

// Die Arbeitsmappe speichern
workbook.save("output.xlsx");
```
## Alle Pivot-Tabellen in einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – zum Beispiel, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht relevant sind und nicht angefasst werden sollen. Für diesen Fall bietet Aspose.Cells `Worksheet.refreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.
Dies ist selektiver als `Workbook.refreshAll()`: Es werden nur die Pivot-Tabellen auf dem Zielarbeitsblatt aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.
Das folgende Beispiel füllt die gleichen Fruit/Year/Amount-Quelldaten, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.
```java
import java.lang.System;
import com.aspose.cells.Workbook;
import com.aspose.cells.pivot.*;

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
## Eine einzelne Pivot-Tabelle aktualisieren
Wenn Sie eine feinkörnige Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.
### Quelldaten geändert – Verwenden Sie `PivotCache.refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.getPivotCache().refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.
{{% alert color="primary" %}}
Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufgebaut sind – nicht nur die, auf die Sie verweisen. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.
{{% /alert %}}
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten mit gemeinsamem Cache zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.
```java
import java.lang.System;
import com.aspose.cells.Workbook;
import com.aspose.cells.pivot.*;

// Erstellen Sie eine neue Arbeitsmappe und greifen Sie auf das erste Arbeitsblatt zu
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Schreiben Sie die Kopfzeile: Frucht / Jahr / Betrag
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Schreiben Sie ungefähr 9 Datenzeilen (Traube / Blaubeere / Kiwi / Kirsche über 2020-2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Fügen Sie die erste Pivot-Tabelle "Pivot1" hinzu, verankert bei Zelle E3, Quellbereich A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Felder für Pivot1 zuweisen
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// Fügen Sie eine ZWEITE Pivot-Tabelle "Pivot2" hinzu, verankert bei E15, mit demselben Quellbereich A1:C9
// Sowohl Pivot1 als auch Pivot2 teilen sich einen einzelnen PivotCache, da der Quellbereich identisch ist.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Dieselben Felder für Pivot2 zuweisen
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// Ändern Sie mehrere Betragszellwerte in den Quelldaten, um eine Datenänderung zu simulieren
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Aktualisieren Sie den gemeinsam genutzten PivotCache.
// Da Pivot1 und Pivot2 denselben PivotCache teilen, aktualisiert dieser einzelne Aufruf
// BEIDE Pivot-Tabellen (Daten + Stil) aus der aktualisierten Quelle.
pivotTable1.getPivotCache().refresh();

// Speichern Sie die Arbeitsmappe
workbook.save("output.xlsx");
```
### Nur Ansicht/Layout geändert – Verwenden Sie `calculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet wurde), ist kein Round-Trip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Dadurch wird der unnötige Quellabruf vermieden und ist deutlich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.
Das folgende Beispiel ändert eine Eigenschaft, die nicht die Quelle betrifft, der Pivot-Tabelle und ruft dann `calculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.
```java
import java.lang.System;
import com.aspose.cells.Workbook;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Schreibt die Kopfzeile mit Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Schreibt 8 Datenzeilen (Zeilen 2-9, passend zum Quellbereich A1:C9)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);

// Fügt eine Pivot-Tabelle namens "Pivot1" hinzu, platziert in der Zielzelle E3, mit Datenquelle A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Weist Felder zu: Fruit zu Zeile, Year zu Spalte, Amount zu Daten
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Ändert eine Ansichts-/Layout-Eigenschaft -- dies ist eine reine Darstellungsänderung,
// daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu aus den
// bereits im PivotCache gespeicherten Daten. Da sich die Quelldaten nicht geändert haben,
// wird kein Roundtrip zur Quelle durchgeführt -- nur die zwischengespeicherten Werte werden
// in die Arbeitsblattzellen neu berechnet.
pivotTable.calculateData();

// Speichert die Arbeitsmappe auf der Festplatte
workbook.save("output.xlsx");
```
## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen
Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsamen Cache aufsetzen. Um sie aufzulisten – beispielsweise vor einer Batch-Aktualisierung oder um die Auswirkungen des gemeinsamen Caches zu diagnostizieren – verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem gegebenen Cache abhängt.
Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen (mit dem Operator `==`) oder einfach die von `getPivotTables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin erscheinen.
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und listet dann die Pivot-Tabellen des Caches auf.

## Migration von der veralteten Methode `PivotTable.refreshData()`
Vor Aspose.Cells for Java v26.7 bestand die Standardmethode zur Aktualisierung einer Pivot-Tabelle darin, `PivotTable.refreshData()` für jede Pivot-Tabelle einzeln aufzurufen. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der `refreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft die Daten jedes Mal aus der Quelle ab, *auch wenn sich die Quelle nicht geändert hat*.
- Jeder Aufruf aktualisiert den gesamten gemeinsamen Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt das wiederholte Aufrufen von `refreshData()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder neu abgerufen wird, was sehr langsam ist.
Die empfohlenen Ersetzungen sind:
- **Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren** → verwenden Sie `workbook.refreshAll();`
- **Einige davon aktualisieren** → verwenden Sie `pivotTable.getPivotCache().refresh();` für einen Cache. Da der Cache gemeinsam genutzt wird, aktualisiert dieser einzige Aufruf jede Pivot-Tabelle, die auf diesem Cache aufbaut. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivotTable.calculateData();`, um aus dem vorhandenen Cache neu zu rendern, ohne einen Round-Trip zur Quelle.
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzelnen Cache gemeinsam nutzen.
```java
import java.lang.System;
import com.aspose.cells.Workbook;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- Quelldaten erstellen: Fruit / Year / Amount (Kopfzeile + 9 Zeilen) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Erste Pivot-Tabelle (Pivot1) an Zielzelle E3 hinzufügen ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// --- ZWEITE Pivot-Tabelle (Pivot2) auf demselben Quellbereich hinzufügen ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// --- Mehrere Amount-Werte in den Quelldaten ändern ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- NEUES Muster ab v26.7+: Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
pivotTable1.getPivotCache().refresh();

// Ansicht/Layout der zweiten Pivot-Tabelle neu rendern, ohne die Quelle zu ändern
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und wann Sie welche wählen sollten.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen in einem einzelnen Blatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE Pivot-Tabellen in diesem gemeinsamen Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.calculateData()` | Überspringt unnötigen Round-Trip zur Quelle. |
| Alle Pivot-Tabellen in einem gemeinsamen Cache auflisten | `pivotCache.getPivotTables()` | Vor einer Massenaktualisierung verwenden. |
In der Praxis sind die cache-basierten APIs der veralteten `refreshData()` pro Tabelle vorzuziehen. Sie kennen gemeinsame Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

{{< app/cells/assistant language="java" >}}
