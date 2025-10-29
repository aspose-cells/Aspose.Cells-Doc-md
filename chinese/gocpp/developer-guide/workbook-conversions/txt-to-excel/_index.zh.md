---
title: 使用C++通过Golang将CSV、TSV和TXT转换为Excel
linktitle: 将CSV、TSV和TXT转换为Excel
type: docs
weight: 30
url: /zh/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: 学习如何使用Aspose.Cells for C++将CSV、TSV和TXT文件转换为Excel。
---

{{% alert color="primary" %}}

使用Aspose.Cells for C++，你可以将CSV文件转换为Excel、OpenOffice、PDF、JSON及其他许多格式。

{{% /alert %}}

## **打开 CSV 文件**

逗号分隔值文件（CSV）包含以逗号分隔的记录。数据存储为表格形式，每列由逗号字符分隔并用双引号括起来。如果字段值包含双引号字符，则用一对双引号转义。你也可以用Microsoft Excel导出电子表格数据为CSV文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **打开CSV文件及替换无效字符**

在Excel中打开带特殊字符的CSV文件时，字符会自动被替换。Aspose.Cells API也会执行相同操作，示例代码如下。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **使用首选解析器**

并非总是需要使用默认解析器设置打开CSV文件。有时导入CSV文件后不能得到预期输出，例如日期格式不符合预期或空字段处理不同。为此，提供了 **TxtLoadOptions.PreferredParsers** ，允许你自定义解析器以根据需求解析不同数据类型。以下示例演示了使用优先解析器的方法。

可以从以下链接下载示例源文件和输出文件，以测试此功能。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **使用自定义分隔符打开文本文件**

文本文件用于在不格式化的情况下保存电子表格数据。 文件是一种可以具有一些自定义分隔符的纯文本文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **打开制表符分隔文件**

制表符分隔（文本）文件包含电子表格数据，但没有任何格式。数据以行和列排布，就像在表格和电子表格中一样。本质上，制表符分隔文件是一种特殊的纯文本文件，每列之间用制表符分隔。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **打开制表符分隔数值（TSV）文件**

制表符分隔值（TSV）文件包含电子表格数据，但没有任何格式。与制表符分隔文件相同，数据以行和列排布。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## ** 高级主题**
- [加载或导入含公式的CSV文件](/cells/zh/cpp/load-or-import-csv-file-with-formulas/)
- [读取带有多种编码的CSV文件](/cells/zh/cpp/reading-csv-file-with-multiple-encodings/)
