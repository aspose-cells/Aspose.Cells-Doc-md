---
title: 入门
type: docs
weight: 10
url: /zh/cpp/getting-started/
description: 如何安装 Aspose Cells for C++ 并创建 Hello World 应用程序。
---
{{% alert color="primary" %}} 

本页将向您展示如何安装 Aspose Cells for C++ 并创建 Hello World 应用程序。

{{% /alert %}}

##  **安装**

###  **安装 Aspose Cells 至 NuGet**

 NuGet 是下载和安装 Aspose.Cells for C++ 的最简单方法。
1. 创建 Microsoft Visual Studio 项目 for C++。
2. 包含头文件“Aspose.Cells.h”。
3.打开Microsoft Visual Studio和NuGet包管理器。
 4.搜索“aspose.cells.cpp”找到所需的Aspose.Cells for C++。
5. 点击“安装”，Aspose.Cells for C++将被下载并在您的项目中引用。

**![安装 Aspose Cells 至 NuGet](InstallThroughNuget.png)**

您还可以从 aspose.cells 的 nuget 网页下载：
[Aspose.Cells for C++ NuGet 封装](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[更多步骤详情](/cells/zh/cpp/installation/)

###  **在 Windows 上使用 Aspose.Cells for C++ 的演示**

1. 从以下页面下载 Aspose.Cells for C++：
[下载 Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. 解压压缩包，您将看到一个关于如何使用 Aspose.Cells for C++ 的示例。
3.使用Visual Studio 2017或更高版本打开example.sln
4. main.cpp：该文件显示了如何编写代码来测试Aspose.Cells for C++

###  **在Linux上使用Aspose.Cells for C++的演示**

1. 从以下页面下载 Aspose.Cells for C++：
[下载 Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. 解压压缩包，您将看到一个关于如何在 Linux 上使用 Aspose.Cells for C++ 的示例。
3. 确保您位于示例所在的路径中。
4.运行“cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release”
5.运行“cmake --build example/build”

###  **在 Mac OS 上使用 Aspose.Cells for C++ 的演示**

1. 从以下页面下载 Aspose.Cells for C++：
[下载 Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. 解压压缩包，您将看到一个关于如何在 MacOS 上使用 Aspose.Cells for C++ 的示例。
3. 确保您位于示例所在的路径中。
4.运行“cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release”
5.运行“cmake --build example/build”

##  **创建 Hello World 应用程序**

以下步骤使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 创建一个实例[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)班级。
1. 如果你有执照的话[应用它](/cells/zh/cpp/licensing/).
如果您使用的是评估版本，请跳过与许可证相关的代码行。
1. 访问 Excel 文件中工作表的任何所需单元格。
1. 将单词“**Hello World！**”插入访问的单元格中。
1. 生成修改后的Microsoft Excel 文件。

下面的例子演示了上述步骤的实现。

###  **代码示例：创建新工作簿**

以下示例从头开始创建一个新工作簿，将“**Hello World!**”插入到第一个工作表的单元格 A1 中，并保存 Excel 文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **代码示例：打开现有文件**

以下示例打开现有的 Microsoft Excel 模板文件，获取一个单元格并检查单元格 A1 中的值。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
