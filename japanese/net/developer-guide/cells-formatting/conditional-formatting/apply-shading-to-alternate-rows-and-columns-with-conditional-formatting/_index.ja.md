---
title: 条件付き書式設定を使用して交互の行と列にシェーディングを適用する
description: C# の Aspose.Cells ライブラリを使用して、行と列を交互に条件付き書式設定のシャドウを適用する方法。これらの基準を調整することで、セルの外観をより詳細に制御できるようになります。
keywords: Aspose.Cells, Conditional Formatting, C#, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /ja/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells API は、条件付き書式ルールを追加および操作する手段を提供します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体。これらのルールは、条件やルールに基づいて目的の書式を取得するために、さまざまな方法で調整できます。この記事では、条件付き書式ルールと Excel の組み込み関数を利用して、Aspose.Cells for .NET API を使用して交互の行と列に網掛けを適用する方法を示します。

{{% /alert %}}

この記事では、ROW、COLUMN、MOD などの Excel の組み込み関数を利用します。ここで提供されるコード スニペットをよりよく理解するために、これらの関数の詳細をいくつか示します。

- **ROW()**関数はセル参照の行番号を返します。参照パラメーターを省略した場合、参照は ROW 関数が入力されたセル アドレスであるとみなされます。
- **COLUMN()**関数はセル参照の列番号を返します。参照パラメータを省略した場合、参照は COLUMN 関数が入力されたセル アドレスであるとみなされます。
- **MOD()**この関数は、数値を除数で割った後の剰余を返します。この関数の最初のパラメーターは剰余を求める数値、2 番目のパラメーターは数値パラメーターに分割するために使用される数値です。除数が 0 の場合、#DIV/0! が返されます。エラー。

Aspose.Cells for .NET API を使用して、この目標を達成するためのコードを書き始めましょう。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

次のスナップショットは、Excel アプリケーションに読み込まれた結果のスプレッドシートを示しています。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

代替列にシェーディングを適用するには、式を変更するだけです。**=MOD(ROW(),2)=0** *=MOD(COLUMN(),2)=0**、つまり;行インデックスを取得する代わりに、列インデックスを取得するように数式を変更します。
この場合、結果として得られるスプレッドシートは次のようになります。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
