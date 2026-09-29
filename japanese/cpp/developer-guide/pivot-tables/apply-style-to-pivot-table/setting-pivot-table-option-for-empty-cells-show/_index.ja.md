---
title: ピボットテーブルオプションの設定  空のセルを表示するためにC++を使用して
linktitle: ピボットテーブルオプションの設定  空白セルに表示する内容を設定する
type: docs
weight: 40
url: /ja/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Aspose.Cellsを使用してC++でピボットテーブルの「空のセルを表示」オプションを設定する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してさまざまなピボットテーブルオプションを設定できます。そのようなオプションの1つは"空白のセルに表示する内容"です。このオプションを設定することで、ピボットテーブル内のすべての空白セルが指定された文字列として表示されます。

{{% /alert %}}

## **Microsoft Excelでのピボットテーブルオプションの設定**

Microsoft Excelでこのオプションを見つけて設定するには:

1. ピボットテーブルを選択し、右クリックします。
1. **ピボットテーブルオプション**を選択します。
1. **レイアウトと書式**タブを選択します。
1. **空白のセルに表示する内容**オプションを選択し、文字列を指定します。

## **Aspose.Cellsを使用したピボットテーブルオプションの設定**

Aspose.Cellsは、「空白セルに表示する内容」ピボットテーブルオプションを設定するための[**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/)および[**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/)プロパティを提供します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 関連記事

- [ピボットテーブルの書式設定](/cells/ja/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
