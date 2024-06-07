---
title: 将 GridWeb 添加到 Web 表单
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: 本文介绍了如何与 GridWeb 中的 Web 表单一起使用。
---

{{% alert color="primary" %}} 

本主题为初学者提供了创建和使用 Aspose.Cells.GridWeb 控件的基本逐步指南。

{{% /alert %}} 
## **创建和使用 Aspose.Cells.GridWeb 控件**
### **第 1 步：创建 Web 应用程序项目**
首先，在其中使用 Aspose.Cells.GridWeb 控件的 Web 应用程序项目中创建一个 Web 应用程序项目：

1. 打开 Visual Studio。
1. 在 **文件** 菜单中，选择 **新建**，然后选择 **项目**。 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



将显示一个新项目对话框。

1. 选择所需语言的 **ASP.NET Web 应用程序**。 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. 选择 **Web Forms** 模板。 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. 向项目添加新的 Web 窗体。
### **第 2 步：将控件嵌入 Web 表单**
从 Visual Studio 工具箱中将 Aspose.Cells.GridWeb 控件拖放到 Web 表单中。 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

要了解如何将 Aspose.Cells Grid 控件添加到 Visual Studio 工具箱中，请阅读 [将 Aspose.Cells.Grid 控件与 Visual Studio.NET 集成](/cells/zh/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/)。

{{% /alert %}} 

当控件已添加到表单中后，它将呈现如下所示: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **步骤 3: 调整控件大小**
表单以默认大小呈现。通过拖动边框或角落来调整大小。 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **步骤 4: 设置控件属性**
Aspose.Cells.GridWeb控件也可以使用各种属性进行配置。 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

可以使用“属性”对话框调整控件的许多属性。基本属性包括高度、宽度、颜色和视觉样式。高级属性包括编辑模式、会话模式和双击模式。此外，还可以在“属性”对话框中设置自定义事件处理程序。

Aspose.Cells.GridWeb还提供了一些额外的配置工具，可在“属性”对话框底部作为超链接查看，或通过右键单击GridWeb控件找到。这些配置工具包括:

- 自定义命令按钮
#### **自定义命令按钮**
打开自定义命令按钮编辑器:
右键单击GridWeb控件，然后选择**自定义命令按钮**。 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



显示“自定义命令按钮集合编辑器”对话框。 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

此对话框允许开发人员在GridWeb控件中添加和删除自定义命令按钮。


### **重要**
Aspose.Cells.GridWeb还提供了与控件一起的资源文件。"acw_client"是一个文件夹(安装目录) ，包含文件，并且Aspose.Cells.GridWeb使用此文件夹来管理其内部配置和其他功能，它包含脚本文件、图像文件和其他文件来指定GridWeb的行为并设置其他操作。配置文件用于管理嵌入式客户端资源 (图像、脚本 等)。此外，当需要部署具有GridWeb控件的 Web 应用程序时，还需要将"acw_client"目录复制到项目文件夹，否则您的 Web 应用程序(在服务器上部署) 将找不到它。您可以通过将以下代码行添加到配置部分(如在 VS.NET 项目中的 web.config 文件) 来始终指定资源文件夹:



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

路径始终与项目目录相关。不应使用任何位于项目目录之外的目录。因此，将"acw_client"目录(@您的GridWeb安装文件夹)复制到项目目录/子目录中是必要的。

{{% /alert %}}
### **步骤 5: 运行 Web 应用程序**
通过按Ctrl+F5或单击**开始**按钮来运行应用程序。 

应用程序在浏览器中运行时，会显示WebForm1.aspx页面，其中现在包含了一个空的Aspose.Cells.GridWeb控件。通过单击单元格添加数值。还可以执行其他任务，如更改行的高度或列的宽度，复制(Ctrl+C)或剪切(Ctrl+X)单元格数据到剪贴板，以及将数据粘贴(Ctrl+V)到单元格。要执行更多操作，请右键单击控件查看所有选项。 

**GridWeb 控件的上下文菜单** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
