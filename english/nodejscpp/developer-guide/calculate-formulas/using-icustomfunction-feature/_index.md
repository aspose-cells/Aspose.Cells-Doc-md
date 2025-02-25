---
title: Using ICustomFunction Feature with Node.js via C++
linktitle: Using ICustomFunction Feature
description: This article describes how to create a custom function in Excel using the ICustomFunction feature in the Aspose.Cells library for Node.js via C++. Load an existing Excel file or create a new one, define and register custom functions, and save the modified file.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions, how to calculate custom functions Node.js via C++.
type: docs
weight: 30
url: /nodejs-cpp/how-to-calculate-custom-functions/
---

{{% alert color="primary" %}} 

This article provides a detailed understanding of how to use the ICustomFunction feature to implement custom functions with Aspose.Cells APIs for Node.js via C++.

The ICustomFunction interface allows adding custom formula calculation functions to extend the Aspose.Cells' core calculation engine to meet certain requirements. This feature is useful to define custom (user-defined) functions in a template file or in code where the custom function can be implemented and evaluated using Aspose.Cells APIs like any other default Excel function.

Please note, this interface has been replaced by [AbstractCalculationEngine](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/) and will be removed in future. Some technical articles/examples about the new API: [here](/cells/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) and [here](/cells/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Creating and Evaluating a User-defined Function**
This article demonstrates the implementation of ICustomFunction interface to write a custom function and use it in the spreadsheet to get the results. We will define a custom function by name **MyFunc** which will accept 2 parameters with the following details.

- 1st parameter refers to a single cell
- 2nd parameter refers to a range of cells

The custom function will add all the values from the cell range specified as the 2nd parameter and divide the result by the value in the 1st parameter.

Here is how we have implemented the CalculateCustomFunction method.

```javascript
const { CustomFunction } = require('your-cpp-addon');

class CustomFunction {
    calculateCustomFunction(functionName, paramsList, contextObjects) {
        let total = 0.0;
        try {
            // Get value of first parameter
            let firstParamB1 = parseFloat(paramsList[0]);

            // Get value of second parameter
            let secondParamC1C5 = paramsList[1];

            // get every item value of second parameter
            secondParamC1C5.forEach(value => {
                total += parseFloat(value[0]);
            });

            total = total / firstParamB1;
        } catch (error) {
            // Handle error
        }

        // Return result of the function
        return total;
    }
}
```

Here is how to use the newly defined function in a spreadsheet

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the workbook
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("B1").putValue(5);
worksheet.getCells().get("C1").putValue(100);
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("C4").putValue(32);
worksheet.getCells().get("C5").putValue(62);

// Adding custom formula to Cell A1
worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

// Calculating Formulas
workbook.calculateFormula(false, new CustomFunction());

// Assign resultant value to Cell A1
worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

// Save the file
workbook.save(path.join(dataDir, "UsingICustomFunction_out.xls"));
```
## **Overview**
The Aspose.Cells APIs just put the ReferredArea object into the "paramsList" when the corresponding parameter is a reference or its calculated result is a reference. If you need the reference itself then you can use the ReferredArea directly. If you need to get the value of a single cell from the reference corresponding to the formula's position, you can use ReferredArea.getValue(rowOffset, colOffset) method. If you need cell values array for the whole area then you can use ReferredArea.getValues method.

As the Aspose.Cells APIs give the ReferredArea in "paramsList", the ReferredAreaCollection in "contextObjects" will not be needed anymore (in old versions it was not able to give one-to-one map to the parameters of the custom function always) therefore it has been removed from the "contextObjects".

{{< highlight javascript >}}
function CalculateCustomFunction(functionName, paramsList, contextObjects) {
    // ...
    let o = paramsList[i];

    if (o instanceof ReferredArea) { // fetch data from reference
        let ra = o;
        if (ra.isArea) {
            o = ra.getValues();
        } else {
            o = ra.getValue(0, 0);
        }
    }

    if (Array.isArray(o)) {
        // ...
    } else if (/* ... */) {
        // ...
    }
}
{{< /highlight >}}
