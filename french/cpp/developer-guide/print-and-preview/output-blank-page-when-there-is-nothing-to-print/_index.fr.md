---  
title: Afficher une page blanche lorsqu’il n’y a rien à imprimer avec C++  
linktitle: Afficher une page blanche lorsqu il n y a rien à imprimer  
type: docs  
weight: 90  
url: /fr/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Gérez les feuilles vides et imprimez des pages blanches avec Aspose.Cells en utilisant C++.  
---  

## **Scénarios d'utilisation possibles**  

Si la feuille est vide, alors Aspose.Cells n’imprimera rien lorsque vous exportez une feuille en image. Vous pouvez changer ce comportement en utilisant la propriété [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/). Lorsqu’elle est définie sur **true**, elle imprimera la page blanche.  

## **Afficher une page vierge lorsqu'il n'y a rien à imprimer**  

Le code échantillon suivant crée le classeur vide qui possède une feuille de calcul vide et affiche cette feuille sous forme d'image après avoir défini la propriété [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) à **true**. Par conséquent, il génère la page blanche car il n'y a rien à imprimer, comme vous pouvez le voir dans l'image ci-dessous.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Code d'exemple**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
{{< app/cells/assistant language="cpp" >}}
