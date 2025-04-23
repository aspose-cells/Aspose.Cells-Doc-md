---
title: Imprimir comentarios al guardar en PDF con C++
linktitle: Imprimir comentarios al guardar en PDF
type: docs
weight: 10
url: /es/cpp/print-comments-while-saving-to-pdf/
description: Aprende cómo imprimir comentarios al guardar archivos de Excel en PDF usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel te permite imprimir comentarios al imprimir o guardar en formato PDF con las siguientes opciones:

- Ninguno
- Al final de la hoja
- Según se muestra en la hoja

Aspose.Cells ofrece el enum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) para soportar la misma función. El enum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) tiene los siguientes miembros:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **Imprimir comentarios al guardar en PDF**

El siguiente código de ejemplo ilustra cómo usar [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) para imprimir comentarios al guardar en PDF.

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
