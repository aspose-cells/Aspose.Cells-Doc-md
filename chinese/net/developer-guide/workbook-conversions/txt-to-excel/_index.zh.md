---
title: 将 CSV、TSV 和 TXT 转换为 Excel
type: docs
weight: 30
url: /zh/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

使用Aspose.Cells，您可以将CSV文件转换为Excel、OpenOffice、Pdf、Json和许多其他不同的格式。

{{% /alert %}}


## **打开 CSV 文件**

逗号分隔值（CSV）文件包含记录，其中值由逗号分隔。 数据存储为表格，其中每列由逗号字符分隔并由双引号字符引用。 如果字段值包含双引号字符，则用一对双引号字符进行转义。 您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **打开 CSV 文件并替换无效字符**

在 Excel 中，打开具有特殊字符的 CSV 文件时，字符会自动替换。 Aspose.Cells API 也采用相同的方法，示例如下所示的代码示例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **使用首选解析器**

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


## **高级主题**
- [加载或导入带公式的CSV文件](/cells/zh/net/load-or-import-csv-file-with-formulas/)
- [读取带有多种编码的CSV文件](/cells/zh/net/reading-csv-file-with-multiple-encodings/)

