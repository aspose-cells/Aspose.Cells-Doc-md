---
title: C++を使用したExcelワークシートのフリーズペイン
linktitle: ウィンドウ枠の固定
type: docs
weight: 190
url: /ja/cpp/how-to-freeze-panes-of-excel-worksheet
description: この記事では、Aspose.Cells APIを用いてC++ライブラリでExcelワークシートのペインをプログラム的にフリーズする方法を学びます。
keywords: ペインを固定、ウィンドウを固定。
---

## **紹介**

この記事では、ペインを固定する方法を学びます。共通の見出しの下に大量のデータがある場合、ヘッダーがスクロールダウン時に見えなくなることがあります。このとき、ペインを固定すると、その固定部分はスクロールしても見えるままです。ヘッダー行や最初の列を簡単に見ることができます。ペインの固定と解除は、データの表示を変更せずにデータ自体を変更しません。

## **Excelで**

**![Excelでのウィンドウ枠の固定](Freeze-panes.png)**

1. 固定ペインを作成したい場合は、行と列を固定します。まずセル（例：B2）を選択してください。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで、ウィンドウ枠の固定をクリックします。
4. 下または右にスクロールすると、最初の行と列が固定されます。

**![固定ペイン](Frozen-Panes.png)**

ご覧のとおり、1行目と列Aが固定されており、2行目は3、表示されている2列目はDです。

ペインの固定により、大量のデータを行や列のラベルを追跡せずに表示できます。

## **ペインを固定（Aspose.Cells for C++）で操作**
Aspose.Cells for C++を使ったペインの固定は簡単です。`[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)`メソッドを使用して、選択したセルでペインを固定してください。
1. ワークブックを作成またはファイルを開きます。
2. Worksheet.FreezePanes()メソッドを使用してペインをフリーズします。
3. ファイルを保存します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

添付 [サンプルExcelファイル](Freeze.xlsx)。
{{< app/cells/assistant language="cpp" >}}
