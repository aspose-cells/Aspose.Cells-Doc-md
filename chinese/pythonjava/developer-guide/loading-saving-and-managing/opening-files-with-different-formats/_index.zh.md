---
title: 打开不同格式的文件
type: docs
weight: 30
url: /zh/python-java/opening-files-with-different-formats/
description: Aspose.Cells for .NET API 允许您打开/阅读不同的格式，如 XLSX、HTML、CSV、ODS、TSV、SXC、FODS 等。
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

使用 Aspose.Cells 您可以打开不同格式的文件。**Aspose.Cells**可以打开一系列文件格式，例如 Microsoft Excel 电子表格（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、逗号分隔值 (CSV)、制表符分隔或制表符分隔值 (TSV) 文件等。

如果您需要了解所有支持的文件格式，请参阅以下页面：
[支持的文件格式](https://docs.aspose.com/cells/python-java/supported-file-formats/)

{{% /alert %}}

## **打开不同格式的文件**

Aspose.Cells 允许开发人员打开不同格式的电子表格文件，例如 SpreadsheetML、逗号分隔值 (CSV)、制表符分隔值或制表符分隔值 (TSV)、ODS 文件。要打开此类文件，开发人员可以使用与打开不同 Microsoft Excel 版本的文件相同的方法。

### **打开 SpreadsheetML 文件**

SpreadsheetML 文件是电子表格的 XML 表示，包括有关它的所有信息，例如格式、公式等。自 Microsoft Excel XP 起，一个 XML 导出选项被添加到 Microsoft Excel，可将电子表格导出到 SpreadsheetML 文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenSpreadsheetMLFile.py" >}}

### **打开 HTML 文件**

Aspose.Cells 允许您将 HTML 文件打开到 Workbook 对象中。 HTML 文件应该是 Microsoft 面向 Excel 的，即 MS-Excel 应该能够打开它。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenHTMLFile.py" >}}

### **打开 CSV 文件**

逗号分隔值 (CSV) 文件包含值以逗号分隔的记录。数据存储为表格，其中每列由逗号分隔并由双引号引起来。如果字段值包含双引号字符，则使用一对双引号字符进行转义。您还可以使用 Microsoft Excel 将电子表格数据导出为 CSV。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenCSVFile.py" >}}

#### **打开 CSV 文件并替换无效字符**

在 Excel 中，当打开带有特殊字符的 CSV 文件时，字符会被自动替换。 Aspose.Cells API 完成了同样的操作，在下面给出的代码示例中进行了演示。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenCSVFileAndReplaceInvalidCharacters.py" >}}

可以从以下链接下载示例源文件以测试此功能。

[无效字符.csv](InvalidCharacters.csv)

### **使用自定义分隔符打开文本文件**

文本文件用于保存不带格式的电子表格数据。该文件是一种纯文本文件，可以有一些自定义的分隔符。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTextFilewithCustomSeparator.py" >}}

可以从以下链接下载示例源文件以测试此功能。

[自定义分隔符.txt](CustomSeparator.txt)

### **打开制表符分隔的文件**

制表符分隔（文本）文件包含电子表格数据，但没有任何格式。数据以行和列的形式排列，就像在表格和电子表格中一样。基本上，制表符分隔文件是一种特殊的纯文本文件，每列之间有一个制表符。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTabDelimitedFile.py" >}}

可以从以下链接下载示例源文件以测试此功能。

[制表符分隔符.txt](TabDelimited.txt)

### **打开制表符分隔值 (TSV) 文件**

制表符分隔值 (TSV) 文件包含电子表格数据，但没有任何格式。这与制表符分隔文件相同，其中数据按行和列排列，就像在表格和电子表格中一样。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTSVFile.py" >}}

### **打开 SXC 文件**

StarSuite Calc 类似于 Microsoft Excel，支持公式、图表、函数和宏。使用此软件创建的电子表格以 SXC 扩展名保存。 SXC 文件也用于 OpenOffice.org Calc 电子表格文件。 Aspose.Cells 可以读取 SXC 文件，如以下代码示例所示。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenSXCFile.py" >}}

### **打开 FODS 文件**

FODS 文件是保存在 OpenDocument XML 中的电子表格，没有任何压缩。 Aspose.Cells 可以读取 FODS 文件，如以下代码示例所示。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFODSFile.py" >}}
