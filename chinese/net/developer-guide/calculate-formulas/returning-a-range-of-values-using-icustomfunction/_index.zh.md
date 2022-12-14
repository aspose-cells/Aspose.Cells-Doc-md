---
title: 使用 ICustomFunction 返回值范围
type: docs
weight: 50
url: /zh/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

这[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)自 Aspose.Cells for Java 20.8 发布以来已弃用。请使用[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)班级。使用的[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)类在下面的文章中描述。

[使用 AbstractCalculationEngine 返回值范围](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells提供[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)用于实现 Microsoft Excel 不支持的用户定义或自定义函数的接口作为内置函数。

大多数情况下，当您实施[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)接口方法，需要返回单个单元格值。但有时，您需要返回一系列值。本文将解释如何从返回值的范围[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

下面代码实现[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)并通过其方法返回值的范围。

创建一个带有函数的类*计算自定义函数*.这个类实现[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

现在在你的程序中使用上面的函数

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
