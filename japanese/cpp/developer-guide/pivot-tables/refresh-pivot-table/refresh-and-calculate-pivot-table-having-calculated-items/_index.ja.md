---
title: 計算されたアイテムを持つピボットテーブルの更新と計算（C++）
linktitle: ピボットテーブルを更新し計算項目を持つピボットテーブルを更新する
type: docs
weight: 40
url: /ja/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aspose.Cellsを使用して計算アイテムを持つピボットテーブルを更新および計算する方法（C++）
---

{{% alert color="primary" %}}

Aspose.Cellsは今、計算項目を持つピボットテーブルを更新および計算する機能をサポートしています。この機能を実行するには通常通りに[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/)および[**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)を使用してください。

{{% /alert %}}

## **計算項目を持つピボットテーブルを更新および計算する**

 次のサンプルコードは、3つの計算アイテムを持つピボットテーブルを含むソースExcelファイル（5115238.xlsx）を読み込みます。まずセルD2の値を20に変更し、その後、Aspose.Cells APIを使ってピボットテーブルを更新と計算し、ワークブックをPDF形式で保存します。結果として、[出力PDF](5115229.pdf)には、Aspose.Cellsが計算アイテムを持つピボットテーブルを正しく更新と計算したことが示されています。Microsoft Excelを使って、手動でセルD2に20を入力し、Alt+F5ショートカットキーや、ピボットテーブルの更新ボタンをクリックして更新できます。

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

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
