---
title: C++を使用してExcelワークシートの上端の行を固定
linktitle: 行を凍結
type: docs
weight: 190
url: /ja/cpp/how-to-freeze-rows-of-excel-worksheet
description: この記事では、Aspose.Cells APIを使用してプログラムmatically Excelワークシートの上端の行を固定する方法を学びます。
keywords: 最上行の固定、最上行の固定
---

## **紹介**

この記事では、上端行を固定する方法を学びます。複数の行を固定したい場合、スクロールダウンしても見出しを確認できるようになります。ヘッダーが見える状態でスクロールします。

## **Excelで行を凍結する**

**![Excelで行を凍結](Freeze-Rows.png)**

1. 上端の行を固定したい場合、その下の行を最初に選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「上部行を凍結」をクリックします。
4. 下にスクロールすると、常に最初の行が上部ビューに表示されます。

**![Frozen row](Frozen-Row.png)**

ご覧のとおり、第1行は固定されており、スクロールしても最上部に常に表示されます。

行を固定することで、大きなデータを見やすくし、行ラベルを見失うことがありません。

## **Aspose.Cells for C++を使った行の固定**
Aspose.Cells for C++を使用して行を固定するのは簡単です。 
選択した行で行を固定するには、[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)メソッドを使用してください。
1. ワークブックを作成またはファイルを開きます。
2. Worksheet.FreezePanes()メソッドを使用して最初の行を固定します。
3. ファイルを保存します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

添付の[サンプルソースExcelファイル](../Freeze.xlsx)。
{{< app/cells/assistant language="cpp" >}}
