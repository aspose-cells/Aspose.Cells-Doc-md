---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for Python via Java
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Python via Java mithilfe der Pivot-Refresh-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Python via Java, Pivot-Tabelle, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stellt eine geschichtete Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Bereichen neu laden können — von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Python via Java v26.7** ist die Legacy-Methode `PivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.

{{% /alert %}}

## Einführung

Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Hinter den Kulissen pflegt Aspose.Cells eine geschichtete Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.

Die vierschichtige Datenkette ist:

1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

Ein besonders wichtiges Konzept ist der **geteilte Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert jede abhängige `PivotTable` auf einmal.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`SHEET`** und **`CONSOLIDATION`** — also Daten, die in Arbeitsblattbereichen liegen. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.

{{% /alert %}}

Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:

- **`PivotCache.refresh()`** — lädt die Quelle → den Cache neu UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.calculateData()`** — berechnet die Anzeige einer `PivotTable` aus den bereits zwischengespeicherten Daten neu, ohne einen Roundtrip zurück zur Datenquelle.

Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, daher ist der Quelltyp `SHEET` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.

## Erforderliche Importe

Alle Python-Beispiele in diesem Artikel basieren auf den folgenden Importen, da die Pivot-Typen im Namespace `aspose.cells.pivot` definiert sind:

- `import jpype`
- `import aspose.cells as cells`

Das Modul `jpype` wird zum Bootstrappen der JVM verwendet, während `aspose.cells` die workbook/worksheet/cell/pivot-Typen bereitstellt, die durchgehend verwendet werden.

## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren

Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe — er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, vollständige Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.

Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich Fruit/Year/Amount, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Erstellen einer neuen Arbeitsmappe
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

# Hinzufügen einer Pivot-Tabelle: Quellbereich "A1:C9", Zielzelle "E3", Name "Pivot1"
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

# Arbeitsmappe speichern
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren

Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — beispielsweise, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht in Beziehung stehen und nicht angefasst werden sollten. Für diesen Fall stellt Aspose.Cells `Worksheet.refreshPivotTables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

Dies ist selektiver als `Workbook.refreshAll()`: Nur die Pivot-Tabellen auf dem Zielarbeitsblatt werden aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.

Das folgende Beispiel füllt die gleichen Fruit/Year/Amount-Quelldaten, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.

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

## Eine einzelne Pivot-Tabelle aktualisieren

Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layout-Einstellungen der Pivot-Tabelle selbst.

### Quelldaten geändert — Verwenden Sie `PivotCache.refresh()`

Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.getPivotCache().refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

{{% alert color="primary" %}}

Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufgebaut sind — nicht nur die, die Sie referenzieren. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.

{{% /alert %}}

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten des geteilten Caches zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Erstelle eine neue Arbeitsmappe und greife auf das erste Arbeitsblatt zu
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Schreibe die Kopfzeile: Frucht / Jahr / Betrag
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Schreibe ungefähr 9 Datenzeilen (Traube / Heidelbeere / Kiwi / Kirsche über 2020-2021)
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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# Füge die erste Pivot-Tabelle "Pivot1" hinzu, verankert an Zelle E3, Quellbereich A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Weise Felder für Pivot1 zu
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Füge eine ZWEITE Pivot-Tabelle "Pivot2" hinzu, verankert an E15, unter Verwendung des GLEICHEN Quellbereichs A1:C9
# Sowohl Pivot1 als auch Pivot2 teilen sich einen einzelnen PivotCache, da der Quellbereich identisch ist.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Weise die gleichen Felder für Pivot2 zu
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Ändere mehrere Betragszellenwerte in den Quelldaten, um eine Datenänderung zu simulieren
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Aktualisiere den gemeinsam genutzten PivotCache.
# Da Pivot1 und Pivot2 denselben PivotCache teilen, aktualisiert dieser einzelne Aufruf
# BEIDE Pivot-Tabellen (Daten + Stil) aus der aktualisierten Quelle.
pivotTable1.getPivotCache().refresh()

# Speichere die Arbeitsmappe
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Nur Ansicht/Layout geändert — Verwenden Sie `calculateData()`

Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layout-Einstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben wurde oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet wurde), ist kein Roundtrip zurück zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.

Dies vermeidet den unnötigen Quellabruf und ist erheblich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.

Das folgende Beispiel ändert eine nicht quellbezogene Eigenschaft der Pivot-Tabelle und ruft dann `calculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Schreibe Kopfzeile Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Schreibe 8 Datenzeilen (Zeilen 2-9, passend zum Quellbereich A1:C9)
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

# Füge eine Pivot-Tabelle namens "Pivot1" hinzu, platziert an der Zielzelle E3, mit Quelle A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Weise Felder zu: Fruit zu Zeile, Year zu Spalte, Amount zu Daten
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Ändere eine Ansichts-/Layout-Eigenschaft — dies ist eine reine Präsentationsänderung,
# erfordert also KEIN erneutes Lesen der Quelldaten über PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) aus den
# bereits im PivotCache gehaltenen Daten neu. Da sich die Quelldaten nicht geändert haben,
# wird kein Round-Trip zur Quelle durchgeführt — nur die zwischengespeicherten Werte werden neu
# in die Arbeitsblattzellen berechnet.
pivotTable.calculateData()

# Speichere die Arbeitsmappe auf der Festplatte
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache aufbauen. Um sie aufzulisten — z. B. vor der Durchführung einer Batch-Aktualisierung oder zur Diagnose der Auswirkungen des geteilten Caches — verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.

Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen oder einfach die von `getPivotTables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin enthalten sind.

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und listet dann die Pivot-Tabellen des Caches auf.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# portierter Code hier
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Migration von der veralteten `PivotTable.refreshData()`

Vor Aspose.Cells for Python via Java v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.refreshData()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.

Es gibt zwei Gründe, warum der `refreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:

- Er ruft die Daten *jedes Mal* aus der Quelle erneut ab, wenn er aufgerufen wird, auch wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten geteilten Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt das wiederholte Aufrufen von `refreshData()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder erneut abgerufen wird, was sehr langsam ist.

Die empfohlenen Ersetzungen sind:

- **ALLE Pivot-Tabellen in der Arbeitsmappe aktualisieren** → verwenden Sie `workbook.refreshAll();`
- **EINIGE davon aktualisieren** → verwenden Sie `pivotTable.getPivotCache().refresh();` für einen Cache. Da der Cache geteilt wird, aktualisiert dieser einzige Aufruf jede Pivot-Tabelle, die auf diesem Cache aufbaut. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivotTable.calculateData();`, um aus dem vorhandenen Cache ohne Quell-Roundtrip neu zu rendern.

Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Erstellen einer neuen Arbeitsmappe und Zugriff auf das erste Arbeitsblatt
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Quelldaten erstellen: Obst / Jahr / Betrag (Kopfzeile + 9 Zeilen) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- Hinzufügen der ersten Pivot-Tabelle (Pivot1) in Zielzelle E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Hinzufügen der ZWEITEN Pivot-Tabelle (Pivot2) im SELBEN Quellbereich ---
# Sowohl Pivot1 als auch Pivot2 teilen sich EINEN zugrunde liegenden PivotCache.
# Dies ist genau das Szenario, in dem der alte Ansatz mit RefreshData() pro Tabelle ineffizient wird:
# Das Aktualisieren einer Tabelle ruft den gesamten gemeinsamen Cache erneut ab,
# sodass das Aktualisieren von N Tabellen den teuren Abruf N-mal durchführt.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Mehrere Betragswerte in den Quelldaten ändern ---
sheet.getCells().get("C2").putValue(5000)   # Grape  2020
sheet.getCells().get("C5").putValue(7500)   # Cherry 2020
sheet.getCells().get("C9").putValue(9500)   # Cherry 2021

# --- VERALTETES Muster (vor 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // ruft erneut aus der Quelle ab, aktualisiert den gesamten Cache
# pivotTable2.RefreshData();  // ruft ERNEUT ab — der Cache ist bereits aktuell!
# Jeder Aufruf baut den gemeinsamen Cache neu auf, daher N Tabellen = N redundante Abrufe.

# --- NEUES Muster ab v26.7: Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
# Ein Aufruf von PivotCache.Refresh() übernimmt die geänderten Werte in den gemeinsamen
# Cache UND berechnet die Anzeige JEDER Pivot-Tabelle neu, die darauf verweist.
# Da Pivot1 und Pivot2 einen PivotCache gemeinsam nutzen, aktualisiert dieser einzige Aufruf
# beide Tabellen — kein zweiter Quellrundgang ist erforderlich.
pivotTable1.getPivotCache().refresh()

# CalculateData() rendert nur die Anzeige einer Pivot-Tabelle neu (Daten + Stil)
# aus den bereits im Cache befindlichen Daten — es greift NICHT auf die Quelle zu.
# Wir rufen es hier auf Pivot2 nur auf, um die API zu demonstrieren: nachdem der Cache
# einmal aktualisiert wurde, kann jede abhängige Tabelle neu gerendert werden, ohne
# auf die Quelle zurückzugreifen. Verwenden Sie CalculateData() eigenständig, wenn sich nur die
# Ansichts-/Layout-Einstellungen der Pivot-Tabelle geändert haben und der Cache aktuell ist.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Welche Aktualisierungs-API sollte ich verwenden?

Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und wann jede gewählt werden sollte.

| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem geteilten Cache. |
| Nur Ansichts-/Layout-Einstellungen geändert | `pivotTable.calculateData()` | Überspringt unnötigen Quell-Roundtrip. |
| Alle Pivot-Tabellen auf einem geteilten Cache auflisten | `pivotCache.getPivotTables()` | Zum Auflisten vor der Massenaktualisierung verwenden. |

In der Praxis bevorzugen Sie die cache-basierten APIs gegenüber der veralteten `refreshData()` pro Tabelle. Sie sind sich der geteilten Caches bewusst, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Bereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

{{< app/cells/assistant language="python" >}}