---
title: 如何将 Excel 方程导出为其他类型的表达式
linktitle: 导出公式
type: docs
weight: 100
url: /zh/net/export-equation/
---

有时候你可能需要在代码中将Excel公式导出为其他格式以满足工作需要，Aspose.Cells库可以满足你的需求。以下内容介绍一些导出Excel公式为其他格式的方法，希望这些方法对你有所帮助。

这里提供了示例代码，帮助您使用Aspose.Cells实现目标，同时也提供了必要的示例文件。

示例文件：[Sample.xlsx](Sample.xlsx)

## 将公式导出为LaTeX表达式

如果你想将Excel中的公式导出为LaTeX表达式，可以使用[ToLaTeX()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tolatex/)方法。 

下方示例代码展示了如何使用[ToLaTeX()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tolatex/)方法，并将生成的结果插入到HTML中：

### C#-转LaTeX

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Export-equations-as-LaTeX-expressions.cs" >}}

## 将公式导出为MathML表达式

如果你想将Excel中的公式导出为MathML表达式，可以使用[ToMathML()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tomathml/)方法。 

下方示例代码展示了如何使用[ToMathML()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tomathml/)方法，并将生成的结果插入到HTML中：

### C#-转MathML

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Export-equations-as-MathML-expressions.cs" >}}



{{< app/cells/assistant language="csharp" >}}
