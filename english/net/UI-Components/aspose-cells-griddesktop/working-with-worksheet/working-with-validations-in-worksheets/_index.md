---
title: Working with Validations in Worksheets
type: docs
weight: 70
url: /net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop,validations,validation
description: This article introduces how to work with validation in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop also supports adding validations (or validation rules) to the cells of a worksheet. By applying validation rules to cells, developers can restrict users from entering data into the grid in a specific format. Different modes of validations are supported by Aspose.Cells.GridDesktop. In this topic, we will not only discuss those validation modes but also explain the manipulation of these validations.

{{% /alert %}} 
## **Validation Modes**
There are three validation modes supported by Aspose.Cells.GridDesktop as follows:

- Is Required Validation Mode
- Regular Expressions Validation Mode
- Custom Validation Mode
### **Is Required Validation Mode**
In this validation mode, users are restricted from entering values into specified cells. Once **Is Required Validation** is applied on a worksheet cell, it becomes mandatory for a user to enter a value into that cell.
### **Regular Expressions Validation Mode**
In this mode, restrictions are applied on worksheet cells for users to submit data into cells in a specific format. The pattern of data format is provided in the form of a **Regular Expression**.
### **Custom Validation Mode**
To use **Custom Validation**, it is mandatory for developers to implement the Aspose.Cells.GridDesktop.ICustomValidation interface. The interface provides a **Validate** method. This method returns true if data is valid, otherwise it returns false.
## **Working With Validations in Aspose.Cells.GridDesktop**
### **Adding Validation**
To add any kind of validation to a worksheet cell, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add a desired validation to the **Validations** collection of the **Worksheet** to specify which validation would be applied to which cell.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

In the above figure, we have also mentioned the validation rules in front of cells where these validation rules are applied. If any invalid value (that is not valid according to the validation rule defined for that cell) is entered, a **MessageBox** will appear to notify the user about the invalid entry.

{{% /alert %}} 
### **Implementing ICustomValidation**
In the above code snippet, we have added a custom validation in **A8** cell, but we have not implemented that custom validation yet. As explained at the beginning of this topic, to apply custom validation we must implement the **ICustomValidation** interface. So, let's try creating a class to implement the **ICustomValidation** interface.

In the code snippet given below, we have implemented a custom validation to perform the following checks:

- Check if the cell's address is accurate where the validation is added
- Check if the data type of the cell's value is double
- Check if the value of the cell is greater than 100

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Accessing Validation**
Once a validation is added to a specific worksheet cell, it may be required by developers to access and modify the attributes of a specific validation at run-time. Aspose.Cells.GridDesktop has made it simple for developers to accomplish this task.

To access a specific validation, please follow the steps below:

- Access a desired **Worksheet**
- Access a specific **Validation** in the worksheet by specifying the cell name on which the validation was applied
- Edit **Validation** attributes, if desired

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

The **Validations** collection has two indexers. One indexer (used in the example below) allows access to a **Validation** object by taking a cell name as its index, while the other indexer takes two parameters (row and column numbers) to perform the same task.

{{% /alert %}} 
### **Removing Validation**
To remove a specific validation from the worksheet, please follow the steps below:

- Access a desired **Worksheet**
- Remove a specific **Validation** from the **Worksheet** by specifying the cell name on which the validation was applied

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
