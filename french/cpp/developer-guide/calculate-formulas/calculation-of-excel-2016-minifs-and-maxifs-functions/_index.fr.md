---
title: Calcul des fonctions MINIFS et MAXIFS d Excel 2016 avec C++
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer les fonctions MINIFS et MAXIFS dans Microsoft Excel 2016 en utilisant C++.
keywords: Aspose.Cells, Excel, 2016, fonction MINIFS, fonction MAXIFS, calcul
type: docs
weight: 300
url: /fr/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Scénarios d'utilisation possibles**
Microsoft Excel 2016 prend en charge les fonctions MINIFS et MAXIFS. Ces fonctions ne sont pas supportées dans Excel 2013 ou versions antérieures. Aspose.Cells prend également en charge le calcul de ces fonctions. La capture d'écran suivante illustre l'utilisation de ces fonctions. Veuillez lire les commentaires en rouge dans la capture pour savoir comment ces fonctions fonctionnent.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcul des fonctions MINIFS et MAXIFS d'Excel 2016**
Le code d'exemple suivant charge le [fichier Excel d'exemple](5115149.xlsx) et appelle la méthode [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) pour effectuer le calcul de la formule via Aspose.Cells, puis enregistre les résultats dans le [PDF de sortie](5115154.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
