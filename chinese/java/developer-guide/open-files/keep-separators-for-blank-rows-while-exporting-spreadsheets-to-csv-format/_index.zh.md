---
title: 在将电子表格导出为CSV格式时保留空行的分隔符
type: docs
weight: 110
url: /zh/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **在将电子表格导出为CSV格式时保留空白行的分隔符**

Aspose.Cells提供了在将电子表格转换为CSV格式时保留行分隔符的能力。为此，您可以使用 **[TxtSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)** 类的 **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)** 属性。 **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)** 是一个boolean属性。要在将Excel文件转换为CSV时保留空行的分隔符，请将 **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)** 属性设置为 **true**。

以下样本代码加载 [源Excel文件](KeepSeparatorsForBlankRow.xlsx)。将 **[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)** 属性设置为 **true**，并另存为 [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv)。截图显示了源Excel文件、将电子表格转换为CSV时生成的默认输出以及将 **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)** 设置为 **true** 时生成的输出之间的比较。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
