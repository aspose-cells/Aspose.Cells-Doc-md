---
title: リンクされた形状の値をリフレッシュ
type: docs
weight: 3000
url: /ja/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Excelファイルには、あるセルにリンクされたリンクされた図形がある場合があります。Microsoft Excelでは、リンクされたセルの値を変更すると、リンクされた図形の値も変更されます。これはAspose.Cellsでも同様に機能し、XLSまたはXLSX形式でブックを保存する場合にうまく機能します。ただし、ブックをPDFまたはHTML形式で保存する場合は、リンクされた図形の値を更新するために[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--)メソッドを呼び出す必要があります。

{{% /alert %}}

## 例

次のスクリーンショットは、以下に示すサンプルコードで使用されるソースExcelファイルを示しています。**Picture 1** がセルA1にリンクされています。セルA1の値をAspose.Cellsで変更し、**Picture 1**の値を更新し、PDF形式で保存します。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

指定されたリンクから[source Excel file](5472956.xlsx)と[output PDF](5472955.pdf)をダウンロードできます。

### リンクされた図形の値を更新するJavaコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
