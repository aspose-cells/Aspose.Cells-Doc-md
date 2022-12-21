---
title: 小計の適用と詳細の下のアウトライン集計行の方向の変更
type: docs
weight: 100
url: /ja/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

この記事では、データに小計を適用する方法と、詳細の下にあるアウトライン集計行の方向を変更する方法について説明します。

を使用して小計をデータに適用できます[**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法。次のパラメータを取ります。

- **セルエリア** - 小計を適用する範囲
- **グループ化** ゼロベースの整数オフセットとして、グループ化するフィールド
- **関数** 小計機能。
- **トータルリスト** 小計が追加されるフィールドを示すゼロから始まるフィールド オフセットの配列。
- **交換** 現在の小計を置き換えるかどうかを示します
- **改ページ** - グループ間に改ページを追加するかどうかを示します
- **概要以下のデータ** データの下に要約を追加するかどうかを示します。

また、アウトラインの方向を制御できます**詳細の下の要約行**次のスクリーンショットに示すように、Worksheet.Outline.SummaryRowBelow プロパティを使用しています。この設定は、Microsoft Excel で開くことができます。**データ > アウトライン > 設定**

![todo:画像_代替_文章](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## ソース ファイルと出力ファイルのイメージ

次のスクリーンショットは、以下のサンプル コードで使用されるソース Excel ファイルを示しており、列 A と B にいくつかのデータが含まれています。

![todo:画像_代替_文章](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

次のスクリーンショットは、サンプル コードによって生成された出力 Excel ファイルを示しています。ご覧のとおり、小計は範囲 A2:B11 に適用され、アウトラインの方向は詳細の下の集計行です。

![todo:画像_代替_文章](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C# 小計を適用し、アウトライン集計行の方向を変更するコード

上記の出力を実現するためのサンプル コードを次に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
