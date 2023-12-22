---
title: 入门
type: docs
weight: 10
url: /zh/net/getting-started/
---
{{% alert color="primary" %}} 

本页将向您展示如何安装 Aspose Cells，并创建 Hello World 应用程序。

{{% /alert %}}

##  **安装**

###  **安装 Aspose.Cells 至 NuGet**

 NuGet 是下载和安装 Aspose.Cells for .NET 的最简单方法。

1. 打开 Microsoft Visual Studio 和 NuGet 包管理器。
1. 搜索“aspose.cells”找到所需的Aspose.Cells for .NET。
1. 点击“安装”，Aspose.Cells for .NET将被下载并在您的项目中引用。
**![安装 Aspose Cells 到 NuGet](install-through-nuget.png)**

您还可以从 aspose.cells 的 nuget 网页下载：
[Aspose.Cells for .NET NuGet 封装](https://www.nuget.org/packages/Aspose.Cells/)

[更多步骤详情](/cells/zh/net/installation/)

###  **在Windows上安装Aspose.Cells**

1. 从以下页面下载 Aspose.Cells.msi：
[下载Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. 双击 Aspose Cells msi 并按照说明进行安装：

**![在 Windows 上安装 Aspose Cells](install-on-windows.png)**

[更多步骤详情](/cells/zh/net/installing-aspose-cells-on-windows/)

###  **在linux上安装Aspose.Cells**

在这个例子中，我使用Ubuntu来展示如何在Linux上开始使用Aspose.Cells。

1. 创建一个 .netcore 应用程序，命名为“AsposeCellsTest”。
2. 打开文件“AsposeCellsTest.csproj”，将以下行添加到其中以获取 Aspose.Cells 包引用：
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="23.12" />
  </ItemGroup>
{{< /highlight >}}
3.在Ubuntu上使用VSCode打开项目：
**![在linux上安装Aspose Cells](install-on-linux.png)**
4.使用以下代码运行测试：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

注意：Aspose.Cells For .NetStandard 可以支持您在 Linux 上的要求。

适用于：NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0及高级版本。

###  **在 MAC 操作系统上安装 Aspose.Cells**

在此示例中，我使用 macOS High Sierra 来演示如何开始在 MAC OS 上使用 Aspose.Cells。

1. 创建一个 .netcore 应用程序，命名为“AsposeCellsTest”。
2. 使用 Visual Studio for Mac 打开应用程序，然后安装 Aspose Cells 到 NuGet：
**![在 macOS 上安装 Aspose Cells](install-on-mac-os.png)**
3.使用以下代码运行测试：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4.如果需要使用绘图相关功能，请在macOS中安装libgdiplus，参见：
[如何在 macOS 中安装 libgdiplus](/cells/zh/net/how-to-install-libgdiplus-in-macos/)

注意：Aspose.Cells For .NetStandard 可以支持您对 MAC 操作系统的要求。

适用于：NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0及高级版本。

###  **[在 Docker 中运行 Aspose Cells](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **如何在Net6非windows平台上使用图形库**

Net6 的 Aspose.Cells 现在使用 SkiaSharp 作为图形库，如中推荐的[Microsoft官方声明](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md)。有关使用 Aspose.Cells 与 NET6 的更多详细信息，请参阅[如何为.Net6运行Aspose.Cells](/cells/zh/net/how-to-run-aspose-cells-for-net6/).

##  **创建 Hello World 应用程序**

以下步骤使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 如果你有执照的话[应用它](/cells/zh/net/licensing/).
如果您使用的是评估版本，请跳过与许可证相关的代码行。
1. 创建一个实例[练习册](https://reference.aspose.com/cells/net/aspose.cells/workbook)类来创建新的 Excel 文件，或打开现有的 Excel 文件。
1. 访问 Excel 文件中工作表的任何所需单元格。
1. 插入单词**Hello World!**进入一个访问的单元格。
1. 生成修改后的Microsoft Excel 文件。

下面的例子演示了上述步骤的实现。

###  **代码示例：创建新工作簿**

以下示例从头开始创建一个新工作簿，插入“Hello World！”到第一个工作表中的单元格 A1 中并另存为 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **代码示例：打开现有文件**

以下示例打开现有的 Microsoft Excel 模板文件“Sample.xlsx”，插入“Hello World！”到第一个工作表中的单元格 A1 中并另存为 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
