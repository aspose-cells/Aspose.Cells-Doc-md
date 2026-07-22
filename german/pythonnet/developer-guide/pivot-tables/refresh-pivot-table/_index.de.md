---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for Python via .NET
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for Python via .NET mit der Pivot-Refresh-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables anhand praktischer Codebeispiele.
keywords: Aspose.Cells, Python via .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stellt eine mehrstufige Refresh-API bereit, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for Python via .NET v26.7** ist die ältere Methode `PivotTable.refresh_data()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.

{{% /alert %}}

## Einführung

Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Hinter den Kulissen verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den in dem Arbeitsblatt angezeigten Werten verbindet. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Refresh-API für jede Situation.

Die vierschichtige Datenkette ist:

1. **Datenquelle** – die ursprünglichen Arbeitsblatt-Bereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** – der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle basiert auf einem `PivotCache`; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** – das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *ausschließlich* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** – die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Formatierungen rendert.

Ein besonders wichtiges Konzept ist der **freigegebene Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Ein einzelner `PivotCache` kann von vielen Pivot-Tabellen referenziert werden, und das Aktualisieren dieses Caches aktualisiert jede abhängige `PivotTable` auf einmal.

{{% alert color="primary" %}}

`PivotCache.source_type` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.refresh()` nur die Quelltypen **`Sheet`** und **`Consolidation`** – also Daten, die in Arbeitsblatt-Bereichen liegen. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.

{{% /alert %}}

Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:

- **`PivotCache.refresh()`** – lädt die Quelle neu in den Cache UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.calculate_data()`** – berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne einen Roundtrip zur Datenquelle durchzuführen.

Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, daher ist der Quelltyp `Sheet` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.

## Erforderliche Importe

Alle Python-Beispiele in diesem Artikel beginnen mit den folgenden drei Import-Anweisungen, da sich die Pivot-Typen im Namespace `aspose.cells.pivot` befinden:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren

Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die aktuellen Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.refresh_all()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, dokumentweite Aktualisierungen, bei denen die Leistung keine Rolle spielt.

Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `refresh_all()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```python
import aspose.cells as ac

# Erstellen einer neuen Arbeitsmappe
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Kopfzeile in die Zellen A1:C1 schreiben
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Obst-Daten über 2020 und 2021)
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

# Pivot-Felder zuweisen: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Mehrere Amount-Werte in den Quelldaten ändern, um Änderungen zu simulieren
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Jede Pivot-Tabelle / jeden Pivot-Cache in der Arbeitsmappe aktualisieren
workbook.refresh_all()

# Arbeitsmappe speichern
workbook.save("output.xlsx")
```

## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren

Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden – beispielsweise wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern unabhängig sind und nicht berührt werden sollten. Für diesen Fall stellt Aspose.Cells `Worksheet.refresh_pivot_tables()` bereit, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

Dies ist selektiver als `Workbook.refresh_all()`: Es werden nur die Pivot-Tabellen auf dem Ziel-Arbeitsblatt aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.

Das folgende Beispiel füllt dieselben Fruit/Year/Amount-Quelldaten ein, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.

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

Wenn Sie eine feinkörnige Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrundeliegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.

### Quelldaten geändert – Verwenden Sie `PivotCache.refresh()`

Wenn sich die zugrundeliegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivot_table.pivot_cache.refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

{{% alert color="primary" %}}

Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache basieren – nicht nur die, auf die Sie verweisen. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.

{{% /alert %}}

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten mit gemeinsamem Cache zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.

```python
import aspose.cells as ac

# Erstelle eine neue Arbeitsmappe und greife auf das erste Arbeitsblatt zu
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Schreibe die Kopfzeile: Frucht / Jahr / Betrag
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Schreibe ungefähr 9 Datenzeilen (Traube / Blaubeere / Kiwi / Kirsche über 2020-2021)
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

# Füge die erste PivotTable "Pivot1" hinzu, verankert an Zelle E3, Quellbereich A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Weise Felder für Pivot1 zu
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Füge eine ZWEITE PivotTable "Pivot2" hinzu, verankert an E15, mit demselben Quellbereich A1:C9
# Sowohl Pivot1 als auch Pivot2 teilen sich einen einzelnen PivotCache, da der Quellbereich identisch ist.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Weise dieselben Felder für Pivot2 zu
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Ändere mehrere Betragszellenwerte in den Quelldaten, um eine Datenänderung zu simulieren
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Aktualisiere den geteilten PivotCache.
# Da Pivot1 und Pivot2 denselben PivotCache teilen, aktualisiert dieser einzelne Aufruf
# BEIDE PivotTables (Daten + Stil) aus der aktualisierten Quelle.
pivotTable1.pivot_cache.refresh()

# Speichere die Arbeitsmappe
workbook.save("output.xlsx")
```

### Nur Ansicht/Layout geändert – Verwenden Sie `calculate_data()`

Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben oder eine Einstellung "Bei Dateiöffnung aktualisieren" umgeschaltet wurde), ist kein Roundtrip zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivot_table.calculate_data()` die richtige Wahl.

Dies vermeidet den unnötigen Quellabruf und ist erheblich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.

Das folgende Beispiel ändert eine Nicht-Quelle-Eigenschaft der Pivot-Tabelle und ruft dann `calculate_data()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Schreibe die Kopfzeile Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Schreibe 8 Datenzeilen (Zeilen 2-9, passend zum Quellbereich A1:C9)
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

# Füge eine Pivot-Tabelle mit dem Namen "Pivot1" hinzu, platziert in der Zielzelle E3, mit Quelle aus A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Weise Felder zu: Fruit zur Zeile, Year zur Spalte, Amount zu Daten
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Ändere eine Anzeige-/Layout-Eigenschaft – dies ist eine reine Darstellungsänderung,
# daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
pivot_table.refresh_data_on_opening_file = False

# CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu aus den
# bereits im PivotCache gespeicherten Daten. Da sich die Quelldaten nicht geändert haben,
# wird kein Roundtrip zur Quelle durchgeführt – nur die zwischengespeicherten Werte werden
# in die Arbeitsblattzellen neu berechnet.
pivot_table.calculate_data()

# Speichere die Arbeitsmappe auf der Festplatte
workbook.save("output.xlsx")
```

## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache basieren. Um sie aufzulisten – beispielsweise vor einer Stapelaktualisierung oder zur Diagnose der Auswirkungen des gemeinsamen Caches – verwenden Sie `PivotCache.get_pivot_tables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.

Dies ist auch die direkteste Methode, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen oder einfach die von `get_pivot_tables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin enthalten sind.

Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und listet dann die Pivot-Tabellen des Caches auf.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

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

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## Migration von der veralteten Methode `PivotTable.refresh_data()`

Vor Aspose.Cells for Python via .NET v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.refresh_data()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.

Es gibt zwei Gründe, warum der tabellenweise `refresh_data()`-Ansatz in realen Arbeitsmappen problematisch ist:

- Er ruft die Daten jedes Mal *neu* aus der Quelle ab, selbst wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten gemeinsamen Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, führt das wiederholte Aufrufen von `refresh_data()` pro Pivot-Tabelle dazu, dass derselbe Cache immer wieder neu abgerufen wird, was sehr langsam ist.

Die empfohlenen Ersetzungen sind:

- **Aktualisieren Sie ALLE Pivot-Tabellen in der Arbeitsmappe** → verwenden Sie `workbook.refresh_all();`
- **Aktualisieren Sie einige davon** → verwenden Sie `pivot_table.pivot_cache.refresh();` für einen Cache. Da der Cache gemeinsam genutzt wird, aktualisiert dieser einzige Aufruf jede Pivot-Tabelle, die auf diesem Cache basiert. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache basieren, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivot_table.calculate_data();`, um aus dem vorhandenen Cache neu zu rendern, ohne einen Quell-Roundtrip durchzuführen.

Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.

```python
import aspose.cells as ac

# Erstellen Sie eine neue Arbeitsmappe und greifen Sie auf das erste Arbeitsblatt zu
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Quelldaten erstellen: Frucht / Jahr / Betrag (Kopfzeile + 9 Zeilen) ---
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

# --- Erste Pivot-Tabelle (Pivot1) in Zielzelle E3 hinzufügen ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- ZWEITE Pivot-Tabelle (Pivot2) für denselben Quellbereich hinzufügen ---
# Sowohl Pivot1 als auch Pivot2 teilen sich EINEN zugrunde liegenden PivotCache.
# Dies ist genau das Szenario, in dem der ältere pro-Tabelle RefreshData()
# Ansatz ineffizient wird: Das Aktualisieren einer Tabelle ruft den gesamten
# gemeinsamen Cache erneut ab, sodass das Aktualisieren von N Tabellen den gleichen teuren Abruf N-mal durchführt.
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
# pivot_table2.refresh_data();  # ruft ERNEUT ab — der Cache ist bereits frisch!
# Jeder Aufruf baut den gemeinsamen Cache neu auf, also N Tabellen = N redundante Abrufe.

# --- NEUES Muster v26.7+: Den Cache EINMAL aktualisieren, dann nach Bedarf neu rendern ---
# Ein Aufruf von PivotCache.Refresh() zieht die geänderten Werte in den gemeinsamen
# Cache UND berechnet die Anzeige JEDER Pivot-Tabelle neu, die darauf verweist.
# Da Pivot1 und Pivot2 einen PivotCache teilen, aktualisiert dieser einzige Aufruf
# beide Tabellen — kein zweiter Quellrundgang ist erforderlich.
pivot_table1.pivot_cache.refresh()

# CalculateData() rendert nur die Anzeige einer Pivot-Tabelle neu (Daten + Stil)
# aus den bereits im Cache vorhandenen Daten — es greift NICHT auf die Quelle zu.
# Wir rufen es hier auf Pivot2 auf, nur um die API zu demonstrieren: nachdem der Cache
# einmal aktualisiert wurde, kann jede abhängige Tabelle neu gerendert werden ohne
# zur Quelle zurückzukehren. Verwenden Sie CalculateData() eigenständig, wenn nur die
# Ansichts-/Layouteinstellungen der Pivot-Tabelle geändert wurden und der Cache aktuell ist.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Welche Refresh-API sollte ich verwenden?

Die folgende Tabelle fasst die verfügbaren Refresh-APIs zusammen und zeigt, wann welche zu wählen ist.

| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.refresh_all()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.refresh_pivot_tables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivot_table.pivot_cache.refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsamen Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivot_table.calculate_data()` | Überspringt unnötigen Quell-Roundtrip. |
| Alle Pivot-Tabellen auf einem gemeinsamen Cache auflisten | `pivot_cache.get_pivot_tables()` | Verwenden Sie dies, um vor der Stapelaktualisierung aufzulisten. |

In der Praxis sind die cache-basierten APIs der veralteten tabellenweisen Methode `refresh_data()` vorzuziehen. Sie kennen gemeinsame Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

{{< app/cells/assistant language="python" >}}