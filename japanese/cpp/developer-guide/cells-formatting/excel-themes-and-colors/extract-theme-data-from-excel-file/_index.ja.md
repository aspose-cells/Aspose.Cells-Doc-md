---
title: Excelファイルからテーマデータを抽出する（C++）
linktitle: Excelファイルからテーマデータを抽出する
description: Aspose.Cellsはスプレッドシートファイルの操作に使えるC++ライブラリです。Excelファイルからテーマデータを抽出し、ドキュメントのスタイルや書式情報を取得できます。この記事では、Aspose.Cellsライブラリを使用してExcelファイルからテーマデータを抽出する方法を紹介します。
keywords: Aspose.Cells、Excelファイル、テーマデータ、スタイル、書式
type: docs
weight: 120
url: /ja/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Excelファイルからテーマに関するデータを抽出できます。たとえば、ワークブックに適用されたテーマ名やセルに適用されたテーマカラー、セルのボーダーなどを抽出可能です。

Microsoft Excelのページレイアウト > テーマコマンドを使用して、テーマをワークブックに適用できます。

{{% /alert %}}

## Excelファイルからテーマデータを抽出するC++コード例

以下のサンプルコードは、ソースワークブックに適用されたテーマ名を抽出し、その後セルA1に適用されたテーマカラーと、そのセルの下端境界に適用されたテーマカラーも抽出します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
