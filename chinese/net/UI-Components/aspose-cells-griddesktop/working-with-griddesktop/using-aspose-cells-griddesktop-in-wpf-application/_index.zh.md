---
title: 在 WPF 应用程序中使用 Aspose.Cells.GridDesktop 控件
type: docs
weight: 50
url: /zh/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: 本文介绍了如何在 WPF 应用程序中使用 GridDesktop。
---

{{% alert color="primary" %}} 

本文展示了如何使用 Visual Studio 的 Windows Presentation Foundation (WPF) 设计器来在 WPF 应用程序中托管 Windows Forms 控件，如 Aspose.Cells.GridDesktop。 
我们将使用 Visual Studio 2015 来演示这个过程，但您可以使用任何版本，包括 Visual Studio 2008 或更高。

{{% /alert %}} 

本教程将引导您完成将 Aspose.Cells.GridDesktop 控件添加到 WPF 应用程序的过程。您需要一个支持 WPF 开发的 Visual Studio IDE 版本才能在本地尝试。
## **使用 Visual Studio 创建一个 WPF 应用程序**
首先，在 Visual Studio IDE 中创建一个 WPF 应用程序。单击 **文件** >> **新建** >> **项目** 菜单，从模板中选择 **WPF 应用程序**，命名项目并点击 **确定**。您可以将项目目标设置为任何高于 2.0 的 .NET Framework，但不能使用客户端配置文件 .NET Framework。
## **添加必需的命名空间的引用**
通过右键单击解决方案资源管理器窗口中的引用，选择 **添加引用** 菜单，向以下程序集添加引用。

- WindowsFormsIntegration 程序集 (WindowsFormsIntegration.dll)。
- Windows Forms 程序集 (System.Windows.Forms.dll)。
- Aspose.Cells.GridDesktop 程序集 (Aspose.Cells.GridDesktop.dll)。

此操作将所需的程序集添加到应用程序中，即将程序集复制到应用程序的 Bin 文件夹中。
## **在 XAML 中添加引用**
接下来，转到 XAML 文件，在 Windows 标记内添加以下命名空间和程序集引用。

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**最终的 Windows 标记将类似于下面所示。**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **在 XAML 中添加 Aspose.Cells.GridDesktop 控件**
只需在 XAML 的 Grid 标记中添加下面的代码。**WindowsFormsHost** 标记用于承载 Windows Forms 控件，**gridDesktop:GridDesktop** 标记表示 Aspose.Cells.GridDesktop 控件。您还可以对控件进行命名，以便在代码中更轻松地引用。

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**最终的 XAML 将如下所示。** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **使用 Aspose.Cells.GridDesktop**
现在，在 .cs 文件中可以像其他 Windows Forms 应用程序一样访问和使用 Aspose.Cells.GridDesktop 控件。为了保持演示简单，我们只是在 Aspose.Cells.GridDesktop 控件中加载一个示例电子表格并将其保存。此外，我们已使用 FrameworkElement_OnLoaded 事件来触发以下语句。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **构建和运行**
现在，使用 Visual Studio UI 上的**F5**按钮或**启动**按钮构建和运行应用程序。
