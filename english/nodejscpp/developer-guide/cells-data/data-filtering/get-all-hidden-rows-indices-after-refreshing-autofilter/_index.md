---  
title: Get All Hidden Rows Indices after Refreshing AutoFilter with Node.js via C++  
type: docs  
weight: 320  
url: /nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for Node.js via C++ API.  
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter Node.js via C++, Obtain All Hidden Rows Indices after Refreshing AutoFilter Node.js via C++, Retrieve All Hidden Rows Indices after Refreshing AutoFilter Node.js via C++  
---  

## **Possible Usage Scenarios**  

When you apply the auto filter on worksheet cells, then some of the rows get hidden automatically. But it might be the case that some of the rows are already hidden manually by Excel end user and they are not hidden by an auto filter. It therefore makes difficult to know which of the rows are hidden by the auto filter and which of them are hidden manually by Excel end user. Aspose.Cells for Node.js via C++ deals with this problem using the `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refreshboolean-). This method returns the row indices of all the rows that are hidden by the auto filter and not manually by the Excel end user.  

## **Get All Hidden Rows Indices after Refreshing AutoFilter**  

Please see the following sample code that loads the [sample Excel file](64716909.xlsx) which contains some of the rows hidden manually by Excel end user. The code applies the auto filter and refreshes it using the `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refreshboolean-) method that returns the row indices of all the hidden rows by the auto filter. It then prints the indices of the hidden rows on the console along with cells names and values.  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply autofilter
worksheet.getAutoFilter().addFilter(0, "Orange");

// True means, it will refresh autofilter and return hidden rows.
// False means, it will not refresh autofilter but return same hidden rows.
const rowIndices = worksheet.getAutoFilter().refresh(true);

console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
console.log("--------------------------");

rowIndices.forEach(r => {
    const cell = worksheet.getCells().get(r, 0);
    console.log(`${r}\t${cell.getName()}\t${cell.getStringValue()}`);
});
```  

## **Console Output**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
