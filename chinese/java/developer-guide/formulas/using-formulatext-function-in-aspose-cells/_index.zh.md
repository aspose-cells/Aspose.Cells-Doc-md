---
title: 在Aspose.Cells中使用FormulaText函数
type: docs
weight: 530
url: /zh/java/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

*FormulaText* 是 Excel 2013 及更高版本的函数。不支持以前版本，如 Excel 2010 或 2007 等。顾名思义，它打印给定单元格中存在的公式的文本。本文将展示如何利用 Aspose.Cells 使用此函数。

{{% /alert %}} 
## **在 Aspose.Cells 中使用 FormulaText 函数**
以下示例代码展示了在 Aspose.Cells 中使用 *FormulaText* 的用法。该代码首先在单元格 A1 中写入公式，然后在单元格 A2 中使用 *FormulaText* 打印公式的文本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingFormulaTextfunction-UsingFormulaTextfunction.java" >}}
## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
