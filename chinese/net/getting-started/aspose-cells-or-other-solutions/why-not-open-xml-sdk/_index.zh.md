---
title: 为什么不使用 Open XML SDK
type: docs
weight: 90
url: /zh/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

我们有时会听到这样的问题：

**为何我们应该使用 Aspose 产品而不是免费的 Open XML SDK？**

这个问题很容易回答: 功能和功能。

{{% /alert %}}

## **什么是Open XML SDK？**

根据[MSDN图书馆](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN)，Open XML SDK被定义为:

"Open XML SDK 2.5简化了操作Open XML包和包内基础Open XML模式元素的任务。Open XML SDK 2.5封装了开发人员在Open XML包上执行的许多常见任务，因此您只需一些代码行就可以执行复杂操作."

OOXML文档本质上是压缩的XML文件，Open XML SDK是一个类集合，允许您以强类型方式处理OOXML文档的内容。即不是解压文件以提取XML，加载XML到DOM树并直接处理XML元素和属性，而是Open XML SDK提供了类来完成这些操作。

## **什么是Aspose.Cells？**

Aspose.Cells是一个类库，允许应用程序执行以下电子表格处理任务:

- 在所有流行的Microsoft Excel格式之间进行高质量转换，包括转换为PDF、HTML、TIFF和打印。
- 使用工作簿对象模型进行编程。
- 能够根据风格格式、图表和图形自动合并数据，从一个或多个文档的片段构建文档。
- 高级功能，例如从不同数据源（包括数组、ArrayList、DataTable / ResultSet）导入数据。
- 支持几乎所有标准和高级Microsoft Excel函数的强大的公式计算引擎。

## **比较Open XML SDK和Aspose.Cells**

以下表格比较了Open XML SDK和Aspose.Cells的特点。

|特性或特性类别|Open XML SDK|Aspose.Cells|
| :- | :- | :- |
|支持的Excel或其他格式|XLSX|XLS、CSV、SpreadsheetML 2003、XLSX、HTML、Tab Delimited、ODS、纯文本（TXT）、PDF、XPS|
|在Excel格式之间转换|否|是|
|使用工作簿对象模型进行高级编程：<br>- 查找和替换。<br>- 组装电子表格。<br>- 在工作簿之间复制文档片段和工作表。|否|是|
|使用文档对象模型进行详细编程，访问所有电子表格元素的单独元素和格式属性。|是|是|
|直接全面访问底层XML元素和属性（如关系标识符、OOXML文档的列表标识符）。|是|否|
|<p>生成报告，用数据填充文档：</p><p>- 将数据导入/导出至 DataTable / ResultSet。</p><p>- 智能标记功能。</p><p>- 插入/删除行/列/范围。</p><p>- 自定义数据源。</p>|否|是|
|<p>渲染和打印：* 将工作表页面渲染为光栅图像（TIFF，多页 TIFF，PNG，JPEG，BMP）。* 将电子表格页面渲染为矢量图像（EMF）。</p><p>- 将图表转换为图像（TIFF，多页 TIFF，PNG，JPEG，BMP，EMF 等）。</p><p>- 指定图像分辨率、质量、压缩以及其他选项。</p><p>- 使用.NET打印基础结构打印电子表格。该组件具有内置的打印方法，用于打印 Microsoft Excel 打印预览中显示的工作表。</p>|否|是|
|动态计算/重新计算公式|否|是|
|支持的平台|Windows、.NET|Windows、Linux、Java、.NET、Mono|

您可以将OpenXML与Aspose.Cells进行比较。为此，我们建议您熟悉Aspose.Cells for OpenXML项目-该项目展示了如何使用Aspose.Cells for .NET API与OpenXML执行不同任务。该项目还涵盖了仅在Aspose.Cells中可用而不在OpenXML中的文档处理功能。

此项目还对于希望从 OpenXML 迁移到 Aspose.Cells 的开发人员非常有用。

{{% alert color="primary" %}}

探索[与OpenXML进行比较的Aspose.Cells for .NET功能的插件和源代码示例](https://github.com/asposemarketplace/Aspose_for_OpenXML)。

此插件使用 Aspose.Cells 的评估版本。如果您对评估结果满意，可以从 [Aspose 网站](https://purchase.aspose.com/buy) 购买许可证。要消除评估消息和功能限制，您必须应用产品许可证。购买产品后，您将收到一个许可证文件。请按照["许可和订阅"](/cells/zh/net/licensing/)文章中的说明操作。

{{% /alert %}}

**结论**：Open XML SDK 和 Aspose.Cells 并不是直接竞争，因为它们满足了完全不同的需求和受众。

## **OpenXML 不是一个很好的选择**
Open XML SDK 是一个类库，提供了一种强类型的处理 OOXML 文档的方式。Aspose.Cells 是一个非常有用的电子表格处理库，提供了对所有 Microsoft Excel 和其他文件格式的出色支持。

如果您只需要对 XLSX 文档进行一些比较基本的编程操作，那么 Open XML SDK 可能是一个合适的选择。使用 Open XML SDK，您将比较容易地执行简单的任务，如生成简单的 XLSX 文档或删除评论、页眉/页脚、提取图像等。 
某些任务可以使用 Open XML SDK 实现，但无法使用 Aspose.Cells。例如，如果您需要直接访问 OOXML 文档的 XML 元素和属性，则应使用 Open XML SDK。

但是，如果您需要对文档执行复杂操作，例如以下某些任务，则使用 Aspose.Cells 是您的最佳选择：

- 支持除 XLSX 之外的其他文件格式。
- 在工作簿之间复制片段和工作表，或以适当方式合并工作簿，结合对象、样式和其他格式。
- 替换格式化的或未格式化的文本。
- 高级功能，例如从不同数据源（包括数组、ArrayList、DataTable / ResultSet）导入数据。
- 从数据源生成业务文档，例如订单及订单详细信息。
- 将文档转换为 PDF 或 XPS 格式，以便其呈现与 Microsoft Excel 完全一致。
- 开发 .NET 或 Java 应用程序。

