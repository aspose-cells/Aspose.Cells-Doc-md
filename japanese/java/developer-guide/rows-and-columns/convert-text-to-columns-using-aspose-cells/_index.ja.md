---
title: Aspose.Cells を使用してテキストを列に変換します
type: docs
weight: 70
url: /ja/java/convert-text-to-columns-using-aspose-cells/
---
## **考えられる使用シナリオ**
Microsoft Excel を使用して、テキストを列に変換できます。この機能は、*データ ツール*下*データ*タブ。列の内容を複数の列に分割するには、Microsoft Excel がセルの内容を複数のセルに分割するためのコンマ (またはその他の文字) などの特定の区切り文字をデータに含める必要があります。 Aspose.Cells もこの機能を提供しています[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)） 方法。
## **Aspose.Cells を使用してテキストを列に変換します**
次のサンプル コードは、[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)） 方法。このコードは、まず、最初のワークシートの列 A に何人かの人の名前を追加します。姓と名はスペース文字で区切られています。次に、[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) ) メソッドを列 A に適用し、出力 Excel ファイルとして保存します。開くと[出力エクセルファイル](25395230.xlsx)、このスクリーンショットに示すように、名は列 A にあり、姓は列 B にあることがわかります。

![todo:画像_代替_文章](convert-text-to-columns-using-aspose-cells_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
