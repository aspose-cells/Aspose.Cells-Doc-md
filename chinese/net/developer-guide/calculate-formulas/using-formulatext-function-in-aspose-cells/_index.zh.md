---
title: 在 Aspose.Cells 中使用 FormulaText 函数
type: docs
weight: 60
url: /zh/net/using-formulatext-function-in-aspose-cells/
---
{{% alert color="primary" %}} 

FormulaText 是 Excel 2013 及更高版本的函数。 Excel 2010 或 2007 等早期版本不支持它。顾名思义，它打印给定单元格中存在的公式文本。本文将向您展示如何使用 Aspose.Cells 使用此功能。

{{% /alert %}} 

以下示例代码显示了 FormulaText 与 Aspose.Cells 的用法。代码首先在单元格 A1 中写入公式，然后在单元格 A2 中使用 FormulaText 打印公式的文本。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight "java" >}}

 =SUM(B1:B10)

{{< /highlight >}}
