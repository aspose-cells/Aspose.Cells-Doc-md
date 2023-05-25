---
title: ワークシートのページ設定の用紙幅と高さを取得する
type: docs
weight: 50
url: /ja/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: この記事では、.NET API またはライブラリでプログラム的に C# コードを使用して、Excel ワークシートのページ設定の用紙の幅と用紙の高さを取得する方法を説明します。
keywords: excel page setup paper width c#, excel page setup paper height c#
---
##  **考えられる使用シナリオ**

ワークシートのページ設定で設定されている用紙サイズの幅と高さを知る必要がある場合があります。をご利用ください。[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)と[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)この目的のためのプロパティ。

##  **ワークシートのページ設定の用紙幅と高さを取得する**

次のサンプルコードは、[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)と[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)プロパティ。まず、用紙サイズを次のように変更します。*A2*次に、用紙の幅と高さを見つけて、それを次のように変更します。*A3*、*A4*、*レター*用紙の幅と高さをそれぞれ求めます。

###  **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

###  **コンソール出力**

上記のサンプルコードのコンソール出力を次に示します。

{{< highlight "java" >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
