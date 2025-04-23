---
title: 应用Microsoft Excel的高级筛选以显示符合复杂条件的记录
type: docs
weight: 280
url: /zh/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 通过使用 Aspose.Cells for .NET API，学习如何应用Microsoft Excel的高级筛选以显示满足复杂条件的记录。
keywords: 应用高级筛选，设置高级筛选，添加高级筛选，创建高级筛选，如何向范围添加高级筛选 
---

## **可能的使用场景**

Microsoft Excel允许您对工作表数据应用*高级筛选*，以显示符合复杂条件的记录。您可以通过*数据 > 高级*命令应用Microsoft Excel的高级筛选，如下图所示。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells还允许使用[**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)方法应用高级筛选。与Microsoft Excel一样，它接受以下参数。

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

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
