---
title: 打开不同格式的文件
type: docs
weight: 30
url: /zh/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API 允许您打开/读取不同格式，如 XLSX、HTML、CSV、ODS、TSV、SXC、FODS 等。
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

使用 Aspose.Cells 您可以打开不同格式的文件。**Aspose.Cells**可以打开一系列文件格式，例如 Microsoft Excel 电子表格（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、逗号分隔值（CSV）、制表符分隔或制表符分隔值（TSV）文件等。

如果您需要了解所有支持的文件格式，请参阅以下页面：
[支持的文件格式](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **打开不同格式的文件**

Aspose.Cells 允许开发人员打开不同格式的电子表格文件，例如 SpreadsheetML、逗号分隔值 (CSV)、制表符分隔或制表符分隔值 (TSV)、ODS 文件。要打开此类文件，开发人员可以使用与打开不同 Microsoft Excel 版本的文件相同的方法。

###  **打开 SpreadsheetML 文件**

SpreadsheetML 文件是电子表格的 XML 表示形式，包括有关它的所有信息，例如格式、公式等。从 Microsoft Excel XP 开始，Microsoft Excel 添加了 XML 导出选项，可将电子表格导出到 SpreadsheetML 文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **打开 HTML 文件**

Aspose.Cells 允许您将 HTML 文件打开到 Workbook 对象中。 HTML 文件应该面向 Microsoft Excel，即 MS-Excel 应该能够打开它。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **打开 CSV 文件**

逗号分隔值 (CSV) 文件包含值以逗号分隔的记录。数据存储为表，其中每列由逗号字符分隔并由双引号字符引起来。如果字段值包含双引号字符，则会使用一对双引号字符进行转义。您还可以使用Microsoft Excel将电子表格数据导出到CSV。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **打开 CSV 文件并替换无效字符**

在Excel中，当打开含有特殊字符的CSV文件时，字符会被自动替换。 Aspose.Cells API 也完成了同样的操作，这在下面给出的代码示例中进行了演示。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

可以从以下链接下载示例源文件来测试此功能。

[无效字符.csv](InvalidCharacters.csv)

###  **使用自定义分隔符打开文本文件**

文本文件用于保存不带格式的电子表格数据。该文件是一种纯文本文件，可以有一些自定义的分隔符。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

可以从以下链接下载示例源文件来测试此功能。

[自定义分隔符.txt](CustomSeparator.txt)

###  **打开制表符分隔的文件**

制表符分隔（文本）文件包含电子表格数据，但没有任何格式。数据像表格和电子表格一样按行和列排列。基本上，制表符分隔文件是一种特殊类型的纯文本文件，每列之间都有一个制表符。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **打开制表符分隔值 (TSV) 文件**

制表符分隔值 (TSV) 文件包含电子表格数据，但没有任何格式。这与制表符分隔文件相同，其中数据像表格和电子表格一样按行和列排列。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **打开 SXC 文件**

StarSuite Calc 与 Microsoft Excel 类似，支持公式、图表、函数和宏。使用该软件创建的电子表格以 SXC 扩展名保存。 SXC 文件还用于 OpenOffice.org Calc 电子表格文件。 Aspose.Cells 可以读取 SXC 文件，如以下代码示例所示。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **打开 FODS 文件**

FODS 文件是在 OpenDocument XML 中保存的电子表格，未经任何压缩。 Aspose.Cells 可以读取 FODS 文件，如以下代码示例所示。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
