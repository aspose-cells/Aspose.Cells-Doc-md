---
title: 编写GridWeb客户端脚本
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,客户端,js,javascript
description: 本文介绍了如何在GridWeb中使用客户端js api。
---

{{% alert color="primary" %}} 

开发人员可以为Aspose.Cells.GridWeb控件编写客户端脚本。这意味着可以在客户端调用JavaScript函数来执行与GridWeb控件相关的特定任务。例如，开发人员可以编写JavaScript函数将GridWeb数据提交到服务器，或在验证错误发生时显示警报消息等。

本主题通过示例解释了这一功能。

{{% /alert %}} 
## **为Aspose.Cells.GridWeb编写客户端脚本**
### **基本信息**
Aspose.Cells.GridWeb提供了专门用于支持客户端脚本的两个属性:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

在ASPX页面中创建JavaScript函数，并将这些函数的名称分配给OnSubmitClientFunction和OnValidationErrorClientFunction属性。

{{% alert color="primary" %}} 

将分配给OnSubmitClientFunction属性的JavaScript函数必须按如下所示进行定义:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

其中[arg]参数表示控制生成的命令。命令可以是"保存"、"提交"、"撤销"等，[cancelEdit]参数是一个布尔值，表示用户输入是否被取消。

任何分配给OnSubmitClientFunction属性的JavaScript函数都会在将GridWeb数据提交到服务器之前每次被GridWeb控件调用。类似地，如果将函数分配给OnValidationErrorClientFunction属性，那么每当验证错误发生时都会调用该函数。

{{% /alert %}} 
### **客户端脚本函数**
Aspose.Cells.GridWeb还特别为客户端脚本公开了一些函数。这些函数可以在JavaScript函数中使用，以更好地控制Aspose.Cells.GridWeb。这些客户端函数包括:

|**函数**|**描述**|
| :- | :- |
|updateData(bool cancelEdit)|在提交到服务器之前更新 Aspose.Cells.GridWeb 的所有客户端数据。如果 cancelEdit 参数为 true，则 GridWeb 将放弃所有用户输入。|
|validateAll()|用于检查用户输入中是否存在任何验证错误。如果存在错误，则该函数返回 false，否则为 true。|
|submit(string arg, bool cancelEdit)|调用此函数向服务器提交数据。此函数执行更新数据和验证用户输入的两项任务。此函数还可以在服务器端触发命令事件。使用 arg 参数传递您的命令。例如： SAVE 命令用于单击 GridWeb 控件命令栏上的**保存**按钮，CCMD:MYCOMMAND 命令触发自定义命令事件。|
|setActiveCell(int row, int column)|用于激活特定单元格。|
|setCellValue(int row, int column, string value)|用于向指定的单元格放置值，使用其行号和列号进行指定。|
|getCellValue(int row, int column)|返回指定单元格的值。|
|getActiveRow()|与 getActiveColumn() 函数一起使用，确定活动单元格的位置。|
|getActiveColumn()|与 getActiveRow() 函数一起使用，确定活动单元格的位置。|
|getSelectRange()|返回最后选定的范围。|
|setSelectRange()|选择给定的范围。|
|clearSelections()|清除所有选择，不包括当前活动单元格。|
|getCellsArray()|与其他相关函数一起使用，如 getCellName()、 getCellValueByCell()、 getCellRow() 和 getCellColumn()。请阅读此文章以获取有关此函数用法的更多信息：[在客户端读取 GridWeb 单元格的值](/cells/zh/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)。|
创建包含与Aspose.Cells.GridWeb配套工作的客户端脚本的测试应用程序，请按以下步骤进行：

1. 创建要由GridWeb调用的JavaScript函数。
   These functions will be added to the ASP.NET page's <script></script> tag.
2. 将函数的名称分配给OnSubmitClientFunction和OnValidationErrorClientFunction属性。

代码示例的输出如下所示：

**向C1单元格添加验证** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

添加无效值并单击**保存**。将会发生验证错误并执行ValidationErrorFunction。

**在验证错误时调用ValidationErrorFunction** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

直到输入有效值，才会将数据提交到服务器。输入有效值，并单击**保存**。将执行ConfirmFunction。

**在提交GridWeb数据到服务器之前调用ConfirmFunction** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
