---
title: 使用 ICustomFunction 功能
type: docs
weight: 30
url: /zh/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

本文详细介绍了如何使用 ICustomFunction 功能通过 Aspose.Cells API 实现自定义函数。

ICustomFunction 接口允许添加自定义公式计算函数以扩展 Aspose.Cells' 核心计算引擎以满足某些需求。此功能对于在模板文件或代码中定义自定义（用户定义）函数很有用，在这些代码中自定义函数可以像任何其他默认 Microsoft Excel 函数一样使用 Aspose.Cells API 实现和评估。

{{% /alert %}} 
## **创建和评估用户定义的函数**
本文演示了 ICustomFunction 接口的实现，以编写自定义函数并在电子表格中使用它来获取结果。我们将按名称定义一个自定义函数**我的函数**它将接受具有以下详细信息的 2 个参数。

- 第一个参数是指单个单元格
- 第二个参数是指单元格范围

自定义函数将添加指定为第二个参数的单元格范围内的所有值，并将结果除以第一个参数中的值。

下面是我们如何实现 CalculateCustomFunction 方法。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


以下是如何在电子表格中使用新定义的函数



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **概述**
Aspose.Cells API只是在对应参数为引用或其计算结果为引用时将ReferredArea对象放入“paramsList”中。如果您需要引用本身，那么您可以直接使用 ReferredArea。如果需要从与公式位置对应的引用中获取单个单元格的值，可以使用 ReferredArea.GetValue(rowOffset, int colOffset) 方法。如果您需要整个区域的单元格值数组，则可以使用 ReferredArea.GetValues 方法。

由于 Aspose.Cells API 在“paramsList”中提供了 ReferredArea，因此不再需要“contextObjects”中的 ReferredAreaCollection（在旧版本中，它无法始终为自定义函数的参数提供一对一的映射）因此它已从“contextObjects”中删除。

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
