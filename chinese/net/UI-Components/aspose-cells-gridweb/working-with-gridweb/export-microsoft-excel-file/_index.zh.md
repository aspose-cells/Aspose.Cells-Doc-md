---
title: 导出Microsoft Excel文件
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb，导出
description: 本文介绍了如何在GridWeb中导出文件。
---

{{% alert color="primary" %}} 

使用Aspose.Cells.GridWeb控件在网站上以GUI模式创建新的或操作现有的Microsoft Excel文件是可能的。然后可以将文件保存为Excel文件。Aspose.Cells.GridWeb有效地充当在线电子表格编辑器。本主题描述了如何将网格内容保存为Excel文件。

{{% /alert %}} 
## **导出Excel文件**
### **导出为文件**
要将 Aspose.Cells.GridWeb 控件的内容另存为 Excel 文件：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 将您的工作保存为指定路径的 Excel 文件。
1. 运行应用程序。

{{% alert color="primary" %}} 

如果您不知道如何将Aspose.Cells.GridWeb控件添加到Web表单中，则应参考[将GridWeb添加到Web表单中](/cells/zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/)

{{% /alert %}} 

将Aspose.Cells.GridWeb控件添加到Windows表单时，控件会自动实例化并添加到具有默认大小的表单中。您不必创建一个Aspose.Cells.GridWeb控件对象，您只需拖放控件并开始使用。

下面的代码示例说明了如何将网格内容保存为 Excel 文件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

如果您的文件系统是NTFS，请授予ASPNET或Everyone用户帐户读/写访问权限，否则您将在运行时收到拒绝访问的异常。

{{% /alert %}} 

上述代码片段可以以多种方式使用。常见的方法是添加一个按钮，当点击时将网格内容保存为Excel文件。Aspose.Cells.GridWeb提供了更简单的方法。Aspose.Cells.GridWeb具有一个名为SaveCommand的事件。上述代码片段可以添加到SaveCommand事件的事件处理程序中，允许用户通过点击Aspose.Cells.GridWeb的内置**保存**按钮来保存他们的工作。

**GridWeb的SaveCommand事件** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**点击GridWeb的内置保存按钮将网格内容保存到Excel** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

如果您在Visual Studio中工作，可以通过在**属性**窗格中双击事件轻松创建SaveCommand事件的事件处理程序。要了解更多信息，请参阅[使用GridWeb事件](/cells/zh/net/aspose-cells-gridweb/working-with-gridweb-events/)

{{% /alert %}} 
### **作为流导出**
还可以将网格内容保存到流（例如MemoryStream）中。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
