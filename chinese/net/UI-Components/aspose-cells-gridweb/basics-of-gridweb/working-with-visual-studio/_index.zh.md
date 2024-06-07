---
title: 在 Visual Studio 中使用
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,Visual Studio
description: 这篇文章介绍了在 Visual Studio 中使用 GridWeb 的方法。
---

{{% alert color="primary" %}} 

本主题解释了如何在使用Visual Studio.NET 2005的ASP.NET应用程序中使用Aspose.Cells.GridWeb。本主题对于与Aspose.Cells.GridWeb一起工作的初学者级开发人员非常有用。

{{% /alert %}} 
## **使用Visual Studio 2013工作Aspose.Cells.GridWeb**
此主题展示了如何在Visual Studio 2013中制作示例网站使用Aspose.Cells.GridWeb。该过程已分为几个步骤。
### **步骤1：创建新网站**
1. 打开Visual Studio 2013。
1. 从**文件**菜单中选择**新建菜单**，然后选择**网站**。 

![todo:image_alt_text](working-with-visual-studio_1.png)


打开新网站对话框。 

1. 从Visual Studio已安装的模板中选择**ASP.NET Web Forms站点**。
1. 为Web站点的位置选择HTTP模式。 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. 指定Web站点文件将被创建和存储的位置。 
   在新网站对话框中点击**浏览**。 

![todo:image_alt_text](working-with-visual-studio_3.png)



显示选择位置对话框。 

1. 点击**本地IIS**选项卡。
   显示存储在IIS根文件夹中的所有文件夹和Web应用程序（例如：C:\Inetpub\wwwroot）。 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. 现在在本地IIS中创建一个新的Web应用程序，其中将存储网站文件。
   选择位置对话框让您在本地IIS中创建和删除Web应用程序或虚拟目录。要创建Web应用程序，请按照下图中所示点击一个按钮。 

![todo:image_alt_text](working-with-visual-studio_5.png)



创建一个名为WebSite的新Web应用程序。 

1. 重命名Web应用程序。 我们将其命名为GridWebOn2013。
1. 点击**打开**。 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. 点击**确定**，让Visual Studio创建一个网站。 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **步骤2：检查Web页面的源代码和设计视图**
Visual Studio 2013已创建了一个默认的网站。它包含一个默认的.aspx网页，其中包含一些虚拟文本和标记。 

**默认.aspx页面的源代码视图** 

![todo:image_alt_text](working-with-visual-studio_8.png)



所有网页（包括ASP.NET）可以以两种模式打开。 一种是源代码视图，让开发人员访问和修改源代码。 第二种模式是设计视图，可用于以所见即所得的方式设计网页。 上面的截图显示了默认.aspx网页的源代码视图。 要查看设计视图，请点击**设计**。 

**默认.aspx页面的设计视图** 

![todo:image_alt_text](working-with-visual-studio_9.png)




删除Visual Studio添加的默认.aspx页面，并添加一个新的空白Default.aspx页面。

![todo:image_alt_text](working-with-visual-studio_10.png)
### **步骤3：将Aspose.Cells.GridWeb添加到Web页面**
您可以通过从工具箱中拖动Aspose.Cells.GridWeb（或GridWeb）控件来简单地将其添加到网页中。 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

如果您不了解如何将Aspose.Cells.GridWeb添加到工具箱，请参阅[Integrate Aspose.Cells Grid Controls with Visual Studio.NET](/cells/zh/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/)。 

{{% /alert %}} 

一旦GridWeb控件被放置到网页中，它将呈现如下形式: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. 选择完整的标签。 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **第 5 步：调整 Aspose.Cells.GridWeb 控件的大小**
在将 GridWeb 控件拖放到网站后，您可以更改 GridWeb 控件的宽度和高度。 

在设计视图中，您可以调整 GridWeb 的宽度和高度。 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **第 6 步：配置 Aspose.Cells.GridWeb 的属性**
通过单击 Visual Studio 2013 IDE 右侧的 **Properties** 按钮，在 WYSIWYG 中配置 Aspose.Cells.GridWeb 属性。 
将显示一个属性对话框。 

![todo:image_alt_text](working-with-visual-studio_15.png)



属性窗格使得可以配置 GridWeb 的外观和一些其他属性以控制 GridWeb 的行为。
### **第 7 步：运行包含 Aspose.Cells.GridWeb 的第一个网站**
构建并运行网站。 

1. 通过按下 Ctrl+F5 或单击 **开始调试** 直接从 Visual Studio 运行网站。 

![todo:image_alt_text](working-with-visual-studio_16.png)

现在，您可以开始尝试 GridWeb 控件。 

**GridWeb 控件的操作** 

![todo:image_alt_text](working-with-visual-studio_17.png)
