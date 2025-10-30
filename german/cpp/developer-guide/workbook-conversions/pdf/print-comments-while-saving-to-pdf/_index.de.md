---
title: Kommentare beim Speichern als PDF mit C++ drucken
linktitle: Kommentare beim Speichern in PDF drucken
type: docs
weight: 10
url: /de/cpp/print-comments-while-saving-to-pdf/
description: Erfahren Sie, wie Sie Kommentare beim Speichern von Excel Dateien als PDF mit Aspose.Cells for C++ drucken.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht das Drucken von Kommentaren beim Drucken oder Speichern im PDF-Format mit folgenden Optionen:

- Keine
- Am Ende des Blattes
- Wie auf dem Blatt angezeigt

Aspose.Cells stellt die [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)-Aufzählung zur Unterstützung derselben Funktion bereit. Die [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)-Aufzählung hat folgende Mitglieder:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **Kommentare drucken beim Speichern als PDF**

Das folgende Beispiel zeigt, wie [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) verwendet wird, um Kommentare beim Speichern in PDF zu drucken.

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
