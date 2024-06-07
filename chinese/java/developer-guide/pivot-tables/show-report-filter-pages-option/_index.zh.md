---
title: 显示报表筛选器页面选项
type: docs
weight: 140
url: /zh/java/show-report-filter-pages-option/
---

## **显示报表筛选页面选项**

Excel支持创建数据透视表、添加报表筛选器和启用"显示报表筛选器页面"选项。Aspose.Cells也支持在创建的数据透视表上启用"显示报表筛选器页面"选项。以下是在Excel中显示该选项的屏幕。

![todo:image_alt_text](show-report-filter-pages-option_1.png)

由于这个选项的结果，创建的工作簿包含更多工作表。它会将报表筛选器的每个可能值分割成单独的工作表。在这个例子中，它在"Position"上有一个筛选器，并且数据有三个不同的位置（A、B、C）。该功能添加了3个附加的工作表，命名为A、B、C，它们是相同的数据透视表，但具有预选的选项A、B和C。

示例文件和输出文件可以从以下链接下载：

[samplePivotTable.xlsx](81920917.xlsx)

[outputSamplePivotTable.xls](81920918.xlsx)

## 源代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-ShowReportFilterPagesOption-1.java" >}}
