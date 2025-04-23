---
title: Skapa dynamiska diagram med C++
linktitle: Skapa dynamiska diagram
description: Lär dig hur du skapar dynamiska diagram i Aspose.Cells for C++. Vår guide visar dig hur du dynamiskt uppdaterar diagramdata, serier och formatering baserat på dina krav, vilket gör det möjligt att visuellt presentera förändrade data i dina blad.
keywords: Aspose.Cells for C++, diagram, dynamiska diagram, data, serier, formatering, blad, uppdatering.
type: docs
weight: 240
url: /sv/cpp/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dynamiska (eller interaktiva) diagram har förmågan att ändra sig när du ändrar omfånget för data. Med andra ord kan de dynamiska diagrammen automatiskt återspegla förändringar när datakällan ändras. För att trigga ändringen i datakällan kan man använda filteralternativet för Excel-tabeller eller använda en kontroll såsom ComboBox eller rullgardinslista.

Denna artikel demonstrerar användningen av Aspose.Cells for C++ API:er för att skapa dynamiska diagram med både av de nämnda metoderna.

{{% /alert %}}

## **Använda Excel-tabeller**

{{% alert color="primary" %}}

Excel-tabeller kallas ListObjects ur Aspose.Cells perspektiv, därför kommer vi att använda termen "ListObject" istället för "Tabell" för tydlighet. Läs i detalj hur du [skapar ListObjects](/cells/sv/cpp/create-and-format-table/) med Aspose.Cells for C++ API.

{{% /alert %}}

ListObjects ger den inbyggda funktionen för att sortera och filtrera data vid användarinteraktion. Både sorterings- och filtreringsalternativen tillhandahålls via rullgardinslistor som automatiskt läggs till i rubrikraden för [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/). Tack vare dessa funktioner (sortering och filtrering) verkar [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) vara den perfekta kandidaten för att fungera som datakälla till ett dynamiskt diagram eftersom förändringar i sortering eller filtrering kommer att ändra datarepresentationen i diagrammet för att återspegla det aktuella tillståndet av [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/).

För att hålla demonstrationen enkel att förstå, skapar vi [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) från grunden och går framåt steg för steg enligt nedan.

1. Skapa en tom [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Åtkomst till [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) av den första [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) i [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Infoga några data i cellerna.
1. Skapa [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) baserat på den insatta datan.
1. Skapa [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) baserat på dataintervall av [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/).
1. Spara resultatet på disken.

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

    // Create an instance of Workbook
    Workbook book;

    // Access first worksheet from the collection
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cells collection of the first worksheet
    Cells cells = sheet.GetCells();

    // Insert data column wise
    cells.Get(u"A1").PutValue(u"Category");
    cells.Get(u"A2").PutValue(u"Fruit");
    cells.Get(u"A3").PutValue(u"Fruit");
    cells.Get(u"A4").PutValue(u"Fruit");
    cells.Get(u"A5").PutValue(u"Fruit");
    cells.Get(u"A6").PutValue(u"Vegetables");
    cells.Get(u"A7").PutValue(u"Vegetables");
    cells.Get(u"A8").PutValue(u"Vegetables");
    cells.Get(u"A9").PutValue(u"Vegetables");
    cells.Get(u"A10").PutValue(u"Beverages");
    cells.Get(u"A11").PutValue(u"Beverages");
    cells.Get(u"A12").PutValue(u"Beverages");

    cells.Get(u"B1").PutValue(u"Food");
    cells.Get(u"B2").PutValue(u"Apple");
    cells.Get(u"B3").PutValue(u"Banana");
    cells.Get(u"B4").PutValue(u"Apricot");
    cells.Get(u"B5").PutValue(u"Grapes");
    cells.Get(u"B6").PutValue(u"Carrot");
    cells.Get(u"B7").PutValue(u"Onion");
    cells.Get(u"B8").PutValue(u"Cabage");
    cells.Get(u"B9").PutValue(u"Potatoe");
    cells.Get(u"B10").PutValue(u"Coke");
    cells.Get(u"B11").PutValue(u"Coladas");
    cells.Get(u"B12").PutValue(u"Fizz");

    cells.Get(u"C1").PutValue(u"Cost");
    cells.Get(u"C2").PutValue(2.2);
    cells.Get(u"C3").PutValue(3.1);
    cells.Get(u"C4").PutValue(4.1);
    cells.Get(u"C5").PutValue(5.1);
    cells.Get(u"C6").PutValue(4.4);
    cells.Get(u"C7").PutValue(5.4);
    cells.Get(u"C8").PutValue(6.5);
    cells.Get(u"C9").PutValue(5.3);
    cells.Get(u"C10").PutValue(3.2);
    cells.Get(u"C11").PutValue(3.6);
    cells.Get(u"C12").PutValue(5.2);

    cells.Get(u"D1").PutValue(u"Profit");
    cells.Get(u"D2").PutValue(0.1);
    cells.Get(u"D3").PutValue(0.4);
    cells.Get(u"D4").PutValue(0.5);
    cells.Get(u"D5").PutValue(0.6);
    cells.Get(u"D6").PutValue(0.7);
    cells.Get(u"D7").PutValue(1.3);
    cells.Get(u"D8").PutValue(0.8);
    cells.Get(u"D9").PutValue(1.3);
    cells.Get(u"D10").PutValue(2.2);
    cells.Get(u"D11").PutValue(2.4);
    cells.Get(u"D12").PutValue(3.3);

    // Create ListObject, Get the List objects collection in the first worksheet
    ListObjectCollection listObjects = sheet.GetListObjects();

    // Add a List based on the data source range with headers on
    int32_t index = listObjects.Add(0, 0, 11, 3, true);

    sheet.AutoFitColumns();

    // Create chart based on ListObject
    index = sheet.GetCharts().Add(ChartType::Column, 21, 1, 35, 18);
    Chart chart = sheet.GetCharts().Get(index);
    chart.SetChartDataRange(u"A1:D12", true);
    chart.GetNSeries().SetCategoryData(u"A2:B12");

    // Save spreadsheet
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Spreadsheet created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Använda dynamiska formler**

Om du inte vill använda [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) som datakälla till det dynamiska diagrammet, är det andra alternativet att använda Excel-funktioner (eller formler) för att skapa ett dynamiskt dataintervall och en kontroll (såsom ComboBox) för att utlösa förändringen i data. I detta scenario kommer vi att använda VLOOKUP-funktionen för att hämta lämpliga värden baserat på valet av ComboBox. När valet ändras kommer VLOOKUP att uppdatera cellvärdet. Om ett område av celler använder VLOOKUP, kan hela området uppdateras vid användarinteraktion, vilket gör att det kan användas som källa till det dynamiska diagrammet.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå framåt steg för steg enligt följande anvisningar.

1. Skapa en tom [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Åtkomst till [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) av den första [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) i [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Infoga några data i cellerna genom att skapa en namngiven range. Dessa data kommer att tjäna som en serie till det dynamiska diagrammet.
1. Skapa [**ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) baserat på det namngivna intervall som skapades i föregående steg.
1. Infoga mer data i cellerna som kommer att fungera som källa till VLOOKUP-funktionen.
1. Infoga VLOOKUP-funktionen (med lämpliga parametrar) till ett område av celler. Detta område kommer att fungera som källa till den dynamiska diagrammet.
1. Skapa [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) baserat på det område som skapades i föregående steg.
1. Spara resultatet på disken.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range in the second worksheet
    Range range = worksheet.GetCells().CreateRange(u"C21", u"C24");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"North");
    range.Get(1, 0).PutValue(u"South");
    range.Get(2, 0).PutValue(u"East");
    range.Get(3, 0).PutValue(u"West");

    // Add a combo box to the worksheet
    ComboBox comboBox = worksheet.GetShapes().AddComboBox(15, 0, 2, 0, 17, 64);
    comboBox.SetInputRange(u"=MyRange");
    comboBox.SetLinkedCell(u"=B16");
    comboBox.SetSelectedIndex(0);

    // Get the cell and set its style
    Cell cell = worksheet.GetCells().Get(u"B16");
    Style style = cell.GetStyle();
    style.GetFont().SetColor(Color::White());
    cell.SetStyle(style);

    // Set formula for cell C16
    worksheet.GetCells().Get(u"C16").SetFormula(u"=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

    // Put some data for chart source
    // Data Headers
    worksheet.GetCells().Get(u"D15").PutValue(u"Jan");
    worksheet.GetCells().Get(u"D20").PutValue(u"Jan");

    worksheet.GetCells().Get(u"E15").PutValue(u"Feb");
    worksheet.GetCells().Get(u"E20").PutValue(u"Feb");

    worksheet.GetCells().Get(u"F15").PutValue(u"Mar");
    worksheet.GetCells().Get(u"F20").PutValue(u"Mar");

    worksheet.GetCells().Get(u"G15").PutValue(u"Apr");
    worksheet.GetCells().Get(u"G20").PutValue(u"Apr");

    worksheet.GetCells().Get(u"H15").PutValue(u"May");
    worksheet.GetCells().Get(u"H20").PutValue(u"May");

    worksheet.GetCells().Get(u"I15").PutValue(u"Jun");
    worksheet.GetCells().Get(u"I20").PutValue(u"Jun");

    // Data
    worksheet.GetCells().Get(u"D21").PutValue(304);
    worksheet.GetCells().Get(u"D22").PutValue(402);
    worksheet.GetCells().Get(u"D23").PutValue(321);
    worksheet.GetCells().Get(u"D24").PutValue(123);

    worksheet.GetCells().Get(u"E21").PutValue(300);
    worksheet.GetCells().Get(u"E22").PutValue(500);
    worksheet.GetCells().Get(u"E23").PutValue(219);
    worksheet.GetCells().Get(u"E24").PutValue(422);

    worksheet.GetCells().Get(u"F21").PutValue(222);
    worksheet.GetCells().Get(u"F22").PutValue(331);
    worksheet.GetCells().Get(u"F23").PutValue(112);
    worksheet.GetCells().Get(u"F24").PutValue(350);

    worksheet.GetCells().Get(u"G21").PutValue(100);
    worksheet.GetCells().Get(u"G22").PutValue(200);
    worksheet.GetCells().Get(u"G23").PutValue(300);
    worksheet.GetCells().Get(u"G24").PutValue(400);

    worksheet.GetCells().Get(u"H21").PutValue(200);
    worksheet.GetCells().Get(u"H22").PutValue(300);
    worksheet.GetCells().Get(u"H23").PutValue(400);
    worksheet.GetCells().Get(u"H24").PutValue(500);

    worksheet.GetCells().Get(u"I21").PutValue(400);
    worksheet.GetCells().Get(u"I22").PutValue(200);
    worksheet.GetCells().Get(u"I23").PutValue(200);
    worksheet.GetCells().Get(u"I24").PutValue(100);

    // Dynamically load data on selection of Dropdown value
    worksheet.GetCells().Get(u"D16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
    worksheet.GetCells().Get(u"E16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
    worksheet.GetCells().Get(u"F16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
    worksheet.GetCells().Get(u"G16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
    worksheet.GetCells().Get(u"H16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
    worksheet.GetCells().Get(u"I16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

    // Create Chart
    int index = worksheet.GetCharts().Add(ChartType::Column, 0, 3, 12, 9);
    Chart chart = worksheet.GetCharts().Get(index);
    chart.GetNSeries().Add(u"='Sheet1'!$D$16:$I$16", false);
    chart.GetNSeries().Get(0).SetName(u"=C16");
    chart.GetNSeries().SetCategoryData(u"=$D$15:$I$15");

    // Save result on disc
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
