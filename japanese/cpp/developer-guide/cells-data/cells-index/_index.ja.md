---
title: C++でセルインデックスの取得
linktitle: セルのインデックスの取得
type: docs
weight: 600
url: /ja/cpp/get-cells-index/
description: セル名から行や列のインデックスを取得する方法を学びます。Aspose.Cellsを使用してセル名をゼロベースの行と列のインデックスに変換します。
keywords: セルのデフォルトのビューは A1 スタイルの参照です。各列は A、B、C... と定義され、セルは A1、B2、C3... と名前が付けられます。
---

{{% alert color="primary" %}}
ExcelのデフォルトビューはA1スタイルの参照で、各列はA、B、C... と定義され、セルはA1、B2、C3...と名前付けられます。
このセルがどの行と列にあるのか知りたい場合もあります。

{{% /alert %}}

## **可能な使用シナリオ**
特定のデータのみを行と列のインデックスで操作したい場合、その特定のセルの行と列のインデックスを知る必要があります。 
Aspose.Cellsは、行名、列名、セル名からこれらのインデックスを取得する機能を提供します。 
Aspose.Cellsは目標を達成するための次のプロパティとメソッドを提供します：
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

注：インデックスは Aspose.Cells for C++ ではゼロベースですが、MS Excel の行のIDは1ベースです。

## **Aspose.Cells を使用してセルのインデックスを取得**
この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートで特定のセルを見つけます。
1. セルの名前によって行インデックスと列インデックスを取得します。
1. 列の名前によって列インデックスを取得します。
1. 行の名前によって行インデックスを取得します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
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

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
