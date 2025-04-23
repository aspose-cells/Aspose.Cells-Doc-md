---
title: 打开不同格式的文件
type: docs
weight: 30
url: /zh/go-cpp/opening-files-with-different-formats/

description: Aspose.Cells for .NET API 允许您打开/读取 XLSX、HTML、CSV、ODS、TSV、SXC、FODS 等不同格式。
keywords: 打开 xlsx 文件，打开 html 文件，读取 fods 文件，读取 ods 文件，读取 sxc 文件，打开 csv 文件，表格分隔，电子表格 ML，tsv，mhtml
---

{{% alert color="primary" %}}

使用Aspose.Cells，您可以打开多种格式的文件。**Aspose.Cells**支持打开多种文件格式，例如微软Excel（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、逗号分隔值（CSV）、制表符分隔值（TSV）等。

如果您需要了解所有支持的文件格式，请参考以下页面：
[支持的文件格式]（https://docs.aspose.com/cells/go-cpp/supported-file-formats/）

{{% /alert %}}

## **打开具有不同格式的文件**

Aspose.Cells允许开发者以不同格式打开电子表格文件，例如SpreadsheetML、CSV、TSV和ODS文件。可以用与打开不同Microsoft Excel版本文件相同的方法。

### **打开电子表格 ML 文件**

SpreadsheetML文件是电子表格的XML表示，包含所有信息，例如格式化、公式等。从Microsoft Excel XP开始，Microsoft Excel增加了导出为SpreadsheetML的XML导出选项。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **打开 HTML 文件**

Aspose.Cells 允许您将 HTML 文件打开到工作簿对象中。 HTML 文件应该是面向 Microsoft Excel 的，即 MS-Excel 应该能够打开它。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **打开 CSV 文件**

逗号分隔值（CSV）文件包含记录，其中值由逗号分隔。 数据存储为表格，其中每列由逗号字符分隔并由双引号字符引用。 如果字段值包含双引号字符，则用一对双引号字符进行转义。 您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

#### **打开 CSV 文件并替换无效字符**

在 Excel 中，打开具有特殊字符的 CSV 文件时，字符会自动替换。 Aspose.Cells API 也采用相同的方法，示例如下所示的代码示例。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFileAndReplaceInvalidCharacters.go" >}}

可以从以下链接下载样本源文件以测试此功能。

[InvalidCharacters.csv](InvalidCharacters.csv)

### **使用自定义分隔符打开文本文件**

文本文件用于在不格式化的情况下保存电子表格数据。 文件是一种可以具有一些自定义分隔符的纯文本文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

可以从以下链接下载示例源文件，以测试此功能。

[CustomSeparator.txt](CustomSeparator.txt)

### **打开制表符分隔文件**

制表符分隔（文本）文件包含电子表格数据，但没有任何格式。数据按行列排列，类似表格和电子表格。基本上，制表符分隔文件是特殊的纯文本文件，每列之间用制表符分隔。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **打开制表符分隔数值（TSV）文件**

制表符分隔值（TSV）文件包含电子表格数据，没有任何格式，内容与制表符分隔文件相同，列在表格和电子表格中以制表符分隔。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **打开SXC文件**

StarOffice Calc类似于Microsoft Excel，支持公式、图表、函数和宏。使用此软件创建的电子表格保存为SXC扩展名。SXC文件也用于OpenOffice.org Calc电子表格。Aspose.Cells支持读取SXC文件，以下代码示例演示了此功能。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **打开FODS文件**

FODS文件是以OpenDocument XML格式保存的电子表格，无压缩。Aspose.Cells可以读取FODS文件，以下示例代码演示了此功能。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
