---
title: PivotTables nach Bezeichnung oder Wert filtern
linktitle: PivotTables nach Bezeichnung oder Wert filtern
description: Aspose.Cells for C++ unterstützt umfassende Filterfunktionen für PivotTables. Dieser Artikel erläutert, wie Sie PivotTable-Daten mithilfe von Bezeichnungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- oder Einblenden von Pivot-Elementen filtern.
keywords: Aspose.Cells, C++-Bibliothek, Kalkulationstabelle, PivotTable, Filter, Bezeichnungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet fünf praktische Strategien zum Filtern der in einer PivotTable angezeigten Daten. Sie können Bezeichnungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Zellen mit Datums-/Uhrzeitangaben oder Leerzellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter zur Rangierung nach einem Wertfeld einsetzen oder einzelne Pivot-Elemente mithilfe der Eigenschaft `IsHidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs in den Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}

## **Einleitung**
PivotTables sind leistungsstarke Analysewerkzeuge, unaufbereitete Zusammenfassungen enthalten jedoch oft weit mehr Informationen, als Sie darstellen möchten. Filtern ist der wichtigste Mechanismus, um eine PivotTable auf die für einen bestimmten Bericht relevanten Zeilen, Spalten oder Werte einzugrenzen. Aspose.Cells for C++ bildet die in Microsoft Excel verfügbaren Filterfunktionen ab und stellt sie programmatisch bereit, sodass die Berichtserstellung vollständig automatisiert werden kann.
In diesem Artikel werden die folgenden Filterstrategien behandelt:
1. **Bezeichnungsfilter** — filtert Elemente eines Zeilen- oder Spaltenfelds anhand ihrer Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums-/Uhrzeitwerte oder Leerzellen enthalten.
3. **Wertfilter** — filtert Elemente anhand der aggregierten Werte eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die N höchsten oder niedrigsten Elemente an, die anhand eines Wertfelds rangiert sind.
5. **Pivot-Elemente aus-/einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine jeweils andere Methode der Klasse `PivotField` bzw. eine Eigenschaft der Klasse `PivotItem`. Nach dem Anwenden eines Filters müssen Sie `GetPivotCache().Refresh()` für die PivotTable aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterstatus berücksichtigen.

## **Bezeichnungsfilter**
Ein Bezeichnungsfilter ermöglicht es, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem ihre Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder ein anderes auf der Beschriftung basierendes Kriterium erfüllen.
Aspose.Cells stellt die Bezeichnungsfilterung über die Methode `PivotField.FilterByLabel(PivotFilterType, const char16_t*)` bereit. Die Enumeration `PivotFilterType` umfasst Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` usw. Das zweite Argument ist die zum Vergleich verwendete Bezeichnungszeichenfolge.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen PivotTable, wendet einen Bezeichnungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die PivotTable und speichert das Ergebnis.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Datumsfilter**
Datumsfilter ermöglichen es, eine PivotTable anhand von Datumskriterien wie dem heutigen Tag, der letzten Woche, diesem Monat, dem nächsten Quartal oder einem bestimmten Zeitraum einzugrenzen. Es sind spezialisierte Filter, die nur mit Feldern funktionieren, in denen Datums-/Uhrzeitinformationen gespeichert sind.

{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Zellen mit Datums-/Uhrzeitangaben oder Leerzellen enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` bereit. Die Enumeration `PivotFilterType` enthält spezielle Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach ausgewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte; bei `Between` übergeben Sie das Start- und Enddatum.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Zeitraum beschränkt, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Wertfilter**
Wertfilter wirken auf die aggregierten Werte, die eine PivotTable in ihrem Datenbereich berechnet. Statt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle umfassen die Anzeige nur von Produkten, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur von Regionen, deren Anzahl der Transaktionen in einem bestimmten Bereich liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` bereit. Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `valueField` legt fest, welches Datenfeld ausgewertet werden soll, und das letzte Argument bzw. die letzten Argumente liefern die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, die auf Grundlage eines ausgewählten Wertfelds nur die N höchsten oder niedrigsten Elemente beibehält. Er wird häufig für Ranking-Berichte wie „Top 10 Produkte nach Umsatz“ oder „Bottom 5 Regionen nach Verkaufsanzahl“ verwendet.

{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die PivotTable im Datenbereich ein oder mehrere Wertfelder enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, anhand der die Elemente rangiert werden können, und der Filter kann nicht angewendet werden.
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)` bereit. Der Parameter `valueFieldIndex` ist der Index des Datenfelds, dessen aggregierte Werte die Elemente einordnen. `type` legt die Einheit von `itemCount` fest: `PivotFilterType::Count` behält eine feste Anzahl von Elementen bei, während `PivotFilterType::Percent` einen Prozentsatz der Elemente beibehält, sodass `itemCount` selbst der Prozentsatz ist. `isTop` gibt an, ob die höchsten (`true`) oder die niedrigsten Elemente (`false`) beibehalten werden sollen, und `itemCount` legt fest, wie viele Elemente oder welcher Prozentsatz beibehalten werden soll.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die zehn höchsten Elemente nach der Umsatzsumme beizubehalten, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Pivot-Elemente aus- oder einblenden**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Indem Sie die `PivotItems`-Sammlung eines `PivotField` durchlaufen und die Eigenschaft `IsHidden` umschalten, können Sie bestimmte Elemente gezielt ausblenden, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `IsHidden = true` blendet das Element aus der PivotTable aus; das Setzen von `IsHidden = false` blendet es wieder ein und macht es sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementbezogen ist, beispielsweise wenn eine kleine Anzahl benannter Kategorien, die in einem bestimmten Bericht nicht erscheinen dürfen, ausgeblendet werden soll. Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, blendet ein bestimmtes Element anhand seines Namens aus, demonstriert das Einblenden, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Zusammenfassung**
Aspose.Cells for C++ bietet einen vollständigen Satz an PivotTable-Filterfunktionen, die den in Microsoft Excel verfügbaren entsprechen. Bezeichnungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter für Ranking-Berichte geeignet ist. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` eine flexible Alternative auf Elementebene. Die Kombination dieser Strategien – beispielsweise das Anwenden eines Bezeichnungsfilters und das anschließende Ausblenden bestimmter Elemente – ermöglicht es Ihnen, mithilfe von Code präzise zugeschnittene PivotTable-Berichte zu erstellen.

## Verwandte Artikel
- [PivotTable einfügen](/cells/de/cpp/create-pivot-table/)
- [Zeilen- und Spaltenfelder zu einer PivotTable in Aspose.Cells for C++ hinzufügen](/cells/de/cpp/pivot-table-add-row-and-column-fields/)
- [Filterfelder zu einer PivotTable in Aspose.Cells for C++ hinzufügen](/cells/de/cpp/add-page-field-in-pivot-table/)
- [Wertfelder einer PivotTable in Aspose.Cells for C++ verwalten](/cells/de/cpp/manage-value-fields/)
- [PivotTables und Pivot-Caches in Aspose.Cells for C++ aktualisieren](/cells/de/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}