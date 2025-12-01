---
title: Verify that Cell Value Satisfies Data Validation Rules
type: docs
weight: 210
url: /net/verify-that-cell-value-satisfies-data-validation-rules/
description: Learn how to Verify Cell Value Satisfies Data Validation Rules through the Aspose.Cells for .NET API..
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to add data validation rules to cells. For example, a decimal validation specifies that only numbers between 10 and 20 can be entered. If a user enters a different number. Microsoft Excel shows an error message and prompts them to enter a number in the correct range. If you copy and paste a number, say 3, into the cell, Excel does not run a validation check or show an error message.

Sometimes, it is necessary to verify whether a value satisfies the data validation rules applied to the cell programmatically. In the case above, for example, the entry should fail.

{{% /alert %}} 
## **Introduction**
Aspose.Cells provides the [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) method to validate cell values programmatically. If the value in a cell does not satisfy the data validation rule applied to that cell, it returns **False**, else **True**.

The following sample code illustrates how the [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) method works. First, it enters the value 3 into C1. Because this does not satisfy the data validation rule, the [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) method returns **False**. Then, it enters the value 15 into C1. Because this value satisfies the data validation rule, the [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) method returns **True**. Similarly, it returns **False** for value 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Output**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
