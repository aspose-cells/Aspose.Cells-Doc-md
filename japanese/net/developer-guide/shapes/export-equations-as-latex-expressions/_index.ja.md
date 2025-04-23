---
title: Excelから数式を他のタイプにエクスポートする方法
linktitle: 数式をエクスポート
type: docs
weight: 100
url: /ja/net/export-equation/
---

時には、作業ニーズに応じてコード内でExcelの数式を他の形式にエクスポートする必要があります。Aspose.Cellライブラリはこれらのニーズを満たすことができます。以下の内容では、Excelの数式を他の形式にエクスポートする方法についていくつかの手法を紹介します。これらの方法が参考になれば幸いです。

Aspose.Cellsを使用して目標を達成するためのサンプルコードを準備しています。必要なサンプルファイルも提供します。

サンプルファイル：[Sample.xlsx](Sample.xlsx)

## 数式をLaTeX表現としてエクスポート

Excelの数式をLaTeX表現としてエクスポートしたい場合は、[ToLaTeX()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tolatex/)メソッドを使用できます。 

以下のサンプルコードは、[ToLaTeX()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tolatex/)メソッドを使って得られた結果をHTMLに挿入する方法を示しています。

### C#による-LaTeX

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Export-equations-as-LaTeX-expressions.cs" >}}

## 数式をMathML表現としてエクスポート

Excelの数式をMathML表現としてエクスポートしたい場合は、[ToMathML()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tomathml/)メソッドを使用できます。 

以下のサンプルコードは、[ToMathML()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tomathml/)メソッドを使用し、生成された結果をHTMLに挿入する方法を示しています。

### C#による-MathML

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Export-equations-as-MathML-expressions.cs" >}}



{{< app/cells/assistant language="csharp" >}}
