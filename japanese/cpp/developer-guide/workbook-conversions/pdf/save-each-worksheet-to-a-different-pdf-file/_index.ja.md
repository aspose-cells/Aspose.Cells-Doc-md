---
title: 各ワークシートを別々のPDFファイルに保存（C++）
linktitle: 異なるPDFファイルにそれぞれのワークシートを保存する
type: docs
weight: 130
url: /ja/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Aspose.Cellsを使用して、Excelファイル内の各ワークシートを個別のPDFファイルとして保存する方法を学びます（Aspose.Cells for C++）。
---

{{% alert color="primary" %}} 

Aspose.Cellsは、画像やチャートなどを含む XLS ファイルをPDFに変換することをサポートしています。Aspose.Cells for C++は、スプレッドシートをPDFに変換する際に、独立して動作し、Aspose.PDF for C++を使用する必要はありません。変換は、ソフトウェアが一時ファイルを作成または使用せず、すべてメモリ内で行うことができるため、効率的です。

{{% /alert %}} 

## **異なるPDFファイルごとに各ワークシートを保存**
テンプレートのExcelファイル内の各ワークシートを保存して異なるPDFファイルを生成したい場合は、簡単に実現できます。各シートのインデックスを[**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)オプションに設定してPDFにレンダリングしてみてください。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、絶対に[Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)を呼び出してからPDFにレンダリングするのが最良です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
