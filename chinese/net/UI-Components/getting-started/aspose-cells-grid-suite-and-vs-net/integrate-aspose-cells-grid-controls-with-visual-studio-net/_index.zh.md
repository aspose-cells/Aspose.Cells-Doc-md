---
title: 将Aspose.Cells Grid控件与Visual Studio.NET集成
type: docs
weight: 10
url: /zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: 本文描述如何在Visual Studio .NET中使用GridWeb和GridDesktop控件。
keywords: GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Visual Studio.NET开发人员可以轻松地从**工具箱**中拖动控件到Windows或Web表单上。Aspose.Cells Grid套件可以通过MSI安装程序或一组DLL包进行下载。本文解释了在使用DLL而不是安装程序安装Visual Studio.NET时，如何确保可以使用Aspose.Cells.Grid控件。

{{% /alert %}} 
## **将Aspose.Cells Grid控件集成到Visual Studio.NET中**
要将Aspose.Cells Grid控件集成到Visual Studio.NET中：

1. 打开工具箱。
1. 选择“常规”选项卡（或其他要添加控件的选项卡）。
1. 右键单击常规选项卡。
1. 在Visual Studio.NET中，从菜单中选择“选择项目”。将出现“自定义工具箱”对话框（新的VS.NET IDE（如VS.NET 2013/2015或更高版本）的过程大致相同）。
1. 点击“浏览”并定位Aspose.Cells.GridDesktop.dll和Aspose.Cells.GridWeb.dll文件。
1. 选择DLL文件，然后点击“打开”。现在“自定义工具箱”对话框中将包含来自Aspose.Cells Grid Suite的控件。对话框将突出显示新添加的控件。
1. 点击“确定”将控件添加到Visual Studio.NET的工具箱。

Aspose.Cells Grid控件已添加到工具箱的**常规**选项卡。只有GridWeb控件不可用。这是因为我们正在开发Windows窗体应用程序。在Web窗体中才可用GridWeb，而GridDesktop只能用于Windows窗体。
