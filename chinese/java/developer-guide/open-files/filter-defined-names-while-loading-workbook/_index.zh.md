---
title: 在加载工作簿时过滤定义名称
type: docs
weight: 50
url: /zh/java/filter-defined-names-while-loading-workbook/
---

## **可能的使用场景**

Aspose.Cells允许您过滤或移除工作簿中存在的定义名称。请在加载工作簿时使用[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)加载定义名称，并使用~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)在加载工作簿时移除它们。请注意，如果移除了定义名称，则工作簿中的公式可能会中断。

## **在加载工作簿时过滤定义名称**

以下示例代码加载了包含单元格 C1 中包含已定义名称（即 *=SUM(MyName1, MyName2)*）的示例 Excel 文件。由于我们在加载工作簿时使用 ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) 来移除已定义的名称，因此输出的 Excel 文件中单元格 C1 中的公式会中断，显示 *#NAME?*。请参见以下屏幕截图，展示了代码对示例 Excel 文件的影响。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
