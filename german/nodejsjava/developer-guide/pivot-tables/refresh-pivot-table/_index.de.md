---
title: Pivot-Tabellen und Pivot-Caches in Aspose.Cells for Node.js via Java aktualisieren
linktitle: Pivot-Tabellen und Pivot-Caches
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Node.js via Java mit der Pivot-Refresh-API v26.7+ aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Node.js, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt eine mehrschichtige Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier unterschiedlichen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Node.js via Java v26.7** ist die ältere Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## **Einführung**
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den angezeigten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** – die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** – der speicherinterne Schnappschuss der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** – das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** – die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}

Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.CalculateData()`** – berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Roundtrip zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblattzellen als Quelldaten, daher ist der Quelltyp `Sheet` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.

## **Schnellstart**
Wenn Sie nur den kürzestmöglichen Code benötigen, der jede Pivot-Tabelle in der Arbeitsmappe aktualisiert, reicht ein einziger Aufruf:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Der gesamte Rest dieses Artikels erklärt, wann Sie stattdessen eine enger gefasste API wählen sollten.

## **Erforderliche Importe**
- `const aspose = require('aspose.cells');`
- Oder für bestimmte Importe: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## **Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren**
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die aktuellsten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet anschließend jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, dokumentweite Aktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich Obst/Jahr/Betrag, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet anschließend `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```javascript
const AsposeCells = require("aspose.cells");
// Eine neue Arbeitsmappe erstellen
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
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

## **Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren**
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – beispielsweise wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht zusammenhängen und nicht angefasst werden sollen. Für diesen Fall bietet Aspose.Cells `Worksheet.RefreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

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

## **Eine einzelne Pivot-Tabelle aktualisieren**
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts- bzw. Layouteinstellungen der Pivot-Tabelle selbst.

### **Quelldaten geändert – Verwenden Sie `PivotCache.Refresh()`**
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.PivotCache.Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet anschließend jede `PivotTable` neu, die von diesem Cache abhängt.

### **Nur Ansicht/Layout geändert – Verwenden Sie `CalculateData()`**
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben oder eine Beim-Öffnen-aktualisieren-Einstellung umgeschaltet wurde), ist kein Roundtrip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine Nicht-Quell-Eigenschaft der Pivot-Tabelle und ruft anschließend `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Schreibe die Kopfzeile Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Schreibe 8 Datenzeilen (Zeilen 2-9, passend zum Quellbereich A1:C9)
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
// Füge eine Pivot-Tabelle mit dem Namen "Pivot1" hinzu, platziert in der Zielzelle E3, mit Quelle A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Felder zuweisen: Fruit zu Zeile, Year zu Spalte, Amount zu Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Eine Ansichts-/Layout-Eigenschaft ändern – dies ist eine reine Präsentationsänderung,
// daher ist kein erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu aus den
// Daten, die bereits im PivotCache gehalten werden. Da sich die Quelldaten nicht geändert haben,
// erfolgt kein Roundtrip zur Quelle – nur die zwischengespeicherten Werte werden neu berechnet
// in die Arbeitsblatt-Zellen.
pivotTable.calculateData();
// Speichere die Arbeitsmappe auf der Festplatte
workbook.save("output.xlsx");
```

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache basieren. Um sie aufzulisten – beispielsweise vor einer Stapelaktualisierung oder um die Auswirkungen des gemeinsamen Caches zu diagnostizieren – verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die vom angegebenen Cache abhängt.

## **Migration von der veralteten Methode `PivotTable.RefreshData()`**
Vor Aspose.Cells for Node.js via Java v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.RefreshData()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der `RefreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:
- Es ruft die Daten *bei jedem* Aufruf aus der Quelle erneut ab, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersatzlösungen sind:
Das folgende Beispiel zeigt das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.

## **Welche Aktualisierungs-API sollte ich verwenden?**
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Gesamte Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.RefreshPivotTables()` | Beschränkt auf ein Arbeitsblatt. |
| Quelldaten für einen Cache geändert | `pivotTable.PivotCache.Refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsamen Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Quell-Roundtrip. |
| Alle Pivot-Tabellen auf einem gemeinsamen Cache auflisten | `pivotCache.GetPivotTables()` | Vor Stapelaktualisierung zur Aufzählung verwenden. |
In der Praxis sollten die cache-basierten APIs dem veralteten `RefreshData()` pro Tabelle vorgezogen werden. Sie kennen gemeinsame Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## **Häufige Fallstricke**
- **Vergessen, vor dem Speichern zu aktualisieren.** Eine Pivot-Tabelle schreibt ihre gerenderten Werte nur dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.Refresh()` (oder `Workbook.RefreshAll()`) vor `Workbook.save()` auf, sonst enthält die gespeicherte Datei weiterhin die alten aggregierten Werte.
- **Aufruf der veralteten `RefreshData()` pro Tabelle.** In v26.7 ist `PivotTable.RefreshData()` als veraltet markiert und ruft bei jedem Aufruf die Quelle erneut ab. Bei mehreren Pivot-Tabellen, die einen Cache gemeinsam nutzen, bedeutet dies N redundante Quellabrufe. Ersetzen Sie dies durch einen einzigen `PivotCache.Refresh()`, gefolgt von `CalculateData()` pro Tabelle.
- **Aktualisierung, wenn nur das Layout geändert wurde.** Wenn Sie nur die Ansicht einer Pivot-Tabelle geändert haben (Spaltenreihenfolge, `ConsolidationFunction` usw.), ohne die Quelldaten zu berühren, ist `PivotCache.Refresh()` unnötig und langsam. Rufen Sie `pivotTable.CalculateData()` auf, um aus dem vorhandenen Cache neu zu rendern.
- **Externe Quelle wird von `PivotCache.Refresh()` nicht unterstützt.** Wenn die Quelle der Pivot-Tabelle aus einer externen Verbindung stammt (Datenbank, OLAP-Cube usw.), kann `PivotCache.Refresh()` sie in v26.7 nicht aktualisieren – es unterstützt derzeit nur die Quelltypen `Sheet` und `Consolidation`. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder erstellen Sie den Cache aus der Quelle neu.

{{< app/cells/assistant language="nodejs-java" >}}