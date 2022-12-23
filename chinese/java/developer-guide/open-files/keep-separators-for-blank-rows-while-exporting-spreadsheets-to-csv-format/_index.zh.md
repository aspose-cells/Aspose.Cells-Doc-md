---
title: 将电子表格导出为 CSV 格式时保留空白行的分隔符
type: docs
weight: 110
url: /zh/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **将电子表格导出为 CSV 格式时保留空白行的分隔符**

Aspose.Cells 提供了在将电子表格转换为 CSV 格式时保留行分隔符的功能。为此，您可以使用**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**的财产**[TxtSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)**班级。**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**是一个布尔属性。要在将 Excel 文件转换为 CSV 时保留空行分隔符，请设置**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**财产给**真的**.

下面的示例代码加载[源Excel文件](KeepSeparatorsForBlankRow.xlsx).它设置**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**财产给**真的**并将其另存为[KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv).屏幕截图显示了源 Excel 文件、将电子表格转换为 CSV 时生成的默认输出与通过设置生成的输出之间的比较**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**到**真的**.

![待办事项：图片_替代_文本](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
