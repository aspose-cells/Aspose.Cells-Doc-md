---
title: ワークシートのページ設定から用紙の幅と高さを取得する
type: docs
weight: 300
url: /ja/java/get-paper-width-and-height-from-pagesetup-of-worksheet/
---

## **可能な使用シナリオ**

時々、ワークシートのページ設定に設定されている用紙サイズの幅と高さを知る必要があります。この目的には、[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) および [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight) プロパティを使用してください。

## **ワークシートのページ設定から用紙の幅と高さを取得する**

次のサンプルコードでは、[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) および [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight) プロパティの使用方法について説明しています。まず用紙サイズをA2に変更し、その後用紙の幅と高さを求めた後、それをA3、A4、レターに変更して各用紙の幅と高さを求めています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-GetPaperWidthHeight-GetPaperWidthHeight.java" >}}

## **コンソール出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11.0

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
