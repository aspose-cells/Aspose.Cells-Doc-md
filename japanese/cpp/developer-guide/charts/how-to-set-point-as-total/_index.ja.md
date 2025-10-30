---
title: ポイントを合計として設定する方法（C++）
linktitle: 合計としてポイントを設定する方法
description: いくつかのExcelチャート、例えばウォーターフォールチャートでは、ポイントを合計に設定する必要があります。この記事では、C++とAspose.Cellsを使用してこれを行う方法を説明します。
keywords: ウォーターフォールチャート、ポイント、合計として設定。
type: docs
weight: 72
url: /ja/cpp/how-to-set-point-as-total/
---

## Excelチャートの「ポイントを合計に設定」とは

例えばウォーターフォールチャートのように、いくつかのポイントデータは前のポイントの合計になっています。このポイントを「合計に設定」する必要があります。サンプルコードと図解を以下に示します。

## ウォーターフォールチャートは「ポイントを合計に設定」する必要があります 

![todo:image_alt_text](set-as-total1.png)

この画像はExcelのウォーターフォールチャートです。 "Total"から始まる4つのデータポイントがあり、これらは前のデータポイントの合計を示しています。
この図では設定が正確ではありません。 "Total 2024"ポイントを選択すると、Excel内の"設定を合計にする"オプションがチェックされていないことが確認できます。
以下に修正が必要な[サンプルExcelファイル](SampleSheet.xlsx)を添付します。これをAspose.Cellsを使って正しく設定します。

## Aspose.Cellsを使用して「ポイントを合計に設定」 

正しい設定を行うためのコードは以下の通りです：

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

次の正しい[出力ファイル](output.xlsx)を取得できます。

図のように、4つの"合計"データポイントが正しく設定されているのが確認でき、前のチャートとの違いもわかります。

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="cpp" >}}
