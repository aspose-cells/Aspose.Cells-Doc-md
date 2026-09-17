---
title: Pivot-Tabellen und Pivot-Caches in Aspose.Cells for .NET aktualisieren
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for .NET mit der Pivot-Refresh-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables anhand praktischer Codebeispiele.
linktitle: Pivot-Tabellen aktualisieren
keywords: Aspose.Cells, .NET, Pivot-Tabelle, Aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt eine mehrschichtige Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for .NET v26.7** ist die ältere Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## **Einführung**
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — die In-Memory-Momentaufnahme der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *ausschließlich* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}

Aufgrund dieser Kette gibt es zwei grundlegende Aktualisierungspfade in Aspose.Cells:
- **`PivotTable.CalculateData()`** — berechnet die Anzeige einer `PivotTable` aus bereits im Cache befindlichen Daten neu, ohne einen Roundtrip zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, sodass der Quelltyp `Sheet` ist und sich die Aktualisierungsvorgänge wie beschrieben verhalten.

## **Schnellstart**
Wenn Sie nur den kürzestmöglichen Code benötigen, der jede Pivot-Tabelle in der Arbeitsmappe aktualisiert, reicht ein einziger Aufruf:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Alles Weitere in diesem Artikel erklärt, wann stattdessen eine engere API zu wählen ist.

## **Erforderliche Using-Direktiven**
Alle C#-Beispiele in diesem Artikel beginnen mit den folgenden drei using-Direktiven, da die Pivot-Typen im Namespace `Aspose.Cells.Pivot` liegen:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## **Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren**
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die aktuellsten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – jeder `PivotCache` wird aus seiner Quelle aktualisiert und anschließend jede abhängige `PivotTable` neu berechnet. Dies ist der empfohlene Ansatz für allgemeine, dokumentweite Aktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich Fruit/Year/Amount, erzeugt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Erstellen einer neuen Arbeitsmappe
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Kopfzeile in die Zellen A1:C1 schreiben
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Obstdaten für 2020 und 2021)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);
// Pivot-Tabelle hinzufügen: Quellbereich "A1:C9", Zielzelle "E3", Name "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Pivot-Felder zuweisen: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Mehrere Amount-Werte in den Quelldaten ändern, um Änderungen zu simulieren
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// Alle Pivot-Tabellen / Pivot-Caches in der Arbeitsmappe aktualisieren
workbook.RefreshAll();
// Die Arbeitsmappe speichern
workbook.Save("output.xlsx");
```

## **Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren**
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – beispielsweise wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht in Beziehung stehen und nicht angefasst werden sollen. Für diesen Fall stellt Aspose.Cells `Worksheet.RefreshPivotTables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);
worksheet.RefreshPivotTables();
workbook.Save("output.xlsx");
```

## **Eine einzelne Pivot-Tabelle aktualisieren**
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layout-Einstellungen der Pivot-Tabelle selbst.

### **Quelldaten geändert – `PivotCache.Refresh()` verwenden**
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.PivotCache.Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache und berechnet anschließend jede `PivotTable` neu, die von diesem Cache abhängt.

### **Nur Ansicht/Layout geändert – `CalculateData()` verwenden**
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layout-Einstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben oder eine Beim-Öffnen-aktualisieren-Einstellung umgeschaltet wurde), ist kein Roundtrip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine nicht quellbezogene Eigenschaft der Pivot-Tabelle und ruft dann `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Kopfzeile mit Fruit / Year / Amount schreiben
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 8 Datenzeilen schreiben (Zeilen 2-9, passend zum Quellbereich A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);
// Eine Pivot-Tabelle namens "Pivot1" hinzufügen, platziert in der Zielzelle E3, mit Quelle A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Felder zuweisen: Fruit zu Zeile, Year zu Spalte, Amount zu Daten
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Eine Ansichts-/Layout-Eigenschaft ändern — dies ist eine reine Darstellungsänderung,
// daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) aus den
// bereits im PivotCache gespeicherten Daten neu. Da sich die Quelldaten nicht geändert haben,
// wird kein Roundtrip zur Quelle durchgeführt — nur die zwischengespeicherten Werte werden neu berechnet
// in die Arbeitsblattzellen geschrieben.
pivotTable.CalculateData();
// Arbeitsmappe auf der Festplatte speichern
workbook.Save("output.xlsx");
```

Eine Arbeitsmappe enthält häufig viele Pivot-Tabellen, die alle auf einem gemeinsamen Cache aufbauen. Um sie aufzulisten – beispielsweise vor einer Batch-Aktualisierung oder um die Auswirkungen des gemeinsamen Caches zu diagnostizieren – verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die vom angegebenen Cache abhängt.

## **Migration von der veralteten `PivotTable.RefreshData()`**
Vor Aspose.Cells for .NET v26.7 bestand die Standardmethode zum Aktualisieren einer Pivot-Tabelle darin, `PivotTable.RefreshData()` für jede Pivot-Tabelle einzeln aufzurufen. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der `RefreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft die Daten bei jedem Aufruf *erneut* aus der Quelle ab, auch wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind:
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.

## **Welche Aktualisierungs-API sollte ich verwenden?**
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und gibt an, wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren | `Worksheet.RefreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.PivotCache.Refresh()` | Aktualisiert ALLE Pivot-Tabellen in diesem gemeinsamen Cache. |
| Nur Ansichts-/Layout-Einstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Quell-Roundtrip. |
| Alle Pivot-Tabellen in einem gemeinsamen Cache auflisten | `pivotCache.GetPivotTables()` | Zum Auflisten vor der Massenaktualisierung verwenden. |
In der Praxis sind die cache-basierten APIs dem veralteten `RefreshData()` pro Tabelle vorzuziehen. Sie kennen gemeinsame Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## **Häufige Fehlerquellen**
- **Vor dem Speichern das Aktualisieren vergessen.** Eine Pivot-Tabelle schreibt ihre gerenderten Werte nur dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.Refresh()` (oder `Workbook.RefreshAll()`) vor `Workbook.Save()` auf, da die gespeicherte Datei sonst die alten aggregierten Werte enthält.
- **Aufruf der veralteten `RefreshData()` pro Tabelle.** In v26.7 ist `PivotTable.RefreshData()` als veraltet markiert und ruft die Quelle bei jedem Aufruf erneut ab. Bei mehreren Pivot-Tabellen, die einen Cache gemeinsam nutzen, bedeutet dies N redundante Quellabrufe. Ersetzen Sie dies durch einen einzigen `PivotCache.Refresh()`-Aufruf, gefolgt von `CalculateData()` pro Tabelle.
- **Aktualisieren, wenn nur das Layout geändert wurde.** Wenn Sie nur die Ansicht einer Pivot-Tabelle (Spaltenreihenfolge, `ConsolidationFunction` usw.) geändert haben, ohne Quelldaten zu berühren, ist `PivotCache.Refresh()` unnötig und langsam. Rufen Sie `pivotTable.CalculateData()` auf, um aus dem vorhandenen Cache neu zu rendern.
- **Externe Quelle nicht von `PivotCache.Refresh()` unterstützt.** Wenn die Quelle der Pivot-Tabelle aus einer externen Verbindung (Datenbank, OLAP-Cube usw.) stammt, kann `PivotCache.Refresh()` sie in v26.7 nicht aktualisieren – es werden derzeit nur die Quelltypen `Sheet` und `Consolidation` unterstützt. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder erstellen Sie den Cache aus der Quelle neu.

{{< app/cells/assistant language="csharp" >}}