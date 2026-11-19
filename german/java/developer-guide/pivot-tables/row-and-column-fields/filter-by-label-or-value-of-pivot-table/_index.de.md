---
title: PivotTables nach Beschriftung oder Wert filtern
linktitle: PivotTables nach Beschriftung oder Wert filtern
description: Aspose.Cells for Java unterstützt umfangreiche Filterfunktionen für PivotTables. Dieser Artikel erläutert, wie PivotTable-Daten mithilfe von Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- oder Einblenden von Pivot-Elementen gefiltert werden.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, PivotTable, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet fünf praktische Strategien zum Filtern der in einer PivotTable angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Zellen mit Datums-/Uhrzeitwerten oder Leerzellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter verwenden, um nach einem Wertfeld zu ordnen, oder einzelne Pivot-Elemente mithilfe der Eigenschaft `IsHidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}

## **Einführung**
PivotTables sind leistungsfähige Analysewerkzeuge, doch ungefilterte Zusammenfassungen enthalten oft weit mehr Informationen, als Sie in einem Bericht darstellen möchten. Das Filtern ist der zentrale Mechanismus, um eine PivotTable auf die für einen bestimmten Bericht relevanten Zeilen, Spalten oder Werte einzugrenzen. Aspose.Cells for Java bildet die in Microsoft Excel verfügbaren Filterfunktionen ab und stellt sie programmatisch bereit, sodass die Berichtserstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Elemente eines Zeilen- oder Spaltenfelds anhand ihrer Textbeschriftungen.
2. **Datumsfilter** — filtert die Elemente eines Zeilen- oder Spaltenfelds, das ausschließlich Datums-/Uhrzeitwerte oder Leerzellen enthält.
3. **Wertfilter** — filtert Elemente anhand der aggregierten Werte eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die N Elemente mit den höchsten beziehungsweise niedrigsten Werten, geordnet nach einem Wertfeld.
5. **Pivot-Elemente ausblenden/einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nachdem Sie einen Filter angewendet haben, müssen Sie `getPivotCache().refresh()` für die PivotTable aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterstatus berücksichtigen.

## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder ein anderes Kriterium erfüllen, das auf den Beschriftungen basiert.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filterByLabel(PivotFilterType, String)` bereit. Die Enumeration `PivotFilterType` umfasst unter anderem die Werte `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank` und `CaptionIsBlank`. Das zweite Argument ist die zum Vergleich verwendete Beschriftungszeichenfolge.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen PivotTable, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die PivotTable und speichert das Ergebnis.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Datumsfilter**
Datumsfilter ermöglichen es, eine PivotTable anhand datumsbezogener Kriterien wie dem heutigen Tag, der letzten Woche, diesem Monat, dem nächsten Quartal oder einem bestimmten Datumsbereich einzugrenzen. Hierbei handelt es sich um spezialisierte Filter, die ausschließlich für Felder funktionieren, die Datums-/Uhrzeitinformationen speichern.

{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Zellen mit Datums-/Uhrzeitwerten oder Leerzellen enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie vor dem Anwenden dieses Filters sicher, dass das Feld als Datum formatiert ist und ausschließlich gültige `DateTime`-Instanzen oder leere Zellen enthält.
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach ausgewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte. Bei `Between` übergeben Sie das Start- und Enddatum.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Wertfilter**
Wertfilter werden auf die aggregierten Werte angewendet, die im Datenbereich einer PivotTable berechnet werden. Statt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle sind die Anzeige nur solcher Produkte, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur solcher Regionen, deren Transaktionsanzahl in einem bestimmten Bereich liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` bereit. Der Parameter `filterType` kann Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual` annehmen. Der Parameter `valueField` gibt an, welches Datenfeld ausgewertet werden soll. Das letzte Argument beziehungsweise die letzten Argumente liefern den Schwellenwert beziehungsweise die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, bei der ausschließlich die N höchst- oder niedrigstplatzierten Elemente basierend auf einem ausgewählten Wertfeld beibehalten werden. Er wird häufig für Ranking-Berichte wie „die 10 umsatzstärksten Produkte“ oder „die 5 Regionen mit der niedrigsten Verkaufsanzahl“ verwendet.

{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die PivotTable im Datenbereich ein oder mehrere Wertfelder enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, nach der die Elemente geordnet werden können, und der Filter kann nicht angewendet werden.
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)` bereit. Der Parameter `valueFieldIndex` ist der Index des Datenfelds, dessen aggregierte Werte die Elemente einordnen. `filterType` legt die Einheit von `itemCount` fest (`PivotFilterType.COUNT` behält eine feste Anzahl von Elementen bei, `PivotFilterType.PERCENT` behält einen Prozentsatz der Elemente bei, sodass `itemCount` selbst der Prozentsatz ist). `isTop` gibt an, ob die obersten (true) oder untersten (false) Elemente beibehalten werden sollen, und `itemCount` legt fest, wie viele Elemente oder welcher Prozentsatz beibehalten wird.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die 10 Elemente mit der höchsten Umsatzsumme beizubehalten, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Durch Aus- oder Einblenden von Pivot-Elementen filtern**
Neben den strukturierten Filter-APIs bietet Aspose.Cells die Möglichkeit, die Sichtbarkeit jedes einzelnen Pivot-Elements direkt zu steuern. Indem Sie durch die Sammlung `PivotItems` eines `PivotField` iterieren und die Eigenschaft `IsHidden` umschalten, können Sie bestimmte Elemente gezielt ausblenden, ohne einen Filter auf Formelbasis anzuwenden. Durch Festlegen von `IsHidden = true` wird das Element aus der PivotTable ausgeblendet; durch Festlegen von `IsHidden = false` wird es eingeblendet und wieder sichtbar gemacht.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementbezogen ist, beispielsweise wenn eine kleine Anzahl Kategorien mit bestimmten Namen ausgeblendet werden soll, die in einem bestimmten Bericht nicht erscheinen dürfen. Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, blendet ein bestimmtes Element anhand seines Namens aus, demonstriert das Einblenden, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Zusammenfassung**
Aspose.Cells for Java bietet einen vollständigen Satz an Filterfunktionen für PivotTables, die den in Microsoft Excel verfügbaren Funktionen entsprechen. Beschriftungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter Ranking-Berichte ermöglicht. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` eine flexible Alternative auf Elementebene. Durch die Kombination dieser Strategien – beispielsweise indem Sie einen Beschriftungsfilter anwenden und anschließend bestimmte Elemente ausblenden – können Sie PivotTable-Berichte erstellen, die genau auf die jeweiligen Anforderungen zugeschnitten sind, und dies vollständig per Code.

## Verwandte Artikel
- [PivotTable einfügen](/cells/de/java/create-pivot-table/)
- [Zeilen- und Spaltenfelder zu einer PivotTable in Aspose.Cells for Java hinzufügen](/cells/de/java/pivot-table-add-row-and-column-fields/)
- [Filterfelder zu einer PivotTable in Aspose.Cells for Java hinzufügen](/cells/de/java/add-page-field-in-pivot-table/)
- [Wertfelder einer PivotTable in Aspose.Cells for Java verwalten](/cells/de/java/manage-value-fields/)
- [PivotTables und Pivot-Caches in Aspose.Cells for Java aktualisieren](/cells/de/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}