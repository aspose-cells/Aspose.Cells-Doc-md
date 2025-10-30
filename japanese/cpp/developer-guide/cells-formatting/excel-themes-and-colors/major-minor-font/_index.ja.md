---
title: 見出しと本文のテーマフォント（C++）
linktitle: 見出しと本文のテーマフォント
description: Aspose.Cellsはスプレッドシートファイルの操作に使えるC++ライブラリです。Excelドキュメント内の見出しと本文のテーマフォントを設定でき、ドキュメントの外観やスタイルをカスタマイズ可能です。この記事では、Aspose.Cellsライブラリを使用してExcelドキュメントの見出しと本文のテーマフォントを操作する方法を紹介します。
keywords: Aspose.Cells、Excelドキュメント、見出し、本文、テーマフォント、外観、スタイル
type: docs
weight: 120
url: /ja/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

リージョン設定が変更されると、既定のフォントは自動的に変更されます。

デフォルトフォントが変更されると、行の高さや列の幅も変更され、ページレイアウトが乱れることさえあります。

デフォルトフォントの変更の原因は何ですか？

Excelのテーマフォントが設定されている場合、Excelは現在の言語環境に応じて自動的に異なるフォントに切り替えます。

{{% /alert %}}

## **Excelでの見出しと本文のテーマフォント**

Excelでホームタブを選択し、フォントのドロップダウンボックスをクリックすると、「テーマフォント」が表示され、英語の地域設定においては「Calibri Light」（見出し）と「Calibri」（本文）の2つのテーマフォントが上部に表示されます。

**![テーマフォント](Theme-Fonts.png)**

テーマフォントを選択すると、フォント名は地域によって異なる表示になります。
地域によって自動的にフォントが変更されたくない場合は、2つのテーマフォントを選択しないでください。

## **ヘッダーと本文のフォントをプログラムで変更**
Aspose.Cells for C++を使えば、デフォルトのフォントがテーマフォントかどうかを確認したり、[**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/)プロパティを用いてテーマフォントを設定したりできます。

以下のサンプルコードは、テーマフォントの操作方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **動的にローカルテーマフォントをプログラム的に取得**
時々、サーバーとユーザーのマシンが同じ地域にないことがあります。ユーザーがファイル処理に望むフォントをどのように取得すればよいでしょうか？

[**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/) プロパティを持つファイルを読み込む前に、システムの地域設定を設定する必要があります。

次のサンプルコードは、ローカルテーマフォントを取得する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
