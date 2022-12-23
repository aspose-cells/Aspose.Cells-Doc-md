---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /zh/java/spreadsheetml-xlsx-xml/
---
## **关于 SpreadsheetML**
SpreadsheetML 是一系列基于 XML 的电子表格文档格式的名称。 SpreadsheetML有几个版本：

1. SpreadsheetML 版本 2003 是在 Microsoft Word 2003 中引入的。SpreadsheetML 是 Microsoft 向开放文档格式迈出的重要一步。
1. [办公室开放 XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) 是 Microsoft Office 2007 应用程序中引入的基于 XML 的新格式。 Office Open XML 是多种基于 XML 的专用标记语言的容器格式。 SpreadsheetML version 2007是Microsoft Office Excel 2007用来存储其文档的标记语言。
1. Microsoft Excel 2010 及更高版本将文档存储在更新的 OOXML 标准中定义的 SpreadsheetML 版本 2010 中。
## **SpreadsheetML 在 Aspose.Cells**
有 SpreadsheetML 的三个“版本”可用：

|**SpreadsheetML “版本”**|**适用标准/规范**|**支持 Aspose.Cells for Java**|
|:- |:- |:- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|是的|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|是的|
|Microsoft Excel 2010及以后版本|OOXML ISO/IEC DIS 29500|是的|
OOXML SpreadsheetML 文档通常以 XLSX 文件的形式出现，它们是 ZIP 包。除了 XLSX. Aspose.Cells 还提供了对加载、保存和转换 SpreadsheetML 文档的广泛支持。这样一个包罗万象的实现是可能的，因为 Aspose.Cells 在设计时考虑了 Microsoft Excel 文档的结构（并且 SpreadsheetML 以模仿 Microsoft Excel 文档的内部表示而闻名）。

**由Aspose.Cells生成并在Microsoft Excel中打开的XLSX文档** 

![待办事项：图片_替代_文本](spreadsheetml-xlsx-xml_1.png)

**Aspose.Cells生成的XLSX文档遵循Open Packaging Convention，可以在支持ZIP的应用程序中打开** 

![待办事项：图片_替代_文本](spreadsheetml-xlsx-xml_2.png)
## **OOXML 是开放的，为什么要使用 Aspose.Cells？**
的确，Office Open XML 技术可以仅使用 XML 类来构建文档处理和生成应用程序，而无需依赖第三方库（例如 Aspose.Cells）。但是，我们坚信，当您拥有处理 OOXML 文档，而不是通过 XML 或其他库工作。

OOXML 规范长达数千页。开放和标准并不意味着简单。要正确处理或生成 OOXML 文档，必须投入精力学习这种格式。

除了使正确处理和生成有效文档变得更简单之外，Aspose.Cells 还提供了以下重要功能，这些功能在直接通过 XML 或其他第三方库处理 OOXML 文件时是不具备的：

- 许多流行的 Excel 格式之间的质量转换，包括转换为 PDF、HTML、TIFF 和打印。
- 能够从片段、一个或多个文档构建文档，同时通过风格格式、图表和图形自动合并数据。
- 高级功能，例如从Array、ArrayList、DataTable、DataColumn、DataGrid、DataView、DataReader等不同数据源导入数据，或导出数据填充DataTable或Array，一行代码即可。
- 强大的公式计算引擎，支持几乎所有标准和高级 Microsoft Excel 函数。

考虑以下示例。一些单元格包含粗体文本“Hello World”。现在假设您需要编写一个程序来搜索工作表中的所有“Hello World”短语并将它们替换为“再见地球”。
## **Office Open XML 文档的片段**
**XML**

{{< highlight "csharp" >}}

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

在 Office Open XML 文档中实现即使是简单的查找和替换操作也很困难。

**我们的建议：**请记住，开放和标准并不意味着简单并使用 Aspose.Cells。
