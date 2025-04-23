---
title: Convertir Excel en image avec C++
linktitle: Convertir Excel en Image
type: docs
weight: 300
url: /fr/cpp/convert-excel-to-image/
description: Apprenez à convertir les feuilles de calcul Excel en images, y compris les formats TIFF et SVG, en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter une feuille de calcul du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.

{{% /alert %}}

## Conversion du classeur en TIFF

Un fichier Excel peut contenir plusieurs feuilles avec plusieurs pages. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) vous permet de convertir Excel en TIFF avec plusieurs pages. De plus, vous pouvez contrôler plusieurs options pour TIFF, comme [Compression](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Résolution ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Le code ci-dessous montre comment convertir Excel en TIFF avec plusieurs pages. Les [fichier Excel source](workbook-to-tiff-with-mulitiple-pages.xlsx) et [image TIFF générée](workbook-to-tiff-with-mulitiple-pages.tiff) sont joints à titre de référence.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Conversion de la feuille de calcul en image**

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.

En tant que développeur, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images. Par exemple, vous pourriez avoir besoin d'utiliser une image d'une feuille de calcul dans une application ou une page Web. Vous pourriez vouloir insérer une image dans un document Microsoft Word, un fichier PDF, une présentation PowerPoint ou tout autre type de document. En bref, vous voulez qu'une feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.

Aspose.Cells prend en charge la conversion des feuilles de calcul Excel en images. Pour utiliser cette fonctionnalité, vous devez importer l'espace de noms [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) dans votre programme ou projet. Il dispose de plusieurs classes précieuses pour le rendu et l'impression, par exemple [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), et d'autres.

La classe [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) représente une feuille de calcul à rendre sous forme d'images. Elle dispose d'une méthode surchargée, [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), qui peut convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Elle retourne un objet `System.Drawing.Bitmap` et vous pouvez enregistrer un fichier image sur le disque ou en flux. Plusieurs formats d'image sont pris en charge, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image.

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Actuellement, l'API de conversion des feuilles de calcul en images ne prend pas en charge les graphiques à bulles en 3D.

{{% /alert %}}

## **Conversion de feuille de calcul en SVG**

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Aspose.Cells for C++ a été capable de convertir des feuilles de calcul en SVG depuis la version 7.1.0. Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en une image SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Convertir un graphique Excel en image](/cells/fr/cpp/convert-an-excel-chart-to-image/)
- [Conversion de graphique en image au format SVG](/cells/fr/cpp/converting-chart-to-image-in-svg-format/)
- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Suivre la progression de la conversion d'Excel en TIFF](/cells/fr/cpp/track-conversion-progress-of-excel-to-tiff/)
