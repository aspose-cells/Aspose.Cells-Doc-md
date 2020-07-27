+++
title = "Verify that Cell Value Satisfies Data Validation Rules" 
description = "" 
weight = 20488 
+++

Aspose.Cells for .NET : Verify that Cell Value Satisfies Data Validation Rules  

# Aspose.Cells for .NET : Verify that Cell Value Satisfies Data Validation Rules


Microsoft Excel allows users to add data validation rules to cells. For example, a decimal validation specifies that only numbers between 10 and 20 can be entered. If a user enters a different number. Microsoft Excel shows an error message and prompts them to enter a number in the correct range. If you copy and paste a number, say 3, into the cell, Excel does not run a validation check or show an error message.

Sometimes, it is necessary to verify whether a value satisfies the data validation rules applied to the cell programmatically. In the case above, for example, the entry should fail.

## Introduction

Aspose.Cells provides the [Cell.GetValidationValue()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getvalidationvalue) method to validate cell values programmatically. If the value in a cell does not satisfy the data validation rule applied to that cell, it returns **False**, else **True**.

The following sample code illustrates how the [Cell.GetValidationValue()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getvalidationvalue) method works. First, it enters the value 3 into C1. Because this does not satisfy the data validation rule, the [Cell.GetValidationValue()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getvalidationvalue) method returns **False**. Then, it enters the value 15 into C1. Because this value satisfies the data validation rule, the [Cell.GetValidationValue()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getvalidationvalue) method returns **True**. Similarly, it returns **False** for value 30.

### Output

{{< code lang="cs" >}}
Is 3 a Valid Value for this Cell: False
Is 15 a Valid Value for this Cell: True
Is 30 a Valid Value for this Cell: False
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Validation-applied-on-cell-C1.PNG](https://docs2.aspose.com/cells/net/attachments/5017638/5112267.png) (image/png)  

