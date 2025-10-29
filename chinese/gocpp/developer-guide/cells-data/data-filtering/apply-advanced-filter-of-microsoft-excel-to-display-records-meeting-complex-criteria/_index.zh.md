---
title: 使用C++为Golang实现的Microsoft Excel高级筛选，显示满足复杂条件的记录
linktitle: 应用Microsoft Excel的高级筛选以显示符合复杂条件的记录
type: docs
weight: 280
url: /zh/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 学习如何使用Aspose.Cells for C++ API在Microsoft Excel中应用高级筛选，以显示满足复杂条件的记录。
keywords: 应用高级筛选，设置高级筛选，添加高级筛选，创建高级筛选，如何向范围添加高级筛选
---

## **可能的使用场景**

Microsoft Excel允许在工作表数据上应用*高级筛选*以显示满足复杂条件的记录。你可以通过*数据 > 高级*命令应用高级筛选，如此截屏所示。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells还允许你使用[**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/)方法应用高级筛选。就像Microsoft Excel一样，它接受以下参数。

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

以下示例代码在[示例Excel文件](48496692.xlsx)上应用高级筛选，并生成[输出Excel文件](48496691.xlsx)。截图显示两个文件以供比较。如截图所示，数据已根据复杂条件在输出Excel文件中被筛选。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
