---
title: 共有数式の最大行数を指定（C++）
linktitle: 共有式の最大行数を指定
type: docs
weight: 40
url: /ja/cpp/specify-maximum-rows-of-shared-formula/
description: Excelファイルで共有数式の最大行数を指定する方法を学びます。Aspose.Cells for C++を使用します。
---

## **可能な使用シナリオ**

共有数式の既定の最大行数は64ですが、任意の数値（例：1000）に設定可能です。共有数式の行数がこれを超えると、パフォーマンスに影響します。そこで、Aspose.Cellsは[**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/)プロパティを提供し、これを使用して最大行数を指定できます。合計行数がこれを超える場合、共有数式は複数の共有数式に分割されます。以下のスクリーンショット参照。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **共有式の最大行数を指定**

次のサンプルコードは、[**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/)プロパティの使用例です。共有数式の最大行数を5に設定し、セルD1に100行分の共有数式を追加して保存します。[出力エクセルファイル](61767856.xlsx)を確認すると、各5行ごとに共有数式が分割されているのがわかります。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
