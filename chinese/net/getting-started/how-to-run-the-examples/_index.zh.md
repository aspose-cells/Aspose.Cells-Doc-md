---
title: 如何运行示例
type: docs
weight: 140
url: /zh/net/how-to-run-the-examples/
---

## **软件要求**
请确保满足以下要求后再下载和运行示例。

1. Visual Studio 2015或更高版本
1. 在Visual Studio中安装NuGet包管理器。大多数情况下，它已经安装在Visual Studio 2015中。如需安装NuGet包管理器的详细信息，请参阅：[安装NuGet客户端工具](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1. 转到工具->选项->NuGet软件包管理器->软件包源，并确保选中**nuget.org**选项
1. 示例项目使用NuGet自动包还原功能，因此您应该有一个有效的互联网连接。如果在要执行示例的计算机上没有有效的互联网连接，请参阅[安装](/cells/zh/net/installation-and-deployment/)并在示例项目中手动添加对Aspose.Cells.dll的引用。
## **从 GitHub 下载**
Aspose.Cells for .NET的所有示例都托管在[GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET)上。
## **Aspose.Cells示例**
- 您可以使用您喜欢的GitHub客户端克隆存储库，也可以从[此处](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip)下载ZIP文件。
- 将 ZIP 文件的内容提取到计算机上的任何文件夹中。所有示例都位于 **Examples** 文件夹中。
- C#示例的Visual Studio解决方案文件即**Aspose.Cells.Examples.CSharp.sln**。
- 该项目是在Visual Studio 2015中创建和维护的。
- 在 Visual Studio 中打开解决方案文件并构建项目。
- 首次运行时，依赖项将通过NuGet自动下载。您也可以从[此处](https://downloads.aspose.com/cells/net)单独下载DLL。
- **示例**的根文件夹中包含C#示例使用的输入文件。您必须与示例项目一起下载**示例**文件夹。
- 打开**RunExamples.cs**，所有示例都在此处调用。
- 从项目内取消注释您想要运行的示例。
## **Aspose.Cells.GridDesktop示例**
- Aspose.Cells.GridDesktop示例也包含在[Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET)存储库中，并将作为从[此处](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip)下载的ZIP文件的一部分。
- 所有示例都位于**Examples_GridDesktop**文件夹中。
- 与Aspose.Cells示例类似，GridWeb示例的解决方案文件名为**Aspose.Cells.GridDesktop.Examples.CSharp.sln**。
- 在 Visual Studio 中打开解决方案文件并构建项目。
- 所有的依赖项都作为示例项目的一部分包含在其中。您也可以从[这里](https://downloads.aspose.com/cells/net)单独下载DLL。
- **Examples_GridDesktop**的根目录中的**Data**文件夹包含示例使用的输入文件。必须下载**Data**文件夹和示例项目。
- 打开并运行项目。
- 从表单中选择要运行的示例菜单中的示例。
## **Aspose.Cells.GridWeb示例**
- Aspose.Cells.GridWeb示例也包含在[Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET)存储库中，并将作为ZIP文件的一部分可从[这里](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip)下载。
- 所有的示例都位于**Examples_GridWeb**文件夹中。
- 与Aspose.Cells示例类似，GridWeb示例的解决方案文件名为**Aspose.Cells.GridWeb.Examples.CSharp.sln**。
- 在 Visual Studio 中打开解决方案文件并构建项目。
- 所有的依赖项都作为示例项目的一部分包含在其中。您也可以从[这里](https://downloads.aspose.com/cells/net)单独下载DLL。
- **Examples_GridWeb**的根文件夹中的**Data**文件夹包含示例使用的输入文件。必须下载**Data**文件夹和示例项目。
- 打开并运行示例项目中的**Examples.aspx**。
- 在项目中选择要在浏览器中运行的示例。
