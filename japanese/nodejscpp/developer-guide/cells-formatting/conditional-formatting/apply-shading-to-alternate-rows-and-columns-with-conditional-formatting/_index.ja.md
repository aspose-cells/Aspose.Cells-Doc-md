---
title: 条件付き書式を使用して交互の行と列に網掛けを適用する
linktitle: 条件付き書式を使用して交互の行と列に網掛けを適用する
description: Node.js経由のC++でAspose.Cellsライブラリを使用し、行と列の交互に影をつける条件付き書式を適用する方法。これらの基準を調整して、セルの外観や表示をよりコントロールできます。
keywords: Aspose.Cells、条件付き書式、Node.js経由のC++、交互の行、交互の列、影
type: docs
weight: 30
url: /ja/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells APIは、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)オブジェクトの条件付き書式ルールを追加・操作する手段を提供します。これらのルールは、条件やルールに基づいて望ましい書式を得るためにさまざまに調整可能です。この記事では、Aspose.Cells for Node.js via C++ APIを使用して、条件付き書式ルールとExcelのビルトイン関数を用いて交互の行・列にシェーディングを適用する方法を示します。

{{% /alert %}}

この記事では、Excelの組み込み関数であるROW、COLUMN、MODなどの詳細について説明します。これらの関数の詳細な内容を提供し、コードスニペットの理解を深めます。

- **ROW()**関数は、セル参照の行番号を返します。引数に参照を省略した場合は、そのセルアドレスに対して値を返します。
- **COLUMN()**関数は、セル参照の列番号を返します。引数に参照を省略した場合は、そのセルアドレスに対して値を返します。
- **MOD()** 関数は、数値が除算された後の余りを返します。関数の最初のパラメーターは、余りを求めたい数値で、2番目のパラメーターは、数値パラメーターで除算する数です。除数が0の場合、#DIV/0!エラーが返されます。

この目標を達成するためのコードを書き始めましょう。Aspose.Cells for Node.js via C++ APIを使用して。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyShadingToAlternateRowsAndColumns.js" >}}


次のスナップショットは、Excelアプリケーションで読み込まれた結果のスプレッドシートを示しています。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

交互の列に網掛けを適用するためには、単に式を **=MOD(ROW(),2)=0** から **=MOD(COLUMN(),2)=0** に変更するだけで済みます。つまり、行索引を取得する代わりに、式を変更して列索引を取得します。  
この場合の結果のスプレッドシートは以下のようになります。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="nodejs-cpp" >}}
