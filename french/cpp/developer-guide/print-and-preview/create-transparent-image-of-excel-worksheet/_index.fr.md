--- 
title: Créer une image transparente de la feuille Excel avec C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /fr/cpp/create-transparent-image-of-excel-worksheet/ 
description: Générer des images transparentes de feuilles Excel en utilisant Aspose.Cells avec C++. 
--- 

{{% alert color="primary" %}} 

Parfois, vous avez besoin de générer l'image de votre feuille de calcul en tant qu'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules qui n'ont pas de couleur de remplissage. Aspose.Cells fournit la propriété [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/) pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est **fausse**, les cellules sans couleur de remplissage sont dessinées en blanc et lorsqu'elle est **true**, les cellules sans couleur de remplissage sont dessinées de manière transparente. 

{{% /alert %}} 

Dans l'image de la feuille de calcul suivante, la transparence n'a pas été appliquée. Les cellules sans couleur de remplissage sont dessinées en blanc.

|**Sortie sans transparence : l'arrière-plan de la cellule est blanc**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

Alors que dans l'image de feuille de calcul suivante, la transparence a été appliquée. Les cellules sans couleur de remplissage sont transparentes.

|**Sortie avec transparence activée**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

Le code d'exemple suivant génère une image transparente à partir d'une feuille de calcul Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleCreateTransparentImage.xlsx");

    // Apply different image or print options
    ImageOrPrintOptions imgOption;
    imgOption.SetImageType(static_cast<ImageType>(5)); // Png
    imgOption.SetHorizontalResolution(200);
    imgOption.SetVerticalResolution(200);
    imgOption.SetOnePagePerSheet(true);

    // Apply transparency to the output image
    imgOption.SetTransparent(true);

    // Create image after applying image or print options
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOption);
    sr.ToImage(0, outputDir + u"outputCreateTransparentImage.png");

    std::cout << "Image created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
