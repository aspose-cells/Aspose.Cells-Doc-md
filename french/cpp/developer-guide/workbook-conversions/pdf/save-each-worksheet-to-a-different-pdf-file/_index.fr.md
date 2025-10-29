---
title: Enregistrez chaque feuille de calcul dans un fichier PDF différent avec C++
linktitle: Enregistrer chaque feuille de calcul dans un fichier PDF différent
type: docs
weight: 130
url: /fr/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Apprenez comment enregistrer chaque feuille d’un fichier Excel dans un fichier PDF séparé en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge la conversion des fichiers XLS (qui contiennent des images, des graphiques, etc.) en documents PDF. Aspose.Cells for C++ peut fonctionner indépendamment pour convertir une feuille de calcul en PDF et vous n'avez pas besoin d'utiliser Aspose.PDF pour C++ pour la conversion. La conversion ne nécessite pas que le logiciel crée ou utilise des fichiers temporaires, car tout le processus peut se faire en mémoire.

{{% /alert %}} 

## **Sauvegarder chaque feuille de calcul dans un fichier PDF différent**
Si vous avez besoin d'enregistrer chaque feuille de votre modèle Excel pour générer différents fichiers PDF, vous pouvez facilement le faire. Essayez de définir un indice de feuille à l'option [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) à la fois pour rendre en PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de rendre la feuille de calcul en format PDF. Cela garantira que les valeurs dépendantes des formules sont recalculées, et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
