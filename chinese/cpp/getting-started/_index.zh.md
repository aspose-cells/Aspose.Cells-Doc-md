---
title: 入门
type: docs
weight: 10
url: /zh/cpp/getting-started/
description: 如何安装 Aspose Cells for C++ 并创建 Hello World 应用程序。
---
{{% alert color="primary" %}} 

此页面将向您展示如何安装 Aspose Cells for C++ 和创建 Hello World 应用程序。

{{% /alert %}}

## **安装**

### **安装 Aspose Cells 到 NuGet**

NuGet 是下载和安装 Aspose.Cells for C++ 最简单的方法。
1. 创建一个 Microsoft Visual Studio 项目 for C++。
2. 包含头文件“Aspose.Cells.h”。
3. 打开 Microsoft Visual Studio 和 NuGet 包管理器。
 4.搜索“aspose.cells.cpp”找到需要的Aspose.Cells for C++。
5.点击“安装”，Aspose.Cells for C++会被下载并引用到你的项目中。

**![通过 NuGet 安装 Aspose Cells](InstallThroughNuget.png)**

也可以从aspose.cells的nuget网页下载：
[Aspose.Cells for C++ NuGet 包](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[详细步骤更多](/cells/zh/cpp/installation/)

### **在 Windows 上使用 Aspose.Cells for C++ 的演示**

1. 从以下页面下载 Aspose.Cells for C++：
[下载 Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2.解压压缩包，你会发现一个Demo是如何使用Aspose.Cells for C++。
3.用Visual Studio 2017或更高版本打开Demo.sln
4. main.cpp：这个文件展示了如何编写代码来测试 Aspose.Cells for C++
 5. sourceFile/resultFile：这两个文件夹是main.cpp中使用的存放目录

### **如何在 Linux 操作系统上使用 Aspose.Cells for C++**

1. 从以下页面下载 Aspose.Cells for C++：
[下载 Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2.解压压缩包，你会发现一个Demo，是关于如何使用Aspose.Cells for C++ for Linux的。
3. 在 Linux 命令行中运行“cd Demo”
4. 运行“rm -rf build;mkdir build;cd build”
5.运行“cmake ..”将在Demo文件夹中通过CMakeLists.txt创建一个Makefile
6.运行“make”编译
7.运行“./demo”你会看到结果

## **创建 Hello World 应用程序**

以下步骤使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 创建一个实例[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)班级。
1. 如果你有驾照，那么[应用它](/cells/zh/cpp/licensing/).
如果您使用的是评估版，请跳过与许可证相关的代码行。
1. 访问 Excel 文件中工作表的任何所需单元格。
1. 插入单词“**Hello World!**" 进入访问的单元格。
1. 生成修改后的 Microsoft Excel 文件。

下面的示例演示了上述步骤的实现。

### **代码示例：创建新工作簿**

以下示例从头开始创建一个新工作簿，插入“**Hello World!**" 到第一个工作表的单元格 A1 中并保存 Excel 文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **代码示例：打开现有文件**

下面的示例打开一个现有的 Microsoft Excel 模板文件，获取一个单元格并检查单元格 A1 中的值。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
