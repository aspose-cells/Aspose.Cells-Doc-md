---
title: Détecter les cellules fusionnées dans une feuille de calcul avec C++
linktitle: Détecter les cellules fusionnées
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de feuilles de calcul. Elle supporte la détection des cellules fusionnées dans une feuille de calcul, facilitant ainsi l identification et la manipulation de ces cellules. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour détecter les cellules fusionnées.
keywords: Aspose.Cells, Feuille de calcul, Fusionner les cellules, Détecter, Identifier, Opérer
type: docs
weight: 80
url: /fr/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Cet article fournit des informations sur la manière d'obtenir les zones de cellules fusionnées dans une feuille de calcul.

Aspose.Cells vous permet d'obtenir les zones de cellules fusionnées dans une feuille de calcul. Vous pouvez également les défusionner (diviser). Cet article montre le code le plus simple en utilisant l'API Aspose.Cells pour accomplir la tâche.

{{% /alert %}}

Le composant fournit la méthode [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) qui peut obtenir toutes les cellules fusionnées. L'exemple de code suivant montre comment détecter les cellules fusionnées dans une feuille de calcul.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
