---
title: 異なるページに異なるヘッダーとフッターを設定する
type: docs
weight: 35
url: /ja/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: この記事では、C# ライブラリと .NET API を使用して、Excel ワークシートのページ設定設定のさまざまなヘッダーとフッターをプログラムで設定する方法を示すサンプル コードを提供します。ヘッダーとフッターは、最初のページ、奇数ページ、偶数ページに設定できます。
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

MS Excel は、Excel 2007 以降、最初のページ、奇数ページ、偶数ページに異なるヘッダーとフッターの設定をサポートしています。
Aspose.Cells も同じ機能をサポートしています。

{{% /alert %}}

##  **MS Excelで異なるヘッダーとフッターを設定する**

**![異なるヘッダーとフッターを設定する](difpage.png)**

1. *ページ レイアウト > 印刷タイトル > ヘッダー/フッター** をクリックします。
1. チェック**異なる奇数ページと偶数ページ**または *別のモミページ**。
1. 別のヘッダーとフッターを入力します。

##  **Aspose.Cells で異なるヘッダーとフッターを設定する**

Aspose.Cells は Excel と同じように動作します。
1. フラグを設定します[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/)と[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. 別のヘッダーとフッターを入力します。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
