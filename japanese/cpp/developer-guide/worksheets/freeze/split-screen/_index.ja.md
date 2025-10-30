---
title: C++を使ったExcelワークシートの分割表示の方法
linktitle: 画面分割
type: docs
weight: 190
url: /ja/cpp/how-to-split-screen-of-excel-worksheet
description: この記事では、C++を使ってワークシートを2つまたは4つに分割し、特定の行や列を別のペインに表示する方法について学びます。
keywords: 最上行の固定、最上行の固定
---

## **紹介**

この記事では、大規模なデータセットを操作する際に、同じワークシートの異なる部分を比較するために、2つまたは4つに分割して表示する方法を学びます。分割表示機能はあなたのニーズに応えます。

## **Excelで画面を分割する方法**
ワークシートを2つまたは4つの部分に分割するには、次のようにします:

1. 分割を配置したい行/列/セルを選択します。
2. [表示]タブの[ウィンドウ]グループで、[分割]ボタンをクリックします。

**![画面分割](Split-Screen.png)**

## **列単位でワークシートを分割**

スプレッドシートの2つの領域を垂直に分割するには、分割を表示したい列の右側の列を選択し、Excelの[分割]ボタンをクリックします。

Aspose.Cells for C++を使った列の垂直分割、ワークシートの垂直分割
method [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) で分割します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **行単位でワークシートを分割**
Excelウィンドウを水平に分割するには、Excelで分割が発生する行の下の行を選択します。

Aspose.Cells for C++を使った行の水平分割、ワークシートの水平分割
method [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) で分割します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ワークシートを4つの部分に分割する**
同じワークシートの4つの異なるセクションを同時に表示するには、Excelで画面を縦横に分割します。

Aspose.Cells for C++を使った列の垂直分割、ワークシートの垂直分割（最初の行と列ではないセルをアクティブに選択）
method [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) で分割します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **分割を削除する方法**
ワークシートの分割を解除するには、再び分割ボタンをクリックします。

Aspose.Cells for C++は、分割設定を解除するための[**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)メソッドを提供します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
