---
title: 将 CSV、TSV 和 TXT 转换为 Excel
type: docs
weight: 50
url: /zh/java/convert-csv-tsv-and-txt-to-excel/
---

## **打开 CSV 文件**

逗号分隔的值（CSV）文件包含由逗号分隔或分隔的记录值。在 CSV 文件中，数据以字段由逗号字符分隔并由双引号字符引用的表格格式存储。如果字段的值包含双引号字符，则用一对双引号字符进行转义。您还可以使用 Microsoft Excel 将电子表格数据导出为 CSV 文件。

要打开CSV文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) 类并选择在 [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) 枚举中预定义的 [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) 值。

## **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **打开 CSV 文件并替换无效字符**

在 Excel 中，当打开具有特殊字符的 CSV 文件时，这些字符会被自动替换。Aspose.Cells API 也会执行相同的操作，如下面给出的代码示例所示。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **使用首选解析器打开 CSV 文件并不总是必需的。有时导入 CSV 文件会得到意外的输出，例如日期格式不符合预期或空字段的处理方式不同。为此可以使用 **[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)** 来提供自己喜欢的解析器，以根据要求解析不同的数据类型。以下示例代码演示了首选解析器的用法。**

并非总是需要使用默认的解析器设置来打开CSV文件。有时导入CSV文件的输出与预期不同，例如日期格式不符合期望或空字段处理方式不同。为此，可使用 [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) 来提供自己偏好的解析器，以根据需求解析不同的数据类型。以下示例代码演示了首选解析器的用法。  

可以从以下链接下载示例源文件和输出文件，以测试此功能。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **打开 TSV（制表符分隔）文件**

制表符分隔文件包含电子表格数据但不包含任何格式。数据以行和列的形式排列，就像表格和电子表格一样。简单来说，制表符分隔的文件是一种特殊的纯文本文件，在文本中的每一列之间都有一个制表符。

要打开制表符分隔的文件，开发人员应使用 [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) 类并选择在 [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) 枚举中预定义的 [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) 值。

## **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **高级主题**
- [加载或导入带公式的CSV文件](/cells/zh/java/load-or-import-csv-file-with-formulas/)
- [导出电子表格到CSV格式时修剪前导空白行和列](/cells/zh/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

{{< app/cells/assistant language="java" >}}
