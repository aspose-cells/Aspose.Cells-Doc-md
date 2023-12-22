---
title: 詳細の下の概要行の小計の適用と方向の変更
type: docs
weight: 100
url: /ja/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for .NET API を使用して、小計を適用し、詳細の下にあるアウトラインの概要行の方向を変更する方法を学びます。
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

この記事では、データに小計を適用する方法と、詳細の下にあるアウトラインの概要行の方向を変更する方法について説明します。

次を使用してデータに小計を適用できます。[**Worksheet.Cells.小計()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法。次のパラメータを受け取ります。

- **セルエリア** 小計を適用する範囲
- **GroupBy** - グループ化するフィールド (ゼロベースの整数オフセットとして)
- **関数** - 小計機能。
- **合計リスト** 小計が追加されるフィールドを示す、ゼロから始まるフィールド オフセットの配列。
- **交換する** - 現在の小計を置き換えるかどうかを示します
- **改ページ** グループ間に改ページを追加するかどうかを示します
- **データの下の概要** データの下に概要を追加するかどうかを示します。

また、アウトラインの方向を制御することもできます**詳細の下の概要行**次のスクリーンショットに示すように、Worksheet.Outline.summaryRowBelow プロパティを使用します。この設定は、Microsoft Excel で開くことができます。**データ＞アウトライン＞設定**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## ソースファイルと出力ファイルのイメージ

次のスクリーンショットは、以下のサンプル コードで使用されるソース Excel ファイルを示しています。このファイルには列 A と列 B にデータが含まれています。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

次のスクリーンショットは、サンプル コードによって生成された出力 Excel ファイルを示しています。ご覧のとおり、小計は範囲 A2:B11 に適用されており、アウトラインの方向は詳細の下にある概要行です。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C# 小計を適用し、アウトライン集計行の方向を変更するコード

上記のような出力を実現するサンプルコードを次に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
