---
title: 在 WPF 应用程序中使用 Aspose.Cells.GridDesktop
type: docs
weight: 50
url: /zh/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

本文演示如何使用 Windows Presentation Foundation (WPF) Designer for Visual Studio 在 WPF 应用程序中承载 Windows Forms 控件，例如 Aspose.Cells.GridDesktop。
我们将使用 Visual Studio 2015 来演示该过程，但是，您可以使用任何版本，包括 Visual Studio 2008 或更高版本。

{{% /alert %}} 

本教程将引导您完成将 Aspose.Cells.GridDesktop 控件添加到 WPF 应用程序的过程。您需要支持 WPF 开发的任何版本的 Visual Studio IDE 才能在您身边进行尝试。
## **使用 Visual Studio 创建 WPF 应用程序**
首先使用 Visual Studio IDE 创建一个 WPF 应用程序。点击**文件** >> **新的** >> **项目**菜单并选择**WPF应用程序**从模板中，命名项目并单击**好的**.您可以将您的项目定位到任何高于 2.0 的 .NET 框架，但是，您不能使用客户端配置文件 .NET 框架。
## **添加对所需命名空间的引用**
通过右键单击“解决方案资源管理器中的引用”窗口并选择“添加引用”菜单，添加对以下程序集的引用。

- WindowsFormsIntegration 程序集 (WindowsFormsIntegration.dll)。
- Windows 表单程序集 (System.Windows.Forms.dll)。
- Aspose.Cells.GridDesktop 程序集 (Aspose.Cells.GridDesktop.dll)。

此操作将所需的程序集添加到应用程序中，即；将程序集复制到应用程序的 Bin 文件夹中。
## **添加对 XAML 的引用**
接下来，转到 XAML 文件并在 Windows 标记内添加以下命名空间和程序集引用。

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**最终的 Windows 标签将类似于下图所示。**

![待办事项：图像_替代_文本](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **将 Aspose.Cells.GridDesktop 控件添加到 XAML**
只需在 XAML 中的 Grid 标记内添加以下代码。这**Windows窗体主机**标记用于承载 Windows 表单控件和**网格桌面：网格桌面**标记代表 Aspose.Cells.GridDesktop 控件。您还可以命名控件，以便在代码中轻松引用它。

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**最终的 XAML 将如下所示。** 

![待办事项：图像_替代_文本](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **使用 Aspose.Cells.GridDesktop**
我们现在可以像任何其他 Windows Forms 应用程序一样访问和使用 .cs 文件中的 Aspose.Cells.GridDesktop 控件。为了保持演示简单，我们只是在 Aspose.Cells.GridDesktop 控件中加载示例电子表格并将其保存回来。此外，我们还使用了 FrameworkElement_OnLoaded 事件来触发以下语句。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **构建与运行**
现在，使用**F5**或者**开始** Visual Studio UI 上的按钮。
