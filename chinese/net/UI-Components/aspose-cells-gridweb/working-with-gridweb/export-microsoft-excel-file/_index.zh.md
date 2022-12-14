---
title: 导出 Microsoft Excel 文件
type: docs
weight: 50
url: /zh/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

可以使用 Aspose.Cells.GridWeb 控件在 GUI 模式的网站上创建新的或操作现有的 Microsoft Excel 文件。然后可以将文件保存到 Excel 文件中。 Aspose.Cells.GridWeb 有效地充当在线电子表格编辑器。本主题介绍如何将网格内容保存到 Excel 文件。

{{% /alert %}} 
## **导出 Excel 文件**
### **导出为文件**
将 Aspose.Cells.GridWeb 控件的内容保存为 Excel 文件：

1. 将 Aspose.Cells.GridWeb 控件添加到您的 Web 表单。
1. 在指定路径将您的工作保存为 Excel 文件。
1. 运行应用程序。

{{% alert color="primary" %}} 

如果您不知道如何将 Aspose.Cells.GridWeb 控件添加到您的 Web 表单，那么您应该参考[将 GridWeb 添加到 Web 窗体](/cells/zh/net/add-gridweb-to-web-form/)

{{% /alert %}} 

当 Aspose.Cells.GridWeb 控件添加到窗体时，该控件会自动实例化并以默认大小添加到窗体。您不必创建 Aspose.Cells.GridWeb 控件对象，您所要做的就是拖放控件并开始使用它。

下面的代码示例说明了如何将网格内容保存到 Excel 文件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

如果您的文件系统是 NTFS，请授予对 ASPNET 或 Everyone 用户帐户的读/写访问权限，否则您将在运行时遇到拒绝访问的异常。

{{% /alert %}} 

上面的代码片段可以以多种方式使用。一种常见的方法是添加一个按钮，单击该按钮可将网格内容保存到 Excel 文件中。 Aspose.Cells.GridWeb 提供了一种更简单的任务方法。 Aspose.Cells.GridWeb 有一个名为 SaveCommand 的事件。上面的代码片段可以添加到 SaveCommand 事件的事件处理程序中，它允许用户通过单击 Aspose.Cells.GridWeb 的内置**节省**按钮。

**GridWeb 的 SaveCommand 事件** 

![待办事项：图片_替代_文本](export-microsoft-excel-file_1.jpg)

**通过单击 GridWeb 的内置保存按钮将网格内容保存到 Excel** 

![待办事项：图片_替代_文本](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

如果您在 Visual Studio 中工作，则可以通过双击**特性**窗格。要了解更多信息，请参阅[使用 GridWeb 事件](/cells/zh/net/working-with-gridweb-events/)

{{% /alert %}} 
### **导出为流**
也可以将网格内容保存到流中（例如 MemoryStream）。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
