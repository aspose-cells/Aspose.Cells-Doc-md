---
title: Pivot-Tabellen und Pivot-Caches in Aspose.Cells for Python via Java aktualisieren
linktitle: Pivot-Tabellen und Pivot-Caches
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Python via Java mithilfe der v26.7+ Pivot-Aktualisierungs-API aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Python via Java, Pivot-Tabelle, Aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt eine mehrschichtige Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können — von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Python via Java v26.7** ist die Legacy-Methode `PivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Einführung
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Hinter den Kulissen verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte leben.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`SHEET`** und **`CONSOLIDATION`** — also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind derzeit nicht über die Cache-API aktualisierbar.
{{% /alert %}}

Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.calculateData()`** — berechnet die Anzeige einer `PivotTable` aus den bereits zwischengespeicherten Daten neu, ohne Rückkehr zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblattzellen als Quelldaten, sodass der Quelltyp `SHEET` ist und die Aktualisierungsvorgänge wie beschrieben funktionieren.

## Schnellstart
Wenn Sie nur den kürzestmöglichen Code benötigen, der jede Pivot-Tabelle in der Arbeitsmappe aktualisiert, reicht ein einziger Aufruf:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Eine neue Arbeitsmappe erstellen
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Kopfzeile in die Zellen A1:C1 schreiben
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Fruchtdaten für 2020 und 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Eine Pivot-Tabelle hinzufügen: Quellbereich "A1:C9", Zielzelle "E3", Name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Pivot-Felder zuweisen: Frucht zu Zeilen, Jahr zu Spalten, Betrag zu Daten
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Mehrere Betragswerte in den Quelldaten ändern, um Änderungen zu simulieren
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Alle Pivot-Tabellen / Pivot-Caches in der Arbeitsmappe aktualisieren
workbook.refreshAll()
# Die Arbeitsmappe speichern
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Der gesamte Rest dieses Artikels erklärt, wann stattdessen eine eingegrenztere API zu wählen ist.

## Erforderliche Importe
Alle Python-Beispiele in diesem Artikel basieren auf den folgenden Importen, da die Pivot-Typen im Namespace `aspose.cells.pivot` leben:
- `import jpype`
- `import aspose.cells as cells`
Das Modul `jpype` wird zum Starten der JVM verwendet, während `aspose.cells` die workbook/worksheet/cell/pivot-Typen bereitstellt, die durchgängig verwendet werden.

## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die aktuellsten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe — aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, vollständige Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — z. B. wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern irrelevant sind und nicht angefasst werden sollten. Für diesen Fall stellt Aspose.Cells `Worksheet.refreshPivotTables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Kopfzeile mit Fruit / Year / Amount schreiben
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 8 Datenzeilen schreiben (Zeilen 2-9, passend zum Quellbereich A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Eine Pivot-Tabelle namens "Pivot1" hinzufügen, platziert an der Zielzelle E3, mit Quelle aus A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Felder zuweisen: Fruit als Zeile, Year als Spalte, Amount als Daten
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Eine Ansichts-/Layout-Eigenschaft ändern — dies ist eine reine Darstellungsänderung,
# erfordert also KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu aus den
# Daten, die bereits im PivotCache gehalten werden. Da sich die Quelldaten nicht geändert haben,
# wird kein Roundtrip zur Quelle durchgeführt — nur die zwischengespeicherten Werte werden neu
# in die Arbeitsblatt-Zellen berechnet.
pivotTable.calculateData()
# Die Arbeitsmappe auf der Festplatte speichern
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Eine einzelne Pivot-Tabelle aktualisieren
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.

### Quelldaten geändert — Verwenden Sie `PivotCache.refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.getPivotCache().refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

### Nur Ansicht/Layout geändert — Verwenden Sie `calculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben wurde oder eine Aktualisierung-beim-Öffnen-Einstellung umgeschaltet wurde), ist es nicht erforderlich, zur Datenquelle zurückzukehren. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine Nicht-Quell-Eigenschaft der Pivot-Tabelle und ruft dann `calculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.
Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsamen Cache sitzen. Um sie aufzulisten — z. B. vor einer Stapelaktualisierung oder zur Diagnose der Auswirkungen gemeinsamer Caches — verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die vom angegebenen Cache abhängt.

## Migration von der veralteten Methode `PivotTable.refreshData()`
Vor Aspose.Cells for Python via Java v26.7 bestand die Standardmethode zum Aktualisieren einer Pivot-Tabelle darin, `PivotTable.refreshData()` auf jeder Pivot-Tabelle einzeln aufzurufen. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der `refreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft die Daten *jedes Mal* aus der Quelle erneut ab, wenn er aufgerufen wird, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind:
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die sich einen einzelnen Cache teilen.

## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und gibt an, wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|---------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.refreshPivotTables()` | Beschränkt auf ein Arbeitsblatt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsamen Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.calculateData()` | Überspringt unnötige Quellrückkehr. |
| Alle Pivot-Tabellen auf einem gemeinsamen Cache auflisten | `pivotCache.getPivotTables()` | Zur Auflistung vor der Massenaktualisierung verwenden. |
In der Praxis sind die cache-basierten APIs dem veralteten `refreshData()` pro Tabelle vorzuziehen. Sie kennen gemeinsame Caches, vermeiden redundante Quellabrufe und ermöglichen die Auswahl des kleinsten Geltungsbereichs, der Ihre Aktualisierungsanforderung erfüllt.

## Häufige Fallstricke
- **Vergessen der Aktualisierung vor dem Speichern.** Eine Pivot-Tabelle schreibt ihre gerenderten Werte erst dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.Refresh()` (oder `Workbook.RefreshAll()`) vor `Workbook.save()` auf, da die gespeicherte Datei sonst weiterhin die alten aggregierten Werte enthält.
- **Aufrufen des veralteten `RefreshData()` pro Tabelle.** In v26.7 ist `PivotTable.RefreshData()` als veraltet markiert und ruft die Quelle bei jedem Aufruf erneut ab. Bei mehreren Pivot-Tabellen, die sich einen Cache teilen, bedeutet dies N redundante Quellabrufe. Ersetzen Sie dies durch ein einzelnes `PivotCache.Refresh()`, gefolgt von `CalculateData()` pro Tabelle.
- **Aktualisieren, wenn nur das Layout geändert wurde.** Wenn Sie nur die Ansicht einer Pivot-Tabelle geändert haben (Spaltenreihenfolge, `ConsolidationFunction` usw.), ohne die Quelldaten zu berühren, ist `PivotCache.Refresh()` unnötig und langsam. Rufen Sie `pivotTable.CalculateData()` auf, um aus dem vorhandenen Cache neu zu rendern.
- **Externe Quelle wird von `PivotCache.Refresh()` nicht unterstützt.** Wenn die Quelle der Pivot-Tabelle aus einer externen Verbindung stammt (Datenbank, OLAP-Würfel usw.), kann `PivotCache.Refresh()` sie in v26.7 nicht aktualisieren — es werden derzeit nur die Quelltypen `Sheet` und `Consolidation` unterstützt. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder erstellen Sie den Cache aus der Quelle neu.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python" >}}