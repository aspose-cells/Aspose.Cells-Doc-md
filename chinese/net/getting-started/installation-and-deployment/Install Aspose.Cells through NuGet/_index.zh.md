---
title: 通过NuGet安装Aspose Cells
type: docs
weight: 30
url: /zh/net/installation/
---


## **通过NuGet安装Aspose.Cells for .NET**
NuGet是下载和安装Aspose API for .NET 的最简单方式。打开Microsoft Visual Studio和NuGet包管理器。搜索"aspose"以找到所需的Aspose API。单击"安装"，所选API将被下载并引用到您的项目中。

注意：您可以访问nuget网页，了解更多aspose.cells的信息： 
[Aspose.Cells for .NET NuGet包](https://www.nuget.org/packages/Aspose.Cells/)

### **使用包管理器GUI安装Aspose.Cells**
按照以下步骤使用包管理器GUI引用Aspose.Cells组件：

- 在Visual Studio中打开您的解决方案/项目。
- 单击 **工具** -> **库包管理器** -> 从解决方案中的 **管理 NuGet 包**。您也可以轻松通过解决方案资源管理器访问相同的选项。右键单击解决方案或项目，然后从上下文菜单中选择 **管理 NuGet 包**。
- 从左侧菜单中选择 **在线**，在搜索文本框中键入“Aspose.Cells”以查找Aspose.Cells .NET包。
- 点击Aspose.Cells for .NET条目旁边的**安装**按钮来将最新版本安装到您的项目中。
### **使用包管理器控制台安装 Aspose.Cells**
您可以按照以下步骤使用包管理器控制台引用Aspose.Cells组件：

- 在Visual Studio中打开您的解决方案/项目。
- 从菜单中选择 **工具** -> **库包管理器** -> **包管理器控制台** 打开包管理器控制台。
  - 输入命令“Install-Package Aspose.Cells”，然后按Enter键即可将最新完整版本安装到您的应用程序中。或者，您可以在命令中添加“-prerelease”后缀，以指定也要安装包含热修复的最新版本。
- 您将看到窗口左下角出现“正在下载Aspose.Cells…”提示，表明下载正在进行。
- 下载完成后，您将看到以下确认消息。如果您不熟悉Aspose EULA，则建议阅读URL中引用的许可协议。
- 您现在将发现Aspose.Cells已成功添加并在应用程序中引用。
## **从.NET项目引用Aspose.Cells**
要在应用程序中使用Aspose.Cells，需要引用它。在Visual Studio中添加引用：

1. 在 **解决方案资源管理器** 中，展开要添加引用的项目节点。
1. 右键单击项目的 **引用** 节点，然后从菜单中选择 **添加引用**。
1. 在 **添加引用** 对话框中，选择 .NET 选项卡（默认选中）。如果使用MSI安装程序安装，Aspose.Cells将显示在顶部窗格中。
1. 选择它，然后单击 **选择**。

如果您已下载或解压缩了仅DLL：

1. 使用 **浏览** 按钮定位Aspose.Cells.dll文件。Aspose.Cells应出现在对话框框的 **已选择组件** 窗格中。
1. 单击 **确定**。Aspose.Cells引用将出现在项目的 **引用** 节点下。
### **从VS.NET 2010 Client Profile项目中引用组件**
如果您的项目的目标框架是.NET Framework 3.5/4 Client Profile，请使用安装目录中net_ClientProfile文件夹中的Aspose.Cells.dll组件文件。例如：

- 在您的项目的VS.NET 2010 **解决方案资源管理器** 中，右键单击**引用**，然后选择**添加引用**。
- 在对话框中选择**浏览**选项卡，然后点击**查找**下拉菜单。
- 在安装目录中找到并选择Aspose.Cells.dll组件文件，例如：.../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(确保您在计算机上使用MSI安装程序安装了该产品。)**
- 单击**确定**关闭对话框。

{{% alert color="primary" %}} 

如果您的VS.NET 2010项目的目标框架是".NET Framework 4"或其他，请直接使用net4.0/net2.0文件夹中的Aspose.Cells.dll组件文件。

{{% /alert %}} 
## **从.NET项目引用Aspose.Cells网格控件**
要在应用程序中使用网格控件，请添加对其的引用。要在Visual Studio中引用网格控件，请执行以下操作：

- 在**解决方案资源管理器**中，展开要添加引用的项目节点。
- 对该项目的**引用**节点右键单击，然后从菜单中选择**添加引用**。
- 在**添加引用**对话框中，选择**.NET**选项卡（默认选中）。如果您使用MSI安装程序安装了Aspose.Cells for .NET，则Aspose.Cells.GridDesktop和Aspose.Cells.GridWeb将显示在顶部窗格中。
- 选择它们并点击**选择**。
- Aspose.Cells.GridDesktop和Aspose.Cells.GridWeb引用会出现在项目的**引用**节点下。

如果您只下载并解压缩了DLL：

- 使用浏览按钮找到Aspose.Cells.GridDesktop.dll和Aspose.Cells.GridWeb.dll文件。Aspose.Cells Grid套件已被引用，并应该出现在对话框框的**已选组件**窗格中。
- 单击**确定**。
## **卸载Aspose.Cells for .NET**
如果您使用MSI安装程序部署了Aspose.Cells for .NET，请按照以下步骤完全删除组件和控件、相关示例和文档：

- 从**开始**菜单中，选择**设置**，然后选择**控制面板**。
- 单击**添加/删除程序**。
- 选择Aspose.Cells for .NET（版本）。
- 单击**更改/删除**以移除 Aspose.Cells。
