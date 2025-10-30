---
title: Hur man lägger till ett PivotDiagram med C++
linktitle: Pivotdiagram
type: docs
weight: 100
url: /sv/cpp/how-to-add-pivot-chart/
description: Hur man lägger till ett PivotDiagram med Aspose.Cells med C++.
keywords: PivotChart
---

## Vad är PivotChart

Ett pivotdiagram är en visuell representation av datan i en pivottabell. Pivotdiagram ger ett sätt att sammanfatta, analysera, utforska och presentera summerad data. Här är några nyckelfunktioner och aspekter av pivotdiagram:

1. **Dynamisk datarapportering**: Pivotdiagram uppdateras automatiskt för att återspegla förändringar i pivottabellen. Om du lägger till eller tar bort fält i pivottabellen, uppdateras pivotdiagrammet därefter.

1. **Interaktiv**: Pivotdiagram är interaktiva, vilket tillåter användare att filtrera, sortera och fördjupa sig i data. Detta gör det enkelt att utforska olika aspekter av datamängden.

1. **Flexibelt layout**: Användare kan ändra layouten på pivotdiagrammet genom att dra och släppa fält, vilket ger flexibilitet i hur data visualiseras.

1. **Olika diagramtyper**: Pivotdiagram kan skapas med olika diagramtyper som stapeldiagram, linjediagram, cirkeldiagram och fler, beroende på datans natur och insseiten du vill få.

1. **Sammanfattning**: Pivotdiagram sammanfattar stora datamängder och kan visa totalsummor, medelvärden, antal eller andra sammanfattande statistik.

1. **Filtrering**: De erbjuder filtreringsmöjligheter, vilket gör att du kan visa endast den data som uppfyller vissa kriterier.

<br>
Pivotdiagram används ofta inom affärsintelligens och dataanalys för att ge en tydlig och koncis visuell sammanfattning av komplexa datamängder. De är ett kraftfullt verktyg för datadrivna beslut.

## Hur man lägger till en PivotChart med hjälp av Aspose.Cells

### **Lägga till en pivottabell**

För att skapa en pivot tabell med Aspose.Cells:

1. Lägg till data i ett kalkylblad med hjälp av `Cell`-objektets `PutValue` eller `SetValue` metod. Du kan också använda en mallfil som redan är ifylld med data. Data kommer att användas som datakälla för pivot-tabellen.
1. Lägg till en pivot-tabell i kalkylbladet genom att anropa `PivotTables`-samlingen `Add`-metod (inkapslad i `Worksheet`-objektet).
1. Få tillgång till det nya `PivotTable`-objektet från `PivotTables`-samlingen genom att ange dess index. Använd något av pivot-tabellobjekten som kapslas in i `PivotTable`-objektet för att hantera tabellen.

Kodexempel ges nedan.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Name the sheet
    sheet.SetName(u"Data");

    // Get the cells collection
    Cells cells = sheet.GetCells();

    // Setting the values to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Employee");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Quarter");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Product");
    cell = cells.Get(u"D1");
    cell.PutValue(u"Continent");
    cell = cells.Get(u"E1");
    cell.PutValue(u"Country");
    cell = cells.Get(u"F1");
    cell.PutValue(u"Sale");

    // Fill in employee names
    cell = cells.Get(u"A2"); cell.PutValue(u"David");
    cell = cells.Get(u"A3"); cell.PutValue(u"David");
    cell = cells.Get(u"A4"); cell.PutValue(u"David");
    cell = cells.Get(u"A5"); cell.PutValue(u"David");
    cell = cells.Get(u"A6"); cell.PutValue(u"James");
    cell = cells.Get(u"A7"); cell.PutValue(u"James");
    cell = cells.Get(u"A8"); cell.PutValue(u"James");
    cell = cells.Get(u"A9"); cell.PutValue(u"James");
    cell = cells.Get(u"A10"); cell.PutValue(u"James");
    cell = cells.Get(u"A11"); cell.PutValue(u"Miya");
    cell = cells.Get(u"A12"); cell.PutValue(u"Miya");
    cell = cells.Get(u"A13"); cell.PutValue(u"Miya");
    cell = cells.Get(u"A14"); cell.PutValue(u"Miya");
    cell = cells.Get(u"A15"); cell.PutValue(u"Miya");
    cell = cells.Get(u"A16"); cell.PutValue(u"Miya");
    cell = cells.Get(u"A17"); cell.PutValue(u"Miya");
    cell = cells.Get(u"A18"); cell.PutValue(u"Elvis");
    cell = cells.Get(u"A19"); cell.PutValue(u"Elvis");
    cell = cells.Get(u"A20"); cell.PutValue(u"Elvis");
    cell = cells.Get(u"A21"); cell.PutValue(u"Elvis");
    cell = cells.Get(u"A22"); cell.PutValue(u"Elvis");
    cell = cells.Get(u"A23"); cell.PutValue(u"Elvis");
    cell = cells.Get(u"A24"); cell.PutValue(u"Elvis");
    cell = cells.Get(u"A25"); cell.PutValue(u"Jean");
    cell = cells.Get(u"A26"); cell.PutValue(u"Jean");
    cell = cells.Get(u"A27"); cell.PutValue(u"Jean");
    cell = cells.Get(u"A28"); cell.PutValue(u"Ada");
    cell = cells.Get(u"A29"); cell.PutValue(u"Ada");
    cell = cells.Get(u"A30"); cell.PutValue(u"Ada");

    // Fill in quarters
    cell = cells.Get(u"B2"); cell.PutValue(1);
    cell = cells.Get(u"B3"); cell.PutValue(2);
    cell = cells.Get(u"B4"); cell.PutValue(3);
    cell = cells.Get(u"B5"); cell.PutValue(4);
    cell = cells.Get(u"B6"); cell.PutValue(1);
    cell = cells.Get(u"B7"); cell.PutValue(2);
    cell = cells.Get(u"B8"); cell.PutValue(3);
    cell = cells.Get(u"B9"); cell.PutValue(4);
    cell = cells.Get(u"B10"); cell.PutValue(4);
    cell = cells.Get(u"B11"); cell.PutValue(1);
    cell = cells.Get(u"B12"); cell.PutValue(1);
    cell = cells.Get(u"B13"); cell.PutValue(2);
    cell = cells.Get(u"B14"); cell.PutValue(2);
    cell = cells.Get(u"B15"); cell.PutValue(3);
    cell = cells.Get(u"B16"); cell.PutValue(4);
    cell = cells.Get(u"B17"); cell.PutValue(4);
    cell = cells.Get(u"B18"); cell.PutValue(1);
    cell = cells.Get(u"B19"); cell.PutValue(1);
    cell = cells.Get(u"B20"); cell.PutValue(2);
    cell = cells.Get(u"B21"); cell.PutValue(3);
    cell = cells.Get(u"B22"); cell.PutValue(3);
    cell = cells.Get(u"B23"); cell.PutValue(4);
    cell = cells.Get(u"B24"); cell.PutValue(4);
    cell = cells.Get(u"B25"); cell.PutValue(1);
    cell = cells.Get(u"B26"); cell.PutValue(2);
    cell = cells.Get(u"B27"); cell.PutValue(3);
    cell = cells.Get(u"B28"); cell.PutValue(1);
    cell = cells.Get(u"B29"); cell.PutValue(2);
    cell = cells.Get(u"B30"); cell.PutValue(3);

    // Fill in products
    cell = cells.Get(u"C2"); cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C3"); cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C4"); cell.PutValue(u"Chai");
    cell = cells.Get(u"C5"); cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C6"); cell.PutValue(u"Chang");
    cell = cells.Get(u"C7"); cell.PutValue(u"Chang");
    cell = cells.Get(u"C8"); cell.PutValue(u"Chang");
    cell = cells.Get(u"C9"); cell.PutValue(u"Chang");
    cell = cells.Get(u"C10"); cell.PutValue(u"Chang");
    cell = cells.Get(u"C11"); cell.PutValue(u"Geitost");
    cell = cells.Get(u"C12"); cell.PutValue(u"Chai");
    cell = cells.Get(u"C13"); cell.PutValue(u"Geitost");
    cell = cells.Get(u"C14"); cell.PutValue(u"Geitost");
    cell = cells.Get(u"C15"); cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C16"); cell.PutValue(u"Geitost");
    cell = cells.Get(u"C17"); cell.PutValue(u"Geitost");
    cell = cells.Get(u"C18"); cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C19"); cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C20"); cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C21"); cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C22"); cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C23"); cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C24"); cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C25"); cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C26"); cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C27"); cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C28"); cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C29"); cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C30"); cell.PutValue(u"Chocolade");

    // Fill in continents
    cell = cells.Get(u"D2"); cell.PutValue(u"Asia");
    cell = cells.Get(u"D3"); cell.PutValue(u"Asia");
    cell = cells.Get(u"D4"); cell.PutValue(u"Asia");
    cell = cells.Get(u"D5"); cell.PutValue(u"Asia");
    cell = cells.Get(u"D6"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D7"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D8"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D9"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D10"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D11"); cell.PutValue(u"America");
    cell = cells.Get(u"D12"); cell.PutValue(u"America");
    cell = cells.Get(u"D13"); cell.PutValue(u"America");
    cell = cells.Get(u"D14"); cell.PutValue(u"America");
    cell = cells.Get(u"D15"); cell.PutValue(u"America");
    cell = cells.Get(u"D16"); cell.PutValue(u"America");
    cell = cells.Get(u"D17"); cell.PutValue(u"America");
    cell = cells.Get(u"D18"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D19"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D20"); cell.PutValue(u"Europe");
    cell = cells.Get(u"D21"); cell.PutValue(u"Oceania");
    cell = cells.Get(u"D22"); cell.PutValue(u"Oceania");
    cell = cells.Get(u"D23"); cell.PutValue(u"Oceania");
    cell = cells.Get(u"D24"); cell.PutValue(u"Oceania");
    cell = cells.Get(u"D25"); cell.PutValue(u"Africa");
    cell = cells.Get(u"D26"); cell.PutValue(u"Africa");
    cell = cells.Get(u"D27"); cell.PutValue(u"Africa");
    cell = cells.Get(u"D28"); cell.PutValue(u"Africa");
    cell = cells.Get(u"D29"); cell.PutValue(u"Africa");
    cell = cells.Get(u"D30"); cell.PutValue(u"Africa");

    // Fill in countries
    cell = cells.Get(u"E2"); cell.PutValue(u"China");
    cell = cells.Get(u"E3"); cell.PutValue(u"India");
    cell = cells.Get(u"E4"); cell.PutValue(u"Korea");
    cell = cells.Get(u"E5"); cell.PutValue(u"India");
    cell = cells.Get(u"E6"); cell.PutValue(u"France");
    cell = cells.Get(u"E7"); cell.PutValue(u"France");
    cell = cells.Get(u"E8"); cell.PutValue(u"Germany");
    cell = cells.Get(u"E9"); cell.PutValue(u"Italy");
    cell = cells.Get(u"E10"); cell.PutValue(u"France");
    cell = cells.Get(u"E11"); cell.PutValue(u"U.S.");
    cell = cells.Get(u"E12"); cell.PutValue(u"U.S.");
    cell = cells.Get(u"E13"); cell.PutValue(u"Brazil");
    cell = cells.Get(u"E14"); cell.PutValue(u"U.S.");
    cell = cells.Get(u"E15"); cell.PutValue(u"U.S.");
    cell = cells.Get(u"E16"); cell.PutValue(u"Canada");
    cell = cells.Get(u"E17"); cell.PutValue(u"U.S.");
    cell = cells.Get(u"E18"); cell.PutValue(u"Italy");
    cell = cells.Get(u"E19"); cell.PutValue(u"France");
    cell = cells.Get(u"E20"); cell.PutValue(u"Italy");
    cell = cells.Get(u"E21"); cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E22"); cell.PutValue(u"Australia");
    cell = cells.Get(u"E23"); cell.PutValue(u"Australia");
    cell = cells.Get(u"E24"); cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E25"); cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E26"); cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E27"); cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E28"); cell.PutValue(u"Egypt");
    cell = cells.Get(u"E29"); cell.PutValue(u"Egypt");
    cell = cells.Get(u"E30"); cell.PutValue(u"Egypt");

    // Fill in sales
    cell = cells.Get(u"F2"); cell.PutValue(2000);
    cell = cells.Get(u"F3"); cell.PutValue(500);
    cell = cells.Get(u"F4"); cell.PutValue(1200);
    cell = cells.Get(u"F5"); cell.PutValue(1500);
    cell = cells.Get(u"F6"); cell.PutValue(500);
    cell = cells.Get(u"F7"); cell.PutValue(1500);
    cell = cells.Get(u"F8"); cell.PutValue(800);
    cell = cells.Get(u"F9"); cell.PutValue(900);
    cell = cells.Get(u"F10"); cell.PutValue(500);
    cell = cells.Get(u"F11"); cell.PutValue(1600);
    cell = cells.Get(u"F12"); cell.PutValue(600);
    cell = cells.Get(u"F13"); cell.PutValue(2000);
    cell = cells.Get(u"F14"); cell.PutValue(500);
    cell = cells.Get(u"F15"); cell.PutValue(900);
    cell = cells.Get(u"F16"); cell.PutValue(700);
    cell = cells.Get(u"F17"); cell.PutValue(1400);
    cell = cells.Get(u"F18"); cell.PutValue(1350);
    cell = cells.Get(u"F19"); cell.PutValue(300);
    cell = cells.Get(u"F20"); cell.PutValue(500);
    cell = cells.Get(u"F21"); cell.PutValue(1000);
    cell = cells.Get(u"F22"); cell.PutValue(1500);
    cell = cells.Get(u"F23"); cell.PutValue(1500);
    cell = cells.Get(u"F24"); cell.PutValue(1600);
    cell = cells.Get(u"F25"); cell.PutValue(1000);
    cell = cells.Get(u"F26"); cell.PutValue(1200);
    cell = cells.Get(u"F27"); cell.PutValue(1300);
    cell = cells.Get(u"F28"); cell.PutValue(1500);
    cell = cells.Get(u"F29"); cell.PutValue(1400);
    cell = cells.Get(u"F30"); cell.PutValue(1000);

    // Adding a new sheet
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet sheet2 = workbook.GetWorksheets().Get(sheetIndex);

    // Naming the sheet
    sheet2.SetName(u"PivotTable");

    // Getting the pivot tables collection in the sheet
    PivotTableCollection pivotTables = sheet2.GetPivotTables();

    // Adding a PivotTable to the worksheet
    int index = pivotTables.Add(u"=Data!A1:F30", u"B3", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = pivotTables.Get(index);

    // Showing the grand totals
    pivotTable.SetShowRowGrandTotals(true);
    pivotTable.SetShowColumnGrandTotals(true);

    // Setting the PivotTable report is automatically formatted
    pivotTable.SetIsAutoFormat(true);

    // Setting the PivotTable autoformat type
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report6);

    // Dragging the first field to the row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Dragging the third field to the row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 2);

    // Dragging the second field to the row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);

    // Dragging the fourth field to the column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 3);

    // Dragging the fifth field to the data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 5);

    // Setting the number format of the first data field
    pivotTable.GetDataFields().Get(0).SetNumberFormat(u"$#,##0.00");

    // Saving the Excel file
    workbook.Save(outDir + u"pivotTable_test.out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Lägga till en PivotChart**

För att skapa en PivotChart med Aspose.Cells:

1. Lägg till en graf.
1. Ställ in `PivotSource` för diagrammet att hänvisa till en befintlig pivot-tabell i kalkylbladet.
1. Ange andra attribut.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"pivotChart_test_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Adding a new sheet
    int sheetIndex = workbook.GetWorksheets().Add(SheetType::Chart);
    Worksheet sheet3 = workbook.GetWorksheets().Get(sheetIndex);

    // Naming the sheet
    sheet3.SetName(u"PivotChart");

    // Adding a column chart
    int index = sheet3.GetCharts().Add(ChartType::Column, 0, 5, 28, 16);

    // Setting the pivot chart data source
    sheet3.GetCharts().Get(index).SetPivotSource(u"PivotTable!PivotTable1");
    sheet3.GetCharts().Get(index).SetHidePivotFieldButtons(false);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
