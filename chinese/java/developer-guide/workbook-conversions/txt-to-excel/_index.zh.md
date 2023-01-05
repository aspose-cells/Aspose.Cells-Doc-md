---
title: 将 CSV、TSV 和 TXT 转换为 Excel
type: docs
weight: 50
url: /zh/java/convert-csv-tsv-and-txt-to-excel/
---
## **打开 CSV 文件**

逗号分隔值 (CSV) 文件包含其值由逗号分隔或分隔的记录。在 CSV 文件中，数据以表格格式存储，其字段由逗号分隔并由双引号引起来。如果字段的值包含双引号字符，则使用一对双引号字符进行转义。您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV 文件。

要打开 CSV 文件，请使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类并选择**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)**值，预定义在**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

## **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **打开 CSV 文件并替换无效字符**

在 Excel 中，打开带有特殊字符的 CSV 文件时，会自动替换这些字符。 Aspose.Cells API 完成了同样的操作，在下面给出的代码示例中进行了演示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **使用首选解析器打开 CSV 文件**

这并不总是需要使用默认解析器设置来打开 CSV 文件。有时导入 CSV 文件不会创建预期的输出，例如日期格式不符合预期或空字段的处理方式不同。以此目的**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**可根据需要提供自己的首选解析器来解析不同的数据类型。以下示例代码演示了首选解析器的用法。

可以从以下链接下载示例源文件和输出文件以测试此功能。

[示例首选解析器.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **打开 TSV（制表符分隔）文件**

制表符分隔的文件包含电子表格数据，但没有任何格式。数据按行和列排列，例如表格和电子表格。简而言之，制表符分隔文件是一种特殊的纯文本文件，文本中的每一列之间都有一个制表符。

要打开制表符分隔的文件，开发人员应该使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类并选择**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)**值，预定义在**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

## **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **推进主题**
- [使用公式加载或导入 CSV 文件](/cells/zh/java/load-or-import-csv-file-with-formulas/)
- [将电子表格导出为 CSV 格式时修剪前导空白行和列](/cells/zh/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

