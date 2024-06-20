---
title: 条件付き書式を使用して交互の行と列に網掛けを適用する
type: docs
weight: 10
url: /ja/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells APIは、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)オブジェクト用の条件付き書式ルールを追加および操作する手段を提供します。これらのルールは、条件またはルールに基づいて、希望の書式設定を取得するために複数の方法でカスタマイズできます。この記事では、Aspose.Cells for Java APIを使用して条件付き書式ルールおよびExcelの組み込み機能を使用して交互の行と列に網掛けを適用する方法を示します。

{{% /alert %}} 
## **条件付き書式を使用して交互の行および列に網掛けを適用する**
この記事では、Excelの組み込み機能であるROW、COLUMN、MODを使用します。以下に、これらの機能の詳細を示します。提供されるコードスニペットの理解をサポートするために少しの詳細があります。

- **ROW()** 関数は、セル参照の行番号を返します。参照が省略された場合、ROW関数が入力されたセルアドレスを参照と想定します。
- **COLUMN()** 関数は、セル参照の列番号を返します。参照が省略された場合、COLUMN関数が入力されたセルアドレスを参照と想定します。
- **MOD()** 関数は、数値が除算された後の余りを返します。関数の最初のパラメーターは、余りを求めたい数値で、2番目のパラメーターは、数値パラメーターで除算する数です。除数が0の場合、#DIV/0!エラーが返されます。

Aspose.Cells for Java APIのサポートを活用して、目標を達成するためのコードの記述を開始しましょう。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



次のスナップショットは、Excelアプリケーションで読み込まれた結果のスプレッドシートを示しています。

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

交互の列に網掛けを適用するためには、単に式を **=MOD(ROW(),2)=0** から **=MOD(COLUMN(),2)=0** に変更するだけで済みます。つまり、行索引を取得する代わりに、式を変更して列索引を取得します。 
この場合、結果のスプレッドシートは以下の画像のようになります。

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
