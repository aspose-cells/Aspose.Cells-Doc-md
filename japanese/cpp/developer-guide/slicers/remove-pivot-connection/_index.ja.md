---
title: ピボットコネクションの削除（C++）
linktitle: ピボット接続を解除する
type: docs
weight: 30
url: /ja/cpp/remove-pivot-connection/
description: Aspose.Cellsライブラリを使用してC++でピボットコネクションを削除する方法を学びます。
keywords: オフィス2013、オフィス2016、オフィス2019およびオフィス365なしでピボット接続を解除する
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーとピボットテーブルを非連携にしたい場合は、スライサーを右クリックし、「レポートの接続...」アイテムを選択する必要があります。オプションリストでチェックボックスを操作できます。同様に、Aspose.Cells APIを使用してスライサーとピボットテーブルを非連携にしたい場合は、[**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/) メソッドを使用してください。これにより、スライサーとピボットテーブルが非連携になります。

## **スライサーとピボットテーブルの非連携**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](remove-pivot-connection.xlsx) を読み込みます。それからスライサーにアクセスして非連携にします。最後に、ワークブックを[出力Excelファイル](remove-pivot-connection-out.xlsx)として保存します。 

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
