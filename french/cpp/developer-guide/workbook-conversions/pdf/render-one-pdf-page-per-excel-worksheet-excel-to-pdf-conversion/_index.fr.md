---
title: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF avec C++
type: docs
weight: 100
url: /fr/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Convertissez les feuilles de calcul Excel en format PDF avec une page pour chaque feuille en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}} 

Lorsque vous travaillez avec de grands fichiers Excel Microsoft (par exemple un classeur contenant plusieurs feuilles, chacune avec 50 colonnes et 300 lignes ou plus), vous pouvez vouloir que la sortie PDF affiche une page par feuille, indépendamment de la taille de la feuille. Cela signifie que chaque page aura probablement une taille de page très différente. Cela peut être réalisé en utilisant Aspose.Cells for C++.

{{% /alert %}} 

Veuillez consulter le code d'exemple suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.

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

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Si l'option [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) est réglée sur **true**, tout le contenu de la feuille sera rendu sur une seule page PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et que les valeurs correctes sont affichées dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
