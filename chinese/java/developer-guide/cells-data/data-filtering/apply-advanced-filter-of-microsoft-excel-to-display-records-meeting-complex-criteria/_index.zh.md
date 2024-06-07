---
title: 将 Microsoft Excel 的高级筛选应用于满足复杂标准的记录
type: docs
weight: 190
url: /zh/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **可能的使用场景**
Microsoft Excel允许您在工作表数据上应用*高级筛选*，以显示符合复杂条件的记录。您可以通过其*数据 > 高级*命令在Microsoft Excel中应用高级筛选，如此截图所示。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells 还允许您使用 [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) 方法应用高级筛选。就像 Microsoft Excel 一样，它接受以下参数。

**isFilter**

指示是否在原地过滤列表。

**listRange**

列表范围。

**criteriaRange**

条件范围。

**copyTo**

将数据复制到的范围。

**uniqueRecordOnly**

仅显示或复制唯一行。
## **应用Microsoft Excel的高级筛选以显示满足复杂条件的记录**
下面的示例代码对 [样本Excel文件](48496702.xlsx) 应用了高级筛选，并生成了[输出Excel文件](48496705.xlsx)。截图显示了用于比较的两个文件。您可以在截图中看到，根据复杂的条件，数据已经在输出的Excel文件中进行了筛选。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
