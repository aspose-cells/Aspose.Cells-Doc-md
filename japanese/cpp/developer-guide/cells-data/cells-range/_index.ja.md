---
title: C++でセル範囲を取得
linktitle: セル範囲を取得
type: docs
weight: 600
url: /ja/cpp/get-cells-range/
description: Aspose.Cells for C++ APIを通じてセル範囲の取り方を学びます。
keywords: セルの最大表示範囲を取得、セルの最大行を取得、セルの最大データ行を取得、セルの最大列を取得、セルの最大データ列を取得します。
---

## **可能な使用シナリオ**
ワークシート上のいくつかのデータの操作のみが必要な場合、ワークシート全体のデータ範囲を知る必要があります。Aspose.Cellsはこの機能を提供しています。Aspose.Cellsでは、目標を達成するための次のプロパティとメソッドが提供されています。
- [**Cells.GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/)
- [**Cells.GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/)
- [**Cells.GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)
- [**Cells.GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)
- [**Cells.GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/)

## **Aspose.Cellsを使用してセル範囲を取得する**
この例では、次のことができます:

1. ワークブックを作成する。
1. 最初のワークシートのセルにデータを追加する。
1. セル[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)を取得。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    Range range = cells.GetMaxDisplayRange();

    std::cout << cells.GetMaxRow() << std::endl;
    std::cout << cells.GetMaxDataRow() << std::endl;
    std::cout << cells.GetMaxColumn() << std::endl;
    std::cout << cells.GetMaxDataColumn() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
