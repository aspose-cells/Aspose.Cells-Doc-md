---
title: C++を使用したページごとに異なるヘッダーとフッターの設定方法
linktitle: ヘッダーとフッターの設定の違い
type: docs
weight: 35
url: /ja/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: この記事は、C++ライブラリとAPIを使用してExcelワークシートのページ設定のさまざまなヘッダーとフッターをプログラムで設定する方法を示すサンプルコードを提供します。最初のページ、奇数ページ、偶数ページのヘッダーとフッターを設定できます。
keywords: Excelで最初のページ、奇数ページ、偶数ページのヘッダーとフッターを設定する C++、Excelヘッダーとフッターの設定（奇数ページ・偶数ページ・最初のページ）
---

{{% alert color="primary" %}}

 MS Excelは、Excel 2007以降、最初のページ、奇数ページ、偶数ページの異なるヘッダーとフッターの設定をサポートしています。
Aspose.Cellsも同じ機能をサポートしています。

{{% /alert %}}

## **MS Excelで異なるヘッダーとフッターの設定**

**![異なるヘッダーとフッターの設定](difpage.png)**

1. **ページレイアウト > 印刷タイトル > ヘッダー/フッター**をクリックします。
1. **奇数ページと偶数ページを異なる**または**最初のページだけを異なる**をチェックします。
1. 異なるヘッダーとフッターを入力します。

## **Aspose.Cellsで異なるヘッダーとフッターの設定**

Aspose.CellsはExcelと同じように動作します。
1. [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/)および[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/)のフラグを設定します。 
1. 異なるヘッダーとフッターを入力します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
