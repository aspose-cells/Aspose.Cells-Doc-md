---
title: Exporter une plage de cellules d une feuille en image avec C++
linktitle: Exporter une plage de cellules en image
type: docs
weight: 60
url: /fr/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Apprenez comment exporter une plage spécifique de cellules d une feuille en image en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez faire une image d'une feuille de calcul en utilisant Aspose.Cells. Cependant, parfois, vous devez exporter seulement une plage de cellules dans une feuille de calcul vers une image. Cet article explique comment y parvenir.

## **Exporter une plage de cellules d'une feuille de calcul vers une image**

Pour prendre une image d'une plage, définissez la zone d'impression sur la plage souhaitée, puis définissez toutes les marges à 0. Définissez également [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) sur **true**. Le code suivant prend une image de la plage D8:G16. Ci-dessous se trouve une capture d'écran du [fichier Excel d'exemple](47153160.xlsx) utilisé dans le code. Vous pouvez essayer le code avec n'importe quel fichier Excel.

## **Capture d'écran du fichier Excel d'exemple et de son image exportée**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

L'exécution du code crée une image de la plage D8:G16 seulement.

**![todo:image_alt_text](Output-Image.png)**

## **Code d'exemple**

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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
