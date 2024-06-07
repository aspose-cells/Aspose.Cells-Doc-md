---
title: 将Aspose.Cells Grid控件与Visual Studio.NET集成
type: docs
weight: 10
url: /zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: 本文描述了如何在Visual Studio .NET中使用GridWeb和GridDesktop控件。
keywords: GridWeb，GridDesktop，Visual Studio，控件，集成
---

{{% alert color="primary" %}} 

Visual Studio .NET开发人员可以轻松地从**工具箱**拖动控件到Windows或Web表单中。 Aspose.Cells Grid套件可以通过MSI安装程序下载，也可以作为一组DLL包。本文解释了在使用DLL而不是安装程序安装时，如何确保可以在Visual Studio .NET中使用Aspose.Cells.Grid控件。

{{% /alert %}} 
## **将Aspose.Cells Grid控件集成到Visual Studio.NET中**
要将Aspose.Cells Grid控件集成到Visual Studio.NET中：

1. 打开工具箱。
1. 选择General标签（或者您想要添加控件的其他标签）。
1. 右键单击General标签。
1. 在Visual Studio.NET中，从菜单中选择**选择项**。将出现自定义工具箱对话框（对于较新的VS.NET IDE（例如VS.NET 2013/2015或更高版本），此过程或多或少是相同的）。
1. 点击**浏览**，定位Aspose.Cells.GridDesktop.dll和Aspose.Cells.GridWeb.dll文件。
1. 选择DLL文件，然后点击**打开**。 自定义工具箱对话框现在将包含来自Aspose.Cells Grid Suite的控件。 新添加的控件将由对话框突出显示。
1. 点击**确定**，将控件添加到您的Visual Studio.NET工具箱中。

Aspose.Cells Grid控件现在已添加到工具箱的**General**标签。 只有GridWeb控件是不活动的。 这是因为我们正在使用Windows Forms应用程序。 仅当您在使用Web Forms时，GridWeb才可用，而GridDesktop仅适用于Windows Forms。
