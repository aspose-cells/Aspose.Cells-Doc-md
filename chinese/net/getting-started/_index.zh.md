---
title: 入门
type: docs
weight: 10
url: /zh/net/getting-started/
---

{{% alert color="primary" %}} 

此页面将向您展示如何安装Aspose Cells，并创建一个简单的Hello World应用程序。

{{% /alert %}}

## **安装**

### **通过NuGet安装Aspose.Cells**

NuGet是下载和安装Aspose.Cells for .NET最简单的方式。 

1. 打开Microsoft Visual Studio和NuGet软件包管理器。 
1. 搜索"aspose.cells"来找到所需的Aspose.Cells for .NET。 
1. 点击"安装"，Aspose.Cells for .NET将被下载并引用到您的项目中。
**![通过NuGet安装Aspose Cells](install-through-nuget.png)**

您也可以从nuget网页上为aspose.cells下载它： 
[Aspose.Cells for .NET NuGet包](https://www.nuget.org/packages/Aspose.Cells/)

[更多详细步骤](/cells/zh/net/installation/)

### **在Windows上安装Aspose.Cells**

1. 从以下页面下载Aspose.Cells.msi：
[下载Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. 双击Aspose Cells msi并按照指示进行安装：

**![在Windows上安装Aspose Cells](install-on-windows.png)**

[更多详细步骤](/cells/zh/net/installing-aspose-cells-on-windows/)

### **在 Linux 安装 Aspose.Cells**

在这个示例中，我使用 Ubuntu 操作系统来展示如何在 Linux 上开始使用 Aspose.Cells。

1. 创建一个 .netcore 应用程序，名为 "AsposeCellsTest"。
2. 打开文件 "AsposeCellsTest.csproj" ，并添加以下行用于引用 Aspose.Cells 包:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. 使用 VSCode 在 Ubuntu 上打开项目:
**![在 Linux 上安装 Aspose Cells](install-on-linux.png)**
4. 使用以下代码运行测试:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

注意：Aspose.Cells For .NetStandard 能够支持您在 Linux 上的需求。

适用于: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 及更高版本。

### **在 MAC OS 上安装 Aspose.Cells**

在这个示例中，我使用 macOS High Sierra 操作系统来展示如何在 MAC OS 上开始使用 Aspose.Cells。

1. 创建一个 .netcore 应用程序，名为 "AsposeCellsTest"。
2. 用 Visual Studio for Mac 打开应用程序，然后通过 NuGet 安装 Aspose Cells:
**![在 macOS 上安装 Aspose Cells](install-on-mac-os.png)**
3. 使用以下代码运行测试:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. 如果您需要使用与绘图相关的功能，请在 macOS 中安装 libgdiplus，请参阅:
[如何在 macOS 上安装 libgdiplus](/cells/zh/net/how-to-install-libgdiplus-in-macos/)

注意：Aspose.Cells For .NetStandard 能够支持您在 MAC OS 上的需求。

适用于: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 及更高版本。

### [**Run Aspose Cells in Docker**](/cells/zh/net/how-to-run-aspose-cells-in-docker/)

### **如何在使用Net6的非Windows平台上使用图形库**

Aspose.Cells for Net6现在使用SkiaSharp作为图形库，如微软官方声明中所推荐的。有关在NET6中使用Aspose.Cells的更多详情，请参阅[如何运行Aspose.Cells for .Net6](/cells/zh/net/how-to-run-aspose-cells-for-net6/)。

## **创建Hello World应用程序**

以下步骤使用 Aspose.Cells API 创建了 Hello World 应用程序：

1. 如果您有许可证，则[应用它](/cells/zh/net/licensing/)。
   如果您使用的是评估版，则跳过与许可证相关的代码行。
1. 创建[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的实例以创建新的Excel文件，或者打开现有的Excel文件。
1. 访问Excel文件的工作表中的任意单元格。
1. 在访问的单元格中插入单词**Hello World!**。
1. 生成修改后的Microsoft Excel文件。

上述步骤的实现在下面的示例中进行了演示。

### **代码示例：创建新工作簿**

以下示例从头开始创建一个新工作簿，在第一个工作表的A1单元格中插入"Hello World!"，并另存为Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **代码示例：打开现有文件**

以下示例打开现有的Microsoft Excel模板文件"Sample.xlsx"，在第一个工作表的A1单元格中插入"Hello World!"，并另存为Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
