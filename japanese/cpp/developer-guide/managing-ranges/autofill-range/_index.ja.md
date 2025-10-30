---
title: C++を使用したExcelファイルのオートフィールド範囲の自動入力
linktitle: AutoFill 範囲
type: docs
weight: 105
url: /ja/cpp/autofill-ranges/
description: Aspose.CellsとC++を使用して、Excelファイルの指定された範囲でオートフィル操作を実行する方法を学びます。
---

## **Excelの指定範囲でオートフィルを実行**

Excelで範囲を選択し、マウスを右下隅に移動させて、「+」をドラッグしてデータを自動入力します。

## **Aspose.Cells で範囲を自動入力する**

以下の例は、範囲に対してオートフィル操作を行う方法を示しています。こちらはテストに使用できるサンプルファイルです：

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
