---
title: GolangをC++経由で使用して詳細の下のアウトラインサマリー行に小計を適用し、方向を変更する
linktitle: 小計を適用し、詳細以下のアウトラインサマリー行を変更する
type: docs
weight: 100
url: /ja/go-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: サブトータルを適用し、詳細の下にあるアウトライン集計行の方向を変更する方法について、Aspose.Cells for C++ APIを使用して学びます。
keywords: サブトータルを適用し、サブトータルを追加し、詳細の下にアウトラインサマリー行の方向を変更し、詳細の右側にアウトラインサマリー列の方向を変更し、サブトータルを作成し、詳細の下にアウトラインサマリー行の方向を変更する
---

{{% alert color="primary" %}}

この記事では、データにサブトータルを適用し、詳細の下にあるアウトライン集計行の方向を変更する方法について説明します。

データに対してサブトータルを適用するには、[**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/go-cpp/cells/subtotal_cellarea_int_consolidationfunction_int32array/)メソッドを使用します。次のパラメータを取ります：

- **CellArea** - 小計を適用する範囲
- **GroupBy** - グループ化するフィールド（ゼロベースの整数オフセット）
- **Function** - 小計関数
- **TotalList** - 小計が追加されるゼロベースのフィールドオフセットの配列
- **置換** - 現在のサブトータルを置き換えるかどうかを示す
- **ページ区切り** - グループ間にページ区切りを追加するかどうかを示します
- **SummaryBelowData** - データの下にサマリーを追加するかどうかを示します。

また、以下のスクリーンショットのように、`Worksheet.Outline.SummaryRowBelow` プロパティを使用して、アウトラインの **詳細行の下のサマリー** の方向を制御できます。この設定はMicrosoft Excelの **データ > アウトライン > 設定** から開くことができます。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## ソースファイルと出力ファイルの画像

次のスクリーンショットは、以下のサンプルコードで使用されるソース Excel ファイルを示しており、列 A と列 B にいくつかのデータが含まれています。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

サンプルコードによって生成されたExcelファイルの出力画面が以下に表示されています。範囲A2:B11に小計が適用されたことがわかります。また、アウトラインの方向は、詳細の下に集計行が表示されます。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## 小計を適用し、アウトラインサマリー行の方向を変更するC++コード

次に示すコードは、上記の出力を実現するサンプルコードです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyingSubtotalAndChangingDirectionOfOutlineSummaryRowsBelowDetail.go" >}}
