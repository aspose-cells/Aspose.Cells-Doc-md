---
title: Sparkline mit C++ einfügen
linktitle: Sparklines
type: docs
weight: 160
url: /de/cpp/creating-sparklines/
description: Erstellen Sie Sparkline für Excel mit Aspose.Cells und C++
---

## **Eine Sparkline einfügen**
{{% alert color="primary" %}} 

Sparkline ist ein kleines Diagramm in einer Tabellenzelle, das eine visuelle Darstellung der Daten bietet. Verwenden Sie Sparklines, um Trends in einer Werte-Serie anzuzeigen, wie saisonale Steigerungen oder Rückgänge, wirtschaftliche Zyklen oder um Maximal- und Minimalwerte hervorzuheben. Positionieren Sie eine Sparkline in der Nähe ihrer Daten für maximale Wirkung. Es gibt drei Arten von Sparkline: Linie, Säule und gestapelt.

{{% /alert %}} 

Es ist einfach, eine Sparkline mit Aspose.Cells mit folgendem Beispielcode zu erstellen:

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

## **Erweiterte Themen**
- [Verwenden von Sparklines und Einstellungen 3D-Format](/cells/de/cpp/using-sparklines-and-settings-3d-format/)
