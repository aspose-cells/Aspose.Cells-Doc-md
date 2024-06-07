---
title: 在工作表中处理验证
type: docs
weight: 70
url: /zh/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop,验证,验证
description: 本文介绍如何在GridDesktop中处理验证。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop还支持向工作表的单元格添加验证（或验证规则）。通过将验证规则应用于单元格，开发人员可以限制用户以特定格式输入数据到Grid。Aspose.Cells.GridDesktop支持不同的验证模式。在本主题中，我们将不仅讨论这些验证模式，还将解释这些验证的操作。

{{% /alert %}} 
## **验证模式**
Aspose.Cells.GridDesktop支持三种验证模式，如下所示：

- 必填验证模式
- 正则表达式验证模式
- 自定义验证模式
### **必填验证模式**
在此验证模式下，用户被限制在指定单元格中输入值。一旦在工作表单元格上应用了**必填验证**，用户必须在该单元格中输入值。
### **正则表达式验证模式**
在此模式下，对工作表单元格施加限制，使用户以特定格式提交数据到单元格中。数据格式模式以**正则表达式**的形式提供。
### **自定义验证模式**
要使用**自定义验证**，开发人员必须实现Aspose.Cells.GridDesktop.ICustomValidation接口。该接口提供一个**Validate**方法。此方法如果数据有效则返回true，否则返回false。
## **在Aspose.Cells.GridDesktop中处理验证**
### **添加验证**
要向工作表单元格添加任何类型的验证，请按照以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 将所需的验证添加到**工作表**的**验证**集合中，以指定应将哪种验证应用于哪个单元格。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

在上图中，我们还在应用验证规则的单元格前面提到了验证规则。如果输入了任何无效值（与为该单元格定义的验证规则不符的值），将会弹出一个 **MessageBox** 来通知用户输入了无效值。

{{% /alert %}} 
### **实现 ICustomValidation**
在上述代码片段中，我们在 **A8** 单元格中添加了自定义验证，但是我们还没有实现该自定义验证。正如我们在本主题开始时所解释的那样，要应用自定义验证，我们必须实现 **ICustomValidation** 接口。所以，让我们尝试创建一个类来实现 **ICustomValidation** 接口。

在下面的代码片段中，我们实现了一个自定义验证来执行以下检查：

- 检查添加了验证的单元格地址是否准确
- 检查单元格值的数据类型是否为双精度
- 检查单元格的值是否大于100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **访问验证**
一旦将验证添加到特定的工作表单元格中，开发人员可能需要在运行时访问和修改特定验证的属性。因此，Aspose.Cells.GridDesktop 已经让开发人员简化了这项任务。

要访问特定的验证，请按照以下步骤执行：

- 访问所需的 **Worksheet**
- 通过指定应用验证的单元格名称来访问工作表中的特定 **Validation**
- 如果需要，编辑 **Validation** 属性



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Validations** 集合具有两个索引器。在下面的示例中使用的一个索引器允许通过将单元格名称作为其索引来访问 **Validation** 对象，而另一个索引器则使用两个参数（行和列号）来执行相同的任务。

{{% /alert %}} 
### **删除验证**
要从工作表中删除特定的验证，请按照以下步骤执行：

- 访问所需的 **Worksheet**
- 通过指定应用验证的单元格名称从 **Worksheet** 中移除特定的 **Validation**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
