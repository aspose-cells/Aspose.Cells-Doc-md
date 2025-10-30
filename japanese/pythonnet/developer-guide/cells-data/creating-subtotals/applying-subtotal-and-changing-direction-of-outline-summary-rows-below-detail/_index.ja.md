---
title: 小計を適用し、詳細以下のアウトラインサマリー行を変更する
type: docs
weight: 100
url: /ja/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for Python via .NET APIを使用して小計を適用し、アウトラインサマリーの方向を変更する方法を学びます。
keywords: Python Excelライブラリ、小計の適用、小計の追加、アウトラインサマリーの方向の変更、右側のディテールの下のアウトラインサマリー行の方向の変更、小計の作成
---

{{% alert color="primary" %}}

この記事では、データに小計を適用し、詳細の下にアウトラインサマリー行の方向を変更する方法について説明します。

データに小計を適用する方法を説明します。次のパラメータを取ります。

- **ca** - 小計を適用する範囲
- **group_by** - グループ化するフィールド、ゼロベースの整数オフセット
- **function** - 小計関数
- **total_list** - アウトラインに追加されるフィールドのゼロベースのフィールドオフセットの配列
- **replace** - 現在の小計を置き換えるかどうかを示す
- **page_breaks** - グループ間にページ区切りを追加するかどうかを示す
- **summary_below_data** - データの下にサマリーを追加するかどうかを示す

また、以下のスクリーンショットに示すように、Worksheet.Outline.SummaryRowBelowプロパティを使用してアウトラインの**詳細以下のサマリー行**の方向を制御できます。これを実行するには、Microsoft Excelで**データ > アウトライン > 設定**を開くことができます。

![todo:image_alt_text](1.png)

{{% /alert %}}

## **ソースファイルと出力ファイルの画像**

次のスクリーンショットは、以下のサンプルコードで使用されるソース Excel ファイルを示しており、列 A と列 B にいくつかのデータが含まれています。

![todo:image_alt_text](2.png)

サンプルコードによって生成されたExcelファイルの出力画面が以下に表示されています。範囲A2:B11に小計が適用されたことがわかります。また、アウトラインの方向は、詳細の下に集計行が表示されます。

![todo:image_alt_text](3.png)

## **Pythonコードを使用して小計を適用し、アウトラインの方向を変更する方法**

次に示すコードは、上記の出力を実現するサンプルコードです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
