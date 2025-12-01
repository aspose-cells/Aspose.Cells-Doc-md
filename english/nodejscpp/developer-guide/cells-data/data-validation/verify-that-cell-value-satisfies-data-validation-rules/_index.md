---
title: Verify that Cell Value Satisfies Data Validation Rules
type: docs
weight: 210
url: /nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Learn how to Verify Cell Value Satisfies Data Validation Rules through the Aspose.Cells for Node.js via C++ API.
keywords: Get Cell Validation Value Node.js via C++, Obtain Cell Validation Value Node.js via C++, Verify whether a value satisfies the data validation rules applied to the cell Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to add data validation rules to cells. For example, a decimal validation specifies that only numbers between 10 and 20 can be entered. If a user enters a different number, Microsoft Excel shows an error message and prompts them to enter a number in the correct range. If you copy and paste a number, say 3, into the cell, Excel does not run a validation check or show an error message.

Sometimes, it is necessary to verify whether a value satisfies the data validation rules applied to the cell programmatically. In the case above, for example, the entry should fail.

{{% /alert %}} 
## **Introduction**
Aspose.Cells for Node.js via C++ provides the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) method to validate cell values programmatically. If the value in a cell does not satisfy the data validation rule applied to that cell, it returns **false**, else **true**.

The following sample code illustrates how the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) method works. First, it enters the value 3 into C1. Because this does not satisfy the data validation rule, the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) method returns **false**. Then, it enters the value 15 into C1. Because this value satisfies the data validation rule, the [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) method returns **true**. Similarly, it returns **false** for value 30.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **Output**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
