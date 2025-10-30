---
title: C++ ile PDF ye kaydederken Yorumları Yazdırma
linktitle: PDF ye kaydederken Yorumları Yazdır
type: docs
weight: 10
url: /tr/cpp/print-comments-while-saving-to-pdf/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını PDF ye kaydederken yorumların nasıl yazdırılacağını öğrenin.
---

{{% alert color="primary" %}}

Microsoft Excel, aşağıdaki seçeneklerle yazıları yazdırırken veya PDF'ye kaydederken yorumları yazdırmanıza izin verir:

- Hiçbiri
- Sayfa sonunda
- Sayfada gösterildiği gibi

Aspose.Cells, aynı özelliği desteklemek için [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) enum değerini sağlar. [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) enum'unun aşağıdaki üyeleri vardır:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **PDF'ye kaydederken yorumları yazdır**

Aşağıdaki örnek kod, yorumları PDF'ye kaydederken nasıl kullanılacağını gösterir [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) kullanımı.

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
