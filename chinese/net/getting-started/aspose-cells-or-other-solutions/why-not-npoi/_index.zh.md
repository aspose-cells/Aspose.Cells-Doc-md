---
title: Aspose.Cells 或 NPOI
linktitle: 为什么不NPOI
description: 使用 C# 使用 Excel 文件比使用 NPOI 更快更方便地执行大量任务
type: docs
weight: 40
url: /zh/net/why-not-npoi
---
有时我们会遇到以下问题：为什么我们应该使用 Aspose 产品而不是 NPOI？这个问题很容易回答：特性和功能。

NPOI（POI Java项目的NET版本）是一个开源项目，可以帮助你读写Microsoft Office格式的文件。作为当前比较的一部分，请考虑以下 NPOI 组件——HSSF 和 XSSF：

**高速钢**是 POI 项目的 Excel 97(-2007) 文件格式的纯 Java 实现。

**XSSF**是 POI 项目的 Excel 2007 OOXML (.xlsx) 文件格式的纯 Java 实现。

HSSF 和 XSSF 提供了读取电子表格的方法创建、修改、读取和写入 XLS 电子表格。他们提供：

- 为有特殊需要的人提供的低层结构
- 用于高效只读访问的事件模型 API
- 用于创建、读取和修改 XLS 文件的完整用户模型 API

HSSF 和 XSSF 都提供基础文本提取、特定文本提取、页眉和页脚访问以及更改文本功能。虽然 HSSF 和 XSSF 提供类似的功能，但它们目前没有通用接口。它有一个相当稳定的核心 API，提供对 .xlsx 文件主要部分的读或写访问，但它并不完整。

Aspose.Cells是一个非常好用的文档处理库，对所有Microsoft Excel等文档格式提供了很好的支持。使用 Aspose.Cells，您可以在不使用 Microsoft Excel 的情况下读取、生成、修改、转换、呈现和打印文档。

在本文中，我们将了解您何时更喜欢 Aspose.Cells。

## 为什么不NPOI

值得注意的是，有些任务可以用Aspose.Cells完成，但不能用NPOI完成。比如你需要将Excel文件转成Pdf，JSON和图片，那么你不能只使用NPOI，还需要Microsoft Excel 365或者其他工具。

您可以将 NPOI 与 Aspose.Cells 进行比较为此，我们建议您熟悉 NPOI 项目（HSSF 和 XSSF）的 Aspose.Cells——它展示了使用 Aspose.Cells for .NET API 与 NPOI 相比如何完成不同的任务。该项目还涵盖了处理文本文档的功能，这些功能仅在 Aspose.Cells 中可用，但在 NPOI 中不可用。

该项目对于希望从 NPOI 迁移到 Aspose.Cells 的开发人员也很有用。

{{% alert color="primary" %}}

探索[Aspose.Cells for .NET 源码示例插件与NPOI功能对比](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/NPOI).

本插件使用的是Aspose.Cells的评估版，如果您对自己的评估感到满意，可以从[Aspose网站](https://purchase.aspose.com/buy).要删除评估消息和功能限制，您必须申请产品许可证。购买产品后，您将收到一个许可证文件。请按照说明中的说明[“许可和订阅”](/cells/zh/net/licensing/)文章来做到这一点。

{{% /alert %}}

在接下来的章节和文章中，我们将仔细研究 Aspose.Cells 提供的一些特性和能力。

### 稳定

Aspose 组件经过全面测试。由于 Aspose 组件被打包到一个单独的 DLL 中，因此永远不需要安装任何额外的部件或组件来运行它们。这不仅可以提供与 Aspose.Cells 的稳定工作，还可以将不可预见情况的风险降低到几乎为零。

### 可扩展性和速度

Aspose 组件具有高度可扩展性和闪电般的速度。它们是真正的 .NET 解决方案，可以在为单个应用程序提供支持的单个服务器或为企业应用程序提供支持的负载平衡网络场上完美运行。

### 特征

Aspose 组件提供了管理 Office 文件所需的一切，以及更多其他功能。它们的设计理念是让开发人员以最少的工作量取得最大的成果。

Aspose 组件提供许多强大的省时功能。例如，[Aspose.Cells](https://products.aspose.com/cells/net/)提供允许开发人员将 JSON 导入 Excel 文件的功能。值得注意的是，Aspose 系列中的每个组件都提供了自己的一套独特而强大的功能。

## 也可以看看

[更多关于 Apache POI 的信息](https://poi.apache.org/)

