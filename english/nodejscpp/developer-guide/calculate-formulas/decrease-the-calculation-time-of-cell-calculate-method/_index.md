---  
title: Decrease the Calculation Time of Cell.Calculate method with Node.js via C++  
linktitle: Decrease the Calculation Time of Cell.Calculate method  
description: This article introduces how to use the Aspose.Cells library to reduce calculation time for cell calculation methods in Excel using Node.js via C++.  
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time, Node.js via C++  
type: docs  
weight: 100  
url: /nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**

Normally, we recommend that users call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate the entire workbook; they just want to calculate a single cell. Aspose.Cells provides [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--) property, which you can set to **false** to decrease the calculation time of individual cells significantly. When the recursive property is set to **true**, all the dependents of cells are recalculated on each call. However, when the recursive property is **false**, dependent cells are calculated only once and are not recalculated on subsequent calls.

## **Decrease the Calculation Time of Cell.calculate() method**

The following sample code illustrates the usage of [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--) property. Please execute this code with the given [sample Excel file](5113710.xlsx) and check its console output. You will find that setting the recursive property to **false** significantly decreases the calculation time. Please also read the comments for a better understanding of this property.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Test calculation time after setting recursive true
workbook.calculateFormula(); // Call calculateFormula method to initiate calculation

// Test calculation time after setting recursive false
workbook.calculateFormula(false); // Specify ignoreError as false
```  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

function testCalcTimeRecursive(rec) {
    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");
    // Load your sample workbook
    const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

    // Access first worksheet
    const ws = workbook.getWorksheets().get(0);

    // Set the calculation option, set recursive true or false as per parameter
    const opts = new AsposeCells.CalculationOptions();
    opts.setRecursive(rec);

    // Start stop watch
    const start = process.hrtime();

    // Calculate cell A1 one million times
    for (let i = 0; i < 1000000; i++) {
        ws.getCells().get("A1").calculate(opts);
    }

    // Stop the watch
    const end = process.hrtime(start);

    // Calculate elapsed time in seconds
    const estimatedTime = end[0] + end[1] / 1e9;

    // Print the elapsed time in seconds
    console.log(`Recursive ${rec}: ${estimatedTime} seconds`);
}

// Call the function for testing
testCalcTimeRecursive(true);
testCalcTimeRecursive(false);
```

## **Console Output**

This is the console output of the above sample code when executed with the given [sample Excel file](5113710.xlsx) on our machine. Please note that your output may differ, but the elapsed time after setting the recursive property to **false** will always be less than setting it to **true**.

{{< highlight javascript >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
