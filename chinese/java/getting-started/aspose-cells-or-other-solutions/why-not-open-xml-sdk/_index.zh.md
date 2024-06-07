---
title: 为什么不使用Open XML SDK
type: docs
weight: 20
url: /zh/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

有时我们会听到这个问题：

**为什么我们应该使用Aspose产品而不是免费的Open XML SDK？**

这个问题很容易回答：**功能和功能**。

{{% /alert %}} 
## **Open XML SDK是什么？**
根据MSDN Library的定义，Open XML SDK被定义为：Open XML SDK 2.0简化了在Open XML包和包内的Open XML模式元素中操作的任务。Open XML SDK 2.0封装了开发人员在Open XML包上执行的许多常见任务，因此您可以用几行代码执行复杂操作。OOXML文档本质上就是经过压缩的XML文件，而Open XML SDK是一组允许您以强类型方式处理OOXML文档内容的类。这样，您可以使用Open XML SDK的类进行处理而不必解压文件以提取XML，将XML加载到DOM树中并直接使用XML元素和属性。*
## **Aspose.Cells是什么？**
Aspose.Cells是一个允许您的应用程序执行以下电子表格处理任务的类库：所有流行Excel格式之间的高质量转换，包括转换为PDF、HTML、TIFF和打印。使用工作簿对象模型编程。能够构建文档，从单个或多个文档的片段自动合并数据，并通过样式格式、图表和图形自动合并数据。高级功能，如，从不同的数据源（包括数组、ArrayList、DataTable / ResultSet）导入数据。强大的公式计算引擎，支持几乎所有标准和先进的Microsoft Excel函数。

{{% alert color="primary" %}}
## **比较Open XML SDK和Aspose.Cells**
以下表格比较了 Open XML SDK 和 Aspose.Cells 的功能。

|**特点或特点类别**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|支持的Excel或其他格式|XLSX|XLS、CSV、SpreadsheetML 2003、XLSX、HTML、Tab Delimited、ODS、Plain Text (TXT)、PDF、XPS|
|在Excel格式之间进行转换|否|是|
|<p>使用工作簿对象模型进行高级编程：</p><p>- 查找和替换。</p><p>- 组装电子表格。</p><p>- 在工作簿之间复制片段和工作表。</p>|否|是|
|详细的编程与文档对象模型，访问所有电子表格元素的各个元素和格式属性。|是|是|
|直接低级访问底层XML元素和属性，如关系标识符，OOXML文档的列表标识符。|是|否|
|<p>生成报告，填充数据文档：</p><p>- 将数据导入/导出到/从 *DataTable /* ResultSet。</p><p>- 智能标记功能。</p><p>- 插入/删除行/列/范围。</p><p>- 自定义数据源。</p>|没有|有|
|<p>呈现和打印：* 将工作表页面呈现为光栅图像（TIFF、多页TIFF、PNG、JPEG、BMP）。* 将电子表格页面呈现为矢量图像（EMF）。* 将图表转换为图像（TIFF、多页TIFF、PNG、JPEG、BMP、EMF等）。</p><p>- 指定图像分辨率、质量、压缩和其他选项。</p><p>- 使用.NET打印基础设施打印电子表格。该组件具有内置的打印方法，可像在MS Excel的打印预览中显示的那样打印工作表。</p>|没有|有|
|动态计算/重新计算公式|否|是|
|支持的平台|Windows、.NET|Windows、Linux、Java、.NET、Mono|
## **结论**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
