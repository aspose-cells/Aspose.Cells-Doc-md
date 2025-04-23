---
title: C++を使って行単位と列単位でデータを先に入力する方法を学習します。
linktitle: 最初に行、次に列ごとにデータを埋めます
type: docs
weight: 1000
url: /ja/cpp/populate-data-first-by-row-then-by-column/
description: Aspose.Cells for C++ APIを通じて行単位と列単位でデータを先に入力する方法を学びます。
keywords: 行ごとにデータを最初に入力し、次に列ごとにデータを挿入し、行ごとにデータを最初に追加し、高速データ挿入、高速データ追加
---

{{% alert color="primary" %}} 

スプレッドシートにデータを最初に行ごと、次に列ごとに埋めると、全体のパフォーマンスが向上します。

{{% /alert %}} 

A1、B1、A2、B2の順にデータを入れることは、A1、A2、B1、B2の順よりも速くなります。ワークシートに多くのセルがある場合、データを行ごとに入力する場合、このヒントはプログラムをはるかに高速化できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
