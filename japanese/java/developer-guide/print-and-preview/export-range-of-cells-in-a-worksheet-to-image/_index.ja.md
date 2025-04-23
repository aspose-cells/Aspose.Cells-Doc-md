---
title: ワークシート内のセルの範囲をイメージにエクスポート
type: docs
weight: 130
url: /ja/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してワークシートのイメージを作成できます。ただし、ワークシート内のセルの範囲をイメージにエクスポートする必要がある場合があります。この記事では、これをどのように行うかについて説明します。

{{% /alert %}}

範囲の画像を取得するには、印刷範囲を所望の範囲に設定し、すべての余白を0に設定し、[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) を **true** に設定します。

次のコードは、範囲 E8:H10 の画像を取得します。以下はコードで使用されるソースワークブックのスクリーンショットです。任意のワークブックでコードを試すことができます。

**入力ファイル**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

コードを実行すると、範囲 E8:H10 の画像が作成されます。

**出力画像**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

この記事 [ワークシートを異なる画像形式に変換](/cells/ja/java/converting-worksheet-to-different-image-formats/) も参考になるでしょう。
{{< app/cells/assistant language="java" >}}
