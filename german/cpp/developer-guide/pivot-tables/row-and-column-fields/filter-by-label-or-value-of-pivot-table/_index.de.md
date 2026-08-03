---
title: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
linktitle: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
description: Aspose.Cells for C++ unterstützt umfassende Filterfunktionen für Pivot-Tabellen. Dieser Artikel erklärt, wie Pivot-Tabellendaten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- oder Einblenden einzelner Pivot-Elemente gefiltert werden.
keywords: Aspose.Cells, C++ Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells stellt fünf praktische Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten bereit. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Datums-/Uhrzeit-Zellen oder leere Zellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter zur Rangfolge nach einem Wertfeld einsetzen oder einzelne Pivot-Elemente manuell über die Eigenschaft `IsHidden` aus- und wieder einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}
## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, doch Rohzusammenfassungen enthalten oft weitaus mehr Informationen, als Sie präsentieren möchten. Das Filtern ist der wichtigste Mechanismus, um eine Pivot-Tabelle auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for C++ spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt diese programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Elemente von Zeilen- oder Spaltenfeldern basierend auf deren Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums-/Uhrzeit-Werte (oder leere Werte) enthalten.
3. **Wertfilter** — filtert Elemente basierend auf den aggregierten Werten eines Datenfeldes.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente an, sortiert nach einem Wertfeld.
5. **Pivot-Elemente ausblenden / einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nach Anwendung eines beliebigen Filters müssen Sie `RefreshData()` und `CalculateData()` auf der Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.
## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfeldes zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder einem anderen beschriftungsbasierten Kriterium entsprechen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.FilterByLabel(PivotFilterType, const char16_t*)` bereit. Die Enumeration `PivotFilterType` enthält Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere. Das zweite Argument liefert die Beschriftungszeichenfolge für den Vergleich.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen Pivot-Tabelle, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem bestimmten Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // Lade die vorhandene Arbeitsmappe, die eine Pivot-Tabelle enthält
    Workbook wb(fileName);

    // Greife über den Index auf das Arbeitsblatt zu (erstes Arbeitsblatt)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Greife über den Index auf die Pivot-Tabelle zu
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Hole das erste Zeilen-PivotField
    PivotField rowField = pt.GetRowFields().Get(0);

    // Wende den Label-Filter an — zeige nur Zeilenelemente, deren Beschriftungen mit dem angegebenen Präfix beginnen
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // Aktualisiere und berechne die Pivot-Tabellendaten neu, damit der Filter wirksam wird
    pt.RefreshData();

    // Speichere die Arbeitsmappe zurück auf die Festplatte
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine Pivot-Tabelle nach datumsbasierten Kriterien wie heute, letzte Woche, diesem Monat, nächstes Quartal oder einem bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezielle Filter, die nur für Felder funktionieren, die Datums-/Uhrzeit-Informationen speichern.
{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Uhrzeit-Zellen oder leere Werte enthält. Wenn das zugrundeliegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach gewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
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
        // Quellarbeitsmappe nicht gefunden.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // Die vorhandene Arbeitsmappe laden, die die Pivot-Tabelle enthält
    Workbook workbook(U16String(inputPath.c_str()));

    // Auf das Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält (über den Index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auf die Pivot-Tabelle über den Index zugreifen
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Das Datums-PivotField aus dem Zeilenbereich abrufen
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Das Datumskriterium für den Zwischen-Filter definieren
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // Den Datumsfilter auf das Pivot-Feld anwenden
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // Die Pivot-Tabelle aktualisieren und neu berechnen, damit der Filter wirksam wird
    pivotTable.RefreshData();

    // Die Arbeitsmappe speichern
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Gesamtsummen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen nur der Produkte, deren Umsatzsumme einen Zielwert übersteigt, oder nur der Regionen, deren Transaktionsanzahl innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` bereit. Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `valueField` gibt an, welches Datenfeld ausgewertet werden soll, und das letzte Argument (bzw. die letzten Argumente) liefert die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

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

    pivotTable.RefreshData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Top-10-Filter**
Der Top-10-Filter ist eine spezielle Form des Wertfilters, der nur die höchsten oder niedrigsten N Elemente basierend auf einem ausgewählten Wertfeld beibehält. Er wird häufig für Rangberichte wie „Top 10 Produkte nach Umsatz" oder „Untere 5 Regionen nach Verkaufsanzahl" verwendet.
{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle über ein oder mehrere Wertfelder im Datenbereich verfügt. Ohne mindestens ein Wertfeld gibt es keine aggregierte Messgröße, gegen die die Elemente eingestuft werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` bereit. Der Parameter `itemCount` legt fest, wie viele Elemente beibehalten werden, `isTop` gibt an, ob die obersten Elemente (true) oder die untersten Elemente (false) beibehalten werden sollen, `valueField` verweist auf das für die Rangfolge verwendete Datenfeld, und `filterType` steuert, wie der Wert berechnet wird (in der Regel `Sum`, aber auch `Count` und `Percent`).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die obersten 10 Elemente nach der Umsatzsumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
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

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    pivotTable.RefreshData();

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Durch Iteration über die `PivotItems`-Sammlung eines `PivotField` und Umschalten der Eigenschaft `IsHidden` können Sie bestimmte Elemente selektiv unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `IsHidden = true` blendet das Element aus der Pivot-Tabelle aus; das Setzen von `IsHidden = false` blendet es wieder ein und macht es erneut sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa um eine kleine Anzahl benannter Kategorien auszublenden, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet ein bestimmtes Element nach Namen aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Lade eine vorhandene Arbeitsmappe, die eine Pivot-Tabelle enthält
    Workbook workbook(u"pivot_table_sample.xlsx");

    // Greife auf das erste Arbeitsblatt zu, das die Pivot-Tabelle enthält
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Greife über den Index auf die Pivot-Tabelle zu (die erste Pivot-Tabelle auf dem Blatt)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // Rufe das Ziel-PivotField ab (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden werden)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // Durchlaufe die PivotItems-Sammlung des ausgewählten PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // Blende Pivot-Elemente aus, die einem bestimmten Namen/Kriterium entsprechen
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // Demonstriere das Einblenden: zeige ein zuvor ausgeblendetes Pivot-Element erneut an
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // Aktualisiere und berechne die Pivot-Tabelle neu, damit die Änderungen wirksam werden
    pivotTable.CalculateData();

    // Speichere die Arbeitsmappe – ausgeblendete Elemente bleiben in den zugrunde liegenden Daten erhalten,
    // werden jedoch aus der angezeigten Pivot-Tabellen-Ausgabe ausgeschlossen
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Zusammenfassung**
Aspose.Cells for C++ stellt einen vollständigen Satz an Filterfunktionen für Pivot-Tabellen bereit, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter Rangberichte abdeckt. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` eine flexible, elementbezogene Ausweichmöglichkeit. Die Kombination dieser Strategien — beispielsweise das Anwenden eines Beschriftungsfilters und anschließendes Ausblenden bestimmter Elemente — ermöglicht es Ihnen, vollständig aus dem Code heraus präzise zugeschnittene Pivot-Tabellenberichte zu erstellen.
{{< app/cells/assistant language="cpp" >}}