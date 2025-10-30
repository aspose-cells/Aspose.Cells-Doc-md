---
title: Stampare Commenti durante il salvataggio in PDF con C++
linktitle: Stampa commenti durante il salvataggio in PDF
type: docs
weight: 10
url: /it/cpp/print-comments-while-saving-to-pdf/
description: Impara come stampare commenti durante il salvataggio di file Excel in PDF usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel consente di stampare commenti durante la stampa o il salvataggio in formato PDF con le seguenti opzioni:

- Nessuna
- Alla fine del foglio
- Come visualizzato nel foglio

Aspose.Cells fornisce l'enum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) per supportare la stessa funzione. L'enum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) ha i seguenti membri:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **Stampa commenti durante il salvataggio in PDF**

Il seguente esempio di codice illustra come usare [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) per stampare commenti durante il salvataggio in PDF.

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
{{< app/cells/assistant language="cpp" >}}
