---
title: C++で行の最大列インデックスと列の最大行インデックスを取得する
linktitle: 行内の最大列インデックスと列内の最大行インデックスの取得
type: docs
weight: 600
url: /ja/cpp/get-max-index-in-row-and-column/
description: Aspose.Cells for C++ APIを使用して、行の最大列インデックスと列の最大行インデックスを取得する方法を学びます。
keywords: 行内の最大列インデックス、列内の最大行インデックス、行内の最大データ列インデックス、列内の最大データ行インデックスの取得。
---

## **可能な使用シナリオ**
行や列の一部のデータだけを操作する場合、行と列のデータ範囲を知る必要があります。Aspose.Cellsはこの機能を提供します。行の最大列インデックスを取得するには、[Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)や[Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)プロパティを取得し、次に[Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)プロパティを使用して最大列インデックスと最大データ列インデックスを取得します。一方、列の最大行インデックスや最大行データインデックスを取得するには、列に範囲を作成し、その範囲を走査して最後のセルを見つけ、最終的に[Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)属性を取得します。

Aspose.Cellsは、目標を達成するための以下のプロパティとメソッドを提供しています。
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Aspose.Cellsを使用して行内の最大列インデックスと列内の最大行インデックスの取得**
この例では、次のことができます:

1. [サンプルファイル](sample.xlsx)をロードする。
1. 最大列インデックスと最大データ列インデックスを取得する行を取得します。
1. [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)属性を取得
1. 列に基づいて範囲を作成します。
1. イテレータを取得して範囲をトラバースします。
1. [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)属性を取得

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
