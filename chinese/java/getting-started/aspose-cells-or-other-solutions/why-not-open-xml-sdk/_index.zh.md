---
title: 为什么不使用 Open XML SDK
type: docs
weight: 20
url: /zh/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

我们有时会听到这样的问题：

**为何我们应该使用 Aspose 产品而不是免费的 Open XML SDK？**

这个问题很容易回答：**功能和功能**。

{{% /alert %}} 
## **什么是 Open XML SDK？**
根据MSDN库中的定义，Open XML SDK被定义为：Open XML SDK 2.0简化了操作Open XML包和包内基础Open XML模式元素的任务。Open XML SDK 2.0封装了开发人员在Open XML包上执行的许多常见任务，使您可以用几行代码执行复杂操作。OOXML文档本质上是压缩的XML文件，而Open XML SDK是一个类集合，允许您以强类型方式处理OOXML文档的内容。这意味着不需要解压文件以提取XML，将XML加载到DOM树中并直接处理XML元素和属性，Open XML SDK提供了用于执行这些操作的类。
## **什么是Aspose.Cells?**
Aspose.Cells是一个类库，允许您的应用程序执行以下电子表格处理任务：高质量转换所有流行的Excel格式，包括转换为PDF、HTML、TIFF和打印。使用工作簿对象模型进行编程。能够根据格式、图表和图形自动合并数据，从一个或多个文档中构建文档片段。高级功能，如从不同数据源（包括数组、ArrayList、DataTable / ResultSet）导入数据。强大的公式计算引擎，支持几乎所有标准和高级的Microsoft Excel函数。


## **比较Open XML SDK和Aspose.Cells**
以下表格比较了Open XML SDK和Aspose.Cells的功能。 

|特性或特性类别|Open XML SDK|Aspose.Cells|
| :- | :- | :- |
|支持的Excel或其他格式|XLSX|XLS、CSV、SpreadsheetML 2003、XLSX、HTML、Tab Delimited、ODS、纯文本（TXT）、PDF、XPS|
|在Excel格式之间转换|否|是|
|使用工作簿对象模型进行高级编程：<br>- 查找和替换。<br>- 组装电子表格。<br>- 在工作簿之间复制文档片段和工作表。|否|是|
|使用文档对象模型进行详细编程，访问所有电子表格元素的单独元素和格式属性。|是|是|
|直接全面访问底层XML元素和属性（如关系标识符、OOXML文档的列表标识符）。|是|否|
|生成报告，将数据填充到文档中：<br>- 将数据导入/导出到*DataTable / ResultSet。<br>- 智能标记功能。<br>- 插入/删除行/列/范围。<br>- 自定义数据源。|否|是|
|渲染和打印：<br>- 将工作表页面呈现为光栅图像（TIFF、多页TIFF、PNG、JPEG、BMP）。<br>- 将电子表格页面呈现为矢量图像（EMF）。<br>- 将图表转换为图像（TIFF、多页TIFF、PNG、JPEG、BMP、EMF等）。<br>- 指定图像分辨率、质量、压缩和其他选项。<br>- 使用.NET打印基础设施打印电子表格。该组件具有内置打印方法，可将工作表打印为MS Excel中的打印预览中显示的样式。|否|是|
|动态计算/重新计算公式|否 |是 |
|支持的平台|Windows、.NET|Windows、Linux、Java、.NET、Mono|
## **结论**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}
