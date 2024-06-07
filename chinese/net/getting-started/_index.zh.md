---
title: 开始入门
type: docs
weight: 10
url: /zh/net/getting-started/
---

{{% alert color="primary" %}} 

此页面将向您展示如何安装Aspose Cells并创建一个Hello World应用程序。

{{% /alert %}}

## **安装**

### **通过NuGet安装Aspose.Cells**

NuGet是下载和安装Aspose.Cells for .NET的最简单方式。 

1. 打开Microsoft Visual Studio和NuGet包管理器。 
1. 搜索"aspose.cells"以找到所需的Aspose.Cells for .NET。 
1. 点击"安装"，Aspose.Cells for .NET将被下载并引用到您的项目中。
**![通过NuGet安装Aspose Cells](install-through-nuget.png)**

您也可以从aspose.cells的NuGet网页进行下载： 
[Aspose.Cells for .NET NuGet Package](https://www.nuget.org/packages/Aspose.Cells/)

[更多步骤详情](/cells/zh/net/installation/)

### **在Windows上安装Aspose.Cells**

1. 从以下页面下载Aspose.Cells.msi：
[下载Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. 双击Aspose Cells msi并按照说明进行安装：

**![在Windows上安装Aspose Cells](install-on-windows.png)**

[更多步骤详情](/cells/zh/net/installing-aspose-cells-on-windows/)

### **在Linux上安装Aspose.Cells**

在本示例中，我使用Ubuntu来展示如何在Linux上开始使用Aspose.Cells。

1. 创建一个 .netcore 应用程序，命名为"AsposeCellsTest"。
2. 打开文件"AsposeCellsTest.csproj"，添加以下内容以引用Aspose.Cells包：
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="24.5" />
  </ItemGroup>
{{< /highlight >}}
3. 在Ubuntu上使用VSCode打开项目：
**![在Linux上安装Aspose Cells](install-on-linux.png)**
4. 使用以下代码运行测试:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

注意: Aspose.Cells For .NetStandard 可以在 Linux 上支持您的需求。

适用于: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 和高级版本。

### **在 MAC OS 上安装 Aspose.Cells**

在这个示例中，我使用 macOS High Sierra 来展示如何在 MAC OS 上开始使用 Aspose.Cells。

1. 创建一个 .netcore 应用程序，命名为"AsposeCellsTest"。
2. 使用 Visual Studio for Mac 打开应用程序，然后通过 NuGet 安装 Aspose Cells:
**![在 macOS 上安装 Aspose Cells](install-on-mac-os.png)**
3. 使用以下代码运行测试:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. 如果您需要使用与绘图相关的功能，请在 macOS 上安装 libgdiplus，请参阅:
[如何在 macOS 上安装 libgdiplus](/cells/zh/net/how-to-install-libgdiplus-in-macos/)

注意: Aspose.Cells For .NetStandard 可以支持您在 MAC OS 上的需求。

适用于: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 和高级版本。

### **[在 Docker 中运行 Aspose Cells](/cells/zh/net/how-to-run-aspose-cells-in-docker/)**

### **如何在非 Windows 平台上使用 Net6 的图形库**

现在 Aspose.Cells for Net6 使用 SkiaSharp 作为图形库，符合微软的[官方声明](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md)。有关在 NET6 中使用 Aspose.Cells 的更多详细信息，请参阅[How to Run Aspose.Cells for .Net6](/cells/zh/net/how-to-run-aspose-cells-for-net6/)。

## **创建Hello World应用程序**

以下步骤将使用Aspose.Cells API创建Hello World应用程序：

1. 如果您有许可证，那么请[申请许可证](/cells/zh/net/licensing/)。
   如果使用评估版，则跳过与许可相关的代码行.
1. 创建 [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的实例以创建新的 Excel 文件，或打开现有的 Excel 文件。
1. 访问 Excel 文件中的工作表中任何所需单元格。
1. 将 **Hello World!** 插入到所访问的单元格中。
1. 生成修改后的 Microsoft Excel 文件。

上述步骤的实现在以下示例中进行展示。

### **代码示例: 创建新 Workbook**

以下示例从头创建一个新工作簿，在第一个工作表的单元格A1中插入"Hello World!"，然后保存为 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **代码示例: 打开现有文件**

以下示例打开一个现有的 Microsoft Excel 模板文件"Sample.xlsx"，在第一个工作表的单元格A1中插入"Hello World!"，然后保存为 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
