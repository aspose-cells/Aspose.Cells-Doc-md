---
title: Using ICustomFunction Feature
type: docs
weight: 890
url: /java/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

This article provides a detailed understanding of how to use the ICustomFunction feature to implement custom functions with Aspose.Cells APIs.

The ICustomFunction interface allows to add custom formula calculation functions to extend the Aspose.Cells' core calculation engine in order to meet certain requirements. This feature is useful to define custom (user defined) functions in a template file or in code where the custom function can be implemented and evaluated using Aspose.Cells APIs like any other default Microsoft Excel function.

Please note, this interface has been replaced by [AbstractCalculationEngine](https://apireference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) and will be removed in future. Some technical articles/examples atbout the new API: [here](https://docs.aspose.com/cells/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) and [here](https://docs.aspose.com/cells/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

If you are new to Aspose.Cells for Java APIs, please check [this](http://www.aspose.com/docs/display/cellsjava/Installation) article to know how you can acquire and reference the Aspose.Cells for Java in your project.

{{% /alert %}} 
## **Creating and Evaluating a User-defined Function**
This article demonstrates the implementation of ICustomFunction interface to write a custom function and use it in the spreadsheet to get the results. We will define a custom function by name **MyFunc** which will accepts 2 parameters with following details.

- 1st parameter refers to a single cell
- 2nd parameter refers to a range of cells

The custom function will add all the values from the cell range specified as 2nd parameter and divide the result with value in the 1st parameter.

Here is how we have implemented the calculateCustomFunction method.

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

Here is how to use the newly defined function in a spreadsheet

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
## **Overview**
The Aspose.Cells APIs just put the ReferredArea object into the "paramsList" when the corresponding parameter is a reference or its calculated result is reference. If you need the reference itself then you can use the ReferredArea directly. If you need to get value of a single cell from the reference corresponding with the formula's position, you can use ReferredArea.getValue(rowOffset, int colOffset) method. If you need cell values array for the whole area then you can use ReferredArea.getValues method.

As the Aspose.Cells APIs give the ReferredArea in "paramsList", the ReferredAreaCollection in "contextObjects" will not be needed anymore (in old versions it was not able to give one-to-one map to the parameters of the custom function always) therefore it has been removed from the "contextObjects".

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
