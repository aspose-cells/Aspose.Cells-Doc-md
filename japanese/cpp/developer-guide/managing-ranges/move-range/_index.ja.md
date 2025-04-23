---
title: C++を使ったワークシート内のセル範囲の移動
linktitle: ワークシート内のセルの範囲を移動する
type: docs
weight: 370
url: /ja/cpp/move-range-of-cells-in-a-worksheet/
description: Aspose.Cellsを使い、C++でワークシートのセル範囲を移動する方法を学びます。
---

{{% alert color="primary" %}}

この記事では、ワークシート内のセルの範囲を移動する方法を示しています。

{{% /alert %}}

## **ワークシート内のセルの範囲を移動する**
例のコードは、タスクをデモンストレーションするためにテンプレートファイルを使用しています。

**入力ファイル**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

次に、範囲A1:B5をC1:D5に移動した生成されたファイルをご覧ください。

**出力ファイル**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
