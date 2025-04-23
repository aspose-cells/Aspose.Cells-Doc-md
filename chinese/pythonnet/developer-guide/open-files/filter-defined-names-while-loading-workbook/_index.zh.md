---
title: 在加载工作簿时过滤定义名称
type: docs
weight: 50
url: /zh/python-net/filter-defined-names-while-loading-workbook/
---

## **可能的使用场景**

Aspose.Cells for Python via .NET 允许你过滤或删除工作簿内的定义名称。加载工作簿时，请使用 [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) 来加载定义名称，使用 ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) 来删除它们。请注意，如果删除定义名称，工作簿内的公式可能会出错。

## **在加载工作簿时过滤定义名称**

以下示例代码加载了包含单元格**C1**中包含定义名称的公式的[示例Excel文件](61767860.xlsx)。由于在加载工作簿时使用了~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)来移除定义名称，所以[输出Excel文件](61767861.xlsx)中单元格C1中的公式中断了，您会看到*#NAME?*。请参阅以下截图，显示了代码对示例Excel文件的影响。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

