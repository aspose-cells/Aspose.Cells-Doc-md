---
title: 使用ICustomFunction功能
type: docs
weight: 890
url: /zh/java/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

本文详细介绍如何使用ICustomFunction功能使用Aspose.Cells API实现自定义函数。

ICustomFunction接口允许添加自定义公式计算函数以扩展Aspose.Cells的核心计算引擎，以满足特定需求。此功能可用于在模板文件或代码中定义自定义（用户定义）函数，可使用Aspose.Cells API像任何其他默认Microsoft Excel函数一样实现和评估。

请注意，此接口已被[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)取代，并将来会被移除。有关新API的一些技术文章/示例：[这里](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)和[这里](/cells/zh/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

如果您是 Aspose.Cells for Java API 的新手，请查看 [此文档](https://docs.aspose.com/cells/java/installation/) 了解如何在项目中获取和引用 Aspose.Cells for Java。

{{% /alert %}} 
## **创建和评估用户定义的函数**
本文演示了使用ICustomFunction接口实现自定义函数，并在电子表格中使用它获取结果。我们将按名称**MyFunc**定义一个自定义函数，其接受以下参数。

- 第1个参数指代单个单元格
- 第2个参数指代一系列的单元格

自定义函数将添加指定为第2个参数的单元格范围中的所有值，并将结果除以第1个参数中的值。

以下是我们如何实现calculateCustomFunction方法。

Java

{{< highlight csharp >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

以下是如何在电子表格中使用新定义的函数

Java

{{< highlight csharp >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
## **概述**
当对应的参数是引用或其计算结果是引用时，Aspose.Cells API将引用区域对象放入"paramsList"中。如果你需要引用本身，那么可以直接使用引用区域对象。如果需要从与公式位置对应的引用中获取单元格的值，可以使用ReferredArea.getValue(rowOffset, colOffset)方法。如果需要整个区域的单元格值数组，则可以使用ReferredArea.getValues方法。

由于Aspose.Cells API在"paramsList"中提供了ReferredArea，因此"contextObjects"中的ReferredAreaCollection将不再需要（在旧版本中，它并不总是能够给出与自定义函数参数一一对应的映射），因此它已从"contextObjects"中移除。

{{< highlight java >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
