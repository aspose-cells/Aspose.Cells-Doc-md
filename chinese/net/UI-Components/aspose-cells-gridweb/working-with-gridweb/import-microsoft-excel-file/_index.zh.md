---
title: 导入 Microsoft Excel 文件
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb，导入
description: 本文介绍如何在 GridWeb 中导入文件。
---

{{% alert color="primary" %}} 

与 Aspose.Cells.GridDesktop 一样，Aspose.Cells.GridWeb 控件可以在 web 应用程序中打开和加载 Microsoft Excel 文件 - 包括数据、格式、图表、图片等。本主题解释了如何操作。

{{% /alert %}} 
## **导入Excel文件**
### **从文件导入**
使用Aspose.Cells.GridWeb控件打开Excel文件:

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 通过指定文件路径导入 Excel 文件。
1. 运行应用程序。

{{% alert color="primary" %}} 

如果您不知道如何将控件添加到Web表单，请参阅[将GridWeb添加到Web表单](/cells/zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/)。

{{% /alert %}} 

当Aspose.Cells.GridWeb控件添加到Web表单时，该控件将自动实例化并添加到具有默认大小的表单。您无需创建Aspose.Cells.GridWeb控件对象，您只需拖放该控件并开始使用它。

然而，要将Excel文件中的内容加载到Aspose.Cells.GridWeb控件中，您必须调用ImportExcelFile方法来指定Excel文件的路径。之后，Aspose.Cells.GridWeb控件将自动在指定路径中找到文件并显示其内容。下面提供了加载Excel文件内容的代码片段。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


以上代码片段可以随意使用。例如，要在Web表单加载时自动加载Excel文件，请将此代码添加到表单的Page_Load事件中。如果要在单击按钮时打开文件，请将按钮添加到Web表单，并在按钮的Click事件下编写上述代码。

**单击按钮时加载Excel文件** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

如果您的文件系统是NTFS，您应该授予ASPNET或Everyone用户帐户读取访问权限，否则您将在运行时获得拒绝访问异常。

{{% /alert %}} 
### **从流导入**
除了从文件打开Excel文件，Aspose.Cells.GridWeb控件还可以从流中加载Excel文件。使用文件作为流是禁止任何文件访问或共享违规问题的更好方法，因为这种方法通过关闭流来确保关闭对文件的所有连接。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
