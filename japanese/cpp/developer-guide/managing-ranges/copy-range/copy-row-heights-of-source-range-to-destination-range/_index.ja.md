---
title: ソース範囲の行の高さを宛先範囲にコピーする方法（C++）
linktitle: ソース範囲の行の高さを宛先範囲にコピー
type: docs
weight: 590
url: /ja/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Aspose.Cells for C++を使用して、ソース範囲の行の高さを宛先範囲にコピーする方法を学びましょう。
---

{{% alert color="primary" %}}

時々、ユーザーはソース範囲の行の高さを宛先範囲にコピーする必要があります。Aspose.Cellsは、この目的のために[**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/)列挙型を提供しています。[**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/)プロパティに[**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/)列挙型を設定すると、ソース範囲内のすべての行の高さが宛先範囲にコピーされます。

{{% /alert %}}

次のサンプルコードは、[**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) 列挙型を使用してソース範囲から宛先範囲に行の高さをコピーする方法を説明しています。このコードによって生成された出力ExcelファイルをMicrosoft Excelで開くと、宛先範囲の行の高さがソース範囲の行の高さと正確に一致していることがわかります。

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

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
