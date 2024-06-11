---
title: 在工作表中处理验证
type: docs
weight: 70
url: /zh/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop，验证，验证
description: 本文介绍了如何在GridDesktop中处理验证。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop 还支持向工作表单元格添加验证（或验证规则）。通过将验证规则应用于单元格，开发人员可以限制用户以特定格式输入 Grid 中的数据。Aspose.Cells.GridDesktop 支持不同模式的验证。在本主题中，我们不仅将讨论这些验证模式，还将解释如何操作这些验证。

{{% /alert %}} 
## **验证模式**
Aspose.Cells.GridDesktop 支持三种验证模式，如下：

- 必填验证模式
- 正则表达式验证模式
- 自定义验证模式
### **必填验证模式**
在此验证模式下，用户受到限制，无法向指定单元格输入值。一旦在工作表单元格上应用了**必填验证**，用户就必须向该单元格输入值。
### **正则表达式验证模式**
在此模式下，对工作表单元格施加了限制，要求用户以特定格式向单元格提交数据。数据格式的模式以**正则表达式**提供。
### **自定义验证模式**
要使用**自定义验证**，开发人员必须实现 Aspose.Cells.GridDesktop.ICustomValidation 接口。该接口提供一个**验证**方法。此方法在数据有效时返回true，否则返回false。
## **在 Aspose.Cells.GridDesktop 中处理验证**
### **添加验证**
要向工作表单元格添加任何类型的验证，请按照下面的步骤操作：

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 向**工作表**的**验证**集合中添加所需的验证，以指定要在哪个单元格上应用哪个验证



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

在上图中，我们还在应用验证规则的单元格前面提到了验证规则。如果输入了任何无效值（即不符合该单元格定义的验证规则的有效值），将会出现一个**消息框**，通知用户有无效输入。

{{% /alert %}} 
### **实现ICustomValidation**
在上面的代码片段中，我们已经在**A8**单元格中添加了自定义验证，但我们尚未实现该自定义验证。正如我们在本主题开始时所解释的，要应用自定义验证，我们必须实现**ICustomValidation**接口。那么，让我们尝试创建一个类来实现**ICustomValidation**接口。

在下面给出的代码片段中，我们实现了自定义验证以执行以下检查：

- 检查添加验证的单元格地址是否准确
- 检查单元格值的数据类型是否为双精度
- 检查单元格的值是否大于100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **访问验证**
一旦将验证添加到特定工作表单元格，开发人员可能需要在运行时访问和修改特定验证的属性。因此，Aspose.Cells.GridDesktop已经简化了开发人员完成此任务的流程。

要访问特定的验证，请按照以下步骤操作：

- 访问所需的**工作表**
- 通过指定应用了验证的单元格名称在工作表中访问特定的**验证**
- 编辑**验证**属性（如果需要）



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**验证**集合有两个索引器。一个索引器（在下面的示例中使用）允许通过取单元格名称作为其索引来访问**验证**对象，而另一个索引器采用两个参数（即行号和列号）来执行相同的任务。

{{% /alert %}} 
### **移除验证**
要从工作表中移除特定的验证，请按照以下步骤操作：

- 访问所需的**工作表**
- 通过指定应用验证的单元格名称，从工作表中删除特定的**验证**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
