---
title: 入门
type: docs
weight: 10
url: /zh/net/getting-started/
---
{{% alert color="primary" %}} 

本页将向您展示如何安装 Aspose Cells，并创建一个 Hello World 应用程序。

{{% /alert %}}

## **安装**

### **通过 NuGet 安装 Aspose.Cells**

NuGet 是下载和安装 Aspose.Cells for .NET 最简单的方法。

1. 打开 Microsoft Visual Studio 和 NuGet 包管理器。
1. 搜索“aspose.cells”找到所需的 Aspose.Cells for .NET。
1. 点击“安装”，Aspose.Cells for .NET会被下载并引用到你的项目中。
**![安装 Aspose Cells 到 NuGet](install-through-nuget.png)**

也可以从aspose.cells的nuget网页下载：
[Aspose.Cells for .NET NuGet 包](https://www.nuget.org/packages/Aspose.Cells/)

[详细步骤更多](/cells/zh/net/installation/)

### **在 Windows 上安装 Aspose.Cells**

1. 从以下页面下载 Aspose.Cells.msi：
[下载 Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. 双击 Aspose Cells msi 并按照说明进行安装：

**![在 Windows 上安装 Aspose Cells](install-on-windows.png)**

[详细步骤更多](/cells/zh/net/installing-aspose-cells-on-windows/)

### **在 linux 上安装 Aspose.Cells**

在这个例子中，我使用 Ubuntu 来展示如何在 linux 上开始使用 Aspose.Cells。

1. 创建一个名为“AsposeCellsTest”的 .netcore 应用程序。
2. 打开文件“AsposeCellsTest.csproj”，为 Aspose.Cells 包引用添加以下行：
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="22.12" />
  </ItemGroup>
{{< /highlight >}}
3.在Ubuntu上用VSCode打开项目：
**![在 linux 上安装 Aspose Cells](install-on-linux.png)**
4. 使用以下代码运行测试：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

注意：Aspose.Cells For .NetStandard 可以支持您在 linux 上的要求。

适用于：NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0及高级版本。

### **在 MAC OS 上安装 Aspose.Cells**

在此示例中，我使用 macOS High Sierra 来展示如何在 MAC OS 上开始使用 Aspose.Cells。

1. 创建一个名为“AsposeCellsTest”的 .netcore 应用程序。
2.用Visual Studio for Mac打开应用程序，然后安装Aspose Cells到NuGet：
**![在 macOS 上安装 Aspose Cells](install-on-mac-os.png)**
3. 使用以下代码运行测试：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4、如需使用绘图相关功能，请在macOS中安装libgdiplus，详见：
[如何在 macOS 中安装 libgdiplus](/cells/zh/net/how-to-install-libgdiplus-in-macos/)

注意：Aspose.Cells For .NetStandard 可以支持您在 MAC OS 上的要求。

适用于：NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0及高级版本。

### **[在 Docker 中运行 Aspose Cells](/cells/net/how-to-run-aspose-cells-in-docker/)**

### **如何在非windows平台上使用Net6图形库**

Aspose.Cells for Net6 现在使用 SkiaSharp 作为图形库，如中所推荐[Microsoft官方声明](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md).有关将 Aspose.Cells 与 NET6 一起使用的更多详细信息，请参阅[如何为 .Net6 运行 Aspose.Cells](/cells/zh/net/how-to-run-aspose-cells-for-net6/).

## **创建 Hello World 应用程序**

以下步骤使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 如果你有驾照，那么[应用它](/cells/zh/net/licensing/).
如果您使用的是评估版，请跳过与许可证相关的代码行。
1. 创建一个实例[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)类以创建新的 Excel 文件，或打开现有的 Excel 文件。
1. 访问 Excel 文件中工作表的任何所需单元格。
1. 插入单词**Hello World!**进入访问的单元格。
1. 生成修改后的 Microsoft Excel 文件。

下面的示例演示了上述步骤的实现。

### **代码示例：创建新工作簿**

下面的示例从头开始创建一个新工作簿，插入“Hello World!”到第一个工作表的单元格 A1 中并另存为 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **代码示例：打开现有文件**

以下示例打开一个现有的 Microsoft Excel 模板文件“Sample.xlsx”，插入“Hello World!”到第一个工作表的单元格 A1 中并另存为 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
