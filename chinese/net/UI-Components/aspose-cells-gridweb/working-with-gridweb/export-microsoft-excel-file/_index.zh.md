---
title: 导出 Microsoft Excel 文件
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb，导出
description: 本文介绍了如何在 GridWeb 中导出文件。
---

{{% alert color="primary" %}} 

可以在网站上使用 Aspose.Cells.GridWeb 控件以 GUI 模式创建新的或操作现有的 Microsoft Excel 文件。然后可以将这些文件保存为 Excel 文件。Aspose.Cells.GridWeb 有效地充当在线电子表格编辑器。本主题描述了如何将网格内容保存为 Excel 文件。

{{% /alert %}} 
## **导出 Excel 文件**
### **导出为文件**
将 Aspose.Cells.GridWeb 控件的内容保存为 Excel 文件：

1. 将 Aspose.Cells.GridWeb 控件添加到您的 web 表单上。
1. 将您的工作保存为指定路径的 Excel 文件。
1.运行应用程序

{{% alert color="primary" %}} 

如果您不知道如何将 Aspose.Cells.GridWeb 控件添加到您的 web 表单上，您应参考 [将 GridWeb 添加到 Web 表单](/cells/zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/)

{{% /alert %}} 

当 Aspose.Cells.GridWeb 控件添加到窗体上时，控件会自动实例化，并添加到具有默认大小的窗体中。您不必创建 Aspose.Cells.GridWeb 控件对象，您只需拖放控件并开始使用。

下面的代码示例说明了如何将网格内容保存为 Excel 文件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

如果您的文件系统是 NTFS，请授予 ASPNET 或 Everyone 用户账户读写权限，否则在运行时会出现访问被拒绝的异常。

{{% /alert %}} 

上述代码片段可以以几种方式使用。一个常见的方法是添加一个按钮，当单击按钮时将网格内容保存为 Excel 文件。Aspose.Cells.GridWeb 提供了一个更简单的方法。Aspose.Cells.GridWeb 有一个名为 SaveCommand 的事件。上述代码片段可以添加到 SaveCommand 事件的事件处理程序中，让用户通过点击 Aspose.Cells.GridWeb 的内置 **保存** 按钮来保存他们的工作。

**GridWeb 的 SaveCommand 事件** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**点击 GridWeb 的内置保存按钮将网格内容保存为 Excel** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

如果您在 Visual Studio 中工作，您可以通过双击 **Properties** 窗格中的事件轻松创建 SaveCommand 事件的事件处理程序。有关更多信息，请参考 [处理 GridWeb 事件](/cells/zh/net/aspose-cells-gridweb/working-with-gridweb-events/)

{{% /alert %}} 
### **导出为流**
还可以将网格内容保存到流（例如 MemoryStream）。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
