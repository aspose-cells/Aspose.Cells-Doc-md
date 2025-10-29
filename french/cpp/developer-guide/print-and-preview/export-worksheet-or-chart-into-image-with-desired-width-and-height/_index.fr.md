---
title: Exporter une feuille ou un graphique en image avec la largeur et la hauteur souhaitées avec C++
linktitle: Exporter la feuille de calcul ou le graphique en image avec une largeur et une hauteur souhaitées
type: docs
weight: 290
url: /fr/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Utilisez Aspose.Cells pour exporter une feuille ou un graphique en une image avec la largeur et la hauteur souhaitées en C++.
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour exporter votre feuille de calcul ou votre graphique en image avec la largeur et la hauteur souhaitées. Il fournit [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) méthode pour définir la largeur et la hauteur de l'image exportée. La largeur et la hauteur sont spécifiées en pixels.

{{% /alert %}}

Le code suivant exporte la feuille de calcul en une image de taille 400x400.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleWorksheetToImageDesiredSize.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetDesiredSize(400, 400, false);

    // Render sheet into image
    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outputDir + u"outputWorksheetToImageDesiredSize.png");

    std::cout << "Worksheet rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
