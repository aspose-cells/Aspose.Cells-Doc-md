---
title: 为什么不使用Open XML SDK
type: docs
weight: 90
url: /zh/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

有时我们会听到这个问题：

**为什么我们应该使用Aspose产品而不是免费的Open XML SDK？**

这个问题很容易回答：功能和功能。

{{% /alert %}}

## **什么是Open XML SDK？**

根据[MSDN Library](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN)，Open XML SDK被定义为：

“Open XML SDK 2.5简化了操作Open XML包以及包内的基础Open XML模式元素的任务。Open XML SDK 2.5封装了开发人员在Open XML包上执行的许多常见任务，因此您可以仅凭几行代码执行复杂操作。”

OOXML文档本质上是压缩的XML文件，Open XML SDK是一个集合类，允许您以强类型方式处理OOXML文档的内容。这样，您就无需解压文件以提取XML，将XML加载到DOM树中并直接处理XML元素和属性，而Open XML SDK提供了类来执行这些操作。

## **什么是Aspose.Cells？**

Aspose.Cells是一个类库，允许应用程序执行以下电子表格处理任务：

- 在所有流行的Microsoft Excel格式之间进行高质量转换，包括转换为PDF、HTML、TIFF和打印。
- 使用工作簿对象模型进行编程。
- 能够从片段、一个或多个文档构建文档，同时通过样式格式、图表和图形自动合并数据。
- 高级功能，比如从不同数据源（包括数组、ArrayList、DataTable / ResultSet）导入数据。
- 强大的公式计算引擎，支持几乎所有标准和高级Microsoft Excel函数。

## **比较Open XML SDK和Aspose.Cells**

下表比较了Open XML SDK和Aspose.Cells的特点。

|**特点或特点类别**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|支持的Excel或其他格式|XLSX|XLS、CSV、SpreadsheetML 2003、XLSX、HTML、Tab Delimited、ODS、Plain Text (TXT)、PDF、XPS|
|在Excel格式之间进行转换|否|是|
|<p>使用工作簿对象模型进行高级编程：</p><p>- 查找和替换。</p><p>- 组装电子表格。</p><p>- 在工作簿之间复制片段和工作表。</p>|否|是|
|详细的编程与文档对象模型，访问所有电子表格元素的各个元素和格式属性。|是|是|
|直接低级访问底层XML元素和属性，如关系标识符，OOXML文档的列表标识符。|是|否|
|<p>生成报告，使用数据填充文档：</p><p>- 将数据导入/导出到 DataTable / ResultSet。</p><p>- 智能标记功能。</p><p>- 插入/删除行/列/范围。</p><p>- 自定义数据源。</p>|否|是|
|<p>呈现和打印：* 将工作表页呈现为光栅图像（TIFF、多页 TIFF、PNG、JPEG、BMP）。* 将电子表格页呈现为矢量图像（EMF）。</p><p>- 将图表转换为图像（TIFF、多页 TIFF、PNG、JPEG、BMP、EMF 等）</p><p>- 指定图像分辨率、质量、压缩以及其他选项。</p><p>- 使用.NET 打印基础结构打印电子表格。该组件具有内置的打印方法，可像 Microsoft Excel 的打印预览中显示的那样打印工作表。</p>|否|是|
|动态计算/重新计算公式|否|是|
|支持的平台|Windows、.NET|Windows、Linux、Java、.NET、Mono|

您可以将OpenXML与Aspose.Cells进行比较。为此，我们建议您熟悉Aspose.Cells for OpenXML项目-它展示了如何使用Aspose.Cells for .NET API与OpenXML执行不同任务。该项目还涵盖了仅在Aspose.Cells中可用而不在OpenXML中的处理文本文档的功能。

该项目对于希望从OpenXML迁移到Aspose.Cells的开发人员也是有用的。

{{% alert color="primary" %}}

探索[使用Aspose.Cells for .NET功能与OpenXML进行比较的插件带有源代码示例](https://github.com/asposemarketplace/Aspose_for_OpenXML)。

该插件使用Aspose.Cells的评估版本。在您满意评估后，您可以从[Aspose网站](https://purchase.aspose.com/buy)购买许可证。要删除评估消息和功能限制，您必须应用产品许可证。购买产品后，您将收到一个许可证文件。请按照["许可和订阅"](/cells/zh/net/licensing/)文章中的说明进行操作。

{{% /alert %}}

**结论**：Open XML SDK和Aspose.Cells并不直接竞争，因为它们涵盖的需求和受众相当不同。

## **为什么不使用Open XML SDK**
Open XML SDK是一个类库，提供了一种强类型的方式来处理OOXML文档。Aspose.Cells是一个非常有用的电子表格处理库，为所有Microsoft Excel和其他文件格式提供了出色的支持。

如果您只需要对XLSX文档执行一些基本的编程操作，那么Open XML SDK可能是一个合适的选择。使用Open XML SDK，您可以比较轻松地执行简单任务，例如生成简单的XLSX文档、删除注释、页眉/页脚、提取图像或其他任务。 
使用Open XML SDK可以完成一些任务，但使用Aspose.Cells无法完成。例如，如果您需要直接访问OOXML文档的XML元素和属性，则应该使用Open XML SDK。

但是，如果您需要在文档上执行复杂操作，例如以下一些任务，则使用Aspose.Cells是您的最佳选择：

- 支持除XLSX之外的其他文件格式。
- 在工作簿之间复制片段和工作表，或以适当的方式结合对象、样式和其他格式设置地连接工作簿。
- 替换格式化或未格式化的文本。
- 高级功能，比如从不同数据源（包括数组、ArrayList、DataTable / ResultSet）导入数据。
- 生成业务文档，比如从数据源生成带有订单详细信息的订单。
- 将文档转换为PDF或XPS，使其完全符合Microsoft Excel的转换方式。
- 开发.NET或Java应用程序。

