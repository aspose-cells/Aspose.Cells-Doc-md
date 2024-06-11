---
title: 添加单元格验证
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb，GridValidation，列表验证，自定义表达式验证
description: 本文介绍了如何在GridWeb中添加列表验证、下拉列表验证和自定义表达式验证。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb的一个高级功能是为单元格添加输入验证规则。开发人员可以为单元格创建不同类型的验证规则，以控制和验证输入值。本主题讨论了支持的验证类型以及如何创建它们。

{{% /alert %}} 
## **验证类型**
使用Aspose.Cells.GridWeb可以应用三种验证类型：

- 列表验证。
- 下拉列表验证。
- 自定义表达式验证。

下文将对每种验证进行详细讨论。
### **列表验证**
列表验证允许用户通过键入或从菜单中选择数值来提供单元格输入。要为单元格创建列表验证：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单中。
1. 访问工作表。
2. 访问要添加验证的单元格。
3. 为单元格创建验证并将验证类型指定为列表。
4. 为列表验证添加数值。

示例代码为C1添加了列表验证。当用户点击单元格时，将显示一个列表。

**输出：从列表中选择一个值** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **下拉列表验证**
下拉列表验证允许用户通过从预定义列表中选择值来为单元格提供输入。要创建下拉列表验证：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单中。
1. 访问工作表。
1. 访问要创建验证的单元格。
1. 为单元格创建验证，并将类型指定为DropDownList。
1. 为验证添加值。

示例代码向C1添加了下拉列表验证。当用户点击该单元格时，会显示一个下拉列表，用户可以从中选择值。

从下拉列表中选择值 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **自定义表达式验证**
自定义表达式验证允许开发人员编写自己的自定义正则表达式来验证输入值。要创建自定义表达式验证：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单中。
1. 访问工作表。
1. 访问要创建验证的单元格。
1. 为单元格创建验证，并将类型指定为CustomExpression。
1. 设置验证的正则表达式。

示例代码向C1添加了自定义表达式验证。用户只能按照正则表达式指定的格式向单元格添加日期。

根据正则表达式向C1添加日期值 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **强制验证**
使用Aspose.Cells.GridWeb，用户可以将输入数据发送到服务器。即使不同单元格有验证规则，但是如果GridWeb控件的ForceValidation属性未设置为true，则错误的输入数据也会被提交到服务器，并且不会强制进行验证。GridWeb的ForceValidation属性默认总是设置为true。

当ForceValidation属性为true时，控件不会将数据提交到Web服务器，直到所有单元格的输入值都有效。例如，如果有人在单元格中输入了无效的值，或者没有输入值，客户端验证将被激活，用户即使点击“提交”也无法发送数据。

GridWeb突出显示的错误输入值 

![todo:image_alt_text](add-cell-validations_4.png)
