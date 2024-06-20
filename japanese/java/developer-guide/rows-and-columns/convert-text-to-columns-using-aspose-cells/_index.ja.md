---
title: Aspose.Cellsを使用したテキストを列に変換する
type: docs
weight: 70
url: /ja/java/convert-text-to-columns-using-aspose-cells/
---

## **可能な使用シナリオ**
Microsoft Excelを使用してデータツールの*データ*タブの下から、テキストを列に変換することが可能です。1つのセルの内容を複数のセルに分割するには、Microsoft Excelがセルの内容を複数のセルに分割するために利用するカンマ（または任意の文字）などの特定のデリミタがデータに含まれている必要があります。Aspose.Cellsも[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) メソッドを介してこの機能を提供します。
## **Aspose.Cellsを使用したテキストを列に変換する**
以下のサンプルコードは、[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) メソッドの使用方法を説明しています。コードはまず、最初のワークシートの列Aにいくつかの人の名前を追加します。名前の頭と名字はスペースで区切られています。そして、[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) メソッドを列Aに適用し、出力エクセルファイルとして保存します。[出力されたエクセルファイル](25395230.xlsx)を開くと、名前が列Aに、姓が列Bに入っているのが確認できます。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
