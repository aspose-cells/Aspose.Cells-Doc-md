---
title: 转换 CSV，TSV 和 TXT 到 Excel
type: docs
weight: 50
url: /zh/java/convert-csv-tsv-and-txt-to-excel/
---

## **打开 CSV 文件**

逗号分隔值（CSV）文件包含以逗号分隔或分隔的值记录。在 CSV 文件中，数据以表格格式存储，其字段由逗号字符分隔并由双引号字符引用。如果字段的值包含双引号字符，则会用一对双引号字符进行转义。您还可以使用 Microsoft Excel 将您的电子表格数据导出到 CSV 文件。

要打开 CSV 文件，请使用 **[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** 类，并在 **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举中选择预定义的 **[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** 值。

## **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **打开 CSV 文件并替换无效字符**

在 Excel 中，打开带有特殊字符的 CSV 文件时，字符会被自动替换。Aspose.Cells API 也会执行相同的操作，代码示例如下所示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **使用首选解析器打开 CSV 文件**

不一定要使用默认解析器设置来打开 CSV 文件。有时导入 CSV 文件不会产生预期的输出，例如日期格式不如预期或空字段的处理方式不同。为此，**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)** 可提供自己的首选解析器，以根据需要解析不同的数据类型。以下示例代码演示了首选解析器的使用。  

可从以下链接下载示例源文件和输出文件以测试此功能。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **打开 TSV（制表符分隔）文件**

制表符分隔文件包含电子表格数据，但没有任何格式。数据以行和列的形式排列，如表格和电子表格。简言之，制表符分隔文件是一种特殊类型的纯文本文件，其中文本中的每个列之间有一个制表符。

要打开制表符分隔文件，开发人员应使用 **[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** 类，并在 **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举中选择预定义的 **[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** 值。

## **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **高级主题**
- [加载或导入带有公式的 CSV 文件](/cells/zh/java/load-or-import-csv-file-with-formulas/)
- [在将电子表格导出为CSV格式时修剪前导空白行和列](/cells/zh/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

