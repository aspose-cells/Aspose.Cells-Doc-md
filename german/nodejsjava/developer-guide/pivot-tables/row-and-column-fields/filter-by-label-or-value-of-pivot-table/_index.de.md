---
title: Pivot-Tabellen nach Beschriftung oder Wert filtern
description: Aspose.Cells for Node.js via Java unterstützt umfassende Pivot-Tabellen-Filterfunktionen. Dieser Artikel erklärt, wie Pivot-Tabellen-Daten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern und durch Aus- oder Einblenden von Pivot-Elementen gefiltert werden.
linktitle: Filtern nach Beschriftung oder Wert
url: /de/nodejs-java/filter-by-label-or-value-of-pivot-table/
keywords: Aspose.Cells, Node.js via Java Bibliothek, Tabellenkalkulation, PivotTable, Filter, Beschriftungsfilter, Wertefilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet fünf praxisorientierte Strategien zum Filtern der in einer PivotTable angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Datums-/Uhrzeit-Zellen oder leere Zellen enthält, Wertefilter auf aggregierte Zahlen anwenden, Top-10-Filter zum Rangordnen nach einem Wertefeld einsetzen oder einzelne Pivot-Elemente über die Eigenschaft `IsHidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}

## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, aber rohe Zusammenfassungen enthalten häufig weitaus mehr Informationen, als Sie darstellen müssen. Filtern ist der primäre Mechanismus, um eine PivotTable auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for Node.js via Java spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** – filtert Elemente von Zeilen- oder Spaltenfeldern anhand ihrer Textbeschriftungen.
2. **Datumsfilter** – filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums-/Uhrzeit-Werte (oder leere Werte) enthalten.
3. **Wertefilter** – filtert Elemente basierend auf den aggregierten Werten eines Datenfelds.
4. **Top-10-Filter** – zeigt nur die obersten oder untersten N Elemente, geordnet nach einem Wertefeld.
5. **Pivot-Elemente aus- / einblenden** – steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nachdem ein beliebiger Filter angewendet wurde, müssen Sie `getPivotCache().refresh()` auf der PivotTable aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.

## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder einem anderen beschriftungsbasierten Kriterium entsprechen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filterByLabel(PivotFilterType, string)` bereit. Die Enumeration `PivotFilterType` enthält Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere. Das zweite Argument liefert die Beschriftungszeichenfolge für den Vergleich.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen PivotTable, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die PivotTable und speichert das Ergebnis.

```javascript
const AsposeCells = require("aspose.cells");
let fileName = "sample.xlsx";
let prefix = "B";
// Load the existing workbook containing a pivot table
let workbook = new AsposeCells.Workbook(fileName);
// Access the worksheet by index (first worksheet)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
let rowField = pivotTable.getRowFields().get(0);
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(AsposeCells.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine PivotTable anhand datumsbezogener Kriterien wie heute, letzte Woche, diesen Monat, nächstes Quartal oder einen bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezialisierte Filter, die nur für Felder funktionieren, die Datums-/Uhrzeit-Informationen speichern.

{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Uhrzeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und dass alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Abhängig vom gewählten Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
var pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
let dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Wertefilter**
Wertefilter arbeiten mit den aggregierten Werten, die eine PivotTable in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Gesamtsummen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen nur von Produkten, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur von Regionen, deren Anzahl an Transaktionen innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertefilterung über die Methode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` bereit. Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `valueField` legt fest, welches Datenfeld ausgewertet werden soll, und das bzw. die letzten Argumente liefern den bzw. die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, wendet einen Wertefilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);
var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.VALUE_GREATER_THAN, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, der nur die höchsten oder niedrigsten N Elemente basierend auf einem ausgewählten Wertefeld beibehält. Er wird häufig für Rangordnungsberichte wie „Top 10 Produkte nach Umsatz" oder „Untere 5 Regionen nach Verkaufsanzahl" verwendet.

{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die PivotTable ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertefeld gibt es keine aggregierte Messgröße, gegen die die Elemente geordnet werden können, und der Filter kann nicht angewendet werden.
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)` bereit. Der Parameter `valueFieldIndex` ist der Index des Datenfelds, dessen aggregierte Werte die Elemente reihenfolgen, `filterType` wählt die Einheit von `itemCount` (`PivotFilterType.COUNT` behält eine feste Anzahl von Elementen, `PivotFilterType.PERCENT` behält einen Prozentsatz der Elemente, sodass `itemCount` der Prozentsatz selbst ist), `isTop` gibt an, ob die obersten (true) oder die untersten (false) Elemente behalten werden, und `itemCount` legt fest, wie viele Elemente oder welcher Prozentsatz erhalten bleibt.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, die ein Wertefeld enthält, wendet einen Top-10-Filter an, um nur die 10 höchsten Elemente nach der Summe der Verkäufe beizubehalten, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
let rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
let valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Durch Iteration über die Sammlung `PivotItems` eines `PivotField` und Umschalten der Eigenschaft `IsHidden` können Sie bestimmte Elemente selektiv unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `IsHidden = true` blendet das Element aus der PivotTable aus; das Setzen von `IsHidden = false` blendet es wieder ein und macht es sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa beim Ausblenden einer kleinen Anzahl benannter Kategorien, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine PivotTable, blendet ein bestimmtes Element anhand seines Namens aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
let sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
let pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
let pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3") {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Zusammenfassung**
Aspose.Cells for Node.js via Java stellt einen vollständigen Satz an Pivot-Tabellen-Filterfunktionen bereit, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertefilter decken die gängigsten Analyseszenarien ab, während der Top-10-Filter Rangordnungsberichte verarbeitet. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` eine flexible, elementbezogene Rückfalloption. Die Kombination dieser Strategien – beispielsweise das Anwenden eines Beschriftungsfilters und das anschließende Ausblenden bestimmter Elemente – ermöglicht es Ihnen, vollständig aus Code heraus präzise zugeschnittene Pivot-Tabellen-Berichte zu erstellen.

{{< app/cells/assistant language="nodejs-java" >}}