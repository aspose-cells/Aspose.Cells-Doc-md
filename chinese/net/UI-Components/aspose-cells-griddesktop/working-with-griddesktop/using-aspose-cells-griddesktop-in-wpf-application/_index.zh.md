---
title: 在WPF应用程序中使用Aspose.Cells.GridDesktop
type: docs
weight: 50
url: /zh/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop，wpf
description: 本文介绍了如何在WPF应用程序中使用GridDesktop。
---

{{% alert color="primary" %}} 

本文演示如何在WPF应用程序中使用Windows Presentation Foundation (WPF) Designer for Visual Studio来托管Windows Forms控件，如Aspose.Cells.GridDesktop。 
我们将使用Visual Studio 2015来演示该过程，但您也可以使用包括Visual Studio 2008在内的任何版本。

{{% /alert %}} 

本教程将指导您完成将Aspose.Cells.GridDesktop控件添加到WPF应用程序的过程。您需要任何支持WPF开发的Visual Studio IDE版本才能在本地尝试。
## **使用Visual Studio创建WPF应用程序**
首先使用Visual Studio IDE创建一个WPF应用程序。单击**文件** >> **新建** >> **项目**菜单，选择**WPF应用程序**模板，命名项目并单击**确定**。您可以将项目目标设置为高于2.0的任何.NET Framework版本，但不能使用客户端配置文件.NET Framework。
## **添加所需命名空间的引用**
通过右键单击解决方案资源管理器窗口中的引用并选择**添加引用**菜单，添加对以下程序集的引用。

- WindowsFormsIntegration 程序集 (WindowsFormsIntegration.dll)。
- Windows Forms 程序集 (System.Windows.Forms.dll)。
- Aspose.Cells.GridDesktop 程序集 (Aspose.Cells.GridDesktop.dll)。

此操作将向应用程序添加所需的程序集，即将程序集复制到应用程序的Bin文件夹中。
## **添加XAML的引用**
接下来，转到XAML文件并在Windows标记内添加以下命名空间和程序集引用。

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**最终的Windows标记将如下所示。**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **将Aspose.Cells.GridDesktop控件添加到XAML**
只需在XAML的Grid标记内添加以下代码。**WindowsFormsHost**标记用于托管Windows Forms控件，**gridDesktop:GridDesktop**标记代表Aspose.Cells.GridDesktop控件。您还可以命名该控件，以便在代码中轻松引用。

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**最终的XAML将如下所示。** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **使用Aspose.Cells.GridDesktop**
现在，我们可以像使用其他Windows Forms应用程序一样在.cs文件中访问和使用Aspose.Cells.GridDesktop控件。为了保持演示简单，我们只是在Aspose.Cells.GridDesktop控件中加载了一个示例电子表格，并将其保存。此外，我们使用FrameworkElement_OnLoaded事件来触发以下语句。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **构建和运行**
现在，使用Visual Studio UI上的**F5**或**开始**按钮构建并运行应用程序。
