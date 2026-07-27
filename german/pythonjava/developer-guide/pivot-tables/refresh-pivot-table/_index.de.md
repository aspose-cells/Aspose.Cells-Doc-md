---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for Python via Java
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Python via Java mithilfe der v26.7+ Pivot-Refresh-API aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Python via Java, Pivot-Tabelle, Aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells stellt eine geschichtete Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Bereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Python via Java v26.7** ist die Legacy-Methode `PivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}
## Einführung
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine geschichtete Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die Arbeitsblatt-`Cells`, in die die `PivotTable` ihre berechneten Werte und Stile rendert.
Ein besonders wichtiges Konzept ist der **geteilte Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert sofort jede abhängige `PivotTable`.
{{% alert color="primary" %}}
`PivotCache.getSourceType()` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`SHEET`** und **`CONSOLIDATION`** — also Daten, die in Arbeitsblattbereichen gespeichert sind. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotCache.refresh()`** — lädt die Quelle neu in den Cache UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.calculateData()`** — berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Rückgriff auf die Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellquellendaten, daher ist der Quelltyp `SHEET` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
## Erforderliche Importe
Alle Python-Beispiele in diesem Artikel basieren auf den folgenden Importen, da sich die Pivot-Typen im Namespace `aspose.cells.pivot` befinden:
- `import jpype`
- `import aspose.cells as cells`
Das Modul `jpype` wird zum Bootstrappen der JVM verwendet, während `aspose.cells` die Workbook-/Worksheet-/Cell-/Pivot-Typen bereitstellt, die im gesamten Dokument verwendet werden.
## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – jeder `PivotCache` wird aus seiner Quelle aktualisiert und dann jede abhängige `PivotTable` neu berechnet. Dies ist der empfohlene Ansatz für allgemeine, dokumentweite Aktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich Fruit/Jahr/Betrag, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.
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

# Eine Pivot-Tabelle hinzufügen: Quellbereich "A1:C9", Zielzelle "E3", Name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Pivot-Felder zuweisen: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Mehrere Amount-Werte in den Quelldaten ändern, um Änderungen zu simulieren
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Alle Pivot-Tabellen / Pivot-Caches in der Arbeitsmappe aktualisieren
workbook.refreshAll()

# Die Arbeitsmappe speichern
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## Alle Pivot-Tabellen in einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – beispielsweise wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht verwandt sind und nicht berührt werden sollten. Für diesen Fall bietet Aspose.Cells `Worksheet.refreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.
Dies ist selektiver als `Workbook.refreshAll()`: nur die Pivot-Tabellen auf dem Zielarbeitsblatt werden aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.
Das folgende Beispiel befüllt dieselben Fruit/Jahr/Betrag-Quelldaten, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.
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
Wenn Sie eine feinkörnige Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.
### Quelldaten geändert — Verwenden Sie `PivotCache.refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.getPivotCache().refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.
{{% alert color="primary" %}}
Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufgebaut sind – nicht nur die, auf die Sie verweisen. Wenn zwei Pivot-Tabellen denselben Quellbereich teilen, aktualisiert das Aktualisieren eines Caches beide.
{{% /alert %}}
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten mit geteiltem Cache zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Eine neue Arbeitsmappe erstellen und auf das erste Arbeitsblatt zugreifen
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Kopfzeile schreiben: Frucht / Jahr / Betrag
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Ungefähr 9 Datenzeilen schreiben (Traube / Blaubeere / Kiwi / Kirsche über 2020-2021)
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

# Die erste Pivot-Tabelle "Pivot1" hinzufügen, verankert an Zelle E3, Quellbereich A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Felder für Pivot1 zuweisen
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Eine ZWEITE Pivot-Tabelle "Pivot2" hinzufügen, verankert an E15, unter Verwendung desselben Quellbereichs A1:C9
# Sowohl Pivot1 als auch Pivot2 teilen sich einen einzigen PivotCache, da der Quellbereich identisch ist.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Dieselben Felder für Pivot2 zuweisen
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Mehrere Betragszellenwerte in den Quelldaten ändern, um eine Datenänderung zu simulieren
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Den gemeinsam genutzten PivotCache aktualisieren.
# Da Pivot1 und Pivot2 denselben PivotCache teilen, aktualisiert dieser einzelne Aufruf
# BEIDE Pivot-Tabellen (Daten + Stil) aus den aktualisierten Quellen.
pivotTable1.getPivotCache().refresh()

# Die Arbeitsmappe speichern
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
### Nur Ansicht/Layout geändert — Verwenden Sie `calculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben oder eine Aktualisierungs-beim-Öffnen-Einstellung umgeschaltet wurde), ist kein Rückgriff auf die Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Dies vermeidet den unnötigen Quellabruf und ist erheblich schneller, wenn viele Pivot-Tabellen denselben Cache teilen.
Das folgende Beispiel ändert eine Nicht-Quelle-Eigenschaft der Pivot-Tabelle und ruft dann `calculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Schreibt die Kopfzeile Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Schreibt 8 Datenzeilen (Zeilen 2-9, passend zum Quellbereich A1:C9)
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

# Fügt eine Pivot-Tabelle mit dem Namen "Pivot1" hinzu, platziert an der Zielzelle E3, mit Quelle aus A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Weist Felder zu: Fruit in Zeile, Year in Spalte, Amount in Daten
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Ändert eine Ansichts-/Layout-Eigenschaft — dies ist eine reine Darstellungsänderung,
# daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) aus den
# bereits im PivotCache gespeicherten Daten neu. Da sich die Quelldaten nicht geändert haben,
# erfolgt kein Roundtrip zur Quelle — nur die zwischengespeicherten Werte werden neu berechnet
# und in Arbeitsblattzellen geschrieben.
pivotTable.calculateData()

# Speichert die Arbeitsmappe auf der Festplatte
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## Alle Pivot-Tabellen abrufen, die denselben PivotCache teilen
Eine Arbeitsmappe enthält häufig viele Pivot-Tabellen, die alle auf einem einzigen geteilten Cache aufbauen. Um sie aufzulisten – beispielsweise vor einer Batch-Aktualisierung oder um die Auswirkungen des geteilten Caches zu diagnostizieren – verwenden Sie `PivotCache.getPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.
Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz teilen: Sie können Cache-Referenzen vergleichen oder einfach die von `getPivotTables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin erscheinen.
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz teilen, und listet dann die Pivot-Tabellen des Caches auf.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

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
Vor Aspose.Cells for Python via Java v26.7 bestand die Standardmethode zum Aktualisieren einer Pivot-Tabelle darin, `PivotTable.refreshData()` für jede Pivot-Tabelle einzeln aufzurufen. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der Ansatz `refreshData()` pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft *bei jedem* Aufruf Daten aus der Quelle erneut ab, selbst wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten geteilten Cache. Wenn viele Pivot-Tabellen einen Cache teilen, führt der wiederholte Aufruf von `refreshData()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder neu abgerufen wird, was sehr langsam ist.
Die empfohlenen Ersetzungen sind:
- **Aktualisieren Sie ALLE Pivot-Tabellen in der Arbeitsmappe** → verwenden Sie `workbook.refreshAll();`
- **Aktualisieren Sie EINIGE davon** → verwenden Sie `pivotTable.getPivotCache().refresh();` für einen Cache. Da der Cache geteilt wird, aktualisiert dieser einzige Aufruf jede Pivot-Tabelle, die auf diesem Cache aufgebaut ist. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivotTable.calculateData();`, um aus dem vorhandenen Cache neu zu rendern, ohne Quellrundreise.
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache teilen.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Neue Arbeitsmappe erstellen und auf das erste Arbeitsblatt zugreifen
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Quelldaten aufbauen: Frucht / Jahr / Betrag (Kopfzeile + 9 Zeilen) ---
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

# --- Erste Pivot-Tabelle (Pivot1) an Zielzelle E3 hinzufügen ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- ZWEITE Pivot-Tabelle (Pivot2) auf demselben Quellbereich hinzufügen ---
# Pivot1 und Pivot2 teilen sich EINEN zugrundeliegenden PivotCache.
# Genau dies ist das Szenario, in dem der alte pro-Tabelle RefreshData()-
# Ansatz ineffizient wird: Das Aktualisieren einer Tabelle ruft den gesamten
# gemeinsam genutzten Cache erneut ab, sodass N Tabellen N-mal denselben
# teuren Abruf durchführen.
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
# pivotTable1.RefreshData();  // ruft erneut von der Quelle ab, aktualisiert gesamten Cache
# pivotTable2.RefreshData();  // ruft ERNEUT ab — der Cache ist bereits aktuell!
# Jeder Aufruf baut den gemeinsam genutzten Cache neu auf, daher N Tabellen = N überflüssige Abrufe.

# --- NEUES Muster ab v26.7: Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
# Ein einziger Aufruf von PivotCache.Refresh() holt die geänderten Werte in den
# gemeinsam genutzten Cache UND berechnet die Anzeige JEDER Pivot-Tabelle neu,
# die darauf verweist. Da Pivot1 und Pivot2 einen PivotCache teilen, aktualisiert
# dieser eine Aufruf beide Tabellen — kein erneuter Quellzugriff ist nötig.
pivotTable1.getPivotCache().refresh()

# CalculateData() rendert nur die Anzeige einer Pivot-Tabelle (Daten + Stil)
# aus den bereits im Cache vorhandenen Daten neu — die Quelle wird NICHT berührt.
# Wir rufen es hier auf Pivot2 nur auf, um die API zu demonstrieren: Nachdem der
# Cache einmal aktualisiert wurde, kann jede abhängige Tabelle neu gerendert
# werden, ohne zur Quelle zurückzugehen. Verwenden Sie CalculateData() eigenständig,
# wenn sich nur die Ansichts-/Layout-Einstellungen der Pivot-Tabelle geändert haben
# und der Cache aktuell ist.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und gibt an, wann Sie welche wählen sollten.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.refreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem geteilten Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.calculateData()` | Überspringt unnötige Quellrundreise. |
| Alle Pivot-Tabellen auf einem geteilten Cache auflisten | `pivotCache.getPivotTables()` | Vor Massenaktualisierung zum Auflisten verwenden. |
In der Praxis sollten Sie die cache-basierten APIs der veralteten Methode `refreshData()` pro Tabelle vorziehen. Sie kennen geteilte Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Bereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.
## Verwandte Artikel
- [Einfügen eines Bildes in eine Zelle](/cells/de/python-java/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/python-java/dbf/)
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/python-java/splitting-excel-files-into-multiple-files/)
- [Sparklines in Aspose.Cells for Python via Java](/cells/de/python-java/sparkline/)
{{< app/cells/assistant language="python" >}}