---
title: 使用 ICustomFunction 返回值范围
description: 本文介绍如何使用 Aspose.Cells 库在 Microsoft Excel 中通过 ICustomFunction 返回一系列值。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法来获取一定范围的值并返回结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, ICustomFunction, returns a series of values
type: docs
weight: 50
url: /zh/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

这[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)自 Aspose.Cells for Java 20.8 发布以来已弃用。请使用[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)班级。使用[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)类在下面的文章中描述。

[使用 AbstractCalculationEngine 返回一系列值](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells提供[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)接口，用于实现 Microsoft Excel 不支持的用户定义或自定义函数作为内置函数。

大多数时候当你实施[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)接口方法，您需要返回单个单元格值。但有时，您需要返回一系列值。本文将解释如何返回值的范围[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

下面的代码实现[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)并通过其方法返回值的范围。

创建一个带有函数 *CalculateCustomFunction* 的类。这个类实现了[**自定义函数**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

现在在您的程序中使用上面的函数

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
