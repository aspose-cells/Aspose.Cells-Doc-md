---
title: C++による範囲の切り取りと貼り付け
linktitle: 範囲の切り取りと貼り付け
type: docs
weight: 130
url: /ja/cpp/cut-and-paste-cells/
description: Aspose.Cellsを使用してAspose.Cells for C++でワークシート内のセルを切り取り貼り付ける方法を学びます。
---

## **セルの切り取りと貼り付け**

Aspose.Cellsは[**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/)コレクションの[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)メソッドを使用して、ワークシート内のセルを切り取り貼り付けることができます。[**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/)メソッドは次のパラメータを受け取ります：

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): 切り取るセルの範囲
- 行インデックス: セルを挿入する行のインデックス
- 列インデックス: セルを挿入する列のインデックス
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): 列のシフト方向

次の例は、ワークシート内でセルを切り取り、貼り付ける方法を示しています。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(0, 2).SetValue(1);
    worksheet.GetCells().Get(1, 2).SetValue(2);
    worksheet.GetCells().Get(2, 2).SetValue(3);
    worksheet.GetCells().Get(2, 3).SetValue(4);

    Range namedRange = worksheet.GetCells().CreateRange(0, 2, 3, 1);
    namedRange.SetName(u"NamedRange");

    Range cut = worksheet.GetCells().CreateRange(u"C:C");

    worksheet.GetCells().InsertCutCells(cut, 0, 1, ShiftType::Right);

    workbook.Save(outDir + u"CutAndPasteCells.xlsx");

    std::cout << "Cells cut and pasted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
