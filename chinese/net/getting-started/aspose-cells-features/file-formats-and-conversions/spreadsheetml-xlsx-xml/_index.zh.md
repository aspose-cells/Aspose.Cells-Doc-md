---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /zh/net/spreadsheetml-xlsx-xml/
---

## **关于SpreadsheetML**
SpreadsheetML是一系列面向电子表格文档的基于XML的格式的名称。有几个版本的SpreadsheetML：

1. 电子表格版本2003是在Microsoft Word 2003中引入的。 SpreadsheetML是微软向着将文档格式开放化迈出的重要一步。
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML)是Microsoft Office 2007应用程序中引入的新基于XML的格式。 Office Open XML是几种专门的基于XML的标记语言的容器格式。 SpreadsheetML版本2007是Microsoft Office Excel 2007用于存储其文档的标记语言。
1. Microsoft Excel 2010以更新的OOXML标准中定义的SpreadsheetML版本2010存储文档。
## **Aspose.Cells中的SpreadsheetML**
有三个可用的"版本"的SpreadsheetML：

|**SpreadsheetML “Version”**|**适用的标准/规范**|**在Aspose.Cells for .NET中支持**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|是|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|是|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|是|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|是|
OOXML SpreadsheetML文档通常以XLSX文件的形式出现，这些文件是ZIP包。除了XLSX之外，Aspose.Cells还提供了对加载、保存和转换SpreadsheetML文档的广泛支持。这种全面的实现是可能的，因为Aspose.Cells的设计考虑了Microsoft Excel文档的结构（而SpreadsheetML被认为是模仿Microsoft Excel文档的内部表示）。 
### **OOXML是开放的，为什么要使用Aspose.Cells？**
确实，Office Open XML技术使得可以仅使用XML类构建文档处理和生成应用程序，而无需依赖于Aspose.Cells等第三方库。 但是，我们坚信在处理OOXML文档时，使用Aspose.Cells仍然非常有益，而不是通过XML或其他库进行工作。

OOXML规范内容非常丰富。 开放和标准并不意味着简单。 要正确处理或生成OOXML文档，必须投入大量时间学习该格式。

除了使得正确处理和生成有效文档更简单外，Aspose.Cells还提供了以下你在通过XML或其他第三方库直接处理OOXML文件时没有的重要功能：

- 在许多流行的Excel格式之间进行优质转换，包括转换为PDF、HTML、TIFF和打印。
- 能够从片段构建文档，从一个或多个文档，同时通过样式格式化、图表和图形自动合并数据。
- 高级功能，例如，从不同的数据源（包括数组、ArrayList、DataTable、DataColumn、DataGrid、DataView和DataReader）导入数据，或者通过一行代码将数据导出到填充有数据的DataTable或数组中。
- 强大的公式计算引擎，支持几乎所有标准和高级的 Microsoft Excel 函数。

考虑以下示例。某些单元格以粗体包含文本“Hello World”。现在想象一下，您需要编写一个程序，以搜索工作表中的所有“Hello World”短语并将其替换为“Goodbye Earth”。
### **Office Open XML 文档的片段**
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


甚至在Office Open XML文档中执行一个简单的查找和替换操作也是困难的。我们的建议：记住开放和标准并不意味着简单，使用Aspose.Cells。
