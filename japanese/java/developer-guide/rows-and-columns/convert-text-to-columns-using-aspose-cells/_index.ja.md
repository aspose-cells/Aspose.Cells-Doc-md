---
title: Aspose.Cellsを使用したテキストを列に変換する
type: docs
weight: 70
url: /ja/java/convert-text-to-columns-using-aspose-cells/
---

## **可能な使用シナリオ**
Microsoft Excelを使用してテキストを列に変換できます。この機能は、*Data Tools*の*Data*タブにあります。列の内容を複数の列に分割するには、そのデータに特定の区切り文字（カンマやその他の文字）を含める必要があり、その区切り文字に基づいてMicrosoft Excelはセルの内容を複数のセルに分割します。Aspose.Cellsもこの機能を[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-)メソッドを通じて提供しています。
## **Aspose.Cellsを使用したテキストを列に変換する**
次のサンプルコードは、[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) メソッドの使用方法を説明しています。最初に、最初のワークシートの列Aにいくつかの人名を追加します。名前と名字はスペース文字で区切られています。その後、列Aに対して [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) を適用し、出力Excelファイルとして保存します。[出力Excelファイル](25395230.xlsx) を開くと、スクリーンショットのように、名前が列Aに、名字が列Bにあるのが見えます。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
