---
title: Aspose.Cells或NPOI
linktitle: 为什么不使用NPOI
description: "使用C#比NPOI更快、更方便地执行大量的Excel文件任务。"
type: docs
weight: 40
url: /zh/net/why-not-npoi
---

有时我们会遇到以下问题：为什么我们应该使用Aspose产品而不是NPOI？这个问题很容易回答：功能和功能。

NPOI（POI Java 项目的.NET版本）是一个开源项目，可以帮助您读取或写入Microsoft Office格式的文件。作为当前比较的一部分，请考虑以下NPOI组件 –  HSSF和XSSF：

** HSSF ** 是POI项目对Excel 97(-2007)文件格式的纯Java实现。

XSSF是POI项目的纯Java实现Excel 2007 OOXML(.xlsx)文件格式。

HSSF和XSSF提供了读取电子表格创建、修改、读取和写入XLS电子表格的方法。他们提供：

-专门需求的低级结构
-高效的只读访问的事件模型API
-用于创建、读取和修改XLS文件的完整用户模型API

HSSF 和 XSSF 均提供了基本文本提取、特定文本提取、访问页眉和页脚以及更改文本功能。虽然 HSSF 和 XSSF 提供了类似的功能，但它们目前没有共同的接口。它具有相当稳定的核心 API，可以读取或写入 .xlsx 文件的主要部分，但并不完整。

Aspose.Cells 是一个非常有用的文档处理库，对所有 Microsoft Excel 和其他文档格式提供了很好的支持。使用 Aspose.Cells，您可以在不使用 Microsoft Excel 的情况下读取、生成、修改、转换、渲染和打印文档。

本文将讨论何时使用 Aspose.Cells 最为合适。

## 为什么不使用 NPOI

值得注意的是，有些任务可以通过 Aspose.Cells 实现，但使用 NPOI 则无法完成。例如，如果您需要将 Excel 文件转换为 Pdf、JSON 和图像，则不能只使用 NPOI，您还需要 Microsoft Excel 365 或其他工具。

你可以比较NPOI和Aspose.Cells，为此，我们建议您熟悉Aspose.Cells for NPOI项目（HSSF和XSSF），它展示了使用Aspose.Cells for .NET API与NPOI执行不同任务的方法。该项目还涵盖了仅在Aspose.Cells中可用而不在NPOI中的用于处理文本文档的功能。

对于希望从 NPOI 迁移到 Aspose.Cells 的开发人员，此项目也非常有用。

{{% alert color="primary" %}}

探索[具有源代码示例的Aspose.Cells for .NET功能与NPOI对比的插件](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/NPOI)。

此插件使用 Aspose.Cells 的评估版本。如果您对评估结果满意，可以从 [Aspose 网站](https://purchase.aspose.com/buy) 购买许可证。要消除评估消息和功能限制，您必须应用产品许可证。购买产品后，您将收到一个许可证文件。请按照["许可和订阅"](/cells/zh/net/licensing/)文章中的说明操作。

{{% /alert %}}

在以下章节和文章中，我们将仔细研究Aspose.Cells提供的一些功能和能力。

### 稳定性

Aspose 组件经过充分测试。由于 Aspose 组件打包成一个单独的 DLL，因此永远不需要安装任何其他部件或部分才能使其正常工作。这不仅可以确保与 Aspose.Cells 的稳定工作，还能将意外情况的风险几乎降低到零。

### 可扩展性和速度

Aspose 组件具有高度的可扩展性和闪电般的速度。它们是真正的 .NET 解决方案，在单个服务器驱动单个应用程序或负载平衡 Web 农场驱动企业应用程序上，它们可以完美运行。

### 功能

Aspose 组件提供了管理办公文件所需的一切，还有很多更多。它们的设计理念是允许开发人员在最小的工作量下实现最大的结果。

Aspose 组件提供了许多强大的节省时间的功能。例如，[Aspose.Cells](https://products.aspose.com/cells/net/) 提供了一个允许开发人员将 JSON 导入到 Excel 文件中的功能。值得注意的是，Aspose 家族中的每个组件都提供了其独特而强大的功能集。

## 另请参阅

* [关于Apache POI的更多信息](https://poi.apache.org/)

