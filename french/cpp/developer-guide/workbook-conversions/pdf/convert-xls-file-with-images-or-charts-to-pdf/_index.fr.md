---
title: Convertir un fichier XLS avec images ou graphiques en PDF avec C++
linktitle: Convertir un fichier XLS avec des images ou des graphiques en PDF
type: docs
weight: 50
url: /fr/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Convertir des fichiers XLS contenant des images ou des graphiques en documents PDF en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supporte la conversion des fichiers XLS contenant des images et des graphiques en documents PDF. Aspose.Cells for C++ peut fonctionner indépendamment pour convertir une feuille de calcul en PDF : Aspose.PDF pour C++ n'est pas requis pour la conversion. Le processus peut être effectué en mémoire car il ne dépend pas de fichiers XML temporaires ou intermédiaires. Cela signifie que de gros fichiers Excel, par exemple ceux contenant des images, des graphiques et d'autres objets de dessin, peuvent être convertis rapidement et efficacement.

{{% /alert %}} 
## **Code d'exemple**

```c++
#include <iostream>
#include <memory>
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
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) juste avant de rendre en PDF. Cela garantit que les valeurs dépendantes des formules seront recalculées et que les bonnes valeurs seront affichées dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
