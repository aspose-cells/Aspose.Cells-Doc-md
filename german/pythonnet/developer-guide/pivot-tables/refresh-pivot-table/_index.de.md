---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for Python via .NET
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Python via .NET mithilfe der Pivot-Refresh-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, Python via .NET, Pivot-Tabelle, aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt eine mehrstufige Aktualisierungs-API bereit, mit der Sie Pivot-Daten in vier unterschiedlichen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Python via .NET v26.7** ist die Legacy-Methode `PivotTable.refresh_data()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}
## Einführung
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Wahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte leben.
2. **PivotCache** — der speicherinterne Snapshot der Quelldaten. Jede Pivot-Tabelle baut auf einem `PivotCache` auf; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.
Ein besonders wichtiges Konzept ist der **gemeinsam genutzte Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert alle abhängigen `PivotTable`s gleichzeitig.
{{% alert color="primary" %}}
`PivotCache.source_type` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quellentypen **`Sheet`** und **`Consolidation`** — also Daten, die in Arbeitsblattbereichen liegen. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotCache.refresh()`** — lädt Quelle → Cache neu UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.calculate_data()`** — berechnet die Anzeige einer `PivotTable` anhand bereits zwischengespeicherter Daten neu, ohne Rückkehr zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, daher ist der Quellentyp `Sheet` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
## Erforderliche Importe
Alle Python-Beispiele in diesem Artikel beginnen mit den folgenden drei Import-Anweisungen, da sich die Pivot-Typen im Namespace `aspose.cells.pivot` befinden:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`
## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die aktuellsten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refresh_all()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe — aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, umfassende Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich Fruit/Year/Amount, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refresh_all()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.
```python
import aspose.cells as ac

# Erstellen einer neuen Arbeitsmappe
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Kopfzeile in die Zellen A1:C1 schreiben
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Fruchtdaten für 2020 und 2021)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)

# Hinzufügen einer Pivot-Tabelle: Quellbereich "A1:C9", Zielzelle "E3", Name "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Zuweisen der Pivot-Felder: Frucht zu Zeilen, Jahr zu Spalten, Menge zu Daten
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Ändern mehrerer Mengenwerte in den Quelldaten, um Änderungen zu simulieren
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Alle Pivot-Tabellen / Pivot-Caches in der Arbeitsmappe aktualisieren
workbook.refresh_all()

# Arbeitsmappe speichern
workbook.save("output.xlsx")
```
## Alle Pivot-Tabellen in einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — zum Beispiel, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht in Beziehung stehen und nicht berührt werden sollen. Für diesen Fall bietet Aspose.Cells `Worksheet.refresh_pivot_tables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.
Dies ist selektiver als `Workbook.refresh_all()`: nur die Pivot-Tabellen auf dem Zielarbeitsblatt werden aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.
Das folgende Beispiel füllt dieselben Fruit/Year/Amount-Quelldaten, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)

pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)

worksheet.refresh_pivot_tables()

workbook.save("output.xlsx")
```
## Eine einzelne Pivot-Tabelle aktualisieren
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrundeliegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.
### Quelldaten geändert — Verwenden Sie `PivotCache.refresh()`
Wenn sich die zugrundeliegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivot_table.pivot_cache.refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.
{{% alert color="primary" %}}
Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufbauen — nicht nur diejenige, auf die Sie verweisen. Wenn zwei Pivot-Tabellen denselben Quellbereich nutzen, aktualisiert das Aktualisieren eines Caches beide.
{{% /alert %}}
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten des gemeinsam genutzten Caches zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.
```python
import aspose.cells as ac

# Erstellen Sie eine neue Arbeitsmappe und greifen Sie auf das erste Arbeitsblatt zu
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Kopfzeile schreiben: Frucht / Jahr / Betrag
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Ungefähr 9 Datenzeilen schreiben (Traube / Blaubeere / Kiwi / Kirsche über 2020-2021)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# Fügen Sie die erste Pivot-Tabelle "Pivot1" verankert an Zelle E3 hinzu, Quellbereich A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Felder für Pivot1 zuweisen
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Fügen Sie eine ZWEITE Pivot-Tabelle "Pivot2" verankert an E15 hinzu, die denselben Quellbereich A1:C9 verwendet
# Sowohl Pivot1 als auch Pivot2 teilen sich einen einzigen PivotCache, da der Quellbereich identisch ist.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Dieselben Felder für Pivot2 zuweisen
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Mehrere Betragszellenwerte in den Quelldaten ändern, um eine Datenänderung zu simulieren
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Den gemeinsam genutzten PivotCache aktualisieren.
# Da Pivot1 und Pivot2 denselben PivotCache teilen, aktualisiert dieser einzige Aufruf
# BEIDE Pivot-Tabellen (Daten + Stil) aus der aktualisierten Quelle.
pivotTable1.pivot_cache.refresh()

# Die Arbeitsmappe speichern
workbook.save("output.xlsx")
```
### Nur Ansicht/Layout geändert — Verwenden Sie `calculate_data()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (zum Beispiel, wenn ein Feld in einen anderen Bereich verschoben oder eine Einstellung „Beim Öffnen aktualisieren" umgeschaltet wurde), ist es nicht erforderlich, zur Datenquelle zurückzukehren. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivot_table.calculate_data()` die richtige Wahl.
Dies vermeidet den unnötigen Quellabruf und ist erheblich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.
Das folgende Beispiel ändert eine Nicht-Quelleneigenschaft der Pivot-Tabelle und ruft dann `calculate_data()` auf, um sie aus dem vorhandenen Cache neu zu rendern.
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fruit / Jahr / Betrag Kopfzeile schreiben
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 8 Datenzeilen schreiben (Zeilen 2-9, passend zum Quellbereich A1:C9)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)

# Eine Pivot-Tabelle mit dem Namen "Pivot1" hinzufügen, platziert an der Zielzelle E3, mit Quelle aus A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Felder zuweisen: Fruit zu Zeile, Year zu Spalte, Amount zu Daten
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Eine Ansichts-/Layout-Eigenschaft ändern — dies ist eine reine Präsentationsänderung,
# daher ist KEIN erneutes Lesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivot_table.refresh_data_on_opening_file = False

# CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) aus den
# bereits im PivotCache gespeicherten Daten neu. Da sich die Quelldaten nicht geändert haben,
# wird kein Roundtrip zur Quelle durchgeführt — nur die zwischengespeicherten Werte werden neu
# in die Arbeitsblattzellen berechnet.
pivot_table.calculate_data()

# Arbeitsbuch auf der Festplatte speichern
workbook.save("output.xlsx")
```
## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen
Eine Arbeitsmappe enthält häufig viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache sitzen. Um sie aufzulisten — zum Beispiel vor einer Massenaktualisierung oder um die Auswirkungen des gemeinsam genutzten Caches zu diagnostizieren — verwenden Sie `PivotCache.get_pivot_tables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.
Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen oder einfach die von `get_pivot_tables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin erscheinen.
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und zählt dann die Pivot-Tabellen des Caches auf.

## Migration von der veralteten `PivotTable.refresh_data()`
Vor Aspose.Cells for Python via .NET v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.refresh_data()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der `refresh_data()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft Daten bei jedem Aufruf erneut aus der Quelle ab, auch wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten gemeinsam genutzten Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt der wiederholte Aufruf von `refresh_data()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder erneut abgerufen wird, was sehr langsam ist.
Die empfohlenen Ersetzungen sind:
- **Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren** → verwenden Sie `workbook.refresh_all();`
- **Einige davon aktualisieren** → verwenden Sie `pivot_table.pivot_cache.refresh();` für einen Cache. Da der Cache gemeinsam genutzt wird, aktualisiert dieser einzige Aufruf jede Pivot-Tabelle, die auf diesem Cache aufbaut. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivot_table.calculate_data();`, um aus dem vorhandenen Cache neu zu rendern, ohne einen Quellrückgriff.
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzelnen Cache gemeinsam nutzen.
```python
import aspose.cells as ac

# Erstellen einer neuen Arbeitsmappe und Zugriff auf das erste Arbeitsblatt
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Quelldaten aufbauen: Obst / Jahr / Betrag (Kopfzeile + 9 Zeilen) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- Erste Pivot-Tabelle (Pivot1) an Zielzelle E3 hinzufügen ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- ZWEITE Pivot-Tabelle (Pivot2) am GLEICHEN Quellbereich hinzufügen ---
# Sowohl Pivot1 als auch Pivot2 teilen sich EINEN zugrundeliegenden PivotCache.
# Dies ist genau das Szenario, in dem der alte RefreshData()-Ansatz pro Tabelle
# ineffizient wird: Das Aktualisieren einer Tabelle ruft den gesamten
# gemeinsam genutzten Cache erneut ab, sodass N Tabellen den gleichen teuren Abruf N-mal durchführen.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Mehrere Betragswerte in den Quelldaten ändern ---
sheet.cells["C2"].put_value(5000)   # Traube 2020
sheet.cells["C5"].put_value(7500)   # Kirsche 2020
sheet.cells["C9"].put_value(9500)   # Kirsche 2021

# --- VERALTETES Muster (vor 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # ruft erneut von der Quelle ab, aktualisiert den gesamten Cache
# pivot_table2.refresh_data();  # ruft ERNEUT ab — der Cache ist bereits aktuell!
# Jeder Aufruf baut den gemeinsam genutzten Cache neu auf, also N Tabellen = N redundante Abrufe.

# --- NEUES Muster ab v26.7: Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
# Ein Aufruf von PivotCache.Refresh() holt die geänderten Werte in den gemeinsam genutzten
# Cache UND berechnet die Anzeige JEDER Pivot-Tabelle neu, die darauf verweist.
# Da Pivot1 und Pivot2 einen PivotCache teilen, aktualisiert dieser eine Aufruf
# beide Tabellen — kein zweiter Quellzugriff ist erforderlich.
pivot_table1.pivot_cache.refresh()

# CalculateData() rendert nur die Anzeige einer Pivot-Tabelle neu (Daten + Stil)
# aus den bereits im Cache vorhandenen Daten — es greift NICHT auf die Quelle zu.
# Wir rufen es hier nur auf Pivot2 auf, um die API zu demonstrieren: Nachdem der Cache
# einmal aktualisiert wurde, kann jede abhängige Tabelle neu gerendert werden, ohne
# auf die Quelle zurückzugreifen. Verwenden Sie CalculateData() eigenständig, wenn sich nur
# die Ansichts-/Layouteinstellungen der Pivot-Tabelle geändert haben und der Cache aktuell ist.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```
## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und gibt an, wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refresh_all()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.refresh_pivot_tables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivot_table.pivot_cache.refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsam genutzten Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivot_table.calculate_data()` | Überspringt unnötigen Quellrückgriff. |
| Alle Pivot-Tabellen auf einem gemeinsam genutzten Cache auflisten | `pivot_cache.get_pivot_tables()` | Vor Massenaktualisierung zur Aufzählung verwenden. |
In der Praxis sind die cache-basierten APIs dem veralteten `refresh_data()` pro Tabelle vorzuziehen. Sie kennen gemeinsam genutzte Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

{{< app/cells/assistant language="python-net" >}}
