---
title: 示例运行方式
type: docs
weight: 140
url: /zh/net/how-to-run-the-examples/
---

## **软件要求**
在下载和运行示例之前，请确保满足以下要求。

1. Visual Studio 2015或更高版本
1. 在 Visual Studio 中安装 NuGet Package Manager。通常情况下，它已经安装在 Visual Studio 2015 中。有关如何安装 NuGet 包管理器的详细信息，请查看：[安装 NuGet 客户端工具](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1. 转到 工具->选项->NuGet 包管理器->包源，并确保选项 **nuget.org** 被选中
1. 示例项目使用了 NuGet 自动包恢复功能，因此您需要有一个活动的互联网连接。如果您在执行示例的计算机上没有活动的互联网连接，请查看 [安装](/cells/zh/net/installation-and-deployment/) 并在示例项目中手动添加对 Aspose.Cells.dll 的引用。
## **从 GitHub 下载**
Aspose.Cells for .NET 的所有示例都托管在 [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) 上。
## **Aspose.Cells 示例**
- 您可以使用您喜欢的 GitHub 客户端克隆存储库，或者从 [这里](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip) 下载 ZIP 文件。
- 将 ZIP 文件的内容提取到计算机上的任意文件夹中。所有示例都位于 **Examples** 文件夹中。
- C# 示例的 Visual Studio 解决方案文件是 **Aspose.Cells.Examples.CSharp.sln**。
- 该项目是在 Visual Studio 2015 中创建和维护的。
- 在 Visual Studio 中打开解决方案文件并构建项目。
- 首次运行时，依赖项将通过 NuGet 自动下载。您也可以从 [这里](https://downloads.aspose.com/cells/net) 分别下载 DLL。
- **Examples** 的根目录中的 **Data** 文件夹包含 CSharp 示例使用的输入文件。您必须下载 **Data** 文件夹以及示例项目。
- 打开 **RunExamples.cs**，所有示例都是从这里调用的。
- 在项目内取消注释您想要运行的示例。
## **Aspose.Cells.GridDesktop 示例**
- Aspose.Cells.GridDesktop 示例也包含在 [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) 存储库中，并且将作为从 [这里](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip) 下载的 ZIP 文件的一部分。
- 所有示例都位于 **Examples_GridDesktop** 文件夹中。
- 与 Aspose.Cells 示例类似，GridWeb 示例的解决方案文件名是 **Aspose.Cells.GridDesktop.Examples.CSharp.sln**。
- 在 Visual Studio 中打开解决方案文件并构建项目。
- 所有依赖项都包含在示例项目中。您也可以从 [这里](https://downloads.aspose.com/cells/net) 分别下载 DLL。
- **Examples_GridDesktop** 的根目录中的 **Data** 文件夹包含示例使用的输入文件。您必须下载 **Data** 文件夹以及示例项目。
- 打开并运行项目。
- 从表单中菜单中选择要运行的示例。
## **Aspose.Cells.GridWeb 示例**
- Aspose.Cells.GridWeb 示例也包含在 [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) 存储库中，并将作为可从 [此处](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip) 下载的 ZIP 文件的一部分。
- 所有示例位于 **Examples_GridWeb** 文件夹中。
- 与 Aspose.Cells 示例类似，GridWeb 示例解决方案文件名为 **Aspose.Cells.GridWeb.Examples.CSharp.sln**。
- 在 Visual Studio 中打开解决方案文件并构建项目。
- 所有依赖项都包含在示例项目中。你也可以从 [此处](https://downloads.aspose.com/cells/net) 分别下载 DLL。
- **Examples_GridWeb** 根文件夹中的 **Data** 文件夹包含示例使用的输入文件。你必须与示例项目一起下载 **Data** 文件夹。
- 打开并运行示例项目中的 **Examples.aspx**。
- 在浏览器中单击要从项目内运行的示例。
{{< app/cells/assistant language="csharp" >}}
