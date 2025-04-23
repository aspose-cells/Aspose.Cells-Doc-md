---
title: Générer une miniature de la feuille de calcul avec C++
linktitle: Générer une miniature de la feuille de calcul
type: docs
weight: 110
url: /fr/cpp/generate-thumbnail-of-the-worksheet/
description: Générez des miniatures de feuilles de calcul en tant qu’images en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Il peut être utile de générer des miniatures à partir de feuilles de calcul. Une miniature est une petite image qui peut être collée dans un document Word ou une présentation PowerPoint pour donner un aperçu de ce qui se trouve sur la feuille de calcul. Elle peut être ajoutée à une page web avec un lien pour télécharger le document original et avoir une multitude d'autres utilisations.

{{% /alert %}} 

Aspose.Cells for C++ permet de sortir les feuilles en tant que fichiers image, ce qui rend la génération de miniatures simple. Le code d’exemple ci-dessous montre comment exporter des feuilles en fichiers image en utilisant C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
