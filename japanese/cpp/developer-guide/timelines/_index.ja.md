---
title: タイムラインをC++で挿入
linktitle: タイムライン
type: docs
weight: 170
url: /ja/cpp/create-timeline/
description: Aspose.Cellsを使用してC++でタイムラインを作成する方法を学びましょう。
---

## **可能な使用シナリオ**

フィルターを調整して日付を表示する代わりに、ピボットテーブルのタイムライン——日付/時間で簡単にフィルタリングし、スライダーコントロールで期間をズームインできる動的フィルターオプションを使用できます。Microsoft Excelでは、ピボットテーブルを選択してから *挿入 > タイムライン* をクリックすることでタイムラインを作成できます。Aspose.Cells も [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/) メソッドを使用してタイムラインを作成できます。

## **ピボットテーブルにタイムラインを作成する**

次のサンプルコードを参照してください。ピボットテーブルを含む[サンプルExcelファイル](input.xlsx)をロードし、最初の基本ピボットフィールドに基づいてタイムラインを作成します。最後に、[出力XLSX](output.xlsx)形式でワークブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力されたExcelファイル内のタイムラインを示しています。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
