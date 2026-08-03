---
title: Pivot-Tabellen nach Beschriftung oder Wert filtern
linktitle: Pivot-Tabellen nach Beschriftung oder Wert filtern
description: Aspose.Cells for Python via .NET unterstützt umfassende Filterfunktionen für Pivot-Tabellen. Dieser Artikel erläutert, wie Pivot-Tabellendaten mithilfe von Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- oder Einblenden von Pivot-Elementen gefiltert werden.
keywords: Aspose.Cells, Python via .NET-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells bietet fünf praktische Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Datum-Zeit-Zellen oder leere Zellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter verwenden, um nach einem Wertfeld zu sortieren, oder einzelne Pivot-Elemente mithilfe der Eigenschaft `is_hidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs auf den Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}
## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, aber rohe Zusammenfassungen enthalten häufig weitaus mehr Informationen, als Sie präsentieren möchten. Das Filtern ist der primäre Mechanismus, um eine Pivot-Tabelle auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for Python via .NET spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Zeilen- oder Spaltenfeldelemente anhand ihrer Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datum-Zeit-Werte (oder leere Werte) enthalten.
3. **Wertfilter** — filtert Elemente anhand der aggregierten Werte eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente, sortiert nach einem Wertfeld.
5. **Pivot-Elemente aus-/einblenden** — steuert die Sichtbarkeit jedes einzelnen Elements in einem Feld manuell.
Jeder Ansatz verwendet eine andere Methode auf der Klasse `PivotField` oder eine Eigenschaft auf der Klasse `PivotItem`. Nachdem Sie einen Filter angewendet haben, müssen Sie `refresh_data()` und `calculate_data()` auf der Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.
## **Beschriftungsfilter**
Mit einem Beschriftungsfilter können Sie die Elemente eines Zeilen- oder Spaltenfelds filtern, indem Sie deren Textbeschriftungen mit einem Muster vergleichen. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder einem anderen beschriftungsbasiertes Kriterium entsprechen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filter_by_label(PivotFilterType, label_string)` bereit. Die Enumeration `PivotFilterType` enthält Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere. Das zweite Argument liefert die Beschriftungszeichenfolge für den Vergleich.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen Pivot-Tabelle, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem bestimmten Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.
```python
import aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# Vorhandene Arbeitsmappe mit Pivot-Tabelle laden
workbook = ac.Workbook(fileName)

# Auf das Arbeitsblatt nach Index zugreifen (erstes Arbeitsblatt)
worksheet = workbook.worksheets[0]

# Auf die Pivot-Tabelle nach Index zugreifen
pivot_table = worksheet.pivot_tables[0]

# Das erste Zeilen-PivotField abrufen
row_field = pivot_table.row_fields[0]

# Etikettenfilter anwenden — nur Zeilenelemente anzeigen, deren Beschriftungen mit dem angegebenen Präfix beginnen
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# Die Pivot-Tabellen-Daten aktualisieren und neu berechnen, damit der Filter wirksam wird
pivot_table.pivot_cache.refresh()

# Die Arbeitsmappe wieder auf der Festplatte speichern
workbook.save(fileName)
```
## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine Pivot-Tabelle anhand datumsbezogener Kriterien wie heute, letzte Woche, diesen Monat, nächstes Quartal oder einen bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezielle Filter, die nur für Felder funktionieren, die Datum-Zeit-Informationen enthalten.
{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datum-Zeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filter_by_date(PivotFilterType, *date_times)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach gewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (bei `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# Laden der vorhandenen Arbeitsmappe, die die Pivot-Tabelle enthält
workbook = ac.Workbook(input_path)

# Zugriff auf das Arbeitsblatt, das die Pivot-Tabelle enthält (nach Index)
worksheet = workbook.worksheets[0]

# Zugriff auf die Pivot-Tabelle nach Index
pivot_table = worksheet.pivot_tables[0]

# Abrufen des Datums-PivotField aus dem Zeilenbereich
# (Datumsfilter funktioniert nur, wenn der Zeilen-/Spaltenbereich nur Datum-Uhrzeit-Zellen oder leere Zellen enthält)
date_field = pivot_table.row_fields[0]

# Definieren des Datumskriteriums für den Zwischen-Filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# Anwenden des Datumsfilters auf das Pivot-Feld
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# Aktualisieren und Neuberechnen der Pivot-Tabelle, damit der Filter wirksam wird
pivot_table.pivot_cache.refresh()

# Arbeitsmappe speichern
workbook.save(output_path)
```
## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Gesamtsummen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen nur der Produkte, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur der Regionen, deren Anzahl von Transaktionen in einen bestimmten Bereich fällt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)` bereit. Der Parameter `PivotFilterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `value_field` gibt an, welches Datenfeld ausgewertet werden soll, und das bzw. die letzten Argumente liefern den oder die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# Den Datenfeldindex manuell finden, da PivotFieldCollection kein IndexOf hat
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```
## **Top-10-Filter**
Der Top-10-Filter ist eine spezielle Form des Wertfilters, der nur die höchsten oder niedrigsten N Elemente basierend auf einem ausgewählten Wertfeld beibehält. Er wird häufig für Ranking-Berichte verwendet, wie zum Beispiel „Top-10-Produkte nach Umsatz" oder „untere 5 Regionen nach Verkaufsanzahl".
{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, gegen die die Elemente sortiert werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)` bereit. Der Parameter `item_count` definiert, wie viele Elemente beibehalten werden sollen, `is_top` gibt an, ob die obersten Elemente (True) oder die untersten Elemente (False) beibehalten werden sollen, `value_field` verweist auf das für die Rangfolge verwendete Datenfeld, und `PivotFilterType` steuert, wie der Wert berechnet wird (typischerweise `Sum`, aber auch `Count` und `Percent`).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die 10 höchsten Elemente nach der Umsatzsumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# Zugriff auf das Arbeitsblatt, das die Pivot-Tabelle enthält (Index 0)
worksheet = workbook.worksheets[0]

# Zugriff auf die Pivot-Tabelle nach Index
pivotTable = worksheet.pivot_tables[0]

# Bestätigen Sie, dass es mindestens ein Wert-PivotField im Datenbereich gibt
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# Abrufen des Ziel-Zeilen-PivotField (das Feld, auf das wir Top 10 anwenden möchten)
rowField = pivotTable.row_fields[0]

# Das erste (und einzige) Datenfeld befindet sich bei Index 0; Top 10 sortiert danach.
valueFieldIndex = 0

# Anwenden des Top-10-Filters auf das Zeilenfeld:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (obere N; false würde untere N bedeuten)
#   - valueFieldIndex = der Index des Datenfelds, das zum Sortieren der Elemente verwendet wird
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# Aktualisieren Sie die Pivot-Tabellendaten und berechnen Sie sie neu, damit der Filter wirksam wird
pivotTable.pivot_cache.refresh()

# Speichern der Arbeitsmappe
workbook.save(outputPath)
```
## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Durch Iteration über die `PivotItems`-Auflistung eines `PivotField` und Umschalten der Eigenschaft `is_hidden` können Sie gezielt bestimmte Elemente unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `is_hidden = True` blendet das Element aus der Pivot-Tabelle aus; das Setzen von `is_hidden = False` blendet es wieder ein.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, beispielsweise um eine kleine Anzahl benannter Kategorien auszublenden, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet ein bestimmtes Element nach Namen aus, demonstriert, wie es wieder eingeblendet wird, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
import aspose.cells as ac

# Laden Sie eine vorhandene Arbeitsmappe, die eine Pivot-Tabelle enthält
workbook = ac.Workbook("pivot_table_sample.xlsx")

# Zugriff auf das erste Arbeitsblatt, das die Pivot-Tabelle enthält
sheet = workbook.worksheets[0]

# Zugriff auf die Pivot-Tabelle nach Index (die erste Pivot-Tabelle auf dem Blatt)
pivot_table = sheet.pivot_tables[0]

# Abrufen des Ziel-PivotField (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden)
pivot_field = pivot_table.row_fields[0]

# Durchlaufen der PivotItems-Sammlung des ausgewählten PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # Pivot-Elemente ausblenden, die einem bestimmten Namen/Kriterium entsprechen
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # Einblenden demonstrieren: ein zuvor ausgeblendetes Pivot-Element wieder anzeigen
    if item.name == "Item3":
        item.is_hidden = False

# Aktualisieren und neu berechnen der Pivot-Tabelle, damit die Änderungen wirksam werden
pivot_table.pivot_cache.refresh()

# Arbeitsmappe speichern — ausgeblendete Elemente bleiben in den zugrunde liegenden Daten
# werden jedoch aus der angezeigten Pivot-Tabellenausgabe ausgeschlossen
workbook.save("output_pivot_filtered.xlsx")
```
## **Zusammenfassung**
Aspose.Cells for Python via .NET stellt einen vollständigen Satz an Pivot-Tabellen-Filterfunktionen bereit, die mit denen in Microsoft Excel übereinstimmen. Beschriftungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter für Ranking-Berichte zuständig ist. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.is_hidden` einen flexiblen Fallback auf Elementebene. Die Kombination dieser Strategien — beispielsweise das Anwenden eines Beschriftungsfilters und das anschließende Ausblenden bestimmter Elemente — ermöglicht es Ihnen, vollständig programmatisch präzise zugeschnittene Pivot-Tabellen-Berichte zu erstellen.
{{< app/cells/assistant language="python-net" >}}