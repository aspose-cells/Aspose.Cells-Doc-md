---
title: Convertir une feuille de calcul en image  Supprimer l espace blanc autour des données avec C++
linktitle: Convertir une feuille de calcul en image  Supprimer l espace blanc autour des données
type: docs
weight: 40
url: /fr/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Apprenez à convertir une feuille de calcul en image et à supprimer l espace blanc autour des données en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous devez présenter des images de feuille de calcul dans des applications ou des pages web. Par exemple, vous pourriez avoir besoin d'insérer des images dans un document Word, un fichier PDF, une présentation PowerPoint ou un autre document. Fondamentalement, vous souhaitez afficher une feuille de calcul sous forme d'image afin de pouvoir la coller dans d'autres applications. Aspose.Cells vous permet de convertir des feuilles de calcul Microsoft Excel en images.

{{% /alert %}}

## **Supprimer les espaces vides autour des données**

L'API [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) convertit une feuille de calcul en un fichier image avec les attributs spécifiés, par exemple, le format de l'image, les feuilles paginées, etc. Plusieurs formats d'image sont pris en charge, notamment BMP, GIF, JPG, TIFF et EMF.

Lorsque vous utilisez la fonction de conversion de feuille en image, l'image de sortie comporte par défaut un espace blanc, c'est-à-dire une bordure. Vous pouvez supprimer cela en réglant les marges de configuration de la page supérieure, inférieure, gauche et droite pour la feuille source à 0 et en spécifiant les attributs [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) en conséquence.

Le code suivant supprime les espaces vides autour des données dans l'image de sortie.

```c++
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

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
