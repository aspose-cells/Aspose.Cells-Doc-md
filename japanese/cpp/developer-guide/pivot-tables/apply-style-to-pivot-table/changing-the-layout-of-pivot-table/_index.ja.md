---
title: C++を使用したピボットテーブルのレイアウト変更方法
linktitle: ピボットテーブルのレイアウトを変更する
type: docs
weight: 10
url: /ja/cpp/changing-the-layout-of-pivot-table/
description: Aspose.Cells for C++を使用して、コンパクト、アウトライン、タブラー形式でピボットテーブルのレイアウトを変更する方法を学びます。
---

{{% alert color="primary" %}}

Microsoft Excelでは、*ピボットテーブルツール > デザイン > レポートレイアウト* メニューコマンドを使用してピボットテーブルのレイアウトを変更できます。これらの三つの形式に変更可能です：

- コンパクト形式で表示
- アウトライン形式で表示
- 表形式で表示

Aspose.Cellsは、[**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showincompactform/)、[**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/)、および [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/) のメソッドを提供して、これら三つの形式でピボットテーブルのレイアウトを変更します。

{{% /alert %}}

次のサンプルコードは、最初にピボットテーブルを【コンパクト形式】で表示し、その後【アウトライン形式】で、最後に【タブラー形式】で表示します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_sample.xlsx";

    // Create workbook object from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // 1 - Show the pivot table in compact form
    pivotTable.ShowInCompactForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"CompactForm_out.xlsx");

    // 2 - Show the pivot table in outline form
    pivotTable.ShowInOutlineForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"OutlineForm_out.xlsx");

    // 3 - Show the pivot table in tabular form
    pivotTable.ShowInTabularForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"TabularForm_out.xlsx");

    std::cout << "Pivot table forms saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
