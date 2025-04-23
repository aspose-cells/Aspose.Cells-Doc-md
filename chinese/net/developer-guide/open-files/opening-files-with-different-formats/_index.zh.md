---
title: 打开不同格式的文件
type: docs
weight: 30
url: /zh/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API 允许您打开/读取 XLSX、HTML、CSV、ODS、TSV、SXC、FODS 等不同格式。
keywords: 打开 xlsx 文件，打开 html 文件，读取 fods 文件，读取 ods 文件，读取 sxc 文件，打开 csv 文件，表格分隔，电子表格 ML，tsv，mhtml
---

{{% alert color="primary" %}}

使用 Aspose.Cells ，您可以打开不同格式的文件。 **Aspose.Cells** 可以打开一系列文件格式，如 Microsoft Excel 电子表格（XLS，XLSX，XLSM，XLSB），电子表格 ML，逗号分隔值（CSV），表格分隔或制表符分隔值（TSV）文件等。

如果您需要了解所有支持的文件格式，请参考以下页面：
[支持的文件格式](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **打开具有不同格式的文件**

Aspose.Cells 允许开发人员打开具有不同格式的电子表格文件，如电子表格 ML，逗号分隔值（CSV），表格分隔或制表符分隔值（TSV），ODS 文件。 要打开这些文件，开发人员可以使用与打开不同 Microsoft Excel 版本文件相同的方法。

### **打开电子表格 ML 文件**

电子表格 ML 文件是电子表格的 XML 表示，包括有关其所有信息的格式、公式等等。 自 Microsoft Excel XP 以来，已向 Microsoft Excel 添加了导出到电子表格 ML 文件的 XML 导出选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **打开 HTML 文件**

Aspose.Cells 允许您将 HTML 文件打开到工作簿对象中。 HTML 文件应该是面向 Microsoft Excel 的，即 MS-Excel 应该能够打开它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **打开 CSV 文件**

逗号分隔值（CSV）文件包含记录，其中值由逗号分隔。 数据存储为表格，其中每列由逗号字符分隔并由双引号字符引用。 如果字段值包含双引号字符，则用一对双引号字符进行转义。 您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **打开 CSV 文件并替换无效字符**

在 Excel 中，打开具有特殊字符的 CSV 文件时，字符会自动替换。 Aspose.Cells API 也采用相同的方法，示例如下所示的代码示例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **使用首选解析器**

不总是需要使用CSV文件的默认解析器设置。有时，导入CSV文件不会生成预期的输出，例如日期格式与预期不同或者对待空字段的方式不同。为此目的，**TxtLoadOptions.PreferredParsers**可用于根据要求提供自己的首选解析器来解析不同数据类型。以下示例代码演示了首选解析器的使用。  

可以从以下链接下载示例源文件和输出文件，以测试此功能。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **使用自定义分隔符打开文本文件**

文本文件用于在不格式化的情况下保存电子表格数据。 文件是一种可以具有一些自定义分隔符的纯文本文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **打开制表符分隔文件**

制表符分隔（文本）文件包含电子表格数据，但没有任何格式。数据按行和列排列，就像在表格和电子表格中一样。基本上，制表符分隔文件是一种带有每个列之间制表符的特殊类型的纯文本文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **打开制表符分隔数值（TSV）文件**

制表符分隔数值（TSV）文件包含电子表格数据，但没有任何格式。它与制表符分隔文件相同，其中数据按行和列排列，就像在表格和电子表格中一样。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}

### **打开SXC文件**

StarOffice Calc类似于Microsoft Excel，并支持公式、图表、函数和宏。使用此软件创建的电子表格以SXC扩展名保存。SXC文件也用于OpenOffice.org Calc电子表格文件。Aspose.Cells可以读取SXC文件，如以下代码示例所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **打开FODS文件**

FODS文件是以开放文档XML格式保存的电子表格文件，没有任何压缩。Aspose.Cells可以读取FODS文件，如以下代码示例所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
