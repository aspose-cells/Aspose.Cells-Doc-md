---
title: 打开不同格式的文件
type: docs
weight: 30
url: /zh/python-net/opening-files-with-different-formats/
description: Aspose.Cells for Python via .NET API 允许你打开/读取不同格式的文件，如 XLSX、HTML、CSV、ODS、TSV、SXC、FODS 等。
keywords: 打开 xlsx 文件，打开 html 文件，读取 fods 文件，读取 ods 文件，读取 sxc 文件，打开 csv 文件，表格分隔，电子表格 ML，tsv，mhtml
---

{{% alert color="primary" %}}

使用 Aspose.Cells for Python via .NET，可以打开不同格式的文件。Aspose.Cells for Python via .NET 支持多种文件格式，如 Microsoft Excel 电子表格（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、逗号分隔值（CSV）、制表符分隔或TSV文件等。

如果您需要了解所有支持的文件格式，请参考以下页面：
[支持的文件格式](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **打开具有不同格式的文件**

Aspose.Cells for Python via .NET 允许开发者以不同格式打开电子表格文件，如SpreadsheetML、CSV、TSV、ODS文件。开发者可以用与打开不同Microsoft Excel版本文件相同的方法打开这些文件。

### **打开电子表格 ML 文件**

电子表格 ML 文件是电子表格的 XML 表示，包括有关其所有信息的格式、公式等等。 自 Microsoft Excel XP 以来，已向 Microsoft Excel 添加了导出到电子表格 ML 文件的 XML 导出选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **打开 HTML 文件**

Aspose.Cells for Python via .NET 支持将HTML文件导入为Workbook对象。HTML文件应为Microsoft Excel格式，即应能用MS-Excel打开。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **打开 CSV 文件**

逗号分隔值（CSV）文件包含记录，其中值由逗号分隔。 数据存储为表格，其中每列由逗号字符分隔并由双引号字符引用。 如果字段值包含双引号字符，则用一对双引号字符进行转义。 您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **打开 CSV 文件并替换无效字符**

在Excel中，当打开带有特殊字符的CSV文件时，字符会被自动替换。Aspose.Cells for Python via .NET API 也会这样，以下的示例代码演示了这一点。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **打开制表符分隔文件**

制表符分隔（文本）文件包含电子表格数据，但没有任何格式。数据按行和列排列，就像在表格和电子表格中一样。基本上，制表符分隔文件是一种带有每个列之间制表符的特殊类型的纯文本文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **打开制表符分隔数值（TSV）文件**

制表符分隔数值（TSV）文件包含电子表格数据，但没有任何格式。它与制表符分隔文件相同，其中数据按行和列排列，就像在表格和电子表格中一样。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **打开SXC文件**

StarOffice Calc类似于Microsoft Excel，支持公式、图表、函数和宏。用此软件创建的电子表格使用 SXC 扩展名保存。SXC 文件也用于OpenOffice.org Calc电子表格。Aspose.Cells for Python via .NET可以读取SXC文件，示例代码如下。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **打开FODS文件**

FODS文件是以OpenDocument XML格式保存的电子表格，没有任何压缩。Aspose.Cells for Python via .NET可以读取FODS文件，示例代码如下。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
