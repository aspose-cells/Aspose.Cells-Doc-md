---
title: 将 Microsoft Excel 的高级筛选应用于满足复杂标准的记录
type: docs
weight: 280
url: /zh/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 通过使用 Aspose.Cells for .NET API，学习如何应用 Microsoft Excel 的高级筛选来显示满足复杂标准的记录。
keywords: 应用高级筛选、设置高级筛选、添加高级筛选、创建高级筛选、如何向范围添加高级筛选 
---

## **可能的使用场景**

Microsoft Excel允许您在工作表数据上应用*高级筛选*，以显示符合复杂条件的记录。您可以通过其*数据 > 高级*命令在Microsoft Excel中应用高级筛选，如此截图所示。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells还允许您使用[**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)方法来应用高级筛选。就像Microsoft Excel一样，它接受以下参数。

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

以下示例代码在[示例Excel文件](48496692.xlsx)上应用高级筛选，并生成[输出Excel文件](48496691.xlsx)。 截图显示了两个文件以进行比较。 如截图所示，在输出Excel文件中根据复杂标准对数据进行了筛选。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
