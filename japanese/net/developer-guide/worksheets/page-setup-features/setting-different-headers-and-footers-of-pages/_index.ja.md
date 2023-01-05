---
title: ページごとに異なるヘッダーとフッターを設定する
type: docs
weight: 35
url: /ja/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel は、Excel 2007 以降、最初のページ、奇数ページ、偶数ページに異なるヘッダーとフッターの設定をサポートしています。
Aspose.Cells は同じ機能をサポートしています。

{{% /alert %}}

## **MS Excel で異なるヘッダーとフッターを設定する**

**![異なるヘッダーとフッターの設定](difpage.png)**

1. クリック**ページ レイアウト > 印刷タイトル > ヘッダー/フッター**.
1. 小切手**奇数ページと偶数ページの違い**また**別のモミのページ**.
1. 別のヘッダーとフッターを入力します。

## **Aspose.Cells で異なるヘッダーとフッターを設定する**

Aspose.Cells は Excel と同じように動作します。
1. フラグを設定します[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/)と[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. 別のヘッダーとフッターを入力します。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
