---
title: 小計を適用し、詳細以下のアウトラインサマリー行を変更する
type: docs
weight: 100
url: /ja/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

この記事では、データに小計を適用し、詳細の下にアウトラインサマリー行の方向を変更する方法について説明します。

データに小計を適用する方法を説明します。次のパラメータを取ります。

- **CellArea** - 小計を適用する範囲
- **GroupBy** - グループ化するフィールド（ゼロベースの整数オフセット）
- **Function** - 小計関数
- **TotalList** - 小計が追加されるゼロベースのフィールドオフセットの配列
- **Replace** - 現在の小計を置換するかどうかを示します
- **PageBreaks** - グループ間にページ区切りを追加するかどうかを示します
- **SummaryBelowData** - データの下に要約を追加するかどうかを示します

また、[**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) プロパティを使用して、次のスクリーンショットに示すように、アウトラインの **詳細行の下のサマリー行** の方向を制御できます。これは Microsoft Excel で **データ > アウトライン > 設定** を使用して設定できます。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 例

### サンプルコードでソースと出力ファイルを比較するスクリーンショット

次のスクリーンショットは、以下のサンプルコードで使用されるソース Excel ファイルを示しており、列 A と列 B にいくつかのデータが含まれています。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

次のスクリーンショットは、サンプルコードによって生成された出力 Excel ファイルを示しています。範囲 **A2:B11** に小計が適用され、アウトラインの方向が詳細行の下になっていることがわかります。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### 小計を適用し、詳細の下にアウトラインサマリー行の方向を変更するための Java コード

次に示すコードは、上記の出力を実現するサンプルコードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
{{< app/cells/assistant language="java" >}}
