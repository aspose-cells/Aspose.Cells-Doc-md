---
title: Using ICustomFunction Feature
description: This article describes how to create a custom function in Microsoft Excel using the ICustomFunction feature in the Aspose.Cells library. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to define and register custom functions and get the results. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions, how to calculate custom fuctions.
type: docs
weight: 30
url: /net/how-to-calculate-custom-fuctions/
---

{{% alert color="primary" %}} 

This article provides a detailed understanding of how to use the ICustomFunction feature to implement custom functions with Aspose.Cells APIs.

The ICustomFunction interface allows to add custom formula calculation functions to extend the Aspose.Cells' core calculation engine in order to meet certain requirements. This feature is useful to define custom (user defined) functions in a template file or in code where the custom function can be implemented and evaluated using Aspose.Cells APIs like any other default Microsoft Excel function.

Please note, this interface has been replaced by [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) and will be removed in future. Some technical articles/examples about the new API: [here](/cells/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) and [here](/cells/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Creating and Evaluating a User-defined Function**
This article demonstrates the implementation of ICustomFunction interface to write a custom function and use it in the spreadsheet to get the results. We will define a custom function by name **MyFunc** which will accepts 2 parameters with following details.

- 1st parameter refers to a single cell
- 2nd parameter refers to a range of cells

The custom function will add all the values from the cell range specified as 2nd parameter and divide the result with value in the 1st parameter.

Here is how we have implemented the CalculateCustomFunction method.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Here is how to use the newly defined function in a spreadsheet



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Overview**
The Aspose.Cells APIs just put the ReferredArea object into the "paramsList" when the corresponding parameter is a reference or its calculated result is reference. If you need the reference itself then you can use the ReferredArea directly. If you need to get value of a single cell from the reference corresponding with the formula's position, you can use ReferredArea.GetValue(rowOffset, int colOffset) method. If you need cell values array for the whole area then you can use ReferredArea.GetValues method.

As the Aspose.Cells APIs give the ReferredArea in "paramsList", the ReferredAreaCollection in "contextObjects" will not be needed anymore (in old versions it was not able to give one-to-one map to the parameters of the custom function always) therefore it has been removed from the "contextObjects".

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