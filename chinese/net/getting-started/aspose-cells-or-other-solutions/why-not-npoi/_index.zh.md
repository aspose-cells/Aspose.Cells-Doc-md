---
title: Aspose.Cells 或 NPOI
linktitle: 为什么不用NPOI
description: “使用 C# 比 NPOI 更快更方便地执行大量 Excel 文件任务。”
type: docs
weight: 40
url: /zh/net/why-not-npoi
---

有时我们会收到以下问题：为什么我们应该使用Aspose产品而不是NPOI？这个问题很容易回答：功能和功能。

NPOI（POI Java 项目的 .NET 版本）是一个开源项目，可以帮助您读取或写入 Microsoft Office 格式的文件。作为当前比较的一部分，请考虑以下 NPOI 组件 - HSSF 和 XSSF：

**HSSF** 是 POI 项目对 Excel 97(-2007) 文件格式的纯 Java 实现。

**XSSF** 是 POI 项目对 Excel 2007 OOXML（.xlsx）文件格式的纯 Java 实现。

HSSF 和 XSSF 提供了读取电子表格、创建、修改、读取和写入 XLS 电子表格的方法。它们提供：

- 专为有特殊需求的人员提供低级结构
- 为高效的只读访问提供事件模型 API
- 为创建、读取和修改 XLS 文件提供完整的用户模型 API

HSSF 和 XSSF 提供基础文本提取、特定文本提取、访问页眉和页脚、更改文本功能。虽然 HSSF 和 XSSF 提供了类似的功能，但它们目前并没有共同的接口。它具有相对稳定的核心 API，可提供对 .xlsx 文件主要部分的读取或写入访问权限，但尚不完整。

Aspose.Cells 是一个非常有用的文档处理库，为所有 Microsoft Excel 和其他文档格式提供了强大的支持。使用 Aspose.Cells，您可以在不使用 Microsoft Excel 的情况下读取、生成、修改、转换、渲染和打印文档。

在本文中，我们将看看何时您更喜欢使用 Aspose.Cells。

## 为什么不选择NPOI

值得注意的是，某些任务可以使用 Aspose.Cells 完成，但无法用 NPOI 完成。例如，如果您需要将 Excel 文件转换为 Pdf、JSON 和图像，则不能仅使用 NPOI，还需要 Microsoft Excel 365 或其他工具。

您可以将 NPOI 与 Aspose.Cells 进行比较。为此，我们建议您了解 Aspose.Cells for NPOI 项目（HSSF 和 XSSF）- 它展示了如何使用 Aspose.Cells for .NET API 与 NPOI 完成不同任务。该项目还涵盖了仅在 Aspose.Cells 中可用而不在 NPOI 中的文本文档处理功能。

该项目对于希望从 NPOI 迁移到 Aspose.Cells 的开发人员也非常有用。

{{% alert color="primary" %}}

探索 [Aspose.Cells for .NET 功能与 NPOI 对比的插件及源代码示例](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/NPOI)。

该插件使用Aspose.Cells的评估版本。在您满意评估后，您可以从[Aspose网站](https://purchase.aspose.com/buy)购买许可证。要删除评估消息和功能限制，您必须应用产品许可证。购买产品后，您将收到一个许可证文件。请按照["许可和订阅"](/cells/zh/net/licensing/)文章中的说明进行操作。

{{% /alert %}}

在接下来的章节和文章中，我们将更仔细地研究 Aspose.Cells 提供的一些功能和能力。

### 稳定性

Aspose 组件经过彻底测试。由于 Aspose 组件打包成单个 DLL，因此永远不需要安装任何其他部件或元件才能使它们正常工作。这不仅可以提供与 Aspose.Cells 的稳定工作，而且可以将不可预见的情况风险几乎降至零。

### 可伸缩性和速度

Aspose组件具有高度可伸缩性和闪电般的速度。它们是真正的.NET解决方案，并可以在单个服务器上运行单个应用程序，也可以在负载平衡的Web服务器集群上运行企业应用程序时无缺地运行。

### 特点

Aspose组件提供了处理办公文件所需的一切，以及更多。它们旨在让开发人员以最少的工作量实现最佳结果。

Aspose组件提供了许多强大的省时功能。例如，[Aspose.Cells](https://products.aspose.com/cells/net/)提供了一个功能，允许开发人员将JSON导入到Excel文件中。值得注意的是，Aspose系列中的每个组件都提供了其独有和强大的功能。

## 请参阅

* [关于Apache POI的更多信息](https://poi.apache.org/)

