---
title: Excel を PDF に変換し、各シートを1ページとしてレンダリング  C++によるExcelからPDFへの変換
type: docs
weight: 100
url: /ja/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aspose.Cellsを使用して、Excelの各ワークシートを1ページに変換してPDF形式にします。
---

{{% alert color="primary" %}} 

多くのシートを持つ大きなMicrosoft Excelファイル（例：各シートに50列以上、300行以上のデータ）を扱う場合、サイズに関係なく各ワークシートを1ページとしてPDF出力したいことがあります。これにより、各ページは大きく異なるページサイズになる可能性があります。これはAspose.Cells for C++を使用して実現できます。

{{% /alert %}} 

複数のワークシートを持つExcelファイルをPDFに変換するサンプルコードをご確認ください。

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

[PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)]（https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/）オプションをtrueに設定すると、すべてのシートの内容が1つのPDFページにレンダリングされます。

{{% /alert %}} {{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、絶対に[Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)を呼び出してからPDFにレンダリングするのが最良です。これにより、数式に依存する値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
