---
title: 親ピボットテーブルのネストされた子ピボットテーブルを見つけて更新する方法（C++）
linktitle: ネストされた子ピボットテーブルを見つけて更新する方法
type: docs
weight: 60
url: /ja/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: 親ピボットテーブルの子ピボットテーブルを見つけて更新する方法をAspose.Cells for C++を使って学びます。
---

## **可能な使用シナリオ**

親ピボットテーブルが別のピボットテーブルをデータソースとして使用する場合、それを子ピボットテーブルやネストされたピボットテーブルと呼びます。[**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)を使用して親ピボットテーブルの子ピボットテーブルを見つけることができます。

## **親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する**

次のサンプルコードでは、3つのピボットテーブルを含む[サンプルExcelファイル](61767747.xlsx)をロードし、その下の2つのピボットテーブルが、このスクリーンショットに示すように、上記のピボットテーブルの子であることを示しています。コードは、[**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)を使用して子ピボットテーブルを見つけ、それぞれを更新します。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath = u"sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access third pivot table
    PivotTable ptParent = ws.GetPivotTables().Get(2);

    // Access the children of the parent pivot table
    Vector<PivotTable> ptChildren = ptParent.GetChildren();

    // Refresh all the children pivot table
    int count = ptChildren.GetLength();
    for (int idx = 0; idx < count; idx++)
    {
        // Access the child pivot table
        PivotTable ptChild = ptChildren[idx];

        // Refresh the child pivot table
        ptChild.RefreshData();
        ptChild.CalculateData();
    }

    std::cout << "Children pivot tables refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
