---
title: C++を使用してスタイルのカスタムプロパティを設定する際にカスタム番号形式をチェック
description: Aspose.Cellsは、スプレッドシートファイルに対する操作をサポートするC++ライブラリで、スタイリング時のカスタム番号形式の確認が可能です。この記事では、Aspose.Cellsライブラリを使用してカスタム番号形式を検証し、スタイリングの正確さを確保する方法を説明します。
keywords: Aspose.Cells、C++ライブラリ、スプレッドシート、スタイリング、カスタム番号フォーマット、検証、チェック
type: docs
weight: 170
url: /ja/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **可能な使用シナリオ**

無効なカスタム番号フォーマットを [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) プロパティに割り当てても、Aspose.Cellsは例外をスローしません。ただし、Aspose.Cellsが割り当てられたカスタム番号フォーマットの妥当性を確認すべき場合は、[**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) プロパティを **true**に設定してください。

## **スタイルのカスタムプロパティを設定する際のカスタム番号形式をチェック**

以下のサンプルコードは、無効なカスタム番号フォーマットを [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) プロパティに割り当てた例です。既に [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) プロパティを **true**に設定しているため、例外（例：無効な番号フォーマット）をスローします。詳細はコード内のコメントを参照してください。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
