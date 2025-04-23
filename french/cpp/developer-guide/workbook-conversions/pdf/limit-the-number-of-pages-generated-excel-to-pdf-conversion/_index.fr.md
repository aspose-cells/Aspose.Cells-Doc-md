---
title: Limiter le nombre de pages générées  Conversion Excel en PDF avec C++
linktitle: Limiter le nombre de pages générées
type: docs
weight: 180
url: /fr/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Apprenez comment limiter le nombre de pages générées lors de la conversion d’Excel en PDF en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, vous souhaitez imprimer une plage de pages dans un fichier PDF de sortie. Aspose.Cells a la capacité de limiter le nombre de pages générées lors de la conversion d'une feuille de calcul Excel au format de fichier PDF.

{{% /alert %}}

## **Limitez le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) dans un fichier Microsoft Excel au format PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de la convertir au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et les valeurs correctes sont rendues dans le fichier de sortie.

{{% /alert %}}
