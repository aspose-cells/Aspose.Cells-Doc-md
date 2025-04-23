---
title: C++ でワークシートからピボットテーブルを削除します
linktitle: ピボットテーブルを削除
type: docs
weight: 60
url: /ja/cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells を使ったC++コードによるエクセルワークシートからのピボットテーブル削除。
keywords: C++でワークシートからピボットテーブルを削除、C++でエクセルからピボットテーブルを削除、C++を使ったピボットテーブルの削除方法、ピボットテーブルを削除、エクセルからピボットテーブルを削除する方法、C++でピボットテーブルの削除、C++によるピボットテーブル削除、ピボットテーブルを削除
---

{{% alert color="primary" %}}

Aspose.Cellsでは、ワークシートからピボットテーブルを削除する機能が提供されています。ピボットテーブルオブジェクトやピボットテーブルの位置を使用して削除できます。

{{% /alert %}}

次のサンプルコードは、ワークシートから2つのピボットテーブルを削除します。最初に [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) メソッドを使ってピボットテーブルを削除し、その後 [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) メソッドを使ってもう一つのピボットテーブルを削除します。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
