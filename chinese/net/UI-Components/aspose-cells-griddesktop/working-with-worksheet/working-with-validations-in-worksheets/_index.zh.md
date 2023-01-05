---
title: 在工作表中使用验证
type: docs
weight: 70
url: /zh/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop 还支持向工作表的单元格添加验证（或验证规则）。通过对单元格应用验证规则，开发人员可以限制用户以特定格式向 Grid 中输入数据。 Aspose.Cells.GridDesktop 支持不同的验证模式。在本主题中，我们不仅会讨论这些验证模式，还会解释这些验证的操作。

{{% /alert %}} 
## **验证模式**
Aspose.Cells.GridDesktop支持三种验证模式如下：

- 是否需要验证模式
- 正则表达式验证模式
- 自定义验证模式
### **是否需要验证模式**
在此验证模式下，用户只能在指定的单元格中输入值。一次**是否需要验证**应用于工作表单元格时，用户必须在该单元格中输入值。
### **正则表达式验证模式**
在这种模式下，对工作表单元格施加限制，以便用户以特定格式将数据提交到单元格中。数据格式的模式以一种形式提供**正则表达式**.
### **自定义验证模式**
使用**自定义验证** 开发者必须实现Aspose.Cells.GridDesktop.ICustomValidation接口。该接口提供了一个**证实**方法。如果数据有效，则此方法返回 true，否则返回 false。
## **在 Aspose.Cells.GridDesktop 中使用验证**
### **添加验证**
要向工作表单元格添加任何类型的验证，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 将所需的验证添加到**验证**的集合**工作表**指定哪个验证将应用于哪个单元格。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

在上图中，我们还在应用这些验证规则的单元格前面提到了验证规则。如果输入任何无效值（根据为该单元格定义的验证规则无效），一个**消息框**似乎会通知用户有关无效条目的信息。

{{% /alert %}} 
### **实施 ICustomValidation**
在上面的代码片段中，我们添加了一个自定义验证**A8**单元格，但我们还没有实现自定义验证。正如我们在本主题开头所解释的那样，要应用自定义验证，我们必须实现**自定义验证**界面。那么，让我们尝试创建一个类来实现**自定义验证**界面。

在下面给出的代码片段中，我们实现了自定义验证来执行以下检查：

- 检查添加验证的单元格地址是否准确
- 检查单元格值的数据类型是否为双精度
- 检查单元格的值是否大于100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **访问验证**
将验证添加到特定工作表单元格后，开发人员可能需要在运行时访问和修改特定验证的属性。因此，Aspose.Cells.GridDesktop 使开发人员可以轻松完成此任务。

要访问特定验证，请按照以下步骤操作：

- 访问一个想要的**工作表**
- 访问特定的**验证**在工作表中指定应用验证的单元格名称
- 编辑**验证**属性，如果需要



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**验证**集合有两个索引器。一个索引器（在下面的示例中使用）允许访问一个**验证**对象通过将单元格名称作为其索引，而另一个索引器使用两个参数（即行号和列号）来执行相同的任务。

{{% /alert %}} 
### **删除验证**
要从工作表中删除特定验证，请按照以下步骤操作：

- 访问一个想要的**工作表**
- 删除特定的**验证**来自**工作表**通过指定应用验证的单元格名称



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
