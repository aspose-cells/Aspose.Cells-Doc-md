---
title: Rendre un dégradé pour WordArt lors de la conversion de feuilles de calcul en HTML avec C++
linktitle: Rendu de remplissage dégradé pour le WordArt lors de la conversion des feuilles de calcul en HTML
type: docs
weight: 90
url: /fr/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Apprenez à rendre un dégradé pour WordArt lors de la conversion de feuilles de calcul en HTML avec C++.
---

## **Scénarios d'utilisation possibles**
Avant Aspose.Cells 17.1, Aspose.Cells ne rendait pas le remplissage dégradé de l'art de mot lorsque le fichier Excel était converti au format HTML. Depuis la publication d'Aspose.Cells 17.1, le remplissage dégradé de l'art de mot est pris en charge. La capture d'écran suivante compare l'effet sur le remplissage dégradé en convertissant le fichier Excel à l'aide d'Aspose.Cells 17,1 et de la version précédente.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **Rendu de remplissage dégradé pour le WordArt lors de la conversion des feuilles de calcul en HTML**
Le code d'exemple suivant convertit le [fichier Excel source](22774111.xlsx) en [format HTML de sortie](22774109.zip). Le fichier Excel source contient un objet WordArt avec un remplissage dégradé comme indiqué dans la capture d'écran ci-dessus.
## **Code d'exemple**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
