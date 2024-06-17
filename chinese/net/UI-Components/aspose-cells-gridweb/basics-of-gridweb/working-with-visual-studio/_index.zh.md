---
title: 在Visual Studio中使用
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: 本文介绍了如何在Visual Studio中使用GridWeb。
---

{{% alert color="primary" %}} 

本主题解释了如何在Visual Studio.NET 2005中使用Aspose.Cells.GridWeb在ASP.NET应用程序中维护。这个主题对于初学者级别的开发人员来说非常有用。

{{% /alert %}} 
## **使用Visual Studio 2013使用Aspose.Cells.GridWeb**
本主题展示了如何在Visual Studio 2013中通过制作一个示例网站来使用Aspose.Cells.GridWeb。这个过程已经分成几个步骤。
### **步骤1: 创建新的网站**
1. 打开 Visual Studio 2013。
1. 从 **文件** 菜单中，选择 **新建菜单**，然后选择 **网站**。 

![todo:image_alt_text](working-with-visual-studio_1.png)


打开新建网站对话框。 

1. 从 Visual Studio 安装的模板中选择 **ASP.NET Web Forms Site**。
1. 选择网站的位置为 HTTP 模式。 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. 指定将创建和存储网站文件的位置。 
   1. 在新建网站对话框中点击 **浏览**。 

![todo:image_alt_text](working-with-visual-studio_3.png)



显示选择位置对话框。 

1. 点击 **本地 IIS** 选项卡。
   显示存储在您的 IIS 根目录文件夹中的所有文件夹和 web 应用程序（例如：C:\Inetpub\wwwroot）。 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. 现在在本地 IIS 中创建一个新的 web 应用程序，用于存储网站文件。
   选择位置对话框允许您在本地 IIS 中创建和删除 web 应用程序或虚拟目录。要创建 web 应用程序，请按下图中所示的按钮。 

![todo:image_alt_text](working-with-visual-studio_5.png)



创建一个名为 WebSite 的新 web 应用程序。 

1. 重命名 web 应用程序。我们将其重命名为 GridWebOn2013。
1. 点击 **打开**。 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. 点击 **确定**，让 Visual Studio 创建网站。 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **第 2 步：检查网页的源视图和设计视图**
Visual Studio 2013 已创建一个默认的 web 站点。其中包含一个带有一些虚拟文本和标记的 default.aspx 网页。 

**default.aspx 网页的源视图** 

![todo:image_alt_text](working-with-visual-studio_8.png)



所有网页（包括 ASP.NET）可以以两种模式打开。一种是源视图，让开发人员访问和修改源代码。第二种模式是设计视图，可用于以所见即所得的方式设计网页。上面的截图显示了 default.aspx 网页的源视图。要查看设计视图，请点击 **设计**。 

**default.aspx 网页的设计视图** 

![todo:image_alt_text](working-with-visual-studio_9.png)




删除Visual Studio添加的Default.aspx页面，并添加一个新的空白Default.aspx页面。

![todo:image_alt_text](working-with-visual-studio_10.png)
### **第3步：将Aspose.Cells.GridWeb添加到网页**
您可以通过从工具箱拖动Aspose.Cells.GridWeb（或GridWeb）控件来简单地将其添加到网页。 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

如果您不知道如何将Aspose.Cells.GridWeb添加到工具箱，请参考[Integrate Aspose.Cells Grid Controls with Visual Studio.NET](/cells/zh/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/) 

{{% /alert %}} 

一旦GridWeb控件放置到网页上，它会呈现如下： 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. 选择完整标记。 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **步骤5：调整Aspose.Cells.GridWeb控件的大小**
您可以在将GridWeb拖到网站后更改GridWeb控件的宽度和高度。 

在设计视图中，您可以调整GridWeb的宽度和高度。 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **步骤6：配置Aspose.Cells.GridWeb的属性**
通过单击Visual Studio 2013 IDE右侧的**属性**按钮，在所见即所得中配置Aspose.Cells.GridWeb的属性 
显示属性对话框。 

![todo:image_alt_text](working-with-visual-studio_15.png)



属性窗格使得可以配置GridWeb的外观和一些其他属性来控制GridWeb的行为。
### **步骤7：运行您的第一个包含Aspose.Cells.GridWeb的网站**
构建并运行网站。 

1. 通过按Ctrl+F5或单击**开始调试**直接从Visual Studio运行网站。 

![todo:image_alt_text](working-with-visual-studio_16.png)

现在，您可以开始使用GridWeb控件。 

**GridWeb控件正在运行** 

![todo:image_alt_text](working-with-visual-studio_17.png)
