---
title: Infoga sparkline med C++
linktitle: Sparklines
type: docs
weight: 160
url: /sv/cpp/creating-sparklines/
description: Skapa sparkline för Excel med Aspose.Cells och C++.
---

## **Infoga en sparkline**
{{% alert color="primary" %}} 

Sparkline är en liten diagram i en arbetsbladscell som ger en visuell representation av data. Använd sparklines för att visa trender i en serie av värden, som säsongsvisa ökning eller minskning, ekonomiska cykler eller för att lyfta fram max och min värden. Placera en sparkline nära dess data för störst effekt. Det finns tre typer av Sparkline: Linje, Kolumn och Staplad.

{{% /alert %}} 

Det är enkelt att skapa en sparkline med Aspose.Cells med följande exempelkoder:

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
    Workbook book;
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set values in cells
    sheet.GetCells().Get(u"A1").PutValue(5);
    sheet.GetCells().Get(u"B1").PutValue(2);
    sheet.GetCells().Get(u"C1").PutValue(1);
    sheet.GetCells().Get(u"D1").PutValue(3);

    // Define the CellArea
    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 0;
    ca.EndRow = 0;

    // Add a sparkline group
    int idx = sheet.GetSparklineGroups().Add(SparklineType::Line, sheet.GetName() + u"!A1:D1", false, ca);

    // Get the sparkline group
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);
    group.GetSparklines().Add(sheet.GetName() + u"!A1:D1", 0, 4);

    // Customize Sparklines
    // Create CellsColor
    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    // Set the high points to green and low points to red
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.GetHighPointColor().SetColor(Color::Green());
    group.GetLowPointColor().SetColor(Color::Red());

    // Set line weight
    group.SetLineWeight(1.0);

    // Optionally, apply a preset style
    // group.SetPresetStyle(SparklinePresetStyleType::Style10);

    // Save the workbook
    book.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Använda funktionsspår och inställningar 3D-format](/cells/sv/cpp/using-sparklines-and-settings-3d-format/)
