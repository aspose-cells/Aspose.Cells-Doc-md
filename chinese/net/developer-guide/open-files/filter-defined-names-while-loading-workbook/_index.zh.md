---
title: 加载工作簿时筛选定义名称
type: docs
weight: 50
url: /zh/net/filter-defined-names-while-loading-workbook/
---

## **可能的使用场景**

Aspose.Cells允许您筛选或移除工作簿中存在的定义名称。请使用[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)来加载定义名称，并使用~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)在加载工作簿时移除它们。请注意，如果移除定义名称，则工作簿中的公式可能会中断。

## **加载工作簿时筛选定义名称**

以下示例代码加载了包含单元格**C1**中包含定义名称的公式的[示例Excel文件](61767860.xlsx)。由于在加载工作簿时我们使用了~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)来移除定义名称，因此[输出Excel文件](61767861.xlsx)中单元格C1中的公式中断，您将看到*#NAME?*。请查看以下屏幕截图，展示了代码对示例Excel文件的影响。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
