---
title: ワークシートの Cells の範囲を画像にエクスポート
type: docs
weight: 130
url: /ja/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells を使用してワークシートの画像を作成できます。ただし、ワークシート内のセルの範囲のみを画像にエクスポートする必要がある場合があります。この記事では、これを実現する方法について説明します。

{{% /alert %}}

範囲の画像を取得するには、印刷領域を目的の範囲に設定し、すべての余白を 0 に設定します。[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet)に**真実**.

次のコードは、範囲 E8:H10 の画像を取得します。以下は、コードで使用されているソース ワークブックのスクリーンショットです。任意のブックでコードを試すことができます。

**入力ファイル**

![todo:画像_代替_文章](export-range-of-cells-in-a-worksheet-to-image_1.png)

コードを実行すると、範囲 E8:H10 のみのイメージが作成されます。

**出力画像**

![todo:画像_代替_文章](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

記事もご覧いただけます[ワークシートを別の画像形式に変換する](/cells/ja/java/converting-worksheet-to-different-image-formats/)役に立った。
