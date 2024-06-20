---
title: 条件付き書式を使用して交互の行と列に網掛けを適用する
description: Aspose.CellsライブラリをC#で使用して、セルの外観と表示に条件付き書式のシャドウを適用する方法。これらの条件を調整することで、セルの外観をより細かく制御できます。
keywords: Aspose.Cells, 条件付き書式, C#, 交互の行, 交互の列, シャドウ
type: docs
weight: 30
url: /ja/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells APIは、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)オブジェクトの条件付き書式ルールを追加および操作する手段を提供します。これらのルールは、条件や規則に基づいて所望の書式を得るために多様な方法で調整できます。この記事では、Aspose.Cells for .NET APIを使用して、条件付き書式ルールやExcelの組み込み関数を使用して交互の行と列にシェーディングを適用する方法を示します。

{{% /alert %}}

この記事では、Excelの組み込み関数であるROW、COLUMN、MODなどの詳細について説明します。これらの関数の詳細な内容を提供し、コードスニペットの理解を深めます。

- **ROW()** 関数は、セル参照の行番号を返します。参照パラメータが省略された場合、ROW関数が入力されたセルのセルアドレスを参照するものとします。
- **COLUMN()** 関数は、セル参照の列番号を返します。参照パラメータが省略された場合、COLUMN関数が入力されたセルのセルアドレスを参照するものとします。
- **MOD()** 関数は、数値が除算された後の余りを返します。関数の最初のパラメーターは、余りを求めたい数値で、2番目のパラメーターは、数値パラメーターで除算する数です。除数が0の場合、#DIV/0!エラーが返されます。

Aspose.Cells for .NET APIを使用してこの目標を達成するためにコードを書き始めましょう。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

次のスナップショットは、Excelアプリケーションで読み込まれた結果のスプレッドシートを示しています。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

交互の列に網掛けを適用するためには、単に式を **=MOD(ROW(),2)=0** から **=MOD(COLUMN(),2)=0** に変更するだけで済みます。つまり、行索引を取得する代わりに、式を変更して列索引を取得します。 
この場合の結果のスプレッドシートは以下のようになります。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
