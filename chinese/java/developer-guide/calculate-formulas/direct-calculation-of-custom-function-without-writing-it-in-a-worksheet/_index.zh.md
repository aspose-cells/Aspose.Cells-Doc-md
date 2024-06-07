---
title: 在工作表中直接计算自定义函数而不将其写入
type: docs
weight: 650
url: /zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

本文说明了如何在不先在工作表中编写自定义函数的情况下直接计算您的自定义函数。请使用[Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\))方法实现此目的。

{{% /alert %}} 
## **在工作表中直接计算自定义函数而不将其写入**
请参阅下面的示例代码，说明了此方法的用法。我们使用一个名为* MyCompany.CustomFunction()*的自定义函数，并通过自己计算其值为"Aspose.Cells。"，然后计算引擎会将此值与单元格A1的值自动连接起来，即"Welcome to "，计算的最终值返回为"Welcome to Aspose.Cells."。如您所见的代码，我们未在工作表中编写我们的自定义函数，而是通过我们自己的自定义逻辑直接计算。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **控制台输出**
以下是上述示例代码的控制台输出。

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **相关文章**
{{% alert color="primary" %}} 

- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
