---  
title: Add WordArt Watermark to Chart with C++  
description: Learn how to use Aspose.Cells for C++ to add a WordArt watermark to a chart in Microsoft Excel. Our guide will demonstrate how to create and position a WordArt watermark to enhance the visual appeal and uniqueness of your chart.  
keywords: Aspose.Cells for C++, WordArt Watermark, Chart Watermark, Microsoft Excel, Visual Appeal, Chart Uniqueness.  
type: docs  
weight: 50  
url: /cpp/add-wordart-watermark-to-chart/  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

You can use WordArt to add special text effects to spreadsheets. For example, stretch a title, decorate text, make the text fit a preset shape, or apply the WordArt to a chart’s plot area as a watermark. The WordArt becomes an object that you can move or position in your spreadsheets to add decoration.  

The following example shows how to add a WordArt shape as a watermark for the chart's plot area.  

{{% /alert %}}  

The following example shows how to add a WordArt shape as a watermark for an existing chart’s plot area.  

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

    // Open the existing Excel file.
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

    // Set line format to invisible.
    lineFormat.SetWeight(0.0);

    // Save the Excel file.
    workbook.Save(outputDir + u"output_out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
