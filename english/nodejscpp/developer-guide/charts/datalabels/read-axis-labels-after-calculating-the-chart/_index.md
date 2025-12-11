---  
title: Read Axis Labels after Calculating the Chart with Node.js via C++  
linktitle: Read Axis Labels after Calculating the Chart  
description: Learn how to read axis labels in Aspose.Cells for Node.js via C++ after calculating the chart. Our guide will show you how to access and retrieve axis labels, including their formatting and positioning.  
keywords: Aspose.Cells for Node.js, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning, Node.js via C++  
type: docs  
weight: 90  
url: /nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Possible Usage Scenarios**

You can read axis labels of your chart after calculating its values using the [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--) method. Please use the [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) method for this purpose, which will return the list of axis labels.

## **Read Axis Labels after Calculating the Chart**

Please see the following sample code that loads the [sample Excel file](ReadAxisLabels.xlsx) and reads the category‑axis labels of the chart in the first worksheet. It then prints the values of the axis labels on the console. Refer to the console output of the sample code given below.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing the chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of the category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on the console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
    console.log(lstLabels[i]);
}
```

## **Console Output**

```javascript
Category Axis Labels: 
---------------------
Iran
China
USA
Brazil
England
```

{{< app/cells/assistant language="nodejs-cpp" >}}
