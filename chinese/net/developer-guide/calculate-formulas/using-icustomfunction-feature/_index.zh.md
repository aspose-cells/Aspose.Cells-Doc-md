---
title: 使用ICustomFunction功能
description: 本文描述了如何使用Aspose.Cells库中ICustomFunction功能在Microsoft Excel中创建自定义函数。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法定义和注册自定义函数并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、ICustomFunction 功能、自定义函数、如何计算自定义函数。
type: docs
weight: 30
url: /zh/net/how-to-calculate-custom-fuctions/
---

{{% alert color="primary" %}} 

本文详细介绍如何使用ICustomFunction功能使用Aspose.Cells API实现自定义函数。

ICustomFunction接口允许添加自定义公式计算函数以扩展Aspose.Cells的核心计算引擎，以满足特定需求。此功能可用于在模板文件或代码中定义自定义（用户定义）函数，可使用Aspose.Cells API像任何其他默认Microsoft Excel函数一样实现和评估。

请注意，此接口已被[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/)取代，并将在未来删除。关于新API的一些技术文章/示例：[这里](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)和[这里](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **创建和评估用户定义的函数**
本文演示了使用ICustomFunction接口实现自定义函数，并在电子表格中使用它获取结果。我们将按名称**MyFunc**定义一个自定义函数，其接受以下参数。

- 第1个参数指代单个单元格
- 第2个参数指代一系列的单元格

自定义函数将添加指定为第2个参数的单元格范围中的所有值，并将结果除以第1个参数中的值。

这里是我们如何实现CalculateCustomFunction方法的方式。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


以下是如何在电子表格中使用新定义的函数



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **概述**
Aspose.Cells的API在对应参数为引用或其计算结果为引用时，将ReferredArea对象放入"paramsList"中。如果您需要引用本身，可以直接使用ReferredArea。如果需要获取与公式位置对应的引用中单元格的值，可以使用ReferredArea.GetValue(rowOffset, int colOffset)方法。如果需要整个区域的单元格值数组，则可以使用ReferredArea.GetValues方法。

由于Aspose.Cells API在"paramsList"中提供了ReferredArea，因此"contextObjects"中的ReferredAreaCollection将不再需要（在旧版本中，它并不总是能够给出与自定义函数参数一一对应的映射），因此它已从"contextObjects"中移除。

{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
