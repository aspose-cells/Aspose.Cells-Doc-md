---
title: C++を使用してカスタムソートリストで列のデータを並べ替える方法
linktitle: カスタムソートリストで列内のデータをソートする
type: docs
weight: 290
url: /ja/cpp/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for C++ APIを使用して、カスタムリストを用いた列のデータ並べ替え方法を学びます。
keywords: カスタムリストを使用して列のデータをソートする、カスタムリストによるデータのソート。
---

## **可能な使用シナリオ**

カスタムリストを使用して列のデータを並べ替えることができます。これは [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) メソッドを使用して行います。ただし、この方法は、カスタムリストのアイテムにカンマ（,）が含まれていない場合にのみ機能します。もし "USA,US" や "中国,CN" のようにカンマが含まれている場合は、[**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) メソッドを使用する必要があります。ここで、最後のパラメータは文字列ではなく文字列の配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

以下のサンプルコードは、[**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) メソッドを使用したカスタムソートリストによるデータの並べ替え方法を示しています。コードで使用されている [サンプルExcelファイル](50528327.xlsx) と、それによって生成された [出力Excelファイル](50528328.xlsx) を参照してください。以下のスクリーンショットは、コード実行時のサンプルExcelファイルに対する効果を示しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

```c++
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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
