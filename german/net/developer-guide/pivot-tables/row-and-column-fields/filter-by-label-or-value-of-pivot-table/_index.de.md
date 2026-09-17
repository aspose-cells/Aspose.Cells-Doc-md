---
title: Pivot-Tabellen nach Beschriftung oder Wert filtern
description: Aspose.Cells for .NET unterstützt umfassende Filterfunktionen für Pivot-Tabellen. Dieser Artikel erklärt, wie Pivot-Tabellen-Daten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern und durch Aus- oder Einblenden einzelner Pivot-Elemente gefiltert werden.
linktitle: Filtern nach Beschriftung oder Wert
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet fünf praktische Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld nur Datums-/Uhrzeit-Zellen oder Leerwerte enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter nutzen, um nach einem Wertfeld zu ordnen, oder einzelne Pivot-Elemente mithilfe der `IsHidden`-Eigenschaft manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}

## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, aber Rohzusammenfassungen enthalten oft weit mehr Informationen, als Sie präsentieren möchten. Das Filtern ist der primäre Mechanismus, um eine Pivot-Tabelle auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for .NET spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Elemente von Zeilen- oder Spaltenfeldern basierend auf deren Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die nur Datums-/Uhrzeit-Werte (oder Leerwerte) enthalten.
3. **Wertfilter** — filtert Elemente basierend auf den aggregierten Werten eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente, sortiert nach einem Wertfeld.
5. **Pivot-Elemente aus-/einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nachdem Sie einen Filter angewendet haben, müssen Sie `PivotCache.Refresh()` für die Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.

## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder ein anderes beschriftungsbasiertes Kriterium erfüllen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)` bereit. Das Argument `filterType` wählt den Vergleichsmodus (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` usw.). Die Argumente `label1` und `label2` liefern den Vergleichstext — übergeben Sie `string.Empty` für `label2`, wenn Sie nur einen Einzelwertabgleich benötigen (z. B. beginnt mit oder enthält).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen Pivot-Tabelle, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string fileName = "sample.xlsx";
string prefix = "B";
// Laden Sie die vorhandene Arbeitsmappe mit einer Pivot-Tabelle
Workbook workbook = new Workbook(fileName);
// Zugriff auf das Arbeitsblatt nach Index (erstes Arbeitsblatt)
Worksheet worksheet = workbook.Worksheets[0];
// Zugriff auf die Pivot-Tabelle nach Index
PivotTable pivotTable = worksheet.PivotTables[0];
// Abrufen des ersten Zeilen-PivotField
PivotField rowField = pivotTable.RowFields[0];
// Anwenden des Beschriftungsfilters – nur Zeilenelemente anzeigen, deren Beschriftungen mit dem angegebenen Präfix beginnen
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);
// Aktualisieren und Neuberechnen der Pivot-Tabellendaten, damit der Filter wirksam wird
pivotTable.PivotCache.Refresh();
// Speichern der Arbeitsmappe zurück auf die Festplatte
workbook.Save(fileName);
```

## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine Pivot-Tabelle nach datumsbasierten Kriterien wie heute, letzte Woche, diesen Monat, nächstes Quartal oder einem bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezialisierte Filter, die nur für Felder funktionieren, die Datums-/Uhrzeit-Informationen speichern.

{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Uhrzeit-Zellen oder Leerwerte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und dass alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}

Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach gewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";
if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}
// Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
var workbook = new Workbook(inputPath);
// Zugriff auf das Arbeitsblatt, das die Pivot-Tabelle enthält (nach Index)
var worksheet = workbook.Worksheets[0];
// Zugriff auf die Pivot-Tabelle nach Index
var pivotTable = worksheet.PivotTables[0];
// Abrufen des Datums-PivotField aus dem Zeilenbereich
// (Der Datumsfilter funktioniert nur, wenn der Zeilen-/Spaltenbereich nur Datums-/Uhrzeit-Zellen oder Leerzeichen enthält)
PivotField dateField = pivotTable.RowFields[0];
// Definieren des Datumskriteriums für den Zwischen-Filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Anwenden des Datumsfilters auf das Pivot-Feld
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// Aktualisieren und Neuberechnen der Pivot-Tabelle, damit der Filter wirksam wird
pivotTable.PivotCache.Refresh();
// Speichern der Arbeitsmappe
workbook.Save(outputPath);
```

## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen nur von Produkten, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur von Regionen, deren Transaktionsanzahl innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` bereit. Der Parameter `valueFieldIndex` gibt an, welches Datenfeld ausgewertet werden soll (verwenden Sie `pivotTable.DataFields.IndexOf(dataField)` oder durchlaufen Sie die Auflistung, um die Position zu finden). Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Die beiden `double`-Argumente liefern den oder die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];
var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];
// Datenfeldindex manuell finden, da PivotFieldCollection keine IndexOf-Methode besitzt
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}
pivotTable.PivotCache.Refresh();
workbook.Save("output.xlsx");
```

## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, der nur die höchsten oder niedrigsten N Elemente basierend auf einem ausgewählten Wertfeld beibehält. Er wird häufig für Ranking-Berichte wie „Top-10-Produkte nach Umsatz" oder „Untere 5 Regionen nach Verkaufsanzahl" verwendet.

{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Messgröße, gegen die die Elemente eingestuft werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}

Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)` bereit. Der Parameter `itemCount` definiert, wie viele Elemente beibehalten werden sollen, `filterType` steuert, wie der Wert berechnet wird (typischerweise `Sum`, aber auch `Count` und `Percent`), `isTop` gibt an, ob die obersten Elemente (true) oder die untersten Elemente (false) beibehalten werden sollen, und `valueFieldIndex` ist der Index des Datenfelds, das zum Einstufen der Elemente verwendet wird.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die obersten 10 Elemente nach der Umsatzsumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Zugriff auf das Arbeitsblatt, das die Pivot-Tabelle enthält (Index 0)
Worksheet worksheet = workbook.Worksheets[0];
// Zugriff auf die Pivot-Tabelle nach Index
PivotTable pivotTable = worksheet.PivotTables[0];
// Stellen Sie sicher, dass mindestens ein Wert-PivotField im Datenbereich vorhanden ist
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];
// Abrufen des Ziel-Zeilen-PivotFields (das Feld, auf das wir Top 10 anwenden möchten)
PivotField rowField = pivotTable.RowFields[0];
// Das erste (und einzige) Datenfeld befindet sich bei Index 0; Top 10 ordnet danach.
int valueFieldIndex = 0;
// Anwenden des Top-10-Filters auf das Zeilenfeld:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (obere N; false würde untere N bedeuten)
//   - valueFieldIndex = der Index des Datenfelds, das zum Rangordnen der Elemente verwendet wird
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);
// Aktualisieren Sie die Pivot-Tabellendaten und berechnen Sie sie neu, damit der Filter wirksam wird
pivotTable.PivotCache.Refresh();
// Speichern der Arbeitsmappe
workbook.Save(outputPath);
```

## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Indem Sie durch die Auflistung `PivotItems` eines `PivotField` iterieren und die Eigenschaft `IsHidden` umschalten, können Sie bestimmte Elemente selektiv unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `IsHidden = true` blendet das Element aus der Pivot-Tabelle aus; das Setzen von `IsHidden = false` blendet es wieder ein und macht es wieder sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa das Ausblenden einer kleinen Anzahl benannter Kategorien, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet ein bestimmtes Element nach Namen aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Eine vorhandene Arbeitsmappe mit Pivot-Tabelle laden
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Auf das erste Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält
Worksheet sheet = workbook.Worksheets[0];
// Auf die Pivot-Tabelle nach Index zugreifen (die erste Pivot-Tabelle auf dem Blatt)
PivotTable pivotTable = sheet.PivotTables[0];
// Das Ziel-PivotField abrufen (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden werden)
PivotField pivotField = pivotTable.RowFields[0];
// Durch die PivotItems-Auflistung des ausgewählten PivotField iterieren
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];
    // Pivot-Elemente ausblenden, die einem bestimmten Namen/Kriterium entsprechen
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }
    // Einblenden demonstrieren: Ein zuvor ausgeblendetes Pivot-Element wieder anzeigen
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}
// Die Pivot-Tabelle aktualisieren und neu berechnen, damit die Änderungen wirksam werden
pivotTable.PivotCache.Refresh();
// Die Arbeitsmappe speichern – ausgeblendete Elemente bleiben in den zugrunde liegenden Daten erhalten,
// werden jedoch aus der angezeigten Pivot-Tabellen-Ausgabe ausgeschlossen
workbook.Save("output_pivot_filtered.xlsx");
```

## **Zusammenfassung**
Aspose.Cells for .NET bietet einen vollständigen Satz von Filterfunktionen für Pivot-Tabellen, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertfilter decken die gängigsten Analyseszenarien ab, während der Top-10-Filter Ranking-Berichte verarbeitet. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` einen flexiblen Fallback auf Elementebene. Durch die Kombination dieser Strategien — etwa das Anwenden eines Beschriftungsfilters und anschließendes Ausblenden bestimmter Elemente — können Sie vollständig aus Code heraus präzise zugeschnittene Pivot-Tabellen-Berichte erstellen.

## Verwandte Artikel
- [Hinzufügen von Zeilen- und Spaltenfeldern zu Pivot-Tabellen in Aspose.Cells for .NET](/cells/de/net/pivot-table-add-row-and-column-fields/)
- [Verwalten von Wertfeldern in Pivot-Tabellen in Aspose.Cells for .NET](/cells/de/net/manage-value-fields/)
- [Aktualisieren von Pivot-Tabellen und Pivot-Caches in Aspose.Cells for .NET](/cells/de/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}