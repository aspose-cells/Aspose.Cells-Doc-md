---
title: ExcelからPDFへの変換時に生成されるページ数を制限  C++版
linktitle: 生成されるページ数を制限
type: docs
weight: 180
url: /ja/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aspose.Cellsを使用して、ExcelからPDFへの変換時にページ数を制限する方法を学びます。
---

{{% alert color="primary" %}}

時には、特定のページ範囲を出力PDFファイルに印刷したいことがあります。Aspose.Cellsには、ExcelスプレッドシートをPDFファイル形式に変換する際に生成されるページ数を制限する機能があります。

{{% /alert %}}

## **生成されるページ数の制限**

次の例では、Microsoft Excelファイルのページ3と4をPDFにレンダリングする方法が示されています。

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

スプレッドシートに数式が含まれている場合、PDFにレンダリングする直前に[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値が出力ファイルに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
