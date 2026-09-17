---
title: Pivot-Tabellen nach Beschriftung oder Wert filtern
linktitle: Pivot-Tabellen nach Beschriftung oder Wert filtern
description: Aspose.Cells for Python via .NET unterstützt umfassende Filterfunktionen für Pivot-Tabellen. Dieser Artikel erklärt, wie Pivot-Tabellendaten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern und durch Aus- oder Einblenden einzelner Pivot-Elemente gefiltert werden.
keywords: Aspose.Cells, Python via .NET-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stellt fünf praktische Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten bereit. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Datums-/Uhrzeit-Zellen oder leere Zellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter verwenden, um nach einem Wertfeld zu ordnen, oder einzelne Pivot-Elemente mithilfe der Eigenschaft `is_hidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` verfügbar gemacht.
{{% /alert %}}

## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, aber rohe Zusammenfassungen enthalten häufig weit mehr Informationen, als Sie präsentieren möchten. Das Filtern ist der primäre Mechanismus, um eine Pivot-Tabelle auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for Python via .NET spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Zeilen- oder Spaltenfeldelemente basierend auf deren Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums-/Uhrzeit-Werte (oder leere Werte) enthalten.
3. **Wertfilter** — filtert Elemente basierend auf den aggregierten Werten eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente an, sortiert nach einem Wertfeld.
5. **Pivot-Elemente aus-/einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nach dem Anwenden eines Filters müssen Sie `refresh_data()` und `calculate_data()` auf der Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.

## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder einem anderen beschriftungsbasierten Kriterium entsprechen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filter_by_label(PivotFilterType, label_string)` bereit. Die Enumeration `PivotFilterType` enthält Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere. Das zweite Argument liefert die Beschriftungszeichenfolge, die für den Vergleich verwendet wird.
Das folgende Beispiel lädt eine Arbeitsmappe, die eine vorhandene Pivot-Tabelle enthält, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.

```python
import aspose.cells as ac
fileName = "sample.xlsx"
prefix = "B"
# Laden der vorhandenen Arbeitsmappe, die eine Pivot-Tabelle enthält
workbook = ac.Workbook(fileName)
# Zugriff auf das Arbeitsblatt nach Index (erstes Arbeitsblatt)
worksheet = workbook.worksheets[0]
# Zugriff auf die Pivot-Tabelle nach Index
pivot_table = worksheet.pivot_tables[0]
# Abrufen des ersten Zeilen-PivotFields
row_field = pivot_table.row_fields[0]
# Anwenden des Beschriftungsfilters – nur Zeilenelemente anzeigen, deren Beschriftungen mit dem angegebenen Präfix beginnen
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Aktualisieren und Neuberechnen der Pivot-Tabellen-Daten, damit der Filter wirksam wird
pivot_table.pivot_cache.refresh()
# Speichern der Arbeitsmappe zurück auf die Festplatte
workbook.save(fileName)
```

## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine Pivot-Tabelle anhand datumsbasierter Kriterien wie heute, letzte Woche, diesen Monat, nächstes Quartal oder einen bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezialisierte Filter, die nur für Felder funktionieren, die Datums-/Uhrzeit-Informationen speichern.

{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Uhrzeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und dass alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}

Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filter_by_date(PivotFilterType, *date_times)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach gewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```python
from datetime import datetime
input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"
if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)
# Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
workbook = ac.Workbook(input_path)
# Greifen Sie auf das Arbeitsblatt zu, das die Pivot-Tabelle enthält (nach Index)
worksheet = workbook.worksheets[0]
# Greifen Sie über den Index auf die Pivot-Tabelle zu
pivot_table = worksheet.pivot_tables[0]
# Rufen Sie das Datums-PivotField aus dem Zeilenbereich ab
# (Datumsfilter funktioniert nur, wenn der Zeilen-/Spaltenbereich nur Datums-/Uhrzeit-Zellen oder leere Zellen enthält)
date_field = pivot_table.row_fields[0]
# Definieren Sie das Datumskriterium für den Zwischen-Filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
# Wenden Sie den Datumsfilter auf das Pivot-Feld an
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)
# Aktualisieren und berechnen Sie die Pivot-Tabelle neu, damit der Filter wirksam wird
pivot_table.pivot_cache.refresh()
# Speichern Sie die Arbeitsmappe
workbook.save(output_path)
```

## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen von Produkten, deren Umsatzsumme einen Zielbetrag übersteigt, oder von Regionen, deren Transaktionsanzahl innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)` bereit. Der Parameter `PivotFilterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `value_field` gibt an, welches Datenfeld ausgewertet werden soll, und das letzte Argument (bzw. die letzten Argumente) liefert den Schwellenwert (bzw. die Schwellenwerte).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```python
import aspose.cells as ac
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]
row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]
# Da PivotFieldCollection keine IndexOf-Methode besitzt, wird der Index des Datenfelds manuell ermittelt
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
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, der nur die höchsten oder niedrigsten N Elemente basierend auf einem ausgewählten Wertfeld beibehält. Er wird häufig für Ranking-Berichte wie „Top-10-Produkte nach Umsatz" oder „Untere 5 Regionen nach Verkaufsanzahl" verwendet.

{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, gegen die die Elemente eingestuft werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}

Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)` bereit. Der Parameter `item_count` definiert, wie viele Elemente beibehalten werden sollen, `is_top` gibt an, ob die obersten Elemente (True) oder die untersten Elemente (False) beibehalten werden sollen, `value_field` verweist auf das für das Ranking verwendete Datenfeld, und `PivotFilterType` steuert, wie der Wert berechnet wird (typischerweise `Sum`, aber auch `Count` und `Percent`).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die obersten 10 Elemente nach der Umsatzsumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
# Laden der vorhandenen Arbeitsmappe, die die Pivot-Tabelle enthält
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)
# Zugriff auf das Arbeitsblatt, das die Pivot-Tabelle enthält (Index 0)
worksheet = workbook.worksheets[0]
# Zugriff auf die Pivot-Tabelle über den Index
pivotTable = worksheet.pivot_tables[0]
# Sicherstellen, dass mindestens ein Wert-PivotField im Datenbereich vorhanden ist
if pivotTable.data_fields.count == 0:
    raise Exception("Die Pivot-Tabelle enthält kein Wert-PivotField.")
valueField = pivotTable.data_fields[0]
# Abrufen des Ziel-Zeilen-PivotFields (das Feld, auf das Top 10 angewendet werden soll)
rowField = pivotTable.row_fields[0]
# Das erste (und einzige) Datenfeld befindet sich am Index 0; Top 10 ordnet danach.
valueFieldIndex = 0
# Anwenden des Top-10-Filters auf das Zeilenfeld:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (Top N; false würde Bottom N bedeuten)
#   - valueFieldIndex = der Index des Datenfelds, das zum Sortieren verwendet wird
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)
# Aktualisieren der Pivot-Tabellen-Daten und Neuberechnung, damit der Filter wirksam wird
pivotTable.pivot_cache.refresh()
# Speichern der Arbeitsmappe
workbook.save(outputPath)
```

## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Durch Iteration durch die `PivotItems`-Sammlung eines `PivotField` und Umschalten der Eigenschaft `is_hidden` können Sie bestimmte Elemente gezielt unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `is_hidden = True` blendet das Element aus der Pivot-Tabelle aus; das Setzen von `is_hidden = False` blendet es wieder ein und macht es sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa beim Ausblenden einer kleinen Anzahl benannter Kategorien, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet ein bestimmtes Element nach Namen aus, demonstriert, wie es wieder eingeblendet wird, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```python
import aspose.cells as ac
# Laden Sie eine vorhandene Arbeitsmappe, die eine Pivot-Tabelle enthält
workbook = ac.Workbook("pivot_table_sample.xlsx")
# Greifen Sie auf das erste Arbeitsblatt zu, das die Pivot-Tabelle enthält
sheet = workbook.worksheets[0]
# Greifen Sie über den Index auf die Pivot-Tabelle zu (die erste Pivot-Tabelle auf dem Blatt)
pivot_table = sheet.pivot_tables[0]
# Rufen Sie das Ziel-PivotField ab (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden)
pivot_field = pivot_table.row_fields[0]
# Durchlaufen Sie die PivotItems-Sammlung des ausgewählten PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]
    # Blenden Sie Pivot-Elemente aus, die einem bestimmten Namen/Kriterium entsprechen
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True
    # Demonstrieren Sie das Einblenden: Zeigen Sie ein zuvor ausgeblendetes Pivot-Element wieder an
    if item.name == "Item3":
        item.is_hidden = False
# Aktualisieren und berechnen Sie die Pivot-Tabelle neu, damit die Änderungen wirksam werden
pivot_table.pivot_cache.refresh()
# Speichern Sie die Arbeitsmappe – ausgeblendete Elemente bleiben in den zugrunde liegenden Daten
# werden jedoch aus der angezeigten Pivot-Tabellen-Ausgabe ausgeschlossen
workbook.save("output_pivot_filtered.xlsx")
```

## **Zusammenfassung**
Aspose.Cells for Python via .NET stellt einen vollständigen Satz an Filterfunktionen für Pivot-Tabellen bereit, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertfilter decken die gängigsten Analyseszenarien ab, während der Top-10-Filter Ranking-Berichte handhabt. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.is_hidden` einen flexiblen Fallback auf Elementebene. Die Kombination dieser Strategien — beispielsweise die Anwendung eines Beschriftungsfilters und anschließendes Ausblenden bestimmter Elemente — ermöglicht es Ihnen, präzise zugeschnittene Pivot-Tabellen-Berichte vollständig aus Code zu erstellen.

## Verwandte Artikel
- [Pivot-Tabelle einfügen](/cells/de/python-net/pivot-tables/)
- [Zeilen- und Spaltenfelder zu einer Pivot-Tabelle in Aspose.Cells for Python via .NET hinzufügen](/cells/de/python-net/pivot-table-add-row-and-column-fields/)
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for Python via .NET hinzufügen](/cells/de/python-net/add-page-field-in-pivot-table/)
- [Wertfelder einer Pivot-Tabelle in Aspose.Cells for Python via .NET verwalten](/cells/de/python-net/manage-value-fields/)
- [Pivot-Tabellen und Pivot-Caches in Aspose.Cells for Python via .NET aktualisieren](/cells/de/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}