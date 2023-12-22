---
title: 使用 ICustomFunction 功能
description: 本文介绍如何使用 Aspose.Cells 库中的 ICustomFunction 功能在 Microsoft Excel 中创建自定义函数。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法来定义和注册自定义函数并获取结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /zh/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

本文详细介绍了如何使用 ICustomFunction 功能通过 Aspose.Cells API 实现自定义函数。

ICustomFunction接口允许添加自定义公式计算函数来扩展Aspose.Cells'核心计算引擎以满足某些要求。此功能对于在模板文件或代码中定义自定义（用户定义）函数非常有用，其中可以像任何其他默认 Microsoft Excel 函数一样使用 Aspose.Cells API 来实现和评估自定义函数。

请注意，该接口已被替换为[抽象计算引擎](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/)并将在未来被删除。关于新 API 的一些技术文章/示例：[这里](/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)和[这里](/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **创建和评估用户定义函数**
本文演示了 ICustomFunction 接口的实现，以编写自定义函数并在电子表格中使用它来获取结果。我们将通过名称定义一个自定义函数**我的函数**它将接受 2 个参数以及以下详细信息。

- 第一个参数指的是单个单元格
- 第二个参数指的是单元格范围

自定义函数将添加指定为第二个参数的单元格范围中的所有值，并将结果除以第一个参数中的值。

以下是我们如何实现CalculateCustomFunction 方法。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


以下是如何在电子表格中使用新定义的函数



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **概述**
Aspose.Cells API 只是在相应参数为引用或其计算结果为引用时将 ReferredArea 对象放入“paramsList”中。如果您需要引用本身，那么您可以直接使用 ReferredArea。如果需要从公式位置对应的引用中获取单个单元格的值，可以使用 ReferredArea.GetValue(rowOffset, int colOffset) 方法。如果您需要整个区域的单元格值数组，那么您可以使用 ReferredArea.GetValues 方法。

由于 Aspose.Cells API 在“paramsList”中提供了 ReferredArea，因此不再需要“contextObjects”中的 ReferredAreaCollection（在旧版本中，它无法始终为自定义函数的参数提供一对一映射），因此它已从“contextObjects”中删除。

{{< highlight "java" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
