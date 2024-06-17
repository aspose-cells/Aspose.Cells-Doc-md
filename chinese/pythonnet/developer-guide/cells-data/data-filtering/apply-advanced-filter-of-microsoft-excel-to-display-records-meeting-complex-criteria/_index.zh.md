---
title: 应用Microsoft Excel的高级筛选以显示符合复杂条件的记录
type: docs
weight: 280
url: /zh/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 通过使用Aspose.Cells for Python via .NET API，学习如何应用Microsoft Excel的高级筛选来显示符合复杂条件的记录。
keywords: Python Excel库，Python应用高级筛选，Python设置高级筛选，Python添加高级筛选，Python创建高级筛选，如何使用Python向范围添加高级筛选。
---

## **可能的使用场景**

Microsoft Excel允许您对工作表数据应用*高级筛选*，以显示符合复杂条件的记录。您可以通过*数据 > 高级*命令应用Microsoft Excel的高级筛选，如下图所示。

![todo:image_alt_text](1.png)

Aspose.Cells for Python via .NET也允许您使用[**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool)方法应用高级筛选。就像Microsoft Excel一样，它接受以下参数。

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

下面的示例代码应用于 [示例 Excel 文件](48496692.xlsx) 上的高级筛选，并生成 [输出 Excel 文件](48496691.xlsx)。截图显示了两个文件进行比较。正如您在截图中看到的，根据复杂条件，输出的 Excel 文件中的数据已进行了筛选。

![todo:image_alt_text](2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
