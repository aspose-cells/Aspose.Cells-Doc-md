---
title: 使用Aspose.Cells中的FormulaText函数
description: 本文介绍如何使用Aspose.Cells库中的FormulaText函数处理Microsoft Excel中的公式。通过加载现有的Excel文件或者创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来获取和设置单元格的公式文本并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, FormulaText functions
type: docs
weight: 60
url: /zh/net/using-formulatext-function-in-aspose-cells/
---
{{% alert color="primary" %}} 

FormulaText 是 Excel 2013 及更高版本的函数。 Excel 2010 或 2007 等早期版本不支持它。顾名思义，它打印给定单元格中存在的公式文本。本文将向您展示如何使用 Aspose.Cells 使用此功能。

{{% /alert %}} 

以下示例代码显示了 FormulaText 与 Aspose.Cells 的用法。该代码首先在单元格 A1 中写入公式，然后在单元格 A2 中使用 FormulaText 打印公式文本。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
##  **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight "java" >}}

 =SUM(B1:B10)

{{< /highlight >}}
