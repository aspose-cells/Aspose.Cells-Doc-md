---
title: 您的第一个 Aspose.Cells 申请 - Hello World
type: docs
weight: 30
url: /zh/net/your-first-aspose-cells-application-hello-world/
description: 使用 Aspose.Cells for .NET 以任何支持的格式创建、编辑和保存您的第一个 Excel 文件，体验 C# 的简单性和强大功能。
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
---
{{% alert color="primary" %}}

本教程演示如何使用 Aspose.Cells' simple API 创建第一个应用程序 (Hello World)。这个简单的应用程序创建一个 Microsoft Excel 文件，在指定的工作表单元格中包含文本“Hello World”。

{{% /alert %}}

##  **如何创建 Hello World 应用程序**

以下步骤使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 创建一个实例[练习册](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级。
1. 如果你有执照的话[应用它](/cells/zh/net/licensing/).
如果您使用的是评估版本，请跳过与许可证相关的代码行。
1. 创建新的 Excel 文件，或打开现有的 Excel 文件。
1. 访问 Excel 文件中工作表的任何所需单元格。
1. 插入单词**Hello World!**进入一个访问的单元格。
1. 生成修改后的Microsoft Excel 文件。

下面的例子演示了上述步骤的实现。

###  **如何创建新工作簿**

下面的示例从头开始创建一个新工作簿，写入 Hello World！到第一个工作表上的单元格 A1 中并保存 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **如何打开现有文件**

以下示例打开名为“Sample.xlsx”的现有 Microsoft Excel 模板文件，输入“Hello World!”将文本写入第一个工作表中的 A1 单元格并保存工作簿。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
