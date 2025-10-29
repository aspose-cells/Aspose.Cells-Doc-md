---
title: Rendu du coupeur avec C++
type: docs
weight: 40
url: /fr/cpp/rendering-slicer/
description: Rendez les coupeurs dans les fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells prend en charge le rendu de la forme de tranche. Si vous convertissez votre feuille de calcul en une image ou enregistrez votre classeur au format PDF ou HTML, vous verrez que les tranches sont correctement rendues.
## **Rendu du tronçonneur**
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338479.xlsx) contenant un coupeur existant. Il convertit la feuille de calcul en image en définissant la zone d'impression qui ne couvre que le coupeur. L’image suivante est l'[image de sortie](67338480.png) montrant le coupeur rendu. Comme vous pouvez le voir, le coupeur a été rendu correctement et il ressemble à celui du fichier Excel d'exemple.

![todo:image_alt_text](rendering-slicer_1)
## **Code d'exemple**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
