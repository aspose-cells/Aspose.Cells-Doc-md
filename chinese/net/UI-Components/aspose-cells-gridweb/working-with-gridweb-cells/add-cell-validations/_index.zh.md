---
title: 添加 Cell 验证
type: docs
weight: 70
url: /zh/net/add-cell-validations/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 的高级功能之一是为单元格添加输入验证规则。开发人员可以为单元格创建不同类型的验证规则来控制和验证输入值。本主题讨论支持的验证类型以及如何创建它们。

{{% /alert %}} 
## **验证类型**
使用 Aspose.Cells.GridWeb 可以应用三种类型的验证：

- 列表验证。
- 下拉列表验证。
- 自定义表达式验证。

下面详细讨论每一个。
### **列表验证**
列表验证允许用户通过键入或从菜单中选择值来提供单元格输入。要为单元格创建列表验证：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 访问要向其添加验证的单元格。
1. 为单元格创建验证并将验证类型指定为列表。
1. 为列表验证添加值。

示例代码将列表验证添加到 C1。当用户单击该单元格时，将出现一个列表。

**输出：从列表中选择一个值** 

![待办事项：图片_替代_文本](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **下拉列表验证**
下拉列表验证允许用户通过从预定义列表中选择一个值来为单元格提供输入。要创建下拉列表验证：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 访问要为其创建验证的单元格。
1. 为单元格创建验证并将类型指定为 DropDownList。
1. 添加验证值。

示例代码向 C1 添加了一个下拉列表验证。当用户单击单元格时，会出现一个下拉列表，用户可以从中选择一个值。

**从下拉列表中选择一个值** 

![待办事项：图片_替代_文本](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **自定义表达式验证**
自定义表达式验证允许开发人员编写自己的自定义正则表达式来验证输入值。要创建自定义表达式验证：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 访问要为其创建验证的单元格。
1. 为单元格创建验证并将类型指定为 CustomExpression。
1. 设置验证的正则表达式。

示例代码向 C1 添加自定义表达式验证。用户只能按照正则表达式指定的格式将日期添加到单元格中。

**根据正则表达式向 C1 添加日期值** 

![待办事项：图片_替代_文本](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **强制验证**
使用 Aspose.Cells.GridWeb，用户可以将输入数据发布到服务器。即使不同单元格有校验规则，但GridWeb控件的ForceValidation属性没有设置为true，输入的数据错误也会提交给服务器，不强制校验。默认情况下，GridWeb 的 ForceValidation 属性始终设置为 true。

当 ForceValidation 属性为真时，控件不会将数据发布到 Web 服务器，直到所有单元格的输入值都有效。例如，如果有人在单元格中输入了无效的输入值，或者没有输入值，则会激活客户端验证，用户即使点击也无法发布数据**提交**.

**GridWeb 突出显示的错误输入值** 

![待办事项：图片_替代_文本](add-cell-validations_4.png)
