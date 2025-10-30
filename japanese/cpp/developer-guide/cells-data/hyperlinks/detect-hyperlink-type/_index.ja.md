---
title: ハイパーリンクのタイプをC++で検出
linktitle: ハイパーリンクタイプの検出
type: docs
weight: 160
url: /ja/cpp/detect-hyperlink-type/
description: Aspose.Cells for C++ APIを使ってハイパーリンクタイプを検出する方法を学びます。
keywords: ハイパーリンクのタイプの検出、ハイパーリンクのタイプを検出、ハイパーリンクのタイプを取得
---

## **ハイパーリンクのタイプの検出**

Excelファイルには、外部リンク、セル参照、ファイルパスなど、異なるタイプのハイパーリンクがあります。Aspose.Cellsはハイパーリンクのタイプを検出する機能をサポートしています。ハイパーリンクのタイプは[**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)列挙型によって表されます。[**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)列挙型には以下のメンバーがあります。

- External: 外部リンク
- FilePath: ファイル/フォルダへのローカルな完全なパス
- Email: Email
- CellReference: セルや名前付き範囲へのリンク

ハイパーリンクのタイプを確認するには、[**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/)クラスには[**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/)プロパティがあり、戻り値の型は[**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)です。次のコードスニペットは、この[**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/)プロパティの使用方法を示しています。

### ソースコード

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

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

上記のコードスニペットによって生成された出力は以下の通りです。

コンソール出力
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
{{< app/cells/assistant language="cpp" >}}
