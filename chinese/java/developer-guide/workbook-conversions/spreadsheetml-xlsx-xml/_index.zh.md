---
title: 电子表格ML - XLSX，XML
type: docs
weight: 10
url: /zh/java/spreadsheetml-xlsx-xml/
---

## **关于电子表格ML**
SpreadsheetML 是一系列基于 XML 的电子表格文档格式的名称。有几个版本的 SpreadsheetML：

1. SpreadsheetML 版本 2003 是在 Microsoft Word 2003 中引入的。 SpreadsheetML 是微软朝着使文档格式开放的重要一步。
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML)（OOXML）是 Microsoft Office 2007 应用程序中引入的新基于 XML 的格式。 Office Open XML 是用于存储文档的几种专用基于 XML 的标记语言的容器格式。 SpreadsheetML 版本 2007 是 Microsoft Office Excel 2007 使用的标记语言，用于存储其文档。
1. Microsoft Excel 2010及更高版本按照更新的OOXML标准中定义的SpreadsheetML版本2010存储文档。
## **Aspose.Cells 中的 SpreadsheetML**
可用的三种版本的 SpreadsheetML 是：

|**SpreadsheetML“版本”**|**适用标准/规范**|**Aspose.Cells for Java支持**|
| :- | :- | :- |
|Microsoft Excel 2003| [微软 Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|是|
|Microsoft Excel 2007| [OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|是|
|Microsoft Excel 2010及更高版本|OOXML ISO/IEC DIS 29500|是|
OOXML SpreadsheetML文档通常是ZIP包，常见的是XLSX文件。除了XLSX外，Aspose.Cells还提供了对加载、保存和转换SpreadsheetML文档的广泛支持。这种全面的实现是可能的，因为Aspose.Cells的设计考虑了Microsoft Excel文档的结构（而SpreadsheetML模拟了Microsoft Excel文档的内部表示方式）。

**由Aspose.Cells生成的XLSX文档，并在Microsoft Excel中打开** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_1.png)

**由Aspose.Cells生成的XLSX文档遵循开放包约定，可在支持ZIP的应用程序中打开** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_2.png)
## **OOXML 是开放的，为什么要使用 Aspose.Cells？**
的确，Office Open XML 技术使得可以仅使用 XML 类构建文档处理和生成应用程序，而无需依赖于像 Aspose.Cells 这样的第三方库。然而，我们坚信在处理 OOXML 文档时使用 Aspose.Cells 仍然非常有益处，而不是透过 XML 或其他库进行操作。

OOXML 规范有数千页之长。开放和标准并不意味着简单。要正确处理或生成 OOXML 文档，必须投入时间学习格式。

Aspose.Cells 不仅使得正确处理和生成有效文档更加简单，而且提供以下重要功能，这些功能是在直接通过 XML 或其他第三方库处理 OOXML 文件时所没有的：

- 在许多常见的Excel格式之间进行高质量转换，包括转换为PDF、HTML、TIFF以及打印。
- 能够从片段、一个或多个文档构建文档，同时通过样式格式、图表和图形自动合并数据。
- 高级功能，比如从不同数据源导入数据（包括数组、ArrayList、DataTable、DataColumn、DataGrid、DataView和DataReader），或者用一行代码导出数据来填充DataTable或数组。
- 强大的公式计算引擎，支持几乎所有标准和高级 Microsoft Excel 函数。

考虑以下示例。某些单元格以粗体显示“Hello World”文本。现在想象一下，您需要编写一个程序，该程序搜索工作表中的所有“Hello World”短语，并将其替换为“Goodbye Earth”。
## ** Office Open XML 文档的片段**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}

在Office Open XML文档中实现甚至简单的查找和替换操作都很困难。

**我们的建议：**请记住开放和标准并不意味着简单，请使用Aspose.Cells。
