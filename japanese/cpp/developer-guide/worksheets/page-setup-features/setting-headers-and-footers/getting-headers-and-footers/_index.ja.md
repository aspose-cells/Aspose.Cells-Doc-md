---
title: C++を使用してヘッダーやフッターを取得する方法
linktitle: ヘッダーまたはフッターの取得
type: docs
weight: 30
url: /ja/cpp/get-headers-or-footers/
description: この記事では、C++ APIまたはライブラリを使ってExcelやOpenOfficeのファイルからヘッダーとフッターをプログラムで取得する方法について説明します。
---

{{% alert color="primary" %}}

ヘッダーとフッターは、ページレイアウトビュー、印刷プレビュー、および印刷されたページでのみ表示されます。 

複数のワークシートでヘッダーやフッターを表示する場合は、ページ設定ダイアログボックスも使用できます。 

チャートシートやチャートなどの他のシートタイプでは、ページ設定ダイアログボックスを使用してのみヘッダーやフッターを挿入できます。

{{% /alert %}}

## **MS Excelでのヘッダーとフッターの取得**
1. ヘッダーやフッターを表示または変更したいワークシートをクリックします。
2. 表示タブの「ワークブックビュー」グループで、「ページレイアウト」をクリックします。
  Excelはワークシートをページレイアウトビューで表示します。
3. ヘッダーやフッターを表示または編集するには、ワークシートページの上（ヘッダーの下）または下（フッターの上）にある左、中央、または右のヘッダーまたはフッターテキストボックスをクリックします。


## **Aspose.Cells for C++を使用してヘッダーとフッターを取得する方法**
[**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/)および[**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/)メソッドを使えば、C++開発者はファイルからヘッダーやフッターを簡単に取得できます。

1. ファイルを開くためのワークブックを作成します。
2. ヘッダーやフッターを取得したいワークシートを取得します。
3. 特定のセクションIDを持つヘッダーまたはフッターを取得します。

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ヘッダーとフッターをコマンドリストに解析する**
ヘッダーまたはフッターテキストには、ページ番号、現在の日付、またはテキストの書式設定属性のプレースホルダーなど、特別なコマンドが含まれている可能性があります。

特殊コマンドは、先頭にアンパサンド（"&"）を付けた1つの文字で表されます。

ヘッダーとフッターの文字列は、ABNF文法を用いて構築されています。ビューアなしでは理解しにくいです。

Aspose.Cells for C++には、ヘッダーとフッターをコマンドリストとして解析するための[**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/)メソッドがあります。

以下のコードは、ヘッダーまたはフッターをコマンドリストとして解析し、コマンドを処理する例です。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
