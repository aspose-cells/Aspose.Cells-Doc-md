---
title: C++でクエリテーブルのデータソースを持つテーブルの読み書き
linktitle: クエリテーブルデータソースを持つテーブルの読み書き
type: docs
weight: 30
url: /ja/cpp/read-and-write-table-with-query-table-data-source/
description: Aspose.Cells for C++を使ったクエリテーブルをデータソースとするテーブルの読み書き方法を学ぶ。
---

## **クエリテーブルデータソースを持つテーブルの読み書き**
Aspose.Cellsを使用すると、QueryTableをデータソースとするテーブルの読み書きが可能です。この機能はXLSファイルにも対応しています。以下のコードスニペットは、そのようなテーブルを読み取り、合計行を追加して書き換える例を示しています。

```cpp
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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

ソースと出力のExcelファイルは参考のために添付されています。

[ソースファイル](96928091.xls)

[出力ファイル](96928092.xls)
