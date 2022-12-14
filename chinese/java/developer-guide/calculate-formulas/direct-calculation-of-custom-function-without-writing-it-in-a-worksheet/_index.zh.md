---
title: 自定义函数直接计算，无需写在工作表中
type: docs
weight: 650
url: /zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

本文介绍了如何直接计算自定义函数而无需先将它们写入工作表。请使用[Worksheet.calculateFormula（字符串公式，CalculationOptions opts）](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) 方法用于此目的。

{{% /alert %}} 
## **自定义函数直接计算，无需写在工作表中**
请参阅下面的示例代码，该代码说明了此方法的用法。我们使用了一个名为*我的公司.CustomFunction()*我们计算它的值为“Aspose.Cells”。由我们自己，然后该值自动与计算引擎“欢迎使用”的单元格 A1 的值连接，最终计算值返回为“欢迎使用 Aspose.Cells”。正如您在代码中看到的那样，我们没有在工作表的任何地方编写我们的自定义函数，它是由我们自己的自定义逻辑直接计算的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **控制台输出**
下面是上述示例代码的控制台输出。

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **相关文章**
{{% alert color="primary" %}} 

- [实施自定义计算引擎以扩展 Aspose.Cells 的默认计算引擎](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
