---
title: Working with Validations in Columns
type: docs
weight: 80
url: /net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop,validation,validations
description: This article introduces how to use validations in columns in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

In one of our previous topics, we discussed validations but that was in the context of [Validations in Worksheets](/cells/net/working-with-validations-in-worksheets/) (for general information about validation and validation modes, developers can refer to this topic). In this topic, we will explain validations with respect to columns. Using this feature, it is possible for developers to apply a validation rule on any column of the worksheet. Let's discuss it in detail.

{{% /alert %}} 
## **Adding Column Validation**
To add any kind of validation to a column, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- **Add** a desired **Validation** to any column

**IMPORTANT:** For more information about the types of validation (or validation modes like **Is Required Validation**, **Regular Expression Validation** and **Custom Validation**) and implementing **Custom Validation**, please refer to [Working with Validations in Worksheets.](/cells/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Accessing Column Validation**
To access a specific column validation, please follow the steps below:

- Access a desired **Worksheet**
- Access a specific column **validation** in the **Worksheet**
- Edit **validation** attributes, if desired



{{< highlight csharp >}}

 // Accessing first worksheet of the Grid
Worksheet sheet = gridDesktop1.Worksheets[0];

// Accessing the Validation object applied on a specific column
Validation validation = sheet.Columns[2].Validation;

// Editing the attributes of Validation
validation.IsRequired = true;
validation.RegEx = "";
validation.CustomValidation = null;

{{< /highlight >}}
## **Removing Column Validation**
To remove a specific column validation from the worksheet, please follow the steps below:

- Access a desired **Worksheet**
- Remove a specific column **validation** from the **Worksheet**



{{< highlight csharp >}}

 // Accessing first worksheet of the Grid
Worksheet sheet = gridDesktop1.Worksheets[0];

// Removing the Validation applied on a specific column
sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
