---
title: Ajouter un filigrane WordArt au graphique avec C++
description: Apprenez comment utiliser Aspose.Cells for C++ pour ajouter un filigrane WordArt à un graphique dans Microsoft Excel. Notre guide vous montrera comment créer et positionner un filigrane WordArt pour améliorer l attrait visuel et l unicité de votre graphique.
keywords: Aspose.Cells for C++, Filigrane WordArt, Filigrane de graphique, Microsoft Excel, attrait visuel, unicité du graphique.
type: docs
weight: 50
url: /fr/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

Vous pouvez utiliser WordArt pour ajouter des effets spéciaux de texte aux feuilles de calcul. Par exemple, étirer un titre, décorer du texte, faire en sorte que le texte s'adapte à une forme prédéfinie, ou appliquer le texte affecté à la zone de traçage d'un graphique comme filigrane. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans vos feuilles de calcul pour ajouter des décorations.

L'exemple suivant montre comment ajouter une forme WordArt en filigrane pour la zone de traçage du graphique.

{{% /alert %}} 

L'exemple suivant montre comment ajouter une forme WordArt en filigrane pour la zone de traçage d'un graphique existant.

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
