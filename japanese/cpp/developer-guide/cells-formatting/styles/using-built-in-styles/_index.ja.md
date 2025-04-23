---
title: ビルトインスタイルをC++で使用する
linktitle: 組み込みスタイルの使用
type: docs
weight: 80
url: /ja/cpp/using-built-in-styles/
description: C++でAspose.Cells for C++ APIを使ったExcelのビルトインスタイル適用例
keywords: C++によるExcelのビルトインスタイルの使用、ワークブックへのスタイルのプログラム適用、Excelでビルトインスタイルを適用、ワークブックにビルトインスタイルを適用、コードによるビルトインスタイルの適用、Excelワークブックにビルトインスタイルを適用
---

{{% alert color="primary" %}}

Aspose.Cellsは、スプレッドシート文書内のセルを書式設定するための再利用可能なスタイルの豊富なコレクションを提供します。 作業ブック内で組み込みスタイルを使用することも、カスタムスタイルを作成することもできます。

{{% /alert %}}

## **組み込みスタイルの使用方法**

[**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/)メソッドと[**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/)列挙型を使用すると、組み込みスタイルを簡単に使用できます。以下にすべての可能な組み込みスタイルのリストがあります:

- TWENTY_PERCENT_ACCENT_1
- TWENTY_PERCENT_ACCENT_2
- TWENTY_PERCENT_ACCENT_3
- TWENTY_PERCENT_ACCENT_4
- TWENTY_PERCENT_ACCENT_5
- TWENTY_PERCENT_ACCENT_6
- FORTY_PERCENT_ACCENT_1
- FORTY_PERCENT_ACCENT_2
- FORTY_PERCENT_ACCENT_3
- FORTY_PERCENT_ACCENT_4
- FORTY_PERCENT_ACCENT_5
- FORTY_PERCENT_ACCENT_6
- 60_PERCENT_ACCENT_1
- 60_PERCENT_ACCENT_2
- 60_PERCENT_ACCENT_3
- 60_PERCENT_ACCENT_4
- 60_PERCENT_ACCENT_5
- 60_PERCENT_ACCENT_6
- ACCENT_1
- ACCENT_2
- ACCENT_3
- ACCENT_4
- ACCENT_5
- ACCENT_6
- BAD
- CALCULATION
- CHECK_CELL
- COMMA
- COMMA_1
- CURRENCY
- CURRENCY_1
- 解説文
- 良好
- HEADER_1
- HEADER_2
- HEADER_3
- HEADER_4
- HYPERLINK
- ハイパーリンクをタップ後
- 入力
- リンク先のセル
- 中立
- 通常
- ノート
- 出力
- パーセント
- タイトル
- 合計
- 警告テキスト
- 行レベル
- 列レベル

## C++でビルトインスタイルを使用するコード例

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
