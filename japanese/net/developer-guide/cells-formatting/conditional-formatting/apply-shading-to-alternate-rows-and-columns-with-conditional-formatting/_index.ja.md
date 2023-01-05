---
title: 条件付き書式を使用して交互の行と列に陰影を適用する
type: docs
weight: 30
url: /ja/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells API は、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体。これらのルールは、条件またはルールに基づいて目的のフォーマットを取得するために、さまざまな方法で調整できます。この記事では、Aspose.Cells for .NET API を使用して、条件付き書式ルールと Excel の組み込み関数を使用して、交互の行と列に陰影を適用する方法を示します。

{{% /alert %}}

この記事では、ROW、COLUMN、MOD などの Excel の組み込み関数を使用します。先に提供されたコード スニペットをよりよく理解するために、これらの関数の詳細を次に示します。

- **行（）**関数は、セル参照の行番号を返します。参照パラメーターを省略した場合、参照は ROW 関数が入力されたセル アドレスであると見なされます。
- **桁（）**関数は、セル参照の列番号を返します。参照パラメータが省略された場合、参照は COLUMN 関数が入力されたセル アドレスであると見なされます。
- **モッド（）**関数は、数値を除数で割った後の剰余を返します。ここで、関数の最初のパラメーターは、求めたい剰余の数値であり、2 番目のパラメーターは、number パラメーターへの除算に使用される数値です。除数が 0 の場合、#DIV/0 が返されます。エラー。

Aspose.Cells for .NET API の助けを借りて、この目標を達成するためのコードを書き始めましょう。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

次のスナップショットは、Excel アプリケーションに読み込まれた結果のスプレッドシートを示しています。

|![todo:画像_代替_文章](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
|:- |

シェーディングを別の列に適用するには、式を変更するだけです**=MOD(ROW(),2)=0**なので**=MOD(COLUMN(),2)=0** 、 あれは;行インデックスを取得する代わりに、式を変更して列インデックスを取得します。
この場合、結果のスプレッドシートは次のようになります。

|![todo:画像_代替_文章](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
|:- |
