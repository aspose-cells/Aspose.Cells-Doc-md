---
title: 与 Aspose.Cells.GridDesktop 一起工作
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop、event、events
description: 本文介绍如何在 GridDesktop 中使用事件。
---

{{% alert color="primary" %}} 

事件用于在控件或类发生更改时发送通知。Aspose.Cells.GridDesktop 具有用于在控件中发生特定更改时执行具体任务的多个事件。本主题介绍了 Aspose.Cells.GridDesktop 控件支持的所有事件的概述，并解释了如何处理这些事件。

{{% /alert %}} 
## **介绍**
Aspose.Cells.GridDesktop 控件支持多个事件，以在触发特定事件时提供更多操作控制。以下是 Aspose.Cells.GridDesktop 控件支持的所有事件的完整列表。

{{% alert color="primary" %}} 

此列表不包括那些从 Control 类继承的事件。

{{% /alert %}} 

|**事件**|**描述**|
| :- | :- |
|BeforeCalculate| 在工作簿中计算公式之前发生。|
|BeforeLoadFile|在从文件加载工作簿之前发生。|
|ColumnHeaderClick|在单击列标题时发生。|
|ColumnHeaderDoubleClick|在双击列标题时发生。|
|CellDataChanged|在更改单元格内部数据或值时发生。如果使用 GridCell 的 Value 属性或 SetCellValue 方法以编程方式更改单元格的值，则也可能触发此事件。|
|CellButtonClick|在单击单元格按钮时发生。|
|CellCheckedChanged|在更改单元格复选框的 Checked 属性时发生。|
|CellSelectedIndexChanged|在更改单元格组合框的 SelectedIndex 属性时发生。|
|CellClick|在单击网格单元格时发生。|
|CellDoubleClick|当网格单元格被双击时发生。|
|CellKeyPressed|在单元格具有焦点时按键时发生。如果要为 CellKeyPressed 事件创建事件处理程序，则设置 CellKeyEventArgs 参数的 Handled 属性为 true，以防止 GridDesktop 控件处理键事件。|
|AfterInsertColumns|在插入列时发生。您可以通过使用 Aspose.Cells.GridDesktop.WorksheetEventArgs 参数的 Index 属性获取列索引。|
|AfterInsertRows| 当插入行时发生。您可以通过使用Aspose.Cells.GridDesktop.WorksheetEventArgs参数的Index属性来获取行索引。|
|FailLoadFile| 在加载工作簿失败时发生。|
|FinishCalculate| 在工作簿中计算公式后发生。|
|FinishLoadFile| 工作簿加载完成时发生。|
|FocusedCellChanged| 每当单元格焦点发生更改时发生。|
|RowHeaderClick| 当行标头被点击时发生。|
|RowHeaderDoubleClick| 当行标头被双击时发生。|
|RowColumnHiddenChanged| 当行或列的隐藏状态发生更改时发生。|
|SelectedSheetIndexChanged| 当用户选择新工作表时发生，即从一个工作表更改到另一个工作表时。如果GridDesktop控件的ActiveSheetIndex属性更改，也可以在程序中触发此事件。|
## **处理网格事件**
在特定事件触发时执行特定操作，请创建事件处理程序。当特定事件触发时，事件处理程序执行特定任务。下面，设置了事件处理程序来处理一个简单的Grid事件，使用Visual Studio.NET。

**步骤1：选择Aspose.Cells.GridDesktop控件的事件**

1. 在Visual Studio中，选择Aspose.Cells.GridDesktop控件并打开其**属性**对话框。
1. 点击**事件**选项卡。
1. 选择一个事件。（在此示例中，选择**CellClick**事件）。

**步骤2：创建事件处理程序**

1. 双击**属性**对话框中选定的事件。
1. 双击事件后，Visual Studio.NET将创建一个事件处理程序。以下是设计器生成的代码，显示创建了一个GridControl控件的事件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


现在添加代码在事件处理程序内执行所需操作。例如，我们添加了一行代码，用于显示消息框以进行通知。 
查看Visual Studio添加到GridDesktop控件的CellClick事件的事件处理程序。它看起来像下面的代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**步骤3：运行应用程序**

1.构建并运行应用程序。
1. 每当单元格被点击时，会弹出带有“单元格被点击”消息的消息框。
