---
title: 将GridWeb添加到Web表单
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb，webform，form
description: 本文介绍了如何在GridWeb中使用web表单。
---

{{% alert color="primary" %}} 

本主题为初学者提供了一个基本的逐步指南，以帮助他们在Web应用程序中创建和使用Aspose.Cells.GridWeb控件。

{{% /alert %}} 
## **创建并使用Aspose.Cells.GridWeb控件**
### **步骤1：创建Web应用程序项目**
首先，创建一个Web应用程序项目，在其中使用Aspose.Cells.GridWeb控件：

1.打开Visual Studio。
1.从**文件**菜单中，依次选择**新建**和**项目**。 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



将出现一个新项目对话框。

1.选择您需要的语言的**ASP. NET Web应用程序**。 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1.选择**Web Forms**模板。 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1.向项目添加一个新的Web表单。
### **步骤2：将控件嵌入到Web表单中**
从Visual Studio工具箱中将Aspose.Cells.GridWeb控件拖放到Web表单中。 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

要了解如何将Aspose.Cells Grid控件添加到Visual Studio工具箱，请阅读[Integrate Aspose.Cells.Grid Controls with Visual Studio.NET](/cells/zh/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/)。

{{% /alert %}} 

当控件已添加到表单中时，会呈现如下所示： 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **步骤3：调整控件大小**
表单会以默认大小呈现。通过拖动边框或角落来调整大小。 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **步骤4：设置控件属性**
Aspose.Cells.GridWeb控件也可以使用各种属性进行配置。 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

您可以使用属性对话框调整控件的许多属性。基本属性包括高度、宽度、颜色和视觉样式。高级属性包括编辑模式、会话模式和双击模式。此外，还可以在属性对话框中设置自定义事件处理程序。

Aspose.Cells.GridWeb还提供了一些额外的配置工具，可以在属性对话框的底部作为超链接看到，或者右键单击GridWeb控件找到这些工具。这些配置工具包括：

- 自定义命令按钮
#### **自定义命令按钮**
打开自定义命令按钮编辑器：
右键单击GridWeb控件，然后选择**Custom Command Buttons**。 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



CustomCommandButton Collection Editor对话框将显示。 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

对话框允许开发人员在GridWeb控件中添加和删除自定义命令按钮。


### **重要**
Aspose.Cells.GridWeb还提供了控件的资源文件。"acw_client"是一个文件夹（@您的安装目录），其中包含文件，Aspose.Cells.GridWeb使用该文件夹来管理其内部配置和其他功能，它包含脚本文件、图像文件和其他文件，用于指定GridWeb的行为和设置其他操作。 配置文件用于管理嵌入式客户端资源（图像、脚本等）。此外，当需要部署拥有GridWeb控件的Web应用程序时，还需要将"acw_client"目录复制到项目文件夹中，否则您的Web应用程序（部署在服务器上）找不到它。 您始终可以通过将以下代码添加到配置部分（例如，在VS.NET项目中的web.config文件中）来指定资源文件夹：



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

路径始终与项目目录相关。您不应使用项目目录之外的任何目录。因此，有必要将"acw_client"目录（@您的GridWeb安装文件夹）复制到项目目录/子目录中。

{{% /alert %}}
### **第5步：运行Web应用程序**
按Ctrl+F5运行应用程序或单击**开始**按钮。 

当应用程序在浏览器中运行时，将显示WebForm1.aspx页面，该页面当前包含一个空的Aspose.Cells.GridWeb控件。通过点击单元格添加值。还可以执行其他任务，如更改行的高度或列的宽度，将单元格数据复制（Ctrl+C）或剪切（Ctrl+X）到剪贴板，然后将数据粘贴（Ctrl+V）到单元格中。要执行更多操作，请右键单击控件以查看完整的选项列表。 

**GridWeb控件的上下文菜单** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
