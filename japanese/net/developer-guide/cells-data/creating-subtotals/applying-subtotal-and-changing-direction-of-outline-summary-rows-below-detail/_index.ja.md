---
title: 小計を適用し、詳細以下のアウトラインサマリー行を変更する
type: docs
weight: 100
url: /ja/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for .NET APIを使用して、サブトータルを適用し、詳細の下にアウトラインサマリー行の方向を変更する方法について学びます。
keywords: サブトータルを適用し、サブトータルを追加し、詳細の下にアウトラインサマリー行の方向を変更し、詳細の右側にアウトラインサマリー列の方向を変更し、サブトータルを作成し、詳細の下にアウトラインサマリー行の方向を変更する
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

また、以下のスクリーンショットに示すように、Worksheet.Outline.SummaryRowBelowプロパティを使用してアウトラインの**詳細以下のサマリー行**の方向を制御できます。これを実行するには、Microsoft Excelで**データ > アウトライン > 設定**を開くことができます。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## ソースファイルと出力ファイルの画像

次のスクリーンショットは、以下のサンプルコードで使用されるソース Excel ファイルを示しており、列 A と列 B にいくつかのデータが含まれています。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

サンプルコードによって生成されたExcelファイルの出力画面が以下に表示されています。範囲A2:B11に小計が適用されたことがわかります。また、アウトラインの方向は、詳細の下に集計行が表示されます。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## サブトータルの適用とアウトラインサマリー行の方向変更のためのC#コード

次に示すコードは、上記の出力を実現するサンプルコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
