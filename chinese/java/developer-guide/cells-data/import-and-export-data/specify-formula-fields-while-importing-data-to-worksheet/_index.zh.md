---
title: 将数据导入工作表时指定公式字段
type: docs
weight: 220
url: /zh/java/specify-formula-fields-while-importing-data-to-worksheet/
---
## **可能的使用场景**

您可以在将数据导入工作表时指定公式字段，使用[**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas)方法。此方法采用布尔数组，其中值**真的**表示该字段是公式字段。例如，如果第三个字段是公式字段，则数组中的第三个值将是**真的**.

## **将数据导入工作表时指定公式字段**

请参阅以下示例代码，该代码解释了如何在将数据导入工作表时指定公式字段。请参阅[输出Excel文件](61767850.xlsx)由代码生成，屏幕截图显示代码对输出 Excel 文件的影响。

![待办事项：图像_替代_文本](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
