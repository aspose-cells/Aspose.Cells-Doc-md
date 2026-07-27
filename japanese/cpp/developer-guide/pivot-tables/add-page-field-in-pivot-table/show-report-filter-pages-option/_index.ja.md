---
title: レポートフィルタページオプションをC++で表示
linktitle: レポートフィルタページオプションを表示
type: docs
weight: 110
url: /ja/cpp/show-report-filter-pages-option/
description: Aspose.Cells for C++を使用してピボットテーブルで「レポートフィルタページを表示」オプションを有効にする方法を学びます。
---

## **レポートフィルタページを表示**
Excelはピボットテーブルの作成、レポートフィルタの追加、「レポートフィルタページを表示」オプションの有効化をサポートしています。Aspose.Cellsもこの機能をサポートしており、作成したピボットテーブルに対して「レポートフィルタページを表示」オプションの有効化が可能です。以下は、Excelでの「レポートフィルタページを表示」オプションのスクリーンショットです。

![todo:image_alt_text](show-report-filter-pages-option_1.png)

サンプルソースファイルと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

` [ソースExcelファイル](81920786.xlsx) 

[出力Excelファイル](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
