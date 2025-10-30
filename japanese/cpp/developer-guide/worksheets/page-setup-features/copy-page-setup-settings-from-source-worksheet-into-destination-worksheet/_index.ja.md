---
title: ソースワークシートから宛先ワークシートにページ設定の設定をコピーするC++コード
linktitle: ページ設定のコピー
type: docs
weight: 80
url: /ja/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: この文章は、C++のAPIまたはサンプルコードを使用して、ソースワークシートから宛先ワークシートへページ設定の設定をプログラム的にコピーする方法を解説します。
keywords: ページ設定のコピー C++、ターゲットワークシートにコピー C++
---

## **可能な使用シナリオ**

新しいシートをワークブックに追加すると、デフォルトの*ページ設定の設定*が含まれます。時々、ユーザーが要件に応じてワークシートのページ設定を転送する必要があります。この場合、ページ設定は自動ではありません。Aspose.Cells API を使用して、1 つのワークシートから別のワークシートにページ設定の設定 ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) をコピーする方法について説明します。

## **ソースワークシートからページ設定を宛先ワークシートにコピー**

次のサンプルコードでは、1 つのワークシートから別のワークシートにページ設定の設定をコピーする方法を示しています。参照として、次のサンプルコードとそのコンソール出力をご覧ください。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
