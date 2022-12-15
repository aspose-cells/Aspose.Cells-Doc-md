---
title: 使用 ICustomFunction 功能
type: docs
weight: 890
url: /zh/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

本文详细介绍了如何使用 ICustomFunction 功能通过 Aspose.Cells API 实现自定义函数。

ICustomFunction 接口允许添加自定义公式计算函数以扩展 Aspose.Cells' 核心计算引擎以满足某些需求。此功能对于在模板文件或代码中定义自定义（用户定义）函数很有用，在这些代码中自定义函数可以像任何其他默认 Microsoft Excel 函数一样使用 Aspose.Cells API 实现和评估。

请注意，此接口已被替换为[抽象计算引擎](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)并将在未来被删除。有关新 API 的一些技术文章/示例：[这里](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)和[这里](/cells/zh/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

如果您是 Aspose.Cells for Java API 的新手，请查看[这个](https://docs.aspose.com/cells/java/installation/)文章了解如何在项目中获取和引用 Aspose.Cells for Java。

{{% /alert %}} 
## **创建和评估用户定义的函数**
本文演示了 ICustomFunction 接口的实现，以编写自定义函数并在电子表格中使用它来获取结果。我们将按名称定义一个自定义函数**我的函数**它将接受具有以下详细信息的 2 个参数。

- 第一个参数是指单个单元格
- 第二个参数是指单元格范围

自定义函数将添加指定为第二个参数的单元格范围内的所有值，并将结果除以第一个参数中的值。

以下是我们如何实现 calculateCustomFunction 方法。

**Java**

{{< highlight "csharp" >}}

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

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells API只是在对应参数为引用或其计算结果为引用时将ReferredArea对象放入“paramsList”中。如果您需要引用本身，那么您可以直接使用 ReferredArea。如果需要从与公式位置对应的引用中获取单个单元格的值，可以使用 ReferredArea.getValue(rowOffset, int colOffset) 方法。如果您需要整个区域的单元格值数组，则可以使用 ReferredArea.getValues 方法。

由于 Aspose.Cells API 在“paramsList”中提供了 ReferredArea，因此不再需要“contextObjects”中的 ReferredAreaCollection（在旧版本中，它无法始终为自定义函数的参数提供一对一的映射）因此它已从“contextObjects”中删除。

{{< highlight "java" >}}

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
