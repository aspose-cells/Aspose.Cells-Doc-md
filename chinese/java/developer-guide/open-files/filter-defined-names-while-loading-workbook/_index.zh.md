---
title: 加载工作簿时筛选定义名称
type: docs
weight: 50
url: /zh/java/filter-defined-names-while-loading-workbook/
---

## **可能的使用场景**

Aspose.Cells允许您筛选或移除工作簿中存在的定义名称。请使用[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)来加载定义名称，并使用~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)在加载工作簿时移除它们。请注意，如果移除定义名称，则工作簿中的公式可能会中断。

## **加载工作簿时筛选定义名称**

以下示例代码加载了[sample Excel file](61767873.xlsx)，其中单元格 C1 中包含了已定义名称的公式，例如 *=SUM(MyName1, MyName2)*。由于在加载工作簿时使用了 ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) 来移除已定义名称，因此输出 Excel 文件中的单元格 C1 的公式会中断，您会看到 *#NAME?*。请参阅以下截图，显示了代码对示例 Excel 文件的影响。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
