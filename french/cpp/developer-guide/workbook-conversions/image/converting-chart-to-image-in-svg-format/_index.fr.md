---
title: Conversion d un graphique en image au format SVG avec C++
linktitle: Conversion de graphique en image au format SVG
type: docs
weight: 240
url: /fr/cpp/converting-chart-to-image-in-svg-format/
description: Apprenez comment convertir des graphiques en images SVG en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) est un format d'image vectorielle basé sur XML pour les graphiques en deux dimensions qui prend également en charge l'interactivité et l'animation. La spécification SVG est une norme ouverte développée par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées et compressées. En tant que fichiers XML, les images SVG peuvent être créées et modifiées avec n'importe quel éditeur de texte, mais sont plus souvent créées avec un logiciel de dessin.

Aspose.Cells peut enregistrer des graphiques sous différents formats d’image tels BMP, JPEG, PNG, GIF, SVG, etc. Cet article explique comment enregistrer un graphique au format SVG.

{{% /alert %}}

Le code d'exemple suivant explique comment utiliser Aspose.Cells pour convertir un graphique en une image au format SVG. Le code charge le fichier source Microsoft Excel, puis enregistre le premier graphique trouvé sur la première feuille de calcul en SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
