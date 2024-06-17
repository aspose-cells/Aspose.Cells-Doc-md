---
title: 应用Microsoft Excel的高级筛选以显示符合复杂条件的记录
type: docs
weight: 190
url: /zh/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **可能的使用场景**
Microsoft Excel允许您对工作表数据应用*高级筛选*，以显示符合复杂条件的记录。您可以通过*数据 > 高级*命令应用Microsoft Excel的高级筛选，如下图所示。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells还允许您使用[Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\))方法应用高级筛选。与Microsoft Excel一样，它接受以下参数。

**isFilter**

-**listRange**- 列表范围。

-**criteriaRange**- 条件范围。

列表范围。

**criteriaRange**

条件范围。

**copyTo**

拷贝数据的范围。

**uniqueRecordOnly**

仅显示或拷贝唯一行。
## **将 Microsoft Excel 的高级筛选应用于显示符合复杂条件的记录**
以下示例代码在 [Sample Excel File](48496702.xlsx) 上应用高级筛选，并生成 [Output Excel File](48496705.xlsx)。屏幕截图显示了用于对比的两个文件。正如您在屏幕截图中所看到的，输出Excel文件中的数据已根据复杂条件进行了筛选。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
