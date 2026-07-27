---
title: 显示报表筛选页选项
type: docs
weight: 140
url: /zh/java/show-report-filter-pages-option/
---

## **显示报表筛选页选项**

Excel支持创建数据透视表，添加报表筛选，并启用“显示报表筛选页”选项。Aspose.Cells也支持在创建的数据透视表上启用“显示报表筛选页”选项。以下是Excel中显示该选项的屏幕。

![todo:image_alt_text](show-report-filter-pages-option_1.png)

由于此选项，创建的工作簿包含更多工作表。它在单独的工作表中拆分了报表筛选的每个可能值。在此示例中，它在"Position"上进行了筛选，数据有三个不同的职位（A、B、C）。此功能添加了三个名为A、B、C的附加工作表，它们是相同的数据透视表，但具有预选选项A、B和C。

样本文件和输出文件可从以下链接下载：

[samplePivotTable.xlsx](81920917.xlsx)

[outputSamplePivotTable.xls](81920918.xlsx)

## 源代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-ShowReportFilterPagesOption-1.java" >}}
{{< app/cells/assistant language="java" >}}
