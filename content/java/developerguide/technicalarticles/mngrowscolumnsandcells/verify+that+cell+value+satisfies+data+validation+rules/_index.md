---
title : "Verify that Cell Value Satisfies Data Validation Rules" 
description : "" 
weight : 16454 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngrowscolumnsandcells/verify+that+cell+value+satisfies+data+validation+rules/
---

# Aspose.Cells for Java : Verify that Cell Value Satisfies Data Validation Rules


Microsoft Excel allows users to add data validation rules to worksheet cells. For instance, a decimal validation can be applied to restrict the numbers between 10 and 20. If any other number out of this specified range is entered, the Microsoft Excel shows an error message and prompts the user to reenter a number from the correct range. If user copy pastes a number, say 3, into the cell, Excel does not run the validation check or show an error message.

Sometimes, it is necessary to dynamically verify if a given value satisfies the data validation rules applied to the cell. For this purpose, the Aspose.Cells APIs provide the [cell.getValidationValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidationValue()) method. If the value in a cell does not satisfy the data validation rule applied to that cell, it returns **False**, else **True**.

The following sample Microsoft Excel file is used with the sample code below to test the [cell.getValidationValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidationValue()) method. As you can see in the snapshot that the cells **C1** has **decimal data validation** applied and will only accept values **between 10 and 20**. Whenever the value of the cell is between 10 and 20, [cell.getValidationValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidationValue()) method will return **True**, otherwise, it will return **False**.

![](https://docs2.aspose.com/cells/java/attachments/5276679/5472906.png)

The following sample code illustrates how the [cell.getValidationValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidationValue()) method works. First, it enters the value 3 into C1. Because this does not satisfy the data validation rule, the [cell.getValidationValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidationValue()) method returns **False**. Then, it enters the value 15 into C1. Because this value satisfies the data validation rule, the [cell.getValidationValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidationValue()) method returns **True**. Similarly, it returns **False** for value 30. Here is the console output generated when the sample code is executed with the sample Excel file shown above.

{{< code lang="cs" >}}
Is 3 a Valid Value for this Cell: False
Is 15 a Valid Value for this Cell: True
Is 30 a Valid Value for this Cell: False
{{< /code >}}


## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Validation-applied-on-cell-C1.PNG](https://docs2.aspose.com/cells/java/attachments/5276679/5472906.png) (image/png)  

