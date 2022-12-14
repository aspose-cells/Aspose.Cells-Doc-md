---
title: 使用 Aspose.Cells.GridDesktop 事件
type: docs
weight: 30
url: /zh/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

事件用于在控件或类中发生更改时发送通知。 Aspose.Cells.GridDesktop 有几个事件，用于在控件发生某些更改时执行特定任务。本主题介绍 Aspose.Cells.GridDesktop 控件支持的所有事件，并说明如何处理这些事件。

{{% /alert %}} 
## **介绍**
Aspose.Cells.GridDesktop 控件支持多个事件，这些事件在特定事件被触发时为执行操作提供更多控制。以下是 Aspose.Cells.GridDesktop 控件支持的完整事件列表。

{{% alert color="primary" %}} 

此列表不包括 Aspose.Cells.GridDesktop 从 Control 类继承的那些事件。

{{% /alert %}} 

|**事件**|**描述**|
|:- |:- |
|计算前|在工作簿中计算公式之前发生。|
|加载文件前|在从文件加载工作簿之前发生。|
|列标题点击|单击列标题时发生。|
|列标题双击|双击列标题时发生。|
|单元格数据已更改|当网格单元格内的数据或值更改时发生。如果使用 GridCell 的 Value 属性或 SetCellValue 方法以编程方式更改单元格的值，也可以触发此事件。|
|单元格按钮点击|单击单元格按钮时发生。|
|CellCheckedChanged|当更改单元格复选框的选中属性时发生。|
|CellSelectedIndexChanged|当更改单元格组合框的 SelectedIndex 属性时发生。|
|细胞点击|单击网格单元格时发生。|
|单元格双击|双击网格单元格时发生。|
|CellKeyPressed|在单元格具有焦点时按下某个键时发生。如果要为 CellKeyPressed 事件创建事件处理程序，则将 CellKeyEventArgs 参数的 Handled 属性设置为 true，以防止 GridDesktop 控件处理按键事件。|
|AfterInsertColumns|插入列时发生。您可以使用 Aspose.Cells.GridDesktop.WorksheetEventArgs 参数的 Index 属性获取列索引。|
|AfterInsertRows|插入一行时发生。您可以使用 Aspose.Cells.GridDesktop.WorksheetEventArgs 参数的 Index 属性获取行索引。|
|失败加载文件|加载工作簿失败时发生。|
|完成计算|在工作簿中计算公式后发生。|
|完成加载文件|加载工作簿时发生。|
|FocusedCellChanged|每当更改单元格的焦点时发生。|
|行标题点击|单击行标题时发生。|
|行标题双击|双击行标题时发生。|
|行列隐藏已更改|当行或列的隐藏状态改变时发生。|
|SelectedSheetIndexChanged|当用户选择新工作表时发生，即当所选工作表从一个工作表更改为另一个工作表时发生。如果 GridDesktop 控件的 ActiveSheetIndex 属性更改，也可以通过编程方式触发此事件。|
## **处理网格事件**
要在触发特定事件时执行特定操作，请创建事件处理程序。当触发特定事件时，事件处理程序执行特定任务。下面，使用 Visual Studio.NET 设置事件处理程序来处理简单的网格事件。

**第一步：选择Aspose.Cells.GridDesktop控件的事件**

1. 在 Visual Studio 中，选择 Aspose.Cells.GridDesktop 控件并打开其**特性**对话。
1. 点击**事件**标签。
1. 选择一个事件。 （对于这个例子，**细胞点击**事件被选中）。

**第 2 步：创建事件处理程序**

1. 双击选定的事件**特性**对话。
1. 双击事件时，Visual Studio.NET 创建事件处理程序。以下是设计器生成的代码，它显示为 GridControl 控件创建了一个事件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


现在添加代码以在事件处理程序中执行所需的操作。对于此示例，我们添加了一行代码来显示通知消息框。
查看 visual Studio 添加到 GridDesktop 控件的 CellClick 事件的事件处理程序。它看起来像下面的代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**第 3 步：运行应用程序**

1. 构建并运行应用程序。
1. 每当单击网格单元格时，都会出现一个消息框，其中包含消息“Cell is Clicked”。
