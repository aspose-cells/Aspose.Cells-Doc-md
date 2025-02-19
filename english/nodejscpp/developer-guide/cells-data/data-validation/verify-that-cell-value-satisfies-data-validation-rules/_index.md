---
title: Verify that Cell Value Satisfies Data Validation Rules with Node.js via C++
type: docs
weight: 210
url: /nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Learn how to Verify Cell Value Satisfies Data Validation Rules through the Aspose.Cells for Node.js via C++ API.
keywords: Get Cell Validation Value Node.js via C++, Obtain Cell Validation Value Node.js via C++, Verify whether a value satisfies the data validation rules applied to the cell Node.js via C++
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to add data validation rules to cells. For example, a decimal validation specifies that only numbers between 10 and 20 can be entered. If a user enters a different number, Microsoft Excel shows an error message and prompts them to enter a number in the correct range. If you copy and paste a number, say 3, into the cell, Excel does not run a validation check or show an error message.

Sometimes, it is necessary to verify whether a value satisfies the data validation rules applied to the cell programmatically. In the case above, for example, the entry should fail.

{{% /alert %}} 
## **Introduction**
Aspose.Cells for Node.js via C++ provides the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue) method to validate cell values programmatically. If the value in a cell does not satisfy the data validation rule applied to that cell, it returns **false**, else **true**.

The following sample code illustrates how the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue) method works. First, it enters the value 3 into C1. Because this does not satisfy the data validation rule, the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue) method returns **false**. Then, it enters the value 15 into C1. Because this value satisfies the data validation rule, the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue) method returns **true**. Similarly, it returns **false** for value 30.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the workbook from sample Excel file
const workbook = new AsposeCells.Workbook(dataDir + "sample.xlsx");

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access Cell C1
// Cell C1 has the Decimal Validation applied on it.
// It can take only the values Between 10 and 20
const cell = worksheet.getCells().get("C1");

// Enter 3 inside this cell
// Since it is not between 10 and 20, it should fail the validation
cell.putValue(3);

// Check if number 3 satisfies the Data Validation rule applied on this cell
console.log("Is 3 a Valid Value for this Cell: " + cell.getValidationValue());

// Enter 15 inside this cell
// Since it is between 10 and 20, it should succeed the validation
cell.putValue(15);

// Check if number 15 satisfies the Data Validation rule applied on this cell
console.log("Is 15 a Valid Value for this Cell: " + cell.getValidationValue());

// Enter 30 inside this cell
// Since it is not between 10 and 20, it should fail the validation again
cell.putValue(30);

// Check if number 30 satisfies the Data Validation rule applied on this cell
console.log("Is 30 a Valid Value for this Cell: " + cell.getValidationValue());
```
### **Output**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
