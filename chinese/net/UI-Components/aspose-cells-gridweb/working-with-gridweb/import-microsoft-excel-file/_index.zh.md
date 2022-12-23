---
title: 导入 Microsoft Excel 文件
type: docs
weight: 40
url: /zh/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

与 Aspose.Cells.GridDesktop、Aspose.Cells.GridWeb 控件一样，可以打开和加载 Microsoft Excel 文件 - 包含数据、格式、图表、图像等 - 但在 Web 应用程序中。本主题说明如何。

{{% /alert %}} 
## **导入 Excel 文件**
### **从文件导入**
要使用 Aspose.Cells.GridWeb 控件打开 Excel 文件：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 通过指定文件路径导入 Excel 文件。
1. 运行应用程序。

{{% alert color="primary" %}} 

如果您不知道如何将控件添加到 Web 表单，请参阅[将 GridWeb 添加到 Web 窗体](/cells/zh/net/add-gridweb-to-web-form/).

{{% /alert %}} 

当 Aspose.Cells.GridWeb 控件添加到 Web 窗体时，该控件会自动实例化并以默认大小添加到窗体。您不必创建 Aspose.Cells.GridWeb 控件对象，您所要做的就是拖放控件并开始使用它。

但是，要将 Excel 文件中的内容加载到 Aspose.Cells.GridWeb 控件中，您必须调用 ImportExcelFile 方法来指定 Excel 文件的路径。之后，Aspose.Cells.GridWeb控件会自动从指定路径中查找文件并显示其内容。下面提供了加载 Excel 文件内容的代码片段。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


上面的代码片段可以以任何你想要的方式使用。例如，要在加载 Web 表单时自动加载 Excel 文件，请将此代码添加到表单的 Page_Load 事件。如果想在点击按钮时打开文件，在web窗体中添加一个按钮，在按钮的Click事件下写上上面的代码。

**单击按钮时加载 Excel 文件** 

![待办事项：图片_替代_文本](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

如果您的文件系统是 NTFS，您应该向 ASPNET 或 Everyone 用户帐户授予读取访问权限，否则您将在运行时遇到访问被拒绝的异常。

{{% /alert %}} 
### **从流导入**
除了从文件中打开 Excel 文件外，Aspose.Cells.GridWeb 控件还可以从流中加载 Excel 文件。使用文件作为流是一种更好的方法来禁止任何类型的文件访问或共享冲突问题，因为这种方法确保通过关闭流来关闭与文件的所有连接。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
