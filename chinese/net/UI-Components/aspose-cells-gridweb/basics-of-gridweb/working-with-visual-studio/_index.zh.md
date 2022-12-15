---
title: 使用 Visual Studio
type: docs
weight: 20
url: /zh/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

本主题说明如何使用 Visual Studio.NET 2005 在 ASP.NET 应用程序中使用 Aspose.Cells.GridWeb。本主题对于使用 Aspose.Cells.GridWeb 的初级开发人员很有用。

{{% /alert %}} 
## **使用 Visual Studio 2013 处理 Aspose.Cells.GridWeb**
本主题通过在Visual Studio 2013中制作示例网站来展示如何使用Aspose.Cells.GridWeb。过程分为几个步骤。
### **第 1 步：创建新网站**
1. 打开 Visual Studio 2013。
1. 来自**文件**菜单，选择**新菜单**， 然后**网站**. 

![待办事项：图像_替代_文本](working-with-visual-studio_1.png)


新网站对话框打开。

1. 选择**ASP.NET Web 表单站点**从 Visual Studio 安装的模板。
1. 为网站的位置选择 HTTP 模式。

![待办事项：图像_替代_文本](working-with-visual-studio_2.png)




1. 指定将创建和存储网站文件的位置。
 1.点击**浏览**在新网站对话框中。

![待办事项：图像_替代_文本](working-with-visual-studio_3.png)



将显示“选择位置”对话框。

1. 点击**本地 IIS**标签。
显示存储在 IIS 根文件夹中的所有文件夹和 Web 应用程序（例如：C:\Inetpub\wwwroot）。

![待办事项：图像_替代_文本](working-with-visual-studio_4.png)




1. 现在在您的本地 IIS 中创建一个新的 Web 应用程序，网站文件将存储在该位置。
 “选择位置”对话框允许您在本地 IIS 中创建和删除 Web 应用程序或虚拟目录。要创建 Web 应用程序，请单击一个按钮，如下图所示。

![待办事项：图像_替代_文本](working-with-visual-studio_5.png)



创建一个默认名称为 WebSite 的新 Web 应用程序。

1. 重命名 Web 应用程序。我们将其重命名为 GridWebOn2013。
1. 点击**打开**. 

![待办事项：图像_替代_文本](working-with-visual-studio_6.png)



您返回到“新建网站”对话框。网站位置的路径设置为<http://localhost/GridWebOn2013>. 

1. 点击**好的**让 Visual Studio 创建一个网站。

![待办事项：图像_替代_文本](working-with-visual-studio_7.png)
### **第 2 步：检查网页的源代码和设计视图**
默认网站将由 Visual Studio 2013 创建。它包含一个带有一些虚拟文本和标记的 default.aspx 网页。

**default.aspx 页面的源视图** 

![待办事项：图像_替代_文本](working-with-visual-studio_8.png)



所有网页（包括 ASP.NET）都可以用两种模式打开。一种是允许开发人员访问和修改源代码的源视图。第二种模式是设计视图，可用于以所见即所得的方式设计网页。上面的屏幕截图显示了 default.aspx 网页的源代码视图。要查看设计视图，请单击**设计**. 

**default.aspx 页面的设计视图** 

![待办事项：图像_替代_文本](working-with-visual-studio_9.png)




删除 Visual Studio 添加的 Default.aspx 页面，并添加一个新的空白 Default.aspx 页面。

![待办事项：图像_替代_文本](working-with-visual-studio_10.png)
### **第三步：在网页中添加Aspose.Cells.GridWeb**
您只需将 Aspose.Cells.GridWeb（或 GridWeb）控件从工具箱中拖到网页即可。

![待办事项：图像_替代_文本](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

如果您不知道如何将 Aspose.Cells.GridWeb 添加到工具箱，请参阅[将 Aspose.Cells 网格控件与 Visual Studio 集成 .NET](/cells/zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

一旦 GridWeb 控件被拖放到网页上，它将呈现如下：

![待办事项：图像_替代_文本](working-with-visual-studio_12.png)



### **第 4 步：更改 <!DOCTYPE> 标签**
1. 切换到源代码视图并找到以下内容**<!文档类型>**源代码中的标记：

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1. 选择完整的标签。

![待办事项：图像_替代_文本](working-with-visual-studio_13.png)




1. 保留、更改或删除<!DOCTYPE>标签。
1. 或者修改<!DOCTYPE>使用以下标记：

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **第 5 步：调整 Aspose.Cells.GridWeb 控件的大小**
将 GridWeb 控件拖到网站后，可以改变其宽度和高度。

在设计视图中，您可以调整 GridWeb 的宽度和高度。

![待办事项：图像_替代_文本](working-with-visual-studio_14.png)



### **第六步：配置Aspose.Cells.GridWeb的属性**
通过单击**特性**Visual Studio 2013 IDE 右侧的按钮。
显示属性对话框。

![待办事项：图像_替代_文本](working-with-visual-studio_15.png)



属性窗格可以配置 GridWeb 的外观和一些其他属性来控制 GridWeb 的行为。
### **第 7 步：运行您的第一个包含 Aspose.Cells.GridWeb 的网站**
构建并运行网站。

1. 通过按 Ctrl+F5 或单击直接从 Visual Studio 运行网站**开始调试**. 

![待办事项：图像_替代_文本](working-with-visual-studio_16.png)

现在，您可以开始使用 GridWeb 控件了。

**GridWeb 控件的实际应用** 

![待办事项：图像_替代_文本](working-with-visual-studio_17.png)
