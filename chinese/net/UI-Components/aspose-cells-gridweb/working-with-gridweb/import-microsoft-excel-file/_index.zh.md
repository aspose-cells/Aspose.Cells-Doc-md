---
title: 导入Microsoft Excel文件
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb，导入
description: 本文介绍了如何在GridWeb中导入文件
---

{{% alert color="primary" %}} 

与Aspose.Cells.GridDesktop类似，Aspose.Cells.GridWeb控件可以打开和加载Microsoft Excel文件-包括数据、格式、图表、图像等-但是在Web应用程序中。本主题解释了如何实现这一点

{{% /alert %}} 
## **导入Excel文件**
### **从文件导入**
使用Aspose.Cells.GridWeb控件打开Excel文件的方法:

1.将Aspose.Cells.GridWeb控件添加到Web表单中
1.通过指定文件路径导入Excel文件
1.运行应用程序

{{% alert color="primary" %}} 

如果您不知道如何将控件添加到Web表单，请参考[将GridWeb添加到Web表单](/cells/zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/)

{{% /alert %}} 

将Aspose.Cells.GridWeb控件添加到Web表单后，该控件会自动实例化并添加到具有默认大小的表单中。您不必创建Aspose.Cells.GridWeb控件对象，您只需拖放控件并开始使用

但是，要将Excel文件的内容加载到Aspose.Cells.GridWeb控件中，您必须调用ImportExcelFile方法并指定Excel文件的路径。之后，Aspose.Cells.GridWeb控件将自动从指定路径找到文件并显示其内容。下面提供了加载Excel文件内容的代码片段



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


上述代码片段可随意使用，例如，要在Web表单加载时自动加载Excel文件，请将此代码添加到表单的Page_Load事件中。如果要在单击按钮时打开文件，请向Web表单添加按钮并在按钮的单击事件下编写上述代码

**单击按钮时加载Excel文件** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

如果您的文件系统是NTFS，请授予ASPNET或Everyone用户帐户读取权限，否则您将在运行时得到一个访问被拒绝的异常。

{{% /alert %}} 
### **从流中导入**
除了从文件打开Excel文件外，Aspose.Cells.GridWeb控件还可以从流中加载Excel文件。使用文件作为流是禁止任何文件访问或共享违规问题的更好方法，因为此方法确保通过关闭流关闭所有与文件的连接。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
