---
title: Wie man mit C++ ein dynamisches Diagramm mit Dropdown Liste erstellt
linktitle: Dynamisches Diagramm mit Dropdown Liste erstellen
description: Erfahren Sie, wie Sie ein dynamisches Diagramm erstellen, das basierend auf der Auswahl in einer Dropdown Liste mit Aspose.Cells for C++ aktualisiert wird. Unser Schritt für Schritt Leitfaden zeigt, wie man eine Dropdown Liste in Ihr Diagramm integriert, um flexible Datenvisualisierung zu ermöglichen.
keywords: Aspose.Cells for C++, Dynamisches Diagramm, Dropdown Liste, Datenvisualisierung, Integration, flexible Visualisierung.
type: docs
weight: 76
url: /de/cpp/create-dynamic-chart-with-dropdownlist/
---

## **Mögliche Verwendungsszenarien**
Ein dynamisches Diagramm mit Dropdown-Liste in Excel ist ein leistungsfähiges Werkzeug, das es Benutzern ermöglicht, interaktive Diagramme zu erstellen, die sich basierend auf den ausgewählten Daten dynamisch aktualisieren können. Diese Funktion ist besonders nützlich in Situationen, in denen mehrere Datensätze analysiert oder verschiedene Szenarien verglichen werden müssen.

Eine häufige Anwendung eines dynamischen Diagramms mit Dropdown-Liste liegt in der Finanzanalyse. Zum Beispiel kann ein Unternehmen mehrere Finanzdatensätze für verschiedene Jahre oder Abteilungen haben. Mithilfe einer Dropdown-Liste können Benutzer den spezifischen Datensatz auswählen, den sie analysieren möchten, und das Diagramm wird automatisch aktualisiert, um die entsprechenden Informationen anzuzeigen. Dies ermöglicht einen einfachen Vergleich und die Identifizierung von Trends oder Mustern.

Eine weitere Anwendung liegt im Verkauf und Marketing. Ein Unternehmen kann Verkaufsdaten für verschiedene Produkte oder Regionen haben. Mit einem dynamischen Diagramm mit Dropdown-Liste können Benutzer ein bestimmtes Produkt oder eine bestimmte Region aus der Dropdown-Liste auswählen, und das Diagramm wird sich dynamisch aktualisieren, um die Verkaufsleistung für die ausgewählte Option anzuzeigen. Dies hilft bei der Identifizierung der leistungsstärksten Bereiche oder Produkte und bei der datengesteuerten Entscheidungsfindung.

Zusammenfassend bietet ein dynamisches Diagramm mit Dropdown-Liste in Excel eine flexible und interaktive Möglichkeit, Daten zu visualisieren und zu analysieren. Es ist in Situationen wertvoll, in denen mehrere Datensätze verglichen oder verschiedene Szenarien untersucht werden müssen, wodurch es ein vielseitiges Werkzeug für Finanzanalyse, Verkauf und Marketing sowie viele andere Anwendungen ist.

## **Verwenden Sie Aspose Cells, um ein dynamisches Diagramm mit Dropdown-Liste zu erstellen**
Im folgenden zeigen wir Ihnen, wie Sie mit Aspose.Cells ein dynamisches Diagramm mit Dropdown-Liste erstellen. Wir präsentieren den Code für das Beispiel sowie die Excel-Datei, die mit diesem Code erstellt wurde.

## **Beispielcode**
Der folgende Beispielcode wird die [Datei für das dynamische Diagramm mit Dropdown-Liste](DynamicChartWithDropdownlist.xlsx) generieren.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Anmerkungen**
In der generierten Datei zählt das Diagramm dynamisch die Daten für den ausgewählten Monat. Dies wird im Beispielcode mit der "OFFSET"-Formel durchgeführt:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Sie können versuchen, den Wert der Dropdown-Liste in Zelle "Sheet1!$A$10" zu ändern, und Sie werden die dynamische Änderung des Diagramms sehen. Jetzt haben wir erfolgreich ein dynamisches Diagramm mit Dropdown-Liste unter Verwendung von Aspose.Cells erstellt.
