---
title: 使用ICustomFunction功能
description: 该文章描述了如何使用Aspose.Cells库中的ICustomFunction功能在Microsoft Excel中创建自定义函数。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法定义和注册自定义函数并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, ICustomFunction功能, 自定义函数
type: docs
weight: 30
url: /zh/net/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

本文详细介绍了如何使用ICustomFunction功能来实现使用Aspose.Cells API实现自定义函数。

ICustomFunction接口允许添加自定义公式计算函数以扩展Aspose.Cells的核心计算引擎，以满足特定要求。这个功能对于在模板文件或代码中定义自定义（用户定义）函数很有用，其中可以使用Aspose.Cells API来实现和评估自定义函数，就像任何其他默认的Microsoft Excel函数一样。

请注意，该接口已被 [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) 替换，并将在未来被移除。关于新 API 的一些技术文章/示例：[这里](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) 和 [这里](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **创建和评估用户定义函数**
该文章演示了如何实现ICustomFunction接口来编写自定义函数并在电子表格中使用它来获取结果。我们将通过名称**MyFunc**定义一个自定义函数，它将接受以下两个参数。

- 第一个参数是指一个单元格
- 第二个参数是指一组单元格

自定义函数将会将指定为第二个参数的单元格范围中的所有值相加，并将结果除以第一个参数中的值。

这是我们如何实现CalculateCustomFunction方法。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


这是如何在电子表格中使用新定义的函数



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **概览**
在Aspose.Cells API中，当相应参数是引用或其计算结果为引用时，将ReferredArea对象放入"paramsList"中。如果您需要引用本身，那么可以直接使用ReferredArea。如果您需要根据公式位置获取引用对应的单元格值，可以使用ReferredArea.GetValue(rowOffset, int colOffset)方法。如果您需要整个区域的单元格值数组，则可以使用ReferredArea.GetValues方法。

由于Aspose.Cells API在"paramsList"中提供了ReferredArea，因此“contextObjects”中的ReferredAreaCollection将不再需要（在旧版本中，无法始终将自定义函数的参数一对一映射到“contextObjects”）因此已从“contextObjects”中移除。

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
