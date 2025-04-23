---
title: Lägg till WordArt vattenmärke på diagram med C++
description: Lär dig hur du använder Aspose.Cells for C++ för att lägga till ett WordArt vattenmärke på ett diagram i Microsoft Excel. Vår guide visar hur man skapar och placerar ett WordArt vattenmärke för att förbättra diagrammets visuella tilltalande och unikhet.
keywords: Aspose.Cells for C++, WordArt vattenmärke, Diagramvattenmärke, Microsoft Excel, Visuell tilltalande, Diagramets unika karaktär.
type: docs
weight: 50
url: /sv/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

Du kan använda WordArt för att lägga till specialeffekter på text i kalkylblad. Till exempel: sträck en titel, dekorera text, få texten att passa en förinställd form eller tillämpa den på ett karts plottområde som en vattenstämpel. WordArt blir ett objekt som du kan flytta eller positionera i kalkylbladen för dekoration.

Följande exempel visar hur man lägger till en WordArt-form som en vattenstämpel för diagrammets plottområde.

{{% /alert %}} 

Följande exempel visar hur du lägger till en WordArt-form som en vattenstämpel för ett befintligt diagram.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"sample.xlsx");

    // Get the chart in the first worksheet.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Add a WordArt watermark (shape) to the chart's plot area.
    Shape wordart = chart.GetShapes().AddTextEffectInChart(MsoPresetTextEffect::TextEffect2,
        u"CONFIDENTIAL", u"Arial Black", 66, false, false, 1200, 500, 2000, 3000);

    // Get the shape's fill format.
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency.
    wordArtFormat.SetTransparency(0.9);

    // Get the line format.
    LineFormat lineFormat = wordart.GetLine();

    // Set Line format to invisible.
    lineFormat.SetWeight(0.0);

    // Save the excel file.
    workbook.Save(outputDir + u"output_out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
