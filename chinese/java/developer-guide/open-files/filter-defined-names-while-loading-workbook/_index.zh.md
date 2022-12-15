---
title: 加载工作簿时过滤定义的名称
type: docs
weight: 50
url: /zh/java/filter-defined-names-while-loading-workbook/
---
## **可能的使用场景**

Aspose.Cells 允许您过滤或删除工作簿中存在的已定义名称。请用[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)加载定义的名称并使用 ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)在加载工作簿时删除它们。请注意，如果您要删除已定义的名称，则工作簿中的公式可能会中断。

## **加载工作簿时过滤定义的名称**

下面的示例代码加载[示例 Excel 文件](61767873.xlsx)它在单元格 C1 中有一个公式，其中包含已定义的名称，即*=SUM(我的名字 1, 我的名字 2)*.因为，我们正在使用 ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)要在加载工作簿时删除定义的名称，单元格 C1 中的公式[输出Excel文件](61767872.xlsx)分手，你看*#NAME?*反而。请查看以下屏幕截图，其中显示了代码对示例 Excel 文件的影响。

![待办事项：图像_替代_文本](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
