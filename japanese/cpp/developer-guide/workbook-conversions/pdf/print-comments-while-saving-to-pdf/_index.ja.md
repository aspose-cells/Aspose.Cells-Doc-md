---
title: C++で保存時にコメントを印刷する
linktitle: PDFへ保存する際にコメントを印刷する
type: docs
weight: 10
url: /ja/cpp/print-comments-while-saving-to-pdf/
description: Aspose.Cells for C++を使用して、ExcelファイルをPDFに保存する際にコメントを印刷する方法を学びます。
---

{{% alert color="primary" %}}

Microsoft Excelでは、以下のオプションを使用してコメントの印刷やPDF保存時にコメントを印刷できます。

- なし
- シートの末尾
- シートに表示されている通り

Aspose.Cellsはこれと同じ機能をサポートするために、[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)列挙型を提供します。[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)列挙型には以下のメンバーがあります：

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **PDFへ保存する際にコメントを印刷する**

次のサンプルコードは、コメントを印刷してPDFに保存する方法を示しています。

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
