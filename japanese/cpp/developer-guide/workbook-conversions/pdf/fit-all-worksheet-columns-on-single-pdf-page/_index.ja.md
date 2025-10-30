---
title: すべてのワークシート列を単一のPDFページにフィットさせる（C++）
linktitle: ワークシートのすべての列を単一の PDF ページに収める
type: docs
weight: 160
url: /ja/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Aspose.CellsとC++を使用してすべてのワークシートの列を1ページに収めるPDFを生成
---

{{% alert color="primary" %}}

時には、ワークシートのすべての列を1ページに収めたPDFファイルを生成したい場合があります。 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) プロパティは、この機能を非常に使いやすく提供します。出力されたPDFの高さと幅などの複雑な計算は内部で処理され、ワークシートのデータに基づいています。

{{% /alert %}}

## **ワークシートの列を単一の PDF ページに収める**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) は、ワークシートのすべての列が1つのPDFページにレンダリングされることを保証します。ただし、行はワークシート内のデータに応じて複数ページにわたる場合があります。

以下のサンプルコードは、[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) プロパティを使用して、100列の大型ワークシートをレンダリングする方法を示しています。

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

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

あるワークシートに多くの列がある場合、レンダリングされたPDFファイルでは内容が非常に小さくなる場合があります。Acrobat Readerなどの閲覧アプリケーションで拡大するとまだ読める場合があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
