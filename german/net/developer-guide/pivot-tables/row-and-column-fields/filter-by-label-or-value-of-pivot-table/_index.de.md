---
title: Pivot-Tabellen nach Beschriftung oder Wert filtern
linktitle: Nach Beschriftung oder Wert filtern
description: Aspose.Cells for .NET unterstützt umfassende Filterfunktionen für Pivot-Tabellen. Dieser Artikel erläutert das Filtern von Pivot-Tabellen-Daten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- und Einblenden von Pivot-Elementen.
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stellt fünf praktische Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten bereit. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter für Felder verwenden, die ausschließlich Datums-/Zeit-Zellen oder leere Zellen enthalten, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter zur Rangfolge nach einem Wertfeld einsetzen oder einzelne Pivot-Elemente über die Eigenschaft `IsHidden` manuell ein- und ausblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.

{{% /alert %}}

## **Einführung**

Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, doch Rohzusammenfassungen enthalten häufig weit mehr Informationen, als Sie präsentieren möchten. Das Filtern ist der wichtigste Mechanismus, um eine Pivot-Tabelle auf die für einen bestimmten Bericht relevanten Zeilen, Spalten oder Werte einzugrenzen. Aspose.Cells for .NET bildet die in Microsoft Excel verfügbaren Filterfunktionen ab und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.

Dieser Artikel behandelt die folgenden Filterstrategien:

1. **Beschriftungsfilter** — filtert Elemente von Zeilen- oder Spaltenfeldern anhand ihrer Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums-/Zeit-Werte oder leere Werte enthalten.
3. **Wertfilter** — filtert Elemente anhand der aggregierten Werte eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente, sortiert nach einem Wertfeld.
5. **Pivot-Elemente aus-/einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.

Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nach Anwendung eines Filters müssen Sie `PivotCache.Refresh()` auf der Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.

## **Beschriftungsfilter**

Mit einem Beschriftungsfilter können Sie die Elemente eines Zeilen- oder Spaltenfelds filtern, indem Sie deren Textbeschriftungen mit einem Muster vergleichen. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder ein anderes beschriftungsbasiertes Kriterium erfüllen.

Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)` bereit. Das Argument `filterType` wählt den Vergleichsmodus aus (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere). Die Argumente `label1` und `label2` liefern den Vergleichstext. Übergeben Sie für `label2` den Wert `string.Empty`, wenn nur ein einzelner Vergleichswert benötigt wird, beispielsweise bei „beginnt mit“ oder „enthält“.

Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen Pivot-Tabelle, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);

// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.Worksheets[0];

// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];

// Retrieve the first row PivotField
PivotField rowField = pivotTable.RowFields[0];

// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.PivotCache.Refresh();

// Save the workbook back to disk
workbook.Save(fileName);
```

## **Datumsfilter**

Mit Datumsfiltern können Sie eine Pivot-Tabelle anhand datumsbasierter Kriterien wie heute, letzte Woche, diesen Monat, nächstes Quartal oder einen bestimmten Datumsbereich eingrenzen. Es handelt sich um spezialisierte Filter, die ausschließlich auf Felder angewendet werden können, die Datums-/Zeit-Informationen speichern.

{{% alert color="primary" %}}

Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Zeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie vor dem Anwenden dieses Filters sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind.

{{% /alert %}}

Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält spezielle Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach gewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte. Bei `Between` übergeben Sie das Start- und Enddatum.

Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter für einen bestimmten Datumsbereich an, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

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

// Load the existing workbook that contains the pivot table
var workbook = new Workbook(inputPath);

// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.Worksheets[0];

// Access the pivot table by index
var pivotTable = worksheet.PivotTables[0];

// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.RowFields[0];

// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Apply the date filter on the pivot field
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.PivotCache.Refresh();

// Persist the workbook
workbook.Save(outputPath);
```

## **Wertfilter**

Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle sind die Anzeige nur der Produkte, deren Verkaufssumme einen Zielwert übersteigt, oder nur der Regionen, deren Transaktionsanzahl innerhalb eines bestimmten Bereichs liegt.

Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` bereit. Der Parameter `valueFieldIndex` gibt an, welches Datenfeld ausgewertet werden soll. Bestimmen Sie die Position mit `pivotTable.DataFields.IndexOf(dataField)` oder durch Iteration über die Sammlung. Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Die beiden `double`-Argumente liefern den oder die Schwellenwerte.

Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierte Verkäufe einen numerischen Schwellenwert überschreiten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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

Der Top-10-Filter ist eine spezielle Form des Wertfilters, die nur die höchsten oder niedrigsten N Elemente auf Grundlage eines ausgewählten Wertfelds beibehält. Er wird häufig für Ranglistenberichte wie „Top 10 Produkte nach Umsatz“ oder „unterste 5 Regionen nach Verkaufsanzahl“ verwendet.

{{% alert color="primary" %}}

Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle mindestens ein Wertfeld im Datenbereich enthält. Ohne ein Wertfeld gibt es keine aggregierte Messgröße, nach der die Elemente sortiert werden können, und der Filter kann nicht angewendet werden.

{{% /alert %}}

Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)` bereit. Der Parameter `itemCount` legt fest, wie viele Elemente beibehalten werden. `filterType` steuert, wie der Wert berechnet wird, normalerweise mit `Sum`, aber auch mit `Count` oder `Percent`. `isTop` gibt an, ob die obersten (`true`) oder die untersten (`false`) Elemente beibehalten werden. `valueFieldIndex` ist der Index des Datenfelds, das zur Rangfolge der Elemente verwendet wird.

Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die 10 Elemente mit der höchsten Verkaufssumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Load the existing workbook that contains the pivot table
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.Worksheets[0];

// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];

// Confirm there is at least one value PivotField in the data area
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];

// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.RowFields[0];

// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;

// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.PivotCache.Refresh();

// Save the workbook
workbook.Save(outputPath);
```

## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**

Zusätzlich zu den strukturierten Filter-APIs können Sie mit Aspose.Cells die Sichtbarkeit jedes einzelnen Pivot-Elements direkt steuern. Indem Sie die `PivotItems`-Sammlung eines `PivotField` durchlaufen und die Eigenschaft `IsHidden` ändern, können Sie bestimmte Elemente gezielt ausblenden, ohne einen formelbasierten Filter anzuwenden. `IsHidden = true` blendet ein Element aus der Pivot-Tabelle aus, während `IsHidden = false` es wieder einblendet.

Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, beispielsweise wenn einige benannte Kategorien in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet bestimmte Elemente anhand ihres Namens aus, zeigt das erneute Einblenden, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.Worksheets[0];

// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.PivotTables[0];

// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.RowFields[0];

// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // Hide pivot items that match a specific name/criterion
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// Refresh and recalculate the pivot table so changes take effect
pivotTable.PivotCache.Refresh();

// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.Save("output_pivot_filtered.xlsx");
```

## **Zusammenfassung**

Aspose.Cells for .NET bietet einen vollständigen Satz an Filterfunktionen für Pivot-Tabellen, die den Funktionen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter Ranglistenberichte ermöglicht. Bei unregelmäßigen Filterregeln bietet die Eigenschaft `PivotItem.IsHidden` eine flexible Alternative auf Elementebene. Durch die Kombination dieser Strategien, beispielsweise durch Anwenden eines Beschriftungsfilters und anschließendes Ausblenden bestimmter Elemente, können Sie vollständig im Code präzise zugeschnittene Pivot-Tabellen-Berichte erstellen.
{{< app/cells/assistant language="csharp" >}}
