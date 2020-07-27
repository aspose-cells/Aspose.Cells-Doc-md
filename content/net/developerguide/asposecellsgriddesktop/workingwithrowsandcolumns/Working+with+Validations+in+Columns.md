+++
title = "Working with Validations in Columns" 
description = "" 
weight = 16631 
+++

Aspose.Cells for .NET : Working with Validations in Columns  

# Aspose.Cells for .NET : Working with Validations in Columns


In one of our previous topics, we have discussed about validations but that was in the context of [Validations in Worksheets](https://docs2.aspose.com/cells/net/developerguide/asposecellsgriddesktop/workingwithworksheet/working+with+validations+in+worksheets) (for having general information about validation and validation modes, developers can refer to this topic). In this topic, we will explain validations with respect to columns. Using this feature, it is possible for developers to apply a validation rule on any column of the worksheet. Let's discuss it in detail.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Column Validation](#WorkingwithValidationsinColumns-AddingColumnValidation)
*   2 [Accessing Column Validation](#WorkingwithValidationsinColumns-AccessingColumnValidation)
*   3 [Removing Column Validation](#WorkingwithValidationsinColumns-RemovingColumnValidation)
{{< /panel >}}
 

 

## Adding Column Validation

To add any kind of validation to a column, please follow the steps below:

*   Add Aspose.Cells.GridDesktop control to your **Form**
*   Access any desired **Worksheet**
*   **Add** a desired **Validation** to any column

**IMPORTANT:** For more information about the types of validation (or validation modes like **Is Required Validation**, **Regular Expressions Validation** and **Custom Validation**) and implementing **Custom Validation**, please refer to [Working with Validations in Worksheets.](https://docs2.aspose.com/cells/net/developerguide/asposecellsgriddesktop/workingwithworksheet/working+with+validations+in+worksheets)

## Accessing Column Validation

To access a specific column validation, please follow the steps below:

*   Access a desired **Worksheet**
*   Access a specific column **Validation** in the **Worksheet**
*   Edit **Validation** attributes, if desired

{{< code lang="cs" >}}
//Accessing first worksheet of the Grid
Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column
Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation
validation.IsRequired = true;
validation.RegEx = "";
validation.CustomValidation = null;
{{< /code >}}

## Removing Column Validation

To remove a specific column validation from the worksheet, please follow the steps below:

*   Access a desired **Worksheet**
*   Remove a specific column **Validation** from the **Worksheet**

{{< code lang="cs" >}}
//Accessing first worksheet of the Grid
Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column
sheet.Columns[2].RemoveValidation();
{{< /code >}}

