---
title : "Working with Validations in Worksheets" 
description : "" 
weight : 16611 
toc : false
type: docs
url: /net/developerguide/griddesktop/worksheet/working+with+validations+in+worksheets/
---

# Aspose.Cells for .NET : Working with Validations in Worksheets


`Aspose.Cells.GridDesktop` also supports adding validations (or validation rules) to the cells of a worksheet. By applying validation rules to cells, developers can restrict users to enter data into Grid in a specific format. Different modes of validations are supported by `Aspose.Cells.GridDesktop`. In this topic, we will not only discuss about those validation modes but also explain the manipulation of these validations.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Validation Modes](#validation-modes)
    *   1.1 [Is Required Validation Mode](#is-required-validation-mode)
    *   1.2 [Regular Expressions Validation Mode](#regular-expressions-validation-mode)
    *   1.3 [Custom Validation Mode](#custom-validation-mode)
*   2 [Working With Validations in `Aspose.Cells.GridDesktop`](#working-with-validations-in-`aspose.cells.griddesktop`)
    *   2.1 [Adding Validation](#adding-validation)
    *   2.2 [Implementing `ICustomValidation`](#implementing-`icustomvalidation`)
    *   2.3 [Accessing Validation](#accessing-validation)
    *   2.4 [Removing Validation](#removing-validation)
{{< /panel >}}
 

 

## Validation Modes

There are three validation modes supported by `Aspose.Cells.GridDesktop` as follows:

*   Is Required Validation Mode
*   Regular Expressions Validation Mode
*   Custom Validation Mode

### Is Required Validation Mode

In this validation mode, users are restricted to enter values into specified cells. Once **Is Required Validation** is applied on a worksheet cell, it becomes must for a user to enter value into that cell.

### Regular Expressions Validation Mode

In this mode, restrictions are applied on worksheet cells for the users to submit data into cells in a specific format. The pattern of data format is provided in the form of a **Regular Expression**.

### Custom Validation Mode

To use **Custom Validation**, It is must for developers to implement `Aspose.Cells.GridDesktop.ICustomValidation` interface. The interface provides a **Validate** method. This method returns `true` if data is valid otherwise returns `false`.

## Working With Validations in `Aspose.Cells.GridDesktop`

### Adding Validation

To add any kind of validation to a worksheet cell, please follow the steps below:

*   Add `Aspose.Cells.GridDesktop` control to your **Form**
*   Access any desired **Worksheet**
*   Add a desired validation to the **Validations** collection of the **Worksheet** to specify that which validation would be applied on which cell.

In the above figure, we have also mentioned the validation rules in front of cells where these validation rules are applied. If any invalid value (that is not valid according to the validation rule defined for that cell) is entered, a **`MessageBox`** would appear to notify user about the invalid entry.

### Implementing `ICustomValidation`

In the above code snippet, we have added a custom validation in **A8** cell but we have not implemented that custom validation yet. As we have explained in the beginning of this topic that to apply custom validation, we have to implement **ICustomValidation** interface. So, let's try creating a class to implement **ICustomValidation** interface.

In the code snippet given below, we have implemented a custom validation to perform the following checks:

*   Check if the cell's address is accurate in which the validation is added
*   Check if the data type of the cell's value is double
*   Check if the value of the cell is greater than 100

### Accessing Validation

Once a validation is added to a specific worksheet cell, it may be required by developers to access and modify the the attributes of a specific validation at run-time. So, `Aspose.Cells.GridDesktop` has made it simple for developers to accomplish this task.

To access a specific validation, please follow the steps below:

*   Access a desired **Worksheet**
*   Access a specific **Validation** in the worksheet by specifying the cell name on which the validation was applied
*   Edit **Validation** attributes, if desired

**Validations** collection has two indexers. One indexer (that is used in the example below) allows to access a **Validation** object by taking a cell name as its index while the other indexer takes two parameters (that is row and column numbers) to perform the same task.

### Removing Validation

To remove a specific validation from the worksheet, please follow the steps below:

*   Access a desired **Worksheet**
*   Remove a specific **Validation** from the **Worksheet** by specifying the cell name on which the validation was applied

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Validations in Worksheets-001.png](https://docs2.aspose.com/cells/net/attachments/5017771/5113843.png) (image/png)  

