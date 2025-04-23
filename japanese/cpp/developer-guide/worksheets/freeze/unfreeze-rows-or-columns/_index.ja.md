---
title: C++を使ったExcelワークシートの行または列の固定解除
linktitle: ペインの固定解除
type: docs
weight: 190
url: /ja/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: この記事では、Aspose.Cells for C++ APIを使用してExcelワークシートの行、列、またはペインの固定解除方法を学びます。
keywords: ペインの固定解除、行の固定解除、列の固定解除、ウインドウの固定解除
---

## **紹介**

この記事では、Excelワークシートの行、列、ペインの固定解除方法について学びます。固定されたExcelシートを解除したり、固定された行、列、ペインを調整したい場合があります。

## **Excelで**

1. **表示**タブをクリック > **ウインドウ枠の固定** > **ウインドウ枠の固定解除**。

**![Excel でのペインの固定解除](Unfreeze-Panes.png)**

## **Aspose.Cells for C++を使った行、列、またはペインの固定解除**
Aspose.Cells for C++を使えば、ペインの固定解除は簡単です。[**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/)メソッドを使用してください。

1. `Workbook` オブジェクトを構築して、固定されたファイルを開きます。
2. `Worksheet.UnFreezePanes()` メソッドを使ってウィンドウ枠を解除します。
3. ファイルを保存します。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

添付 [サンプルソースの Excel ファイル](Frozen.xlsx) です。
