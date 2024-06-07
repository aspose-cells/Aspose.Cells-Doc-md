---
title: 在列中使用验证
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop, validation, validations
description: 本文介绍如何在GridDesktop的列中使用验证。
---

{{% alert color="primary" %}} 

在我们之前的话题中，我们已经讨论了验证，但那是在[工作表中的验证](/cells/zh/net/working-with-validations-in-worksheets/)的背景下（开发人员可以参考这个话题获得有关验证和验证模式的一般信息）。在本话题中，我们将详细解释与列相关的验证。使用此功能，开发人员可以在工作表的任何列上应用验证规则。让我们详细讨论一下。

{{% /alert %}} 
## **添加列验证**
要向列添加任何类型的验证，请按照以下步骤进行：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- **添加**所需的**验证**到任何列

**重要：**有关验证类型（或验证模式，如**必需验证**、**正则表达式验证**和**自定义验证**）和实现**自定义验证**的更多信息，请参阅[在工作表中使用验证。](/cells/zh/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **访问列验证**
要访问特定的列验证，请按照以下步骤进行：

- 访问所需的 **Worksheet**
- 在**工作表**中访问特定列的**验证**
- 如果需要，编辑 **Validation** 属性



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **移除列验证**
要从工作表中移除特定的列验证，请按照以下步骤进行：

- 访问所需的 **Worksheet**
- 从**工作表**中移除特定的列**验证**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
