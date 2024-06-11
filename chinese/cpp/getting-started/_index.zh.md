---
title: 入门
type: docs
weight: 10
url: /zh/cpp/getting-started/
description: 如何安装Aspose Cells for C++并创建一个Hello World应用程序。
---

{{% alert color="primary" %}} 

此页面将向您展示如何安装Aspose Cells for C++并创建一个Hello World应用程序。

{{% /alert %}}

## **安装**

### **通过NuGet安装Aspose Cells**

NuGet是最简单的下载和安装Aspose.Cells for C++ 的方法。 
1. 为C++创建一个Microsoft Visual Studio项目。
2. 包含头文件 "Aspose.Cells.h"。
3. 打开Microsoft Visual Studio和NuGet包管理器。
4. 搜索 "aspose.cells.cpp" ，找到所需的Aspose.Cells for C++。 
5. 点击 "安装"，Aspose.Cells for C++ 将被下载并引用到您的项目中。

**![通过NuGet安装Aspose Cells](InstallThroughNuget.png)**

您也可以从nuget网页上为aspose.cells下载它： 
[Aspose.Cells for C++ NuGet包](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[更多详细步骤](/cells/zh/cpp/installation/)

### **在Windows上使用Aspose.Cells for C++的演示**

1. 从以下页面下载Aspose.Cells for C++。
[下载Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. 解压包，找到一个示例说明如何使用Aspose.Cells for C++。
3. 使用Visual Studio 2017或更高版本打开example.sln文件。
4. main.cpp文件展示如何编写代码来测试Aspose.Cells for C++。

### **在Linux上使用Aspose.Cells for C++的演示**

1. 从以下页面下载Aspose.Cells for C++。
[下载Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. 解压包，找到一个示例说明如何在Linux下使用Aspose.Cells for C++。
3. 确保你位于example所在的路径。
4. 运行"cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. 运行"cmake --build example/build"

### **在Mac OS上使用Aspose.Cells for C++的演示**

1. 从以下页面下载Aspose.Cells for C++。
[下载Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. 解压包，找到一个示例说明如何在MacOS下使用Aspose.Cells for C++。
3. 确保你位于example所在的路径。
4. 运行"cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. 运行"cmake --build example/build"

## **创建Hello World应用程序**

以下步骤使用 Aspose.Cells API 创建了 Hello World 应用程序：

1. 创建[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的实例。
1. 如果您有许可证，那么[申请它](/cells/zh/cpp/licensing/)。
   如果您使用的是评估版，则跳过与许可证相关的代码行。
1. 访问Excel文件的工作表中的任意单元格。
1. 将“**Hello World!**”插入到所访问的单元格中。
1. 生成修改后的Microsoft Excel文件。

上述步骤的实现在下面的示例中进行了演示。

### **代码示例：创建新工作簿**

以下示例从头开始创建一个新的工作簿，在第一个工作表的单元格A1中插入“**Hello World!**”，并保存Excel文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **代码示例：打开现有文件**

以下示例打开现有的Microsoft Excel模板文件，获取一个单元格，并检查单元格A1中的值。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
