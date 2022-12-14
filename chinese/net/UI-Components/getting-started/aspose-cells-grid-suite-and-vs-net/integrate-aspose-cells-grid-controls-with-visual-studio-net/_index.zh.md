---
title: 将 Aspose.Cells 网格控件与 Visual Studio 集成 .NET
type: docs
weight: 10
url: /zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 Visual Studio.NET 开发人员可以轻松地将控件从**工具箱**到 Windows 或 Web 表单上。 Aspose.Cells 可以使用 MSI 安装程序或作为一组 DLL 包下载网格套件。本文介绍如何确保 Aspose.Cells.Grid 控件在使用 DLL 而不是安装程序安装时可以在 Visual Studio.NET 中使用。

{{% /alert %}} 
## **将 Aspose.Cells 网格控件与 Visual Studio 集成 .NET**
将 Aspose.Cells 网格控件与 Visual Studio.NET 集成：

1. 打开工具箱。
1. 选择常规选项卡（或您要向其添加控件的任何其他选项卡）。
1. 右键单击“常规”选项卡。
1. 在 Visual Studio.NET 2003 上：选择**添加/删除项目**从菜单中。
1. 在 Visual Studio.NET 2005 上，选择**选择项目**从菜单中。将出现自定义工具箱对话框（此过程与较新的 VS.NET IDE（例如 VS.NET 2013/2015 或更高版本）大致相同）。
1. 点击**浏览**并找到 Aspose.Cells.GridDesktop.dll 和 Aspose.Cells.GridWeb.dll 文件。
1. 选择 DLL，然后单击**打开**.自定义工具箱对话框现在将包含来自 Aspose.Cells Grid Suite 的控件。对话框将突出显示新添加的控件。
1. 点击**好的**将控件添加到您的 Visual Studio.NET 工具箱。

 Aspose.Cells 网格控件将被添加到工具箱的**一般的**标签。只有 GridWeb 控件未处于活动状态。这是因为我们正在处理 Windows 表单应用程序。 GridWeb 仅在您使用 Web 窗体时可用，而 GridDesktop 仅可用于 Windows 窗体。
