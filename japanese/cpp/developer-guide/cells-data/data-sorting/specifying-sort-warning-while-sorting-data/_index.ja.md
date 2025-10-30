---
title: ソート時の警告の指定（C++使用）
linktitle: データをソートする際のソート警告の指定
type: docs
weight: 140
url: /ja/cpp/specifying-sort-warning-while-sorting-data/
description: ソート時の警告を指定する方法をAspose.Cells for C++ APIを使って学びます。
keywords: データをソートする際にソート警告を追加する、データをソートする際にソート警告を設定する、データをソートする際にソート警告を選択する。
---

## **可能な使用シナリオ**

テキストデータ{11, 111, 22}を考慮してください。このテキストデータは、テキストにおいて111が22より前に来るためにソートされます。しかし、このデータをテキストではなく数字としてソートしたい場合、それは{11, 22, 111}になります。Aspose.Cellsはこの問題に対処するために{0}プロパティを提供します。このプロパティを**true**に設定すると、テキストデータが数値データとしてソートされます。次のスクリーンショットは、テキストデータが数字のように見える場合にMicrosoft Excelで表示されるソート警告を示しています。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **サンプルコード**

次のサンプルコードは、上記で説明した[**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/)プロパティの使用方法を説明しています。詳細については、サンプルExcelファイル（43352075.xlsx）とそれに対応する出力Excelファイル（43352076.xlsx）を確認してください。

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

    // Create workbook
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
