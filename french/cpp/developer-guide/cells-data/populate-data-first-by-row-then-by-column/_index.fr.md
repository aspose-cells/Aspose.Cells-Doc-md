---
title: Remplir d’abord par ligne puis par colonne avec C++
linktitle: Remplir d abord les données par ligne puis par colonne
type: docs
weight: 1000
url: /fr/cpp/populate-data-first-by-row-then-by-column/
description: Apprenez comment remplir d’abord par ligne puis par colonne via l’API Aspose.Cells for C++.
keywords: Remplir d abord les données par ligne puis par colonne, Insérer d abord les données par ligne puis par colonne, Ajouter d abord les données par ligne puis par colonne, Insertion de données à haute performance, Ajout de données à haute performance
---

{{% alert color="primary" %}} 

Remplir une feuille de calcul avec des données d'abord par ligne puis par colonne améliore les performances globales.

{{% /alert %}} 

Placer les données dans la séquence A1, B1, A2, B2 est plus rapide que A1, A2, B1, B2. S'il y a de nombreuses cellules dans une feuille de calcul et que vous suivez la deuxième séquence, c'est-à-dire que vous remplissez les données ligne par ligne, ce conseil peut rendre le programme beaucoup plus rapide.

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

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
