---
title: C++ で Worksheet がダイアログシートかどうかを検索
linktitle: ワークシートがダイアログシートであるかを検索する
type: docs
weight: 90
url: /ja/cpp/find-if-the-worksheet-is-dialog-sheet/
description: ダイアログシートは古い形式のシートです。このコードは、C++ API を使用して、プログラム的にExcelワークシートがダイアログシートかどうかを判定する方法とサンプルコードを提供します。
keywords: C++ で Excel ワークシートのダイアログタイプを見つける方法、ワークシートのダイアログを検出
---

## **可能な使用シナリオ**

可能な使用シナリオ

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

シートがダイアログシートかその他の種類のシートかどうかは、Aspose.Cellsによる [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) プロパティを使用して確認できます。もし列挙値 [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) を返す場合、それはダイアログシートを扱っていることを意味します。

## **ワークシートがダイアログシートであるかを検索する**

以下のサンプルコードは、ダイアログシートを含む[サンプルExcelファイル](64716820.xlsx)を読み込みます。それは [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) プロパティをチェックし、[**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) と比較してからメッセージを出力します。詳細は以下のサンプルコードのコンソール出力を参照してください。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
