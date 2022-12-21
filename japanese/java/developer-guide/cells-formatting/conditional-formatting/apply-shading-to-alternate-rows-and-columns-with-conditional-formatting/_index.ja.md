---
title: 条件付き書式を使用して交互の行と列に陰影を適用する
type: docs
weight: 10
url: /ja/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells API は、条件付き書式ルールを追加および操作する手段を提供します[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)物体。これらのルールは、条件またはルールに基づいて目的のフォーマットを取得するために、さまざまな方法で調整できます。この記事では、Aspose.Cells for Java API を使用して、条件付き書式ルールと Excel の組み込み関数を使用して、行と列を交互にシェーディングを適用する方法を示します。

{{% /alert %}} 
## **条件付き書式を使用して交互の行と列に陰影を適用する**
この記事では、ROW、COLUMN、MOD などの Excel の組み込み関数を使用します。先に提供されたコード スニペットをよりよく理解するために、これらの関数の詳細を以下に示します。

- **行（）**関数は、セル参照の行番号を返します。参照を省略した場合、参照はROW関数が入力されたセルアドレスであると見なされます。
- **桁（）**関数は、セル参照の列番号を返します。参照を省略した場合は、COLUMN関数が入力されたセルアドレスを参照したものとみなします。
- **モッド（）**関数は、数値を除数で割った後の剰余を返します。ここで、関数の最初のパラメーターは、求めたい剰余の数値であり、2 番目のパラメーターは、number パラメーターへの除算に使用される数値です。除数が 0 の場合、#DIV/0 が返されます。エラー。

Aspose.Cells for Java API の助けを借りて、目標を達成するためのコードを書き始めましょう。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



次のスナップショットは、Excel アプリケーションに読み込まれた結果のスプレッドシートを示しています。

![todo:画像_代替_文章](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

シェーディングを別の列に適用するには、式を変更するだけです**=MOD(ROW(),2)=0**なので**=MOD(COLUMN(),2)=0** 、 あれは;行インデックスを取得する代わりに、式を変更して列インデックスを取得します。
この場合、結果のスプレッドシートは次の画像のようになります。

![todo:画像_代替_文章](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
