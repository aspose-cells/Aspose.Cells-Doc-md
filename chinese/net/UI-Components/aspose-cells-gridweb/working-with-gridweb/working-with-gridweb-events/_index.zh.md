---
title: 处理 GridWeb 事件
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb，事件，操作
description: 本文介绍了如何处理 GridWeb 中各种事件。
---

{{% alert color="primary" %}} 

所有程序员都必须熟悉事件及其目的。事件用于发送可能发生在控件或类中的更改的通知。Aspose.Cells.GridWeb 具有多个事件，可用于在控件中发生特定更改时执行特定任务。

本主题介绍了 Aspose.Cells.GridWeb 控件支持的所有事件以及如何处理这些事件的一些细节。

{{% /alert %}} 
## **处理网格事件**
### **网格事件简介**
Aspose.Cells.GridWeb 控件支持多个事件，可以在控件中触发特定事件时提供更多控制以执行操作。您可以在下面找到 Aspose.Cells.GridWeb 控件支持的事件的完整列表。

{{% alert color="primary" %}} 

此列表不包括 Aspose.Cells.GridWeb 从 Control 类继承的事件。

{{% /alert %}} 

|**事件** |**描述** |
| :- | :- |
|CellCommand |当单元格的命令超链接被点击时发生。当触发此事件时，其参数e.Argument提供了命令的名称。|
|CellDoubleClick |当双击单元格时发生。|
|CellError |当单元格的输入值存在错误时发生。|
|ColumnDeleted |当用户使用客户端侧菜单从工作表中删除列时发生。|
|ColumnDeleting |当用户尝试使用客户端侧菜单从工作表中删除列时发生。|
|ColumnDoubleClick |当双击列标题时发生。|
|ColumnInserted |当用户使用客户端侧菜单向工作表中插入列时发生。|
|CustomCommand |当用户单击自定义命令按钮时发生。|
|LoadCustomData |当控件的EnableSession属性设置为false并且需要加载工作表数据时发生。您可以在无会话模式下处理此事件，以从文件或数据库加载工作表数据。|
|PageIndexChanged |当控件的工作表页索引更改时发生。|
|RowDeleted |当用户使用客户端侧菜单从工作表中删除行时发生。|
|RowDeleting |当用户尝试使用客户端侧菜单从工作表中删除行时发生。|
|RowDoubleClick |当双击行标题时发生。|
|RowInserted |当用户使用客户端侧菜单向工作表中插入行时发生。|
|SaveCommand |当单击“保存”按钮时发生。|
|SheetDataUpdated |当控件已加载发布的数据并更新了工作表数据时发生。|
|SheetTabClick |当工作表选项卡被点击时发生。|
|SubmitCommand |当单击“提交”按钮时发生。|
|UndoCommand |**撤销**按钮被点击时发生。|
|AjaxCallFinished |在控件的 AJAX 更新完成时触发。(EnableAJAX 应设置为 true)。|
|CellModifiedOnAjax |在 AJAX 调用中修改单元格时触发。|
|OnAfterColumnFilter |筛选器在列上应用后触发。|
|OnBeforeColumnFilter |在列进行筛选前触发。|
## **处理网格事件**
要在触发特定事件时执行特定操作，必须创建事件处理程序。事件处理程序在触发特定事件时执行所需任务。以下步骤说明了如何使用Visual Studio处理简单网格事件。
### **第1步：选择Aspose.Cells.GridWeb控件的事件**
1.选择Aspose.Cells.GridWeb控件并在右侧打开其属性对话框。
1.单击**事件选项卡**按钮。
1.选择一个事件。
   在此示例中，选择了SaveCommand事件。
### **第2步：创建事件处理程序**
1.在属性对话框中双击一个事件。 

   **双击选定事件** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




双击事件后，Visual Studio会自动创建事件处理程序。 

**由Visual Studio创建的事件处理程序** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1.添加代码以在事件处理程序中执行某些操作。

在此处，添加了一行代码，当单击**保存**按钮时，将网格内容保存到Excel文件中。

要获取更多信息，请将光标移动到上方以查看一些代码，然后您将会发现Visual Studio足够智能，可以添加一个事件处理程序到GridWeb的SaveCommand事件中。
### **第3步：运行您的应用程序**
1.构建并运行应用程序。
1.单击**保存**。

网格内容已保存到Excel文件中。 

**运行模式中的应用程序** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
