---
title: 異なるページ用に異なるヘッダーとフッターの設定
type: docs
weight: 35
url: /ja/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: この記事では、C#ライブラリと.NET APIを使用して、Excelワークシートのページ設定設定に異なるヘッダーとフッターをプログラムで設定する方法を示すサンプルコードを提供します。最初のページ、奇数ページ、偶数ページのためのヘッダーとフッターを設定できます。
keywords: C#でエクセルのヘッダーフッターの最初のページを設定する方法、C#でエクセルのヘッダーフッターの奇数ページを設定する方法、C#でエクセルのヘッダーフッターの偶数ページを設定する方法
---

{{% alert color="primary" %}}

ExcelはExcel 2007以降、最初のページ、奇数ページ、偶数ページ用に異なるヘッダーとフッターの設定をサポートしています。
Aspose.Cellsも同じ機能をサポートしています。

{{% /alert %}}

## **MS Excelで異なるヘッダーとフッターの設定**

**![異なるヘッダーとフッターの設定](difpage.png)**

1. **ページレイアウト > 印刷タイトル > ヘッダー/フッター**をクリックします。
1. **奇数と偶数のページを異なるものとする** または **最初のページを異なるものとする** をチェックします。
1. 異なるヘッダーとフッターを入力します。

## **Aspose.Cellsで異なるヘッダーとフッターの設定**

Aspose.CellsはExcelと同じように動作します。
1. [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) および [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) のフラグを設定します。 
1. 異なるヘッダーとフッターを入力します。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
