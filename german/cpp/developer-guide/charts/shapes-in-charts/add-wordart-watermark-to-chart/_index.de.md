---
title: WordArt Wasserzeichen zum Diagramm mit C++ hinzufügen
description: Lernen Sie, wie man Aspose.Cells for C++ verwendet, um ein WordArt Wasserzeichen zu einem Diagramm in Microsoft Excel hinzuzufügen. Unser Leitfaden zeigt, wie man ein WordArt Wasserzeichen erstellt und positioniert, um die visuelle Attraktivität und Einzigartigkeit Ihres Diagramms zu verbessern.
keywords: Aspose.Cells for C++, WordArt Wasserzeichen, Diagrammwasserzeichen, Microsoft Excel, Visueller Reiz, Diagrammunique.
type: docs
weight: 50
url: /de/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

Sie können WordArt verwenden, um spezielle Texteffekte für Tabellenkalkulationen hinzuzufügen. Zum Beispiel einen Titel strecken, Text dekorieren, den Text in eine voreingestellte Form passen lassen oder den betroffenen Text auf den Diagrammbereich eines Diagramms als Wasserzeichen anwenden. Das WordArt wird zu einem Objekt, das Sie in Ihren Tabellenkalkulationen bewegen oder positionieren können, um Dekorationen hinzuzufügen.

Das folgende Beispiel zeigt, wie Sie eine WordArt-Form als Wasserzeichen für den Diagrammbereich hinzufügen.

{{% /alert %}} 

Das folgende Beispiel zeigt, wie Sie eine WordArt-Form als Wasserzeichen für den Plotbereich eines vorhandenen Diagramms hinzufügen.

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
{{< app/cells/assistant language="cpp" >}}
