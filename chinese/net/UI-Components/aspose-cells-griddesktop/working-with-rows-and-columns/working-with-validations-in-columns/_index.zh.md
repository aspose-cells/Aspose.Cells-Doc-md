---
title: 在列中使用验证
type: docs
weight: 80
url: /zh/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

在我们之前的一个主题中，我们讨论了验证，但那是在[工作表中的验证](/cells/zh/net/working-with-validations-in-worksheets/)（有关验证和验证模式的一般信息，开发人员可以参考此主题）。在本主题中，我们将解释关于列的验证。使用此功能，开发人员可以在工作表的任何列上应用验证规则。让我们详细讨论一下。

{{% /alert %}} 
## **添加列验证**
要向列添加任何类型的验证，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- **添加**想要的**验证**到任何列

**重要的：**有关验证类型（或验证模式，如**是否需要验证**, **正则表达式验证**和**自定义验证** 和实施**自定义验证**， 请参阅[在工作表中使用验证。](/cells/zh/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **访问列验证**
要访问特定的列验证，请按照以下步骤操作：

- 访问一个想要的**工作表**
- 访问特定列**验证**在里面**工作表**
- 编辑**验证**属性，如果需要



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **删除列验证**
要从工作表中删除特定列验证，请按照以下步骤操作：

- 访问一个想要的**工作表**
- 删除特定列**验证**来自**工作表**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
