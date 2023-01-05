---
title: リンクされた図形の値を更新
type: docs
weight: 3000
url: /ja/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

場合によっては、セルにリンクされたリンクされた図形が Excel ファイルに含まれていることがあります。 Microsoft エクセルで連結セルの値を変更すると、連結図形の値も変更されます。ワークブックを XLS または XLSX 形式で保存する場合、これは Aspose.Cells でも問題なく機能します。ただし、ワークブックを PDF または HTML 形式で保存する場合は、呼び出す必要があります。[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) メソッドを使用して、リンクされた図形の値を更新します。

{{% /alert %}}

## 例

次のスクリーンショットは、以下のサンプル コードで使用されるソース Excel ファイルを示しています。リンクがあります**写真1**セル A1 にリンクされています。セル A1 の値を Aspose.Cells に変更して呼び出します[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() の値を更新するメソッド**写真1**PDF 形式で保存します。

![todo:画像_代替_文章](refresh-values-of-linked-shapes_1.png)

ダウンロードできます[ソースの Excel ファイル](5472956.xlsx)そしてその[出力 PDF](5472955.pdf)指定されたリンクから。

### Java リンクされた図形の値を更新するコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
