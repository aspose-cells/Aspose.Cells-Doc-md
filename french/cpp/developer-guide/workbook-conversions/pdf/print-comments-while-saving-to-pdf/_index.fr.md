---
title: Imprimer les commentaires lors de l’enregistrement en PDF avec C++
linktitle: Imprimer les commentaires lors de l enregistrement au format PDF
type: docs
weight: 10
url: /fr/cpp/print-comments-while-saving-to-pdf/
description: Apprenez comment imprimer les commentaires lors de l’enregistrement de fichiers Excel en PDF en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel vous permet d'imprimer les commentaires lors de l'impression ou de l'enregistrement au format PDF avec les options suivantes :

- Aucun
- À la fin de la feuille
- Tel qu'affiché sur la feuille

Aspose.Cells fournit l'énum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) pour prendre en charge la même fonctionnalité. L'énum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) a les membres suivants :

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **Imprimer les commentaires lors de l'enregistrement au format PDF**

Le code d'exemple suivant illustre comment utiliser [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) pour imprimer les commentaires lors de l'enregistrement en PDF.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleWorkbookWithComments.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"PrintCommentWhileSavingToPdf_out.pdf";

    // Create a workbook from source Excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    /*
     * For print no comments use "PrintCommentsType::PrintNoComments"
     * and for print the comments as displayed on sheet use "PrintCommentsType::PrintInPlace"
     * For Print the comments at the end of sheet we use "PrintCommentsType::PrintSheetEnd"
    */
    worksheet.GetPageSetup().SetPrintComments(PrintCommentsType::PrintSheetEnd);

    // Save workbook in pdf format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with comments printed at the end of the sheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
