---
title: 编写 GridWeb 客户端脚本
type: docs
weight: 10
url: /zh/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

开发人员可以为 Aspose.Cells.GridWeb 控件编写客户端脚本。这意味着可以在客户端调用 JavaScript 函数来执行与 GridWeb 控件相关的特定任务。例如，开发人员可以编写 JavaScript 函数将 GridWeb 数据提交到服务器或在发生验证错误时显示警告消息等。

本主题借助示例解释此功能。

{{% /alert %}} 
## **为 Aspose.Cells.GridWeb 编写客户端脚本**
### **基本信息**
Aspose.Cells.GridWeb 提供了两个专门为支持客户端脚本而创建的属性：

- OnSubmitClient函数
- OnValidationErrorClientFunction

在 ASPX 页面中创建 JavaScript 函数并将这些函数的名称分配给 OnSubmitClientFunction 和 OnValidationErrorClientFunction 属性。

{{% alert color="primary" %}} 

将分配给 OnSubmitClientFunction 属性的 JavaScript 函数必须正确定义，如下所示：

**JavaScript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

其中 [arg] 参数表示控件生成的命令。该命令可以是“保存”、“提交”、“撤消”等，[cancelEdit]参数为布尔值，表示是否取消用户输入。

在将 GridWeb 数据提交到服务器之前，GridWeb 控件每次都会调用分配给 OnSubmitClientFunction 属性的任何 JavaScript 函数。同样，如果将函数分配给 OnValidationErrorClientFunction 属性，则每次发生验证错误时都会调用该函数。

{{% /alert %}} 
### **客户端脚本函数**
Aspose.Cells.GridWeb 还公开了专门用于客户端脚本的功能。这些函数可以在 JavaScript 函数中使用，以获得对 Aspose.Cells.GridWeb 的更多控制。这些客户端功能包括以下内容：

|**功能**|**描述**|
|:- |:- |
|更新数据（布尔取消编辑）|在将其发布到服务器之前更新 Aspose.Cells.GridWeb 的所有客户端数据。如果 cancelEdit 参数为真，那么 GridWeb 将丢弃所有用户输入。|
|验证所有（）|用于检查用户输入中是否存在任何验证错误。如果有错误，函数返回 false，否则返回 true。|
|提交（字符串参数，布尔取消编辑）|调用此函数向服务器回发或提交数据。此函数执行更新数据和验证用户输入这两项任务。此函数还可以在服务器端触发命令事件。使用 arg 参数传递您的命令。例如：SAVE 命令用于单击**节省**GridWeb 控件命令栏上的按钮和 CCMD:MYCOMMAND 命令触发 CustomCommand 事件。|
|setActiveCell（整数行，整数列）|用于激活特定的单元格。|
|setCellValue（整数行，整数列，字符串值）|用于将值放入使用其行号和列号指定的任何单元格。|
|getCellValue（整数行，整数列）|返回任何指定单元格的值。|
|getActiveRow()|与 getActiveColumn() 函数结合使用以确定活动单元格的位置。|
|getActiveColumn()|与 getActiveRow() 函数结合使用以确定活动单元格的位置。|
|获取选择范围()|返回最后选择的范围。|
|设置选择范围()|选择给定范围。|
|清除选择()|清除除当前活动单元格之外的所有选择。|
|getCellsArray()|它与其他相关函数一起使用，如 getCellName()、getCellValueByCell()、getCellRow() 和 getCellColumn()。请阅读本文以获取有关此功能用法的更多信息：[在客户端读取 GridWeb 单元格的值](/cells/zh/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
要创建包含与 Aspose.Cells.GridWeb 一起使用的客户端脚本的测试应用程序，请按照以下步骤操作：

1. 创建由 GridWeb 调用的 JavaScript 函数。
这些功能将添加到 ASP.NET 页面的<script></script>标签。
1. 将函数的名称分配给 OnSubmitClientFunction 和 OnValidationErrorClientFunction 属性。

代码示例的输出如下所示：

**添加到 C1 单元格的验证** 

![待办事项：图片_替代_文本](write-gridweb-client-side-script_1.png)

添加无效值并单击**节省**.发生验证错误并执行 ValidationErrorFunction。

**验证错误时调用的 ValidationErrorFunction** 

![待办事项：图片_替代_文本](write-gridweb-client-side-script_2.png)

在您输入有效值之前，不会向服务器提交任何数据。输入有效值并单击**节省**ConfirmFunction 被执行。

**在将 GridWeb 数据提交到服务器之前调用 ConfirmFunction** 

![待办事项：图片_替代_文本](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
