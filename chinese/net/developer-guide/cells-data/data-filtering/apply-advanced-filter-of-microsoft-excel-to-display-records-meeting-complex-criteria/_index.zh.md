---
title: 应用 Microsoft Excel 的高级筛选器显示满足复杂条件的记录
type: docs
weight: 280
url: /zh/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 了解如何使用 Aspose.Cells for .NET API 应用 Microsoft Excel 的高级过滤器来显示满足复杂条件的记录。
keywords: Apply Advanced Filter, Set Advanced Filter, Add Advanced Filter, Create Advanced Filter, How to add Advanced Filter to a range 
---
##  **可能的使用场景**

 Microsoft Excel允许您申请*高级过滤器*在工作表数据上显示满足复杂条件的记录。您可以通过 Microsoft Excel 应用高级过滤器*数据 > 高级*命令如该屏幕截图所示。

![待办事项：图像_替代_文本](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells 还允许您使用高级过滤器[**工作表.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)方法。就像 Microsoft Excel 一样，它接受以下参数。

**是过滤器**

指示是否就地过滤列表。

**列表范围**

列表范围。

**标准范围**

标准范围。

**复制到**

复制数据的范围。

**仅唯一记录**

仅显示或复制唯一行。

##  **应用 Microsoft Excel 的高级筛选器显示满足复杂条件的记录**

以下示例代码将高级过滤器应用于[Excel 文件示例](48496692.xlsx)并生成[输出Excel文件](48496691.xlsx)。屏幕截图显示了两个文件以进行比较。正如您在屏幕截图中看到的，输出 Excel 文件中的数据已根据复杂的条件进行了过滤。

![待办事项：图像_替代_文本](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
