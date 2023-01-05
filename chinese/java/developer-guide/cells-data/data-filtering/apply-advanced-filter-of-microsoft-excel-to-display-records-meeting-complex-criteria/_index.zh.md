---
title: 应用 Microsoft Excel 的高级筛选器显示满足复杂条件的记录
type: docs
weight: 190
url: /zh/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **可能的使用场景**
Microsoft Excel让你申请*高级过滤器*在工作表数据上显示满足复杂条件的记录。您可以通过其 Microsoft Excel 应用高级过滤器*数据 > 高级*命令如此屏幕截图所示。

![待办事项：图片_替代_文本](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells 还允许您使用[工作表.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)） 方法。就像 Microsoft Excel 一样，它接受以下参数。

**过滤器**

指示是否就地过滤列表。

**列表范围**

列表范围。

**标准范围**

标准范围。

**复制到**

复制数据的范围。

**唯一记录**

仅显示或复制唯一行。
## **应用 Microsoft Excel 的高级筛选器显示满足复杂条件的记录**
以下示例代码在[示例 Excel 文件](48496702.xlsx)并生成[输出 Excel 文件](48496705.xlsx).屏幕截图显示了两个文件以供比较。正如您在屏幕截图中看到的那样，已根据复杂的条件在输出 Excel 文件中过滤数据。

![待办事项：图片_替代_文本](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
