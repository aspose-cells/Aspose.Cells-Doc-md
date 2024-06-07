---
title: 使用ICustomFunction功能
type: docs
weight: 890
url: /zh/java/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

本文详细介绍了如何使用ICustomFunction功能来实现使用Aspose.Cells API实现自定义函数。

ICustomFunction接口允许添加自定义公式计算函数以扩展Aspose.Cells的核心计算引擎，以满足特定要求。这个功能对于在模板文件或代码中定义自定义（用户定义）函数很有用，其中可以使用Aspose.Cells API来实现和评估自定义函数，就像任何其他默认的Microsoft Excel函数一样。

请注意，此接口已经被[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)替换，并将来会被移除。关于新API的一些技术文章/示例: [这里](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) 和 [这里](/cells/zh/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

如果您对Aspose.Cells for Java APIs还不熟悉，请查阅[此文档](https://docs.aspose.com/cells/java/installation/)了解如何在项目中获取和引用Aspose.Cells for Java。

{{% /alert %}} 
## **创建和评估用户定义函数**
该文章演示了如何实现ICustomFunction接口来编写自定义函数并在电子表格中使用它来获取结果。我们将通过名称**MyFunc**定义一个自定义函数，它将接受以下两个参数。

- 第一个参数是指一个单元格
- 第二个参数是指一组单元格

自定义函数将会将指定为第二个参数的单元格范围中的所有值相加，并将结果除以第一个参数中的值。

这是我们如何实现calculateCustomFunction方法的。

**Java**

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

这是如何在电子表格中使用新定义的函数

**Java**

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
## **概览**
Aspose.Cells APIs在相应的参数是引用或其计算结果是引用时，将ReferredArea对象直接放入"paramsList"中。如果需要引用本身，则可以直接使用ReferredArea。如果需要获得与公式位置对应的引用中的单元格值，可以使用ReferredArea.getValue(rowOffset, int colOffset)方法。如果需要整个区域的单元格值数组，则可以使用ReferredArea.getValues方法。

由于Aspose.Cells API在"paramsList"中提供了ReferredArea，因此“contextObjects”中的ReferredAreaCollection将不再需要（在旧版本中，无法始终将自定义函数的参数一对一映射到“contextObjects”）因此已从“contextObjects”中移除。

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
