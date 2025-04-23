---
title: Afficher l option Page de filtre du rapport avec C++
linktitle: Afficher l option de filtre de rapport
type: docs
weight: 110
url: /fr/cpp/show-report-filter-pages-option/
description: Apprenez comment activer l option "Afficher les pages de filtre de rapport" dans les tableaux croisés dynamiques à l aide de Aspose.Cells for C++.
---

## **Afficher l'option de filtre de rapport**
Excel supporte la création de tableaux croisés dynamiques, l'ajout de filtres de rapport et l'activation de l'option "Afficher les pages de filtre de rapport". Aspose.Cells prend également en charge cette fonctionnalité pour activer cette option sur le tableau croisé dynamique créé. Voici une capture d'écran montrant l'option "Afficher les pages de filtre de rapport" dans Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Le fichier source d'exemple et les fichiers de sortie peuvent être téléchargés ici pour tester le code d'exemple :

` `[Fichier Excel source](81920786.xlsx) 

[Fichier Excel de sortie](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
