---
title: 小計の適用と詳細の下のアウトライン集計行の方向の変更
type: docs
weight: 100
url: /ja/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

この記事では、データに小計を適用する方法と、詳細の下にあるアウトライン集計行の方向を変更する方法について説明します。

を使用して小計をデータに適用できます[**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])） 方法。次のパラメータを取ります。

- **セルエリア** - 小計を適用する範囲
- **グループ化** ゼロベースの整数オフセットとして、グループ化するフィールド
- **関数** 小計機能。
- **トータルリスト** 小計が追加されるフィールドを示すゼロから始まるフィールド オフセットの配列。
- **交換** 現在の小計を置き換えるかどうかを示します
- **改ページ** グループ間に改ページを追加するかどうかを示します
- **概要以下のデータ** データの下に要約を追加するかどうかを示します。

また、アウトラインの方向を制御できます**詳細の下の要約行**次のスクリーンショットに示すように、[**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)財産。この設定は、Microsoft Excel で開くことができます。**データ > アウトライン > 設定**

![todo:画像_代替_文章](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 例

### ソース ファイルと出力ファイルを比較するスクリーンショット

次のスクリーンショットは、以下のサンプル コードで使用されるソース Excel ファイルを示しており、列 A と B にいくつかのデータが含まれています。

![todo:画像_代替_文章](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

次のスクリーンショットは、サンプル コードによって生成された出力 Excel ファイルを示しています。ご覧のとおり、小計が範囲に適用されています**A2:B11**アウトラインの方向は、詳細の下の要約行です。

![todo:画像_代替_文章](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java 小計を適用し、詳細の下にあるアウトライン集計行の方向を変更するコード

上記の出力を実現するためのサンプル コードを次に示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
