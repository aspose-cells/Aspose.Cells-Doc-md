---
title: Pivot-Tabellen in Aspose.Cells for Java aktualisieren
linktitle: Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Java mithilfe der Pivot-Refresh-API ab v26.7+ aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Java, Pivot-Tabelle, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stellt eine mehrschichtige Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Bereichen neu laden können — von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Java v26.7** ist die alte Methode `PivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren, cache-fähigen APIs ersetzt werden, die in diesem Artikel beschrieben werden.

{{% /alert %}}

## Einführung

Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den angezeigten Werten im Arbeitsblatt verbindet. Diese Kette zu verstehen ist der Schlüssel zur Wahl der richtigen Aktualisierungs-API für jede Situation.

Die vierschichtige Datenkette ist:

1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle baut auf einem `PivotCache` auf; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Werte- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Formatierungen rendert.

Ein besonders wichtiges Konzept ist der **geteilte Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert jede abhängige `PivotTable` auf einmal.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (Enum `PivotTableSourceType`) zeigt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quellentypen **`Sheet`** und **`Consolidation`** — also Daten, die in Arbeitsblattbereichen liegen. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.

{{% /alert %}}

Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:

- **`PivotCache.refresh()`** — lädt Quelle → Cache neu UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.calculateData()`** — berechnet die Anzeige einer einzelnen `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Round-Trip zur Datenquelle.

Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, daher ist der Quellentyp `Sheet`, und die Aktualisierungsvorgänge verhalten sich wie beschrieben.

## Erforderliche Import-Anweisungen

Alle Java-Beispiele in diesem Artikel beginnen mit den folgenden Import-Anweisungen, da die Pivot-Typen im Paket `com.aspose.cells.pivot` liegen:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren

Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refreshAll()`. Ein einzelner Aufruf durchläuft die gesamte Arbeitsmappe — er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet anschließend jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, dokumentweite Aktualisierungen, bei denen die Leistung keine Rolle spielt.

Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, legt eine Pivot-Tabelle an, ändert einige Quellwerte und verwendet dann `refreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```java
import com.aspose.cells.*;

// Eine neue Arbeitsmappe erstellen
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Kopfzeile in die Zellen A1:C1 schreiben
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Obst-Daten über 2020 und 2021)
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

// Alle Pivot-Tabellen / Pivot-Caches in der Arbeitsmappe aktualisieren
workbook.refreshAll();

// Die Arbeitsmappe speichern
workbook.save("output.xlsx");
```

## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren

Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — beispielsweise, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht in Beziehung stehen und nicht verändert werden sollen. Für diesen Fall stellt Aspose.Cells `Worksheet.refreshPivotTables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

Dies ist selektiver als `Workbook.refreshAll()`: Es werden nur die Pivot-Tabellen auf dem Zielarbeitsblatt aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.

Das folgende Beispiel füllt die gleichen Fruit/Year/Amount-Quelldaten, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.

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

## Eine einzelne Pivot-Tabelle aktualisieren

Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.

### Quelldaten geändert — Verwenden Sie `PivotCache.refresh()`

Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.getPivotCache().refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet anschließend jede `PivotTable` neu, die von diesem Cache abhängt.

{{% alert color="primary" %}}

Da Pivot-Tabellen eine einzelne `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufbauen — nicht nur die, die Sie referenzieren. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.

{{% /alert %}}

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten des geteilten Caches zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.

```java
import com.aspose.cells.*;

// Eine neue Arbeitsmappe erstellen und auf das erste Arbeitsblatt zugreifen
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Kopfzeile schreiben: Frucht / Jahr / Betrag
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Ungefähr 9 Datenzeilen schreiben (Traube / Blaubeere / Kiwi / Kirsche über 2020-2021)
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

// Die erste Pivot-Tabelle "Pivot1" hinzufügen, verankert bei Zelle E3, Quellbereich A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Felder für Pivot1 zuweisen
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// Eine ZWEITE Pivot-Tabelle "Pivot2" hinzufügen, verankert bei E15, mit demselben Quellbereich A1:C9
// Sowohl Pivot1 als auch Pivot2 teilen sich einen einzigen PivotCache, da der Quellbereich identisch ist.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Dieselben Felder für Pivot2 zuweisen
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// Mehrere Betragszellenwerte in den Quelldaten ändern, um eine Datenänderung zu simulieren
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Den gemeinsam genutzten PivotCache aktualisieren.
// Da Pivot1 und Pivot2 denselben PivotCache gemeinsam nutzen, aktualisiert dieser eine Aufruf
// BEIDE Pivot-Tabellen (Daten + Stil) aus der aktualisierten Quelle.
pivotTable1.refreshData();

// Die Arbeitsmappe speichern
workbook.save("output.xlsx");
```

### Nur Ansicht/Layout geändert — Verwenden Sie `calculateData()`

Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle (zum Beispiel wurde ein Feld in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet), ist kein Round-Trip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.

Dies vermeidet den unnötigen Quellabruf und ist erheblich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.

Das folgende Beispiel ändert eine Nicht-Quelle-Eigenschaft der Pivot-Tabelle und ruft dann `calculateData()` auf, um sie aus dem bestehenden Cache neu zu rendern.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Schreibt die Kopfzeile mit Fruit / Year / Amount
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

// Fügt eine Pivot-Tabelle namens "Pivot1" hinzu, platziert in der Zielzelle E3, mit Quelle A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Weist Felder zu: Fruit zur Zeile, Year zur Spalte, Amount zu den Daten
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Ändert eine Anzeige-/Layout-Eigenschaft -- dies ist eine reine Darstellungsänderung,
// daher ist kein erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) aus den
// bereits im PivotCache gespeicherten Daten neu. Da sich die Quelldaten nicht geändert haben,
// wird kein Roundtrip zur Quelle durchgeführt -- nur die zwischengespeicherten Werte werden neu berechnet
// in Arbeitsblatt-Zellen.
pivotTable.calculateData();

// Speichert die Arbeitsmappe auf der Festplatte
workbook.save("output.xlsx");
```

## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen

Eine Arbeitsmappe enthält häufig viele Pivot-Tabellen, die alle auf einem einzigen geteilten Cache sitzen. Um sie aufzulisten — beispielsweise vor einer Sammelaktualisierung oder zur Diagnose der Auswirkungen des geteilten Caches — verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Sammlung aller `PivotTable`s zurück, die von dem angegebenen Cache abhängen.

Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen (mit dem `==`-Operator) oder einfach die von `getPivotTables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin erscheinen.

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und durchläuft dann die Pivot-Tabellen des Caches.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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

int pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

boolean sameCache = pivotTable1.getPivotCache() == pivotTable2.getPivotCache();
System.out.println("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
System.out.println("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (PivotTable pt : sharedPivotTables)
{
    System.out.println("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migration von der veralteten Methode `PivotTable.refreshData()`

Vor Aspose.Cells for Java v26.7 war die übliche Methode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.refreshData()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-fähigen APIs ersetzt werden.

Es gibt zwei Gründe, warum der Ansatz mit `refreshData()` pro Tabelle in realen Arbeitsmappen problematisch ist:

- Er ruft die Daten bei jedem Aufruf erneut aus der Quelle ab, auch wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten geteilten Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt der wiederholte Aufruf von `refreshData()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder neu abgerufen wird, was sehr langsam ist.

Die empfohlenen Ersetzungen sind:

- **Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren** → verwenden Sie `workbook.refreshAll();`
- **Einige davon aktualisieren** → verwenden Sie `pivotTable.getPivotCache().refresh();` für einen Cache. Da der Cache geteilt wird, aktualisiert dieser einzelne Aufruf jede Pivot-Tabelle, die auf diesem Cache aufbaut. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können gefahrlos übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivotTable.calculateData();`, um aus dem bestehenden Cache neu zu rendern, ohne einen Quell-Round-Trip.

Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die sich einen einzigen Cache teilen.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

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

// --- Erste Pivot-Tabelle (Pivot1) in Zielzelle E3 hinzufügen ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- ZWEITE Pivot-Tabelle (Pivot2) auf demselben Quellbereich hinzufügen ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Mehrere Betragswerte in den Quelldaten ändern ---
sheet.getCells().get("C2").putValue(5000);   // Traube 2020
sheet.getCells().get("C5").putValue(7500);   // Kirsche 2020
sheet.getCells().get("C9").putValue(9500);   // Kirsche 2021

// --- NEUES Muster v26.7+: Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
pivotTable1.getPivotCache().refresh();

// Ansicht/Layout der zweiten Pivot-Tabelle neu rendern, ohne die Quelle zu verändern
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Welche Aktualisierungs-API sollte ich verwenden?

Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann welche zu wählen ist.

| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem geteilten Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.calculateData()` | Überspringt unnötigen Quell-Round-Trip. |
| Alle Pivot-Tabellen auf einem geteilten Cache auflisten | `pivotCache.getPivotTables()` | Zur Auflistung vor der Sammelaktualisierung verwenden. |

In der Praxis sind die cache-basierten APIs dem veralteten `refreshData()` pro Tabelle vorzuziehen. Sie kennen geteilte Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Bereich zu wählen, der Ihre Aktualisierungsanforderungen erfüllt.

{{< app/cells/assistant language="java" >}}