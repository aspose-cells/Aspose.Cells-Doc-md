---
title: 安装 Aspose Cells 到 NuGet
type: docs
weight: 30
url: /zh/net/installation/
---
## **安装 Aspose.Cells for .NET 到 NuGet**
NuGet 是下载和安装 Aspose API for .NET 的最简单方法。打开 Microsoft Visual Studio 和 NuGet 程序包管理器。搜索“aspose”找到所需的Aspose API。点击“安装”，所选的API将被下载并引用到您的项目中。

注意：您可以访问aspose.cells的nuget网页了解更多信息：
[Aspose.Cells for .NET NuGet 包](https://www.nuget.org/packages/Aspose.Cells/)

### **使用包管理器 GUI 安装 Aspose.Cells**
按照以下步骤使用包管理器 GUI 引用 Aspose.Cells 组件：

- 在 Visual Studio 中打开您的解决方案/项目。
- 点击**工具** -> **库包管理器** -> **管理 NuGet 包**来自解决方案。您还可以通过解决方案资源管理器轻松访问相同的选项。右键单击解决方案或项目并选择**管理 NuGet 包**从上下文菜单。
- 选择**在线的**从左侧菜单并在搜索文本框中键入“Aspose.Cells”以查找 Aspose.Cells .NET 包。
- 点击**安装**Aspose.Cells for .NET 条目旁边的按钮，将最新版本安装到您的项目中。
### **使用包管理器控制台安装 Aspose.Cells**
您可以按照以下步骤使用包管理器控制台引用 Aspose.Cells 组件：

- 在 Visual Studio 中打开您的解决方案/项目。
- 选择**工具** -> **库包管理器** -> **包管理器控制台**从菜单打开包管理器控制台。
 输入命令“Install-Package Aspose.Cells”并按回车键将最新的完整版本安装到您的应用程序中。或者，您可以向命令添加“-prerelease”后缀，以指定也安装包括修补程序在内的最新版本。
- 您会看到“正在下载 Aspose.Cells...”提示出现在窗口的左下角，表示下载正在进行中。
- 下载后，您将看到以下确认消息。如果您不熟悉 Aspose EULA，那么最好阅读 URL 中引用的许可证。
- 您现在应该发现 Aspose.Cells 已成功添加并在您的应用程序中引用。
## **从 .NET 项目引用 Aspose.Cells**
为了在应用程序中使用 Aspose.Cells，请添加对它的引用。要使用 Visual Studio 添加引用：

1. 在里面**解决方案资源管理器**，展开要添加引用的项目节点。
1. 右键单击**参考**项目的节点并选择**添加参考**从菜单中。
1. 在里面**添加参考**对话框中，选择 .NET 选项卡（默认选中）。如果您使用 MSI 安装程序安装，Aspose.Cells 将出现在顶部窗格中。
1. 选择它并单击**选择**.

如果您只下载或解压了 DLL：

1. 使用以下命令找到 Aspose.Cells.dll 文件**浏览**按钮。 Aspose.Cells 应该出现在**选定的组件**对话框的窗格。
1. 点击**好的** . Aspose.Cells 参考出现在**参考**项目的节点。
### **从 VS.NET 2010 Client Profile 项目引用组件**
如果您的项目的目标框架是 .NET Framework 3.5/4 Client Profile，请使用位于安装目录的 net_ClientProfile 文件夹中的 Aspose.Cells.dll 组件文件。例如：

- 在**解决方案资源管理器** VS.NET 2010 为您的项目，右键单击**参考**并选择**添加参考**.
- 选择**浏览**对话框中的选项卡，然后单击查找下拉列表。
- 在您的安装目录中找到并选择 Aspose.Cells.dll 组件文件，例如：.../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **（请确保您使用计算机上的 MSI 安装程序安装了该产品.)**
- 点击**好的**关闭对话框

{{% alert color="primary" %}} 

如果您的 VS.NET 2010 项目的目标框架是“.NET Framework 4”或其他，则只需使用位于 net4.0/net2.0 文件夹中的 Aspose.Cells.dll 组件文件。

{{% /alert %}} 
## **从 .NET 项目引用 Aspose.Cells 网格控件**
要在您的应用程序中使用网格控件，请添加对它的引用。要在 Visual Studio 中引用网格控件，请执行以下操作：

- 在**解决方案资源管理器**，展开要添加引用的项目节点。
- 右键单击**参考**项目的节点并选择**添加参考**从菜单中。
- 在里面**添加参考**对话框，选择**.NET 选项卡**（默认选择）。如果您使用 MSI 安装程序安装 Aspose.Cells for .NET，Aspose.Cells.GridDesktop 和 Aspose.Cells.GridWeb 会出现在顶部窗格中。
- 选择它们并单击**选择**.
- Aspose.Cells.GridDesktop 和 Aspose.Cells.GridWeb 引用出现在项目的引用节点下。

如果您仅下载并解压缩 DLL：

- 使用浏览按钮找到 Aspose.Cells.GridDesktop.dll 和 Aspose.Cells.GridWeb.dll 文件。 Aspose.Cells Grid Suite 已被引用并且应该出现在**选定的组件**对话框的窗格。
- 点击**好的。**
## **卸载 Aspose.Cells for .NET**
如果您使用MSI安装程序部署Aspose.Cells for .NET，请按照以下步骤完全删除组件和控件，相关的演示和文档：

- 来自**开始**菜单，选择**设置**， 其次是**控制面板**.
- 点击**添加/删除程序**.
- 选择 Aspose.Cells for .NET（版本）。
- 点击**更改/删除**删除 Aspose.Cells。
