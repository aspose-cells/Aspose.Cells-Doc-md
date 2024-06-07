---
title: 通过NuGet安装Aspose Cells
type: docs
weight: 30
url: /zh/net/installation/
---


## **通过NuGet安装Aspose.Cells for .NET**
NuGet是下载和安装Aspose APIs for .NET的最简便方法。 打开Microsoft Visual Studio和NuGet包管理器。 搜索“aspose”以找到所需的Aspose API。 单击“安装”，所选API将被下载并引用到您的项目中。

备注： 您可以访问NuGet网页以获取关于Aspose.Cells的更多信息： 
[Aspose.Cells for .NET NuGet Package](https://www.nuget.org/packages/Aspose.Cells/)

### **使用包管理器GUI安装Aspose.Cells**
按照下面的步骤使用包管理器GUI引用Aspose.Cells组件：

-在Visual Studio中打开您的解决方案/项目。
-点击 **工具** -> **库包管理器** -> **管理NuGet包** 从解决方案中。 您还可以通过解决方案资源管理器轻松访问同样的选项。 右键单击解决方案或项目并从上下文菜单中选择**管理NuGet包**。
-从左侧菜单中选择**在线**，在搜索文本框中键入“Aspose.Cells”以找到Aspose.Cells .NET包。
-单击 Aspose.Cells for .NET 条目旁边的 **安装** 按钮，以将最新版本安装到您的项目中。
### **使用包管理器控制台安装Aspose.Cells**
您可以按照以下步骤使用包管理器控制台引用Aspose.Cells组件：

-在Visual Studio中打开您的解决方案/项目。
-在菜单中选择 **工具** -> **库包管理器** -> **包管理器控制台** 打开包管理器控制台。
  -键入命令“Install-Package Aspose.Cells”并按回车键将最新完整版本安装到应用程序中。 或者，您可以在命令中添加 “-prerelease” 后缀，以指定安装最新的包括热修复的版本。
-您将看到“正在下载Aspose.Cells...”提示出现在窗口左下角，表示下载正在进行中。
-下载完成后，您将看到以下确认消息。 如果您不熟悉Aspose EULA，则阅读URL中引用的许可证是一个好主意。
-现在您应该发现Aspose.Cells已成功添加并引用到您的应用程序中。
## **从.NET项目引用Aspose.Cells**
要在应用程序中使用Aspose.Cells，请添加对其的引用。 要使用Visual Studio添加引用：

1. 在 **解决方案资源管理器** 中展开要添加引用的项目节点。
1. 右键单击项目的 **引用** 节点，从菜单中选择 **添加引用**。
1. 在 **添加引用** 对话框中，选择.NET选项卡（默认选中）。 如果您使用MSI安装程序安装，Aspose.Cells将出现在顶部面板中。
1. 选择它，然后点击 **选择**。

如果您下载或解压了仅DLL文件：

1. 使用 **浏览** 按钮找到Aspose.Cells.dll文件。 Aspose.Cells应该出现在对话框框的 **已选择的组件** 面板中。
1. 单击 **确定**。 Aspose.Cells 引用出现在项目的 **引用** 节点下。
### **从 VS.NET 2010 客户端配置项目引用组件**
如果您的项目目标框架是.NET Framework 3.5/4客户端配置，请使用安装目录中 net_ClientProfile 文件夹中的 Aspose.Cells.dll 组件文件。 例如:

- 在 VS.NET 2010 的 **解决方案资源管理器** 中，右键单击您的项目的 **引用**，然后选择 **添加引用**。
- 在对话框中选择 **浏览** 选项卡，然后单击下拉菜单。
- 在您的安装目录中找到并选择 Aspose.Cells.dll 组件文件，例如: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(确保您在计算机上使用 MSI 安装程序安装了产品.)**
- 单击 **确定** 关闭对话框

{{% alert color="primary" %}} 

如果您的 VS.NET 2010 项目的目标框架是 ".NET Framework 4" 或其他，请直接使用位于 net4.0/net2.0 文件夹中的 Aspose.Cells.dll 组件文件。

{{% /alert %}} 
## **从.NET项目引用Aspose.Cells Grid控件**
在应用程序中使用网格控件，需添加引用。在Visual Studio中引用网格控件，请执行以下操作:

- 在 **解决方案资源管理器** 中，展开要添加引用的项目节点。
- 右键单击项目的 **引用** 节点，然后从菜单中选择 **添加引用**。
- 在 **添加引用** 对话框中，选择 **.NET** 选项卡（默认选中）。 如果您使用MSI安装程序安装了 Aspose.Cells for .NET，Aspose.Cells.GridDesktop 和 Aspose.Cells.GridWeb 将出现在上面板中。
- 选择它们，然后单击 **选择**。
- Aspose.Cells.GridDesktop和Aspose.Cells.GridWeb 引用将出现在项目的引用节点下。

如果您只下载和解压了DLL文件:

- 使用浏览按钮找到 Aspose.Cells.GridDesktop.dll 和 Aspose.Cells.GridWeb.dll 文件。 Aspose.Cells Grid Suite 已被引用，并应出现在对话框框的 **所选组件** 面板中。
- 单击 **确定**。
## **卸载 Aspose.Cells for .NET**
如果您使用MSI安装程序部署 Aspose.Cells for .NET，请按照以下步骤完全删除组件、控件、相关演示和文档:

- 从 **开始** 菜单中，选择 **设置**，然后选择 **控制面板**。
- 单击 **添加/删除程序**。
- 选择 Aspose.Cells for .NET (版本).
- 单击 **更改/删除** 以移除 Aspose.Cells。
