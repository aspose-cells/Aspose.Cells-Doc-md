---
title: Använda Sparklines och Inställningar 3D format med C++
linktitle: Använda sparklines och inställningar 3D format
type: docs
weight: 40
url: /sv/cpp/using-sparklines-and-settings-3d-format/
description: Lär dig hur du använder sparklines och tillämpar 3D format i Excel filer med Aspose.Cells och C++.
---

## **Användning av sparklines**
Microsoft Excel 2010 kan analysera information på fler sätt än någonsin tidigare. Det låter användarna spåra och markera viktiga datatrender med nya verktyg för dataanalys och visualisering. Sparklines är minidiagram som du kan placera i celler så att du kan se data och diagram på samma tabell. När sparklines används på rätt sätt blir dataanalys snabbare och mer fokuserad. De ger också en enkel vy av information och undviker överfyllda arbetsblad med många upptagna diagram.

Aspose.Cells erbjuder en API för att manipulera sparklines i kalkylblad.
### **Sparklines i Microsoft Excel**
För att infoga sparklines i Microsoft Excel 2010:

1. Välj cellerna där du vill att sparklines ska visas. För att göra dem enkla att visa, välj celler bredvid datan.
1. Klicka på **Infoga** på menyn och välj sedan **kolumn** i **Sparklines** gruppen.
1. Välj eller ange cellområdet på arbetsbladet som innehåller källdata. Graferna kommer att visas.

Sparklines hjälper dig att se trender, till exempel vinst- eller förlustrekord för en softbolliga. Sparklines kan till och med summera hela säsongen för varje lag i ligan.
### **Sparklines med användning av Aspose.Cells**
Utvecklare kan skapa, ta bort eller läsa sparklines (i mallfilen) med API:et från Aspose.Cells. Klasserna som hanterar sparklines finns i [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/) namespace, så du måste importera detta namespace innan du använder dessa funktioner.

Genom att lägga till anpassad grafik för ett givet dataområde har utvecklare friheten att lägga till olika typer av små diagram i utvalda cellområden.

Exemplet nedan demonstrerar funktionen Sparklines. Exemplet visar hur man:

1. Öppna en enkel mallfil.
1. Läs sparklinesinformation för ett arbetsblad.
1. Lägg till nya gnistrande linjer för ett givet datintervall till ett cellområde.
1. Spara Excel-filen på disk.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Inställning 3D-format**
Du kan behöva 3D-diagramstilar så att du kan få just de resultat som behövs för din situation. Aspose.Cells tillhandahåller relevant API för att tillämpa Microsoft Excel 2007 3D-formatering.

Ett komplett exempel ges nedan för att visa hur man skapar ett diagram och tillämpar Microsoft Excel 2007 3D-formatering. Efter att ha exekverat exempelkoden kommer ett stapeldiagram (med 3D-effekter) att läggas till på arbetsbladet.

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

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
