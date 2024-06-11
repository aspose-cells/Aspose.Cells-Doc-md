---
title: 使用Aspose.Cells.GridDesktop事件
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop，事件，事件
description: 本文介绍如何在GridDesktop中使用事件。
---

{{% alert color="primary" %}} 

事件用于在控件或类发生更改时发送通知。Aspose.Cells.GridDesktop有几个事件用于在控件中发生特定更改时执行特定任务。本主题介绍Aspose.Cells.GridDesktop控件支持的所有事件，并说明如何处理这些事件。

{{% /alert %}} 
## **介绍**
Aspose.Cells.GridDesktop控件支持几个事件，在特定事件触发时提供更多的控制执行操作。以下是Aspose.Cells.GridDesktop控件支持的事件的完整列表。

{{% alert color="primary" %}} 

此列表不包括从Control类继承的事件。

{{% /alert %}} 

|**事件**|**描述**|
| :- | :- |
|BeforeCalculate| 在工作簿中计算公式之前发生。
|BeforeLoadFile| 在从文件加载工作簿之前发生。
|ColumnHeaderClick| 当单击列标题时发生。
|ColumnHeaderDoubleClick| 当双击列标题时发生。
|CellDataChanged| 当更改网格单元格内的数据或值时发生。如果使用Value属性或GridCell的SetCellValue方法以编程方式更改单元格的值，则也可以触发此事件。
|CellButtonClick| 当单元格按钮被单击时发生。
|CellCheckedChanged| 单元格复选框的Checked属性更改时发生。
|CellSelectedIndexChanged| 单元格组合框的SelectedIndex属性更改时发生。
|CellClick| 当单元格被单击时发生。
|CellDoubleClick|当单击单元格时发生。
|CellKeyPressed| 当单元格具有焦点时按下按键时发生。如果要为CellKeyPressed事件创建事件处理程序，则为防止GridDesktop控件处理按键事件，设置CellKeyEventArgs参数的Handled属性为true。
|AfterInsertColumns| 插入列时发生。您可以使用Aspose.Cells.GridDesktop.WorksheetEventArgs的Index属性获取列索引。
|AfterInsertRows| 插入行时发生。您可以使用Aspose.Cells.GridDesktop.WorksheetEventArgs的Index属性获取行索引。
|FailLoadFile| 在加载工作簿失败时发生。|
|FinishCalculate|在工作簿中计算公式后发生。|
|FinishLoadFile|在工作簿加载完成时发生。|
|FocusedCellChanged|每当单元格焦点变化时发生。|
|RowHeaderClick|在单击行标题时发生。|
|RowHeaderDoubleClick|在双击行标题时发生。|
|RowColumnHiddenChanged|当行或列的隐藏状态发生改变时发生。|
|SelectedSheetIndexChanged|当用户选择新的工作表时发生，即当所选工作表从一个工作表更改为另一个时。如果 GridDesktop 控件的 ActiveSheetIndex 属性发生更改，也可以在程序中触发此事件。|
## **处理网格事件**
要在触发特定事件时执行特定操作，请创建一个事件处理程序。事件处理程序在特定事件触发时执行特定任务。下面使用 Visual Studio.NET 设置事件处理程序来处理一个简单的 Grid 事件。

**步骤 1：选择 Aspose.Cells.GridDesktop 控件的事件**

1. 在 Visual Studio 中，选择 Aspose.Cells.GridDesktop 控件并打开其**属性**对话框。
1. 单击**事件**选项卡。
1. 选择一个事件。（在此示例中，选择了**CellClick**事件）。

**步骤 2：创建事件处理程序**

1. 双击**属性**对话框中选择的事件。
1. 双击事件后，Visual Studio.NET 会创建一个事件处理程序。以下是设计器生成的代码，显示了为 GridControl 控件创建的事件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


现在添加代码以在事件处理程序内执行所需操作。在此示例中，我们添加了一行代码，用于显示消息框以进行通知。 
查看 Visual Studio 添加到 GridDesktop 控件的 CellClick 事件的事件处理程序。它看起来类似下面的代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**步骤 3：运行应用程序**

1. 构建并运行应用程序。
1. 每当单击网格单元格时，一个带有消息“单元格已被单击”的消息框将出现。
