---
title: 处理GridWeb事件
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb,事件,事件
description: 本文介绍了如何在GridWeb中处理各种事件。
---

{{% alert color="primary" %}} 

所有程序员都必须熟悉事件及其用途。事件用于发送对控件或类可能发生的更改的通知。Aspose.Cells.GridWeb有几个事件，可以在发生特定更改时执行特定任务。

本主题介绍了Aspose.Cells.GridWeb控件支持的所有事件的概述，以及如何处理这些事件的一些细节。

{{% /alert %}} 
## **处理Grid事件**
### **Grid事件简介**
Aspose.Cells.GridWeb 控件支持多个事件，这些事件在控件中触发特定事件时提供更多操作控制。以下是 Aspose.Cells.GridWeb 控件支持的完整事件列表。

{{% alert color="primary" %}} 

此列表不包括Aspose.Cells.GridWeb从Control类继承的事件。

{{% /alert %}} 

|**事件** |**描述** |
| :- | :- |
|CellCommand |当单击单元格的命令超链接时发生。触发此事件时，其参数e.Argument提供了命令的名称。
|CellDoubleClick |当双击单元格时发生。
|CellError |当单元格的输入值有错误时发生。
|ColumnDeleted |当用户使用客户端菜单从工作表中删除列时发生。
|ColumnDeleting |当用户尝试使用客户端菜单从工作表中删除列时发生。
|ColumnDoubleClick |当双击列标题时发生。
|ColumnInserted |当用户使用客户端菜单向工作表中插入列时发生。
|CustomCommand |当用户单击自定义命令按钮时发生。
|LoadCustomData |当控件的EnableSession属性设置为false并且需要加载工作表数据时发生。您可以在无会话模式下处理此事件，以从文件或数据库加载工作表数据。
|PageIndexChanged |当控件的工作表页索引更改时发生。
|RowDeleted |当用户使用客户端菜单从工作表中删除行时发生。
|RowDeleting |当用户尝试使用客户端菜单从工作表中删除行时发生。
|RowDoubleClick |当双击行标题时发生。
|RowInserted |当用户使用客户端菜单向工作表中插入行时发生。
|SaveCommand |当单击**保存**按钮时发生。
|SheetDataUpdated |当控件加载已发布的数据并更新工作表数据时发生。
|SheetTabClick |当单击工作表标签时发生。
|SubmitCommand |当单击**提交**按钮时发生。
|UndoCommand |当单击“撤消”按钮时发生。|
|AjaxCallFinished |在控件的AJAX更新完成时触发。（必须将EnableAJAX设置为true）。|
|CellModifiedOnAjax |当在AJAX调用中修改单元格时触发。|
|OnAfterColumnFilter |在列上应用过滤器后触发。|
|OnBeforeColumnFilter |在列上应用过滤器前触发。|
## **处理网格事件**
要在触发特定事件时执行特定操作，我们必须创建一个事件处理程序。事件处理程序在触发某个特定事件时执行所需的任务。下面的步骤演示如何使用Visual Studio处理简单的网格事件。
### **步骤1：选择Aspose.Cells.GridWeb控件的事件**
1. 选择Aspose.Cells.GridWeb控件并在右侧打开其属性对话框。
1. 单击“事件”选项卡按钮。
1. 选择一个事件。
   在本示例中，选择“SaveCommand”事件。
### **步骤2：创建事件处理程序**
1. 在属性对话框中双击一个事件。 

   **双击所选事件** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




双击事件时，Visual Studio会自动创建一个事件处理程序。 

**由Visual Studio创建的事件处理程序** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. 添加代码以在事件处理程序中执行某些操作。

在这里，已添加一行代码，用于在单击“保存”按钮时将网格内容保存到Excel文件中。

要获取更多信息，请将光标悬停在上面查看一些代码，然后您会发现Visual Studio足够智能，以添加事件处理程序到GridWeb的SaveCommand事件。
### **步骤3：运行您的应用程序**
1. 构建并运行应用程序。
1. 单击**保存**。

网格内容已保存到Excel文件。 

**应用程序运行模式** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
