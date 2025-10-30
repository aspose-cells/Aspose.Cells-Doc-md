---
title: Hur man skapar dynamiskt diagram med dropdownmeny med C++
linktitle: Skapa dynamiskt diagram med dropdownmeny
description: Lär dig hur du skapar ett dynamiskt diagram som uppdateras baserat på ett droplista val med Aspose.Cells for C++. Vår steg för steg guide visar hur du integrerar en drop down lista i ditt diagram för flexibel datavisualisering.
keywords: Aspose.Cells for C++, dynamiskt diagram, dropdownmeny, datavisualisering, integration, flexibel visualisering.
type: docs
weight: 76
url: /sv/cpp/create-dynamic-chart-with-dropdownlist/
---

## **Möjliga användningsscenario**
Ett dynamiskt diagram med rullistan i Excel är ett kraftfullt verktyg som låter användare skapa interaktiva diagram som dynamiskt kan uppdateras baserat på den valda data. Denna funktion är särskilt användbar i situationer där det finns ett behov av att analysera flera dataset eller jämföra olika scenarier.

En vanlig tillämpning av ett dynamiskt diagram med rullistan är inom finansiell analys. Till exempel kan ett företag ha flera uppsättningar av finansiella data för olika år eller avdelningar. Genom att använda en rullista kan användare välja det specifika dataset de vill analysera, och diagrammet kommer automatiskt att uppdateras för att visa den motsvarande informationen. Detta möjliggör enkel jämförelse och identifiering av trender eller mönster.

En annan tillämpning är inom försäljning och marknadsföring. Ett företag kan ha försäljningsdata för olika produkter eller regioner. Med ett dynamiskt diagram med rullista kan användare välja en specifik produkt eller region från rullistan, och diagrammet kommer dynamiskt att uppdateras för att visa försäljningsprestandan för det valda alternativet. Detta hjälper till att identifiera de bäst presterande områdena eller produkterna och fatta data-drivna beslut.

Sammanfattningsvis ger ett dynamiskt diagram med rullista i Excel ett flexibelt och interaktivt sätt att visualisera och analysera data. Det är värdefullt i situationer där det finns ett behov av att jämföra flera dataset eller utforska olika scenarier, vilket gör det till ett mångsidigt verktyg för finansiell analys, försäljning och marknadsföring samt många andra tillämpningar.

## **Använd Aspose Cells för att skapa dynamisk diagram med dropdownlista**
I de följande styckena visar vi hur du skapar ett dynamiskt diagram med dropdownlista med Aspose.Cells. Vi visar koden för exempel samt den Excel-fil som skapas med denna kod.

## **Exempelkod**
Följande exempelkod kommer att generera [Dynamic Chart with Dropdownlist File](DynamicChartWithDropdownlist.xlsx).

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

## **Anteckningar**
I den genererade filen kommer diagrammet dynamiskt att räkna data för den valda månaden. Detta görs med hjälp av "OFFSET"-formeln i provkoden:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Du kan prova att ändra värde i listrutan i cellen "Ark1!$A$10", och du kommer att se den dynamiska förändringen av diagrammet. Nu har vi skapat ett dynamiskt diagram med rullgardinsmeny med hjälp av Aspose.Cells framgångsrikt.
{{< app/cells/assistant language="cpp" >}}
