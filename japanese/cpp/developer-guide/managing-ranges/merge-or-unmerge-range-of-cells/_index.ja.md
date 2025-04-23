---
title: C++を使ったセルの範囲のマージまたは解除
linktitle: セル範囲の結合または解除
type: docs
weight: 190
url: /ja/cpp/merge-or-unmerge-range-of-cells/
description: C++コードを使ってExcelの範囲内のセルをマージおよび解除します。
keywords: C++を使った範囲内のセルのマージと解除、C++でのセルのマージと解除、C++を使用して範囲内のセルをマージおよび解除、C++とExcelでセルをマージおよび解除する、Excelでセルをマージおよび解除（C++使用）
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してセルの範囲を結合または分割できます。 Aspose.Cellsはこの目的のための[**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)および[**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)メソッドを提供します。この記事では、セルの範囲を単一のセルに結合する方法について説明します。

{{% /alert %}}

## **例**

以下のサンプルコードは、最初に範囲（A1:D4）を作成し、その範囲内のセルを[**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)メソッドを使って1つのセルにマージします。同様に、範囲を作成し、[**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)メソッドを呼び出すことでセルを分割できます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
