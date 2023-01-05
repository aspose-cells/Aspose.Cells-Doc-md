---
title: 将 CSV、TSV 和 TXT 转换为 Excel
type: docs
weight: 30
url: /zh/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

使用 Aspose.Cells，您可以将 CSV 文件转换为 Excel、OpenOffice、Pdf、Json 和许多不同的格式。

{{% /alert %}}


## **打开 CSV 文件**

逗号分隔值 (CSV) 文件包含值以逗号分隔的记录。数据存储为表格，其中每列由逗号分隔并由双引号引起来。如果字段值包含双引号字符，则使用一对双引号字符进行转义。也可以用Microsoft Excel导出电子表格数据到CSV。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **打开 CSV 文件并替换无效字符**

在 Excel 中，打开带有特殊字符的 CSV 文件时，会自动替换这些字符。 Aspose.Cells API 完成了同样的操作，在下面给出的代码示例中进行了演示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **使用首选解析器**

这并不总是需要使用默认解析器设置来打开 CSV 文件。有时导入 CSV 文件不会创建预期的输出，例如日期格式不符合预期或空字段的处理方式不同。以此目的**TxtLoadOptions.PreferredParsers**可根据需要提供自己的首选解析器来解析不同的数据类型。以下示例代码演示了首选解析器的用法。

可以从以下链接下载示例源文件和输出文件以测试此功能。

[示例首选解析器.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **使用自定义分隔符打开文本文件**

文本文件用于保存不带格式的电子表格数据。该文件是一种纯文本文件，可以有一些自定义的分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **打开制表符分隔的文件**

制表符分隔（文本）文件包含电子表格数据，但没有任何格式。数据以行和列的形式排列，就像在表格和电子表格中一样。基本上，制表符分隔文件是一种特殊的纯文本文件，每列之间有一个制表符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **打开制表符分隔值 (TSV) 文件**

制表符分隔值 (TSV) 文件包含电子表格数据，但没有任何格式。这与制表符分隔文件相同，其中数据按行和列排列，就像在表格和电子表格中一样。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **推进主题**
- [使用公式加载或导入 CSV 文件](/cells/zh/net/load-or-import-csv-file-with-formulas/)
- [读取具有多个编码的 CSV 文件](/cells/zh/net/reading-csv-file-with-multiple-encodings/)

