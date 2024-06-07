---
title: 开始入门
type: docs
weight: 10
url: /zh/cpp/getting-started/
description: 如何安装Aspose Cells for C++并创建一个Hello World应用程序。
---

{{% alert color="primary" %}} 

此页面将向您展示如何安装Aspose Cells for C++并创建一个Hello World应用程序。

{{% /alert %}}

## **安装**

### **通过 NuGet 安装 Aspose Cells**

NuGet是下载和安装Aspose.Cells for C++的最简单方式。 
1. 为C++创建一个Microsoft Visual Studio项目。
2. 包含头文件"Aspose.Cells.h"。
3. 打开Microsoft Visual Studio和NuGet包管理器。
4. 搜索"aspose.cells.cpp"以找到所需的Aspose.Cells for C++。 
5. 单击"安装"，Aspose.Cells for C++将被下载并引用到您的项目中。

**![通过NuGet安装Aspose Cells](InstallThroughNuget.png)**

您也可以从aspose.cells的NuGet网页进行下载： 
[Aspose.Cells for C++ NuGet包](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[详情请参见](/cells/zh/cpp/installation/)

### **在Windows上使用Aspose.Cells for C++的演示**

1. 从以下页面下载Aspose.Cells for C++:
[下载Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. 解压包，您会找到一个示例，展示了如何使用Aspose.Cells for C++。
3. 用Visual Studio 2017或更高版本打开example.sln
4. main.cpp: 此文件展示了如何编写代码以测试Aspose.Cells for C++

### **在Linux上使用Aspose.Cells for C++的演示**

1. 从以下页面下载Aspose.Cells for C++:
[下载Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. 解压包，您会找到一个示例，展示了如何在Linux上使用Aspose.Cells for C++。
3. 确保您在示例所在路径中。
4. 运行 "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. 运行 "cmake --build example/build"

### **在 Mac OS 上使用Aspose.Cells for C++ 的演示**

1. 从以下页面下载Aspose.Cells for C++:
[下载Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. 解压包，您会找到一个示例，展示了如何在MacOS上使用Aspose.Cells for C++。
3. 确保您在示例所在路径中。
4. 运行 "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. 运行 "cmake --build example/build"

## **创建Hello World应用程序**

以下步骤将使用Aspose.Cells API创建Hello World应用程序：

1. 创建[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的实例。
1. 如果您有许可证，则[应用它](/cells/zh/cpp/licensing/)。
   如果使用评估版，则跳过与许可相关的代码行.
1. 访问 Excel 文件中的工作表中任何所需单元格。
1. 将"**Hello World!**"这几个字插入到一个已访问的单元格中。
1. 生成修改后的 Microsoft Excel 文件。

上述步骤的实现在以下示例中进行展示。

### **代码示例: 创建新 Workbook**

以下示例从头开始创建一个新的工作簿，在第一个工作表的A1单元格插入"**Hello World!**"，并保存Excel文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **代码示例: 打开现有文件**

以下示例打开一个现有的Microsoft Excel模板文件，获取一个单元格并检查单元格A1中的值。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
