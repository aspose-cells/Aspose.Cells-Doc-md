---
title: Excelから数式を他のタイプにエクスポートする方法
linktitle: 数式をエクスポート
type: docs
weight: 100
url: /ja/python-java/export-equation/
---

時には、作業ニーズに応じてコード内でExcelの数式を他の形式にエクスポートする必要があります。Aspose.Cellライブラリはこれらのニーズを満たすことができます。以下の内容では、Excelの数式を他の形式にエクスポートする方法についていくつかの手法を紹介します。これらの方法が参考になれば幸いです。

ここにサンプルコードを用意しました。Aspose.Cells for Python via Javaを使用して目標を達成するのに役立ちます。必要なサンプルファイルも提供しています。

サンプルファイル：[Sample.xlsx](Sample.xlsx)

## 数式をLaTeX表現としてエクスポート

Excelの数式をLaTeX式としてエクスポートしたい場合は、[toLaTeX()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toLaTeX())メソッドを使用できます。 

次のサンプルコードは、[toLaTeX()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toLaTeX())メソッドの使用方法と、生成した結果をHTMLに挿入する方法を示しています。

### To-LaTeX

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Export-equations-as-LaTeX-expressions.py" >}}

## 数式をMathML表現としてエクスポート

Excelの数式をMathML式としてエクスポートしたい場合は、[toMathML()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toMathML())メソッドを使用できます。 

次のサンプルコードは、[toMathML()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toMathML())メソッドの使用方法と、生成した結果をHTMLに挿入する方法を示しています。

### To-MathML

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Export-equations-as-MathML-expressions.py" >}}



{{< app/cells/assistant language="csharp" >}}
