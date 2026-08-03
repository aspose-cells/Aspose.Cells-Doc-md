---
title: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
linktitle: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
description: Aspose.Cells for Python via Java unterstützt umfassende Pivot-Tabellen-Filterfunktionen. Dieser Artikel erläutert, wie Pivot-Tabellen-Daten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- oder Einblenden von Pivot-Elementen gefiltert werden können.
keywords: Aspose.Cells, Python via Java Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells stellt fünf praktische Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten bereit. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Datum-Zeit-Zellen oder leere Zellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter zur Rangfolgebildung nach einem Wertfeld einsetzen oder einzelne Pivot-Elemente manuell über die Eigenschaft `is_hidden` aus- und einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}
## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, doch rohe Zusammenfassungen enthalten häufig weit mehr Informationen, als Sie darstellen möchten. Filtern ist der primäre Mechanismus, um eine Pivot-Tabelle auf die Zeilen, Spalten oder Werte zu reduzieren, die für einen bestimmten Bericht relevant sind. Aspose.Cells for Python via Java spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Zeilen- oder Spaltenfeldelemente basierend auf deren Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datum-Zeit-Werte (oder leere Werte) enthalten.
3. **Wertfilter** — filtert Elemente basierend auf den aggregierten Werten eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente, sortiert nach einem Wertfeld.
5. **Pivot-Elemente aus-/einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nach Anwendung eines beliebigen Filters müssen Sie `refresh_data()` und `calculate_data()` auf der Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.
## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder einem anderen beschriftungsbasierten Kriterium entsprechen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filter_by_label(PivotFilterType, str)` bereit. Die Aufzählung `PivotFilterType` umfasst Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere. Das zweite Argument liefert die Beschriftungszeichenfolge für den Vergleich.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen Pivot-Tabelle, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem bestimmten Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# Vorhandene Arbeitsmappe mit Pivot-Tabelle laden
workbook = Workbook(fileName)

# Auf das Arbeitsblatt nach Index zugreifen (erstes Arbeitsblatt)
worksheet = workbook.getWorksheets().get(0)

# Auf die Pivot-Tabelle nach Index zugreifen
pivotTable = worksheet.getPivotTables().get(0)

# Das erste Zeilen-PivotField abrufen
rowField = pivotTable.getRowFields().get(0)

# Beschriftungsfilter anwenden — nur Zeilenelemente anzeigen, deren Beschriftungen mit dem angegebenen Präfix beginnen
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# Pivot-Tabellendaten aktualisieren und neu berechnen, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh()

# Arbeitsmappe wieder auf der Festplatte speichern
workbook.save(fileName)

jpype.shutdownJVM()
```
## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine Pivot-Tabelle anhand datumsbasierter Kriterien wie heute, letzte Woche, diesen Monat, nächstes Quartal oder einen bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezialisierte Filter, die nur für Felder funktionieren, die Datum-Zeit-Informationen speichern.
{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datum-Zeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filter_by_date(PivotFilterType, values)` bereit. Die Aufzählung `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach gewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
workbook = Workbook(inputPath)

# Greifen Sie auf das Arbeitsblatt zu, das die Pivot-Tabelle enthält (nach Index)
worksheet = workbook.getWorksheets().get(0)

# Greifen Sie nach Index auf die Pivot-Tabelle zu
pivotTable = worksheet.getPivotTables().get(0)

# Abrufen des Datums-PivotField aus dem Zeilenbereich
# (Datumsfilter funktioniert nur, wenn der Zeilen-/Spaltenbereich nur Datums-/Zeitzellen oder Leerzeichen enthält)
dateField = pivotTable.getRowFields().get(0)

# Definieren Sie das Datumskriterium für den Zwischen-Filter
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# Wenden Sie den Datumsfilter auf das Pivot-Feld an
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# Aktualisieren und berechnen Sie die Pivot-Tabelle neu, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh()

# Speichern Sie die Arbeitsmappe
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen nur von Produkten, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur von Regionen, deren Transaktionsanzahl innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.filter_by_value(value_field, filter_type, values)` bereit. Der Parameter `filter_type` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `value_field` gibt an, welches Datenfeld ausgewertet werden soll, und das bzw. die letzten Argumente liefern den bzw. die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierte Verkäufe einen numerischen Schwellenwert überschreiten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# Finden Sie den Datenfeldindex manuell, da PivotFieldCollection keine IndexOf-Methode hat
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break

if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivotTable.getPivotCache().refresh()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, der nur die obersten oder untersten N Elemente basierend auf einem ausgewählten Wertfeld beibehält. Er wird häufig für Ranking-Berichte wie „Top 10 Produkte nach Umsatz" oder „Untere 5 Regionen nach Verkaufsanzahl" verwendet.
{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, gegen die die Elemente eingestuft werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filter_top10(item_count, is_top, value_field, filter_type)` bereit. Der Parameter `item_count` definiert, wie viele Elemente beibehalten werden, `is_top` gibt an, ob die obersten Elemente (true) oder die untersten Elemente (false) beibehalten werden sollen, `value_field` verweist auf das für das Ranking verwendete Datenfeld, und `filter_type` steuert, wie der Wert berechnet wird (typischerweise `Sum`, aber auch `Count` und `Percent`).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die obersten 10 Elemente nach der Verkaufssumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# Vorhandene Arbeitsmappe laden, die die Pivot-Tabelle enthält
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# Auf das Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält (Index 0)
worksheet = workbook.getWorksheets().get(0)

# Auf die Pivot-Tabelle über den Index zugreifen
pivotTable = worksheet.getPivotTables().get(0)

# Bestätigen, dass mindestens ein Wert-PivotField im Datenbereich vorhanden ist
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Die Pivot-Tabelle enthält kein Wert-PivotField (Datenfeld).")
valueField = pivotTable.getDataFields().get(0)

# Das Ziel-Zeilen-PivotField abrufen (das Feld, auf das wir Top 10 anwenden möchten)
rowField = pivotTable.getRowFields().get(0)

# Das erste (und einzige) Datenfeld befindet sich bei Index 0; Top 10 sortiert danach.
valueFieldIndex = 0

# Den Top-10-Filter auf das Zeilenfeld anwenden:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (Top N; false würde Bottom N bedeuten)
#   - valueFieldIndex = der Index des Datenfelds, das zum Sortieren der Elemente verwendet wird
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# Die Pivot-Tabellendaten aktualisieren und neu berechnen, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh()

# Die Arbeitsmappe speichern
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Neben den strukturierten Filter-APIs ermöglicht Aspose.Cells Ihnen, die Sichtbarkeit jedes einzelnen Pivot-Elements direkt zu steuern. Durch Iteration durch die Sammlung `PivotItems` eines `PivotField` und Umschalten der Eigenschaft `is_hidden` können Sie bestimmte Elemente selektiv unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `is_hidden = True` blendet das Element in der Pivot-Tabelle aus; das Setzen von `is_hidden = False` blendet es wieder ein und macht es sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa das Ausblenden einer kleinen Anzahl benannter Kategorien, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet ein bestimmtes Element nach Namen aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# Eine vorhandene Arbeitsmappe mit einer Pivot-Tabelle laden
workbook = Workbook("pivot_table_sample.xlsx")

# Auf das erste Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält
sheet = workbook.getWorksheets().get(0)

# Auf die Pivot-Tabelle nach Index zugreifen (die erste Pivot-Tabelle auf dem Blatt)
pivotTable = sheet.getPivotTables().get(0)

# Das Ziel-PivotField abrufen (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden werden)
pivotField = pivotTable.getRowFields().get(0)

# Durch die PivotItems-Sammlung des ausgewählten PivotField iterieren
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # Pivot-Elemente ausblenden, die einem bestimmten Namen/Kriterium entsprechen
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # Einblenden demonstrieren: ein zuvor ausgeblendetes Pivot-Element wieder anzeigen
    if item.getName() == "Item3":
        item.setIsHidden(False)

# Die Pivot-Tabelle aktualisieren und neu berechnen, damit die Änderungen wirksam werden
pivotTable.getPivotCache().refresh()

# Die Arbeitsmappe speichern — ausgeblendete Elemente bleiben in den zugrunde liegenden Daten
# werden jedoch aus der angezeigten Pivot-Tabellen-Ausgabe ausgeschlossen
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```
## **Zusammenfassung**
Aspose.Cells for Python via Java bietet einen vollständigen Satz von Pivot-Tabellen-Filterfunktionen, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter Ranking-Berichte verarbeitet. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.is_hidden` einen flexiblen Fallback auf Elementebene. Die Kombination dieser Strategien — etwa das Anwenden eines Beschriftungsfilters und anschließendes Ausblenden bestimmter Elemente — ermöglicht es Ihnen, präzise zugeschnittene Pivot-Tabellen-Berichte vollständig aus Code zu erstellen.
{{< app/cells/assistant language="python" >}}