---
title: 将 Microsoft Excel 的高级筛选应用于满足复杂标准的记录
type: docs
weight: 280
url: /zh/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 了解如何通过Aspose.Cells for Python通过.NET API应用Microsoft Excel的高级筛选来显示符合复杂条件的记录。
keywords: Python Excel库，Python应用高级筛选，Python设置高级筛选，Python添加高级筛选，Python创建高级筛选，如何使用Python向范围添加高级筛选。
---

## **可能的使用场景**

Microsoft Excel允许您在工作表数据上应用*高级筛选*，以显示符合复杂条件的记录。您可以通过其*数据 > 高级*命令在Microsoft Excel中应用高级筛选，如此截图所示。

![todo:image_alt_text](1.png)

Aspose.Cells for Python通过.NET还允许您使用[**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool)方法应用高级筛选。就像Microsoft Excel一样，它接受以下参数。

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

![todo:image_alt_text](2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
