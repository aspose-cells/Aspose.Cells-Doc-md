---
title: 转换 CSV，TSV 和 TXT 到 Excel
type: docs
weight: 30
url: /zh/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

使用 Aspose.Cells，您可以将 CSV 文件转换为 Excel、OpenOffice、Pdf、Json和许多不同的格式。

{{% /alert %}}


## **打开 CSV 文件**

逗号分隔值(CSV)文件包含按逗号分隔的值的记录。数据存储为表，其中每列由逗号字符分隔并由双引号字符引用。如果字段值包含双引号字符，则它将以一对双引号字符转义。您也可以使用 Microsoft Excel 将表格数据导出为 CSV 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **打开 CSV 文件并替换无效字符**

在 Excel 中打开具有特殊字符的 CSV 文件时，字符会自动替换。Aspose.Cells API 也会执行相同的操作，下面的代码示例演示了这一点。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **使用首选解析器**

打开 CSV 文件不总是必须使用默认解析器设置。有时导入 CSV 文件会创建预期之外的输出，比如日期格式不如预期或空字段的处理方式不同。为此，可以使用**TxtLoadOptions.PreferredParsers**来提供适合自己的解析器以按需解析不同的数据类型。以下示例代码演示了首选解析器的用法。  

可从以下链接下载示例源文件和输出文件以测试此功能。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **使用自定义分隔符打开文本文件**

文本文件用于保存无格式的电子表格数据。该文件是一种可以具有一些定制分隔符的纯文本文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **打开制表符分隔文件**

制表符分隔(文本)文件包含电子表格数据，但没有任何格式。数据按行和列排列，就像表和电子表格中那样。基本上，制表符分隔文件是一种具有制表符分隔的每列之间有制表符的特殊类型的纯文本文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **打开制表符分隔值(TSV)文件**

制表符分隔值(TSV)文件包含电子表格数据但没有任何格式。它与制表符分隔文件类似，数据按行和列排列，就像表和电子表格中一样。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **高级主题**
- [加载或导入带有公式的 CSV 文件](/cells/zh/net/load-or-import-csv-file-with-formulas/)
- [使用多种编码读取 CSV 文件](/cells/zh/net/reading-csv-file-with-multiple-encodings/)

