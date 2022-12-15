---
title: 将 GridWeb 添加到 Web 窗体
type: docs
weight: 10
url: /zh/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

本主题为初学者提供基本的分步指南，帮助他们在 Web 应用程序中创建和使用 Aspose.Cells.GridWeb 控件。

{{% /alert %}} 
## **创建和使用 Aspose.Cells.GridWeb 控件**
### **第 1 步：创建 Web 应用程序项目**
首先，创建一个 Web 应用程序项目，在其中使用 Aspose.Cells.GridWeb 控件：

1. 打开视觉工作室。
1. 来自**文件**菜单，选择**新的**其次是**项目**. 

![待办事项：图像_替代_文本](add-gridweb-to-web-form_1.png)



出现新项目对话框。

1. 选择**ASP.NET 网络应用程序**所需的语言。

![待办事项：图像_替代_文本](add-gridweb-to-web-form_2.png)

1. 选择**网页表格**模板。

![待办事项：图像_替代_文本](add-gridweb-to-web-form_3.png)

1. 向项目中添加一个新的 Web 表单。
### **第 2 步：将控件嵌入 Web 窗体**
将 Aspose.Cells.GridWeb 控件从 Visual Studio 工具箱拖放到 Web 窗体。

![待办事项：图像_替代_文本](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

要了解如何将 Aspose.Cells 网格控件添加到 Visual Studio 工具箱，请阅读[集成 Aspose.Cells.Grid 控件与 Visual Studio.NET](/cells/zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

将控件添加到窗体后，它呈现如下：

![待办事项：图像_替代_文本](add-gridweb-to-web-form_5.png)
### **第 3 步：调整控件大小**
表单以默认大小呈现。通过拖动边框或角来调整大小。

![待办事项：图像_替代_文本](add-gridweb-to-web-form_6.png)
### **第 4 步：设置控件属性**
Aspose.Cells.GridWeb 控件也可以使用各种属性进行配置。

![待办事项：图像_替代_文本](add-gridweb-to-web-form_7.png)

可以使用“属性”对话框调整控件的许多属性。基本属性包括高度、宽度、颜色和视觉样式。高级属性包括编辑模式、会话模式和双击模式。此外，可以在“属性”对话框中设置自定义事件处理程序。

还有一些用于 Aspose.Cells.GridWeb 的额外配置工具，可以在“属性”对话框的底部看到超链接，或者右键单击 GridWeb 控件以找到它们。这些配置工具包括：

- 自定义命令按钮
#### **自定义命令按钮**
要打开自定义命令按钮编辑器：
右键单击 GridWeb 控件并选择**自定义命令按钮**. 

![待办事项：图像_替代_文本](add-gridweb-to-web-form_8.png)



显示 CustomCommandButton 集合编辑器对话框。

![待办事项：图像_替代_文本](add-gridweb-to-web-form_9.png)

该对话框允许开发人员在 GridWeb 控件中添加和删除自定义命令按钮。


### **重要的**
Aspose.Cells.GridWeb也提供了它的资源文件与控件。 “acw_client”是一个包含文件和Aspose.Cells的文件夹（@你的安装目录）。GridWeb使用这个文件夹来管理它的内部配置和其他功能，它有脚本文件，图像文件和其他文件来指定GridWeb的行为和设置其他操作。 config文件用于管理嵌入式客户端资源（图片、脚本等）。此外，当您需要部署具有GridWeb控件的Web应用程序时，您还需要复制“acw_client”目录到你的项目文件夹中，至少你的 web 应用程序（部署在服务器上）找不到它。你总是可以通过将以下代码行添加到配置部分来指定资源文件夹（例如，在你的 web.config 文件中VS.NET 项目）：



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

该路径始终与项目目录相关。您不应使用项目目录之外的任何目录。所以需要将“acw_client”目录（@你的GridWeb安装文件夹）复制到项目的目录/子目录中。

{{% /alert %}}
### **第 5 步：运行 Web 应用程序**
按 Ctrl+F5 或单击**开始**按钮。

当应用程序在浏览器中运行时，将显示 WebForm1.aspx 页面，其中现在包含一个空的 Aspose.Cells.GridWeb 控件。通过单击向单元格添加值。还可以执行其他任务，例如更改行高或列宽、将单元格数据复制 (Ctrl+C) 或剪切 (Ctrl+X) 到剪贴板以及将数据粘贴 (Ctrl+V) 到单元格.要执行更多操作，请右键单击该控件以查看完整的选项列表。

**GridWeb 控件的上下文菜单** 

![待办事项：图像_替代_文本](add-gridweb-to-web-form_10.png)
