---
title: 直接计算自定义函数，无需先将其编写在工作表中
type: docs
weight: 650
url: /zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

本文介绍如何直接计算您的自定义函数，而无需先在工作表中书写它们。请使用 [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) 方法实现此目的。

{{% /alert %}} 
## **在不将其写入工作表的情况下直接计算自定义函数**
请参阅以下示例代码，以了解此方法的用法。我们使用了一个名为*MyCompany.CustomFunction()*的自定义函数，我们自己计算其值为"Aspose.Cells."，然后此值会自动与单元A1的值"Welcome to "由计算引擎连接，并计算出最终计算后的值"Welcome to Aspose.Cells."。从代码中可以看到，我们没有在工作表中编写自定义函数，而是通过我们自己的自定义逻辑直接计算出来。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **控制台输出**
以下是上面示例代码的控制台输出。

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **相关文章**
{{% alert color="primary" %}} 

- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
