---
title: 编写GridWeb客户端脚本
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb，client，js，javascript
description: 本文介绍了如何在GridWeb中使用客户端js API。
---

{{% alert color="primary" %}} 

开发人员可以为Aspose.Cells.GridWeb控件编写客户端脚本。这意味着可以在客户端调用JavaScript函数来执行与GridWeb控件相关的特定任务。例如，开发人员可以编写JavaScript函数将GridWeb数据提交到服务器，或在验证错误发生时显示警报消息等。

本主题通过示例解释了此功能。

{{% /alert %}} 
## **为Aspose.Cells.GridWeb编写客户端脚本**
### **基本信息**
Aspose.Cells.GridWeb提供了专门用于支持客户端脚本的两个属性:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

在ASPX页面中创建JavaScript函数，并将这些函数的名称分配给OnSubmitClientFunction和OnValidationErrorClientFunction属性。

{{% alert color="primary" %}} 

将分配给OnSubmitClientFunction属性的JavaScript函数必须像下面所示定义:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

其中[arg]参数表示控件生成的命令。命令可以是"Save"、"Submit"、"Undo"等，[cancelEdit]参数是一个布尔值，指示用户输入是否被取消。

将分配给OnSubmitClientFunction属性的任何JavaScript函数在将GridWeb数据提交到服务器之前，每次都会被GridWeb控件调用。同样，如果将函数分配给OnValidationErrorClientFunction属性，那么每次发生验证错误时都会调用该函数。

{{% /alert %}} 
### **客户端脚本的功能**
Aspose.Cells.GridWeb还公开了专门用于客户端脚本的函数。这些函数可以在JavaScript函数中使用，以更好地控制Aspose.Cells.GridWeb。这些客户端函数包括以下内容:

|**函数**|**描述**|
| :- | :- |
|updateData(bool cancelEdit)|在将数据发布到服务器之前更新Aspose.Cells.GridWeb的所有客户端数据。如果cancelEdit参数为true，则GridWeb会放弃所有用户输入。
|validateAll()|用于检查用户输入中是否存在任何验证错误。如果存在错误，该函数返回false，否则返回true。
|submit(string arg, bool cancelEdit)|调用此函数以将数据提交或发布到服务器。此函数执行更新数据和验证用户输入的两项任务。此函数还可以在服务器端触发命令事件。使用arg参数传递您的命令。例如:将SAVE命令用于单击GridWeb控件的命令栏上的**保存**按钮，CCMD:MYCOMMAND命令触发自定义命令事件。
|setActiveCell(int row, int column)|用于激活特定单元格。
|setCellValue(int row, int column, string value)|用于将值放入使用其行和列号指定的任何单元格。
|getCellValue(int row, int column)|返回任何指定单元格的值。
|getActiveRow()|与getActiveColumn()函数结合使用，以确定活动单元格的位置。
|getActiveColumn()|与getActiveRow()函数结合使用，以确定活动单元格的位置。
|getSelectRange()|返回最后选择的范围。
|setSelectRange()|选择指定的范围。
|clearSelections()|清除除当前活动单元格以外的所有选择。
|getCellsArray()|它与其他相关函数一起使用，如getCellName()、getCellByValueByCell()、getCellRow()和getCellColumn()。请阅读此文章以获取关于此函数的更多信息：[在客户端读取GridWeb单元格的值](/cells/zh/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)
创建包含与Aspose.Cells.GridWeb一起工作的客户端脚本的测试应用程序，请按照以下步骤进行：

1. 创建要由GridWeb调用的JavaScript函数。
   These functions will be added to the ASP.NET page's <script></script> tag.
1. 将函数名称分配给OnSubmitClientFunction和OnValidationErrorClientFunction属性。

下面显示了代码示例的输出：

**向C1单元格添加验证** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

添加一个无效值，然后单击**保存**。将发生验证错误，并执行ValidationErrorFunction。

**在验证错误时调用ValidationErrorFunction** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

在输入有效值之前，不会向服务器提交任何数据。输入有效值，然后单击**保存**。将执行ConfirmFunction。

**在将GridWeb数据提交到服务器之前调用ConfirmFunction** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
