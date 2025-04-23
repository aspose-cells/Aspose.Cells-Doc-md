---
title: C++でデータ範囲とスパークライングループの位置を指定してスパークラインをコピー
linktitle: データ範囲と場所を指定してスパークラインをコピー
type: docs
weight: 300
url: /ja/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Aspose.Cells for C++を使用して、データ範囲と位置を指定してスパークラインをコピーする方法を学びます。
---

{{% alert color="primary" %}}

Microsoft Excelでは、データ範囲とスパークライングループの位置を指定してスパークラインをコピーすることができます。Aspose.Cellsでは、この機能をサポートしています。

{{% /alert %}}

Microsoft Excelでスパークラインを他のセルにコピーするには:

1. スパークラインを含むセルを選択します。
1. **デザイン**タブの**スパークライン**セクションから**データの編集**を選択します。
1. **グループの位置とデータの編集**を選択します。
1. データ範囲と位置を指定します。
1. **OK** をクリックします。

Aspose.Cellsは、`SparklineCollection.Add(dataRange, row, column)`メソッドを提供しており、これを使ってスパークラインのデータ範囲と位置を指定できます。以下のサンプルコードは、上のスクリーンショットに示されたソースExcelファイルを読み込み、最初のスパークライングループにアクセスし、データ範囲と位置を追加します。最後に、出力Excelファイルを書き出します（画像も上記のスクリーンショットで示されています）。

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
