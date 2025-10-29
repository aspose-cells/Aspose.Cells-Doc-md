---
title: 在加载工作簿时过滤定义名称
type: docs
weight: 50
url: /zh/go-cpp/filter-defined-names-while-loading-workbook/
---

## **可能的使用场景**

Aspose.Cells允许您筛选或移除工作簿中的定义名称。请使用[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/)在加载工作簿时加载定义名称。注意，移除定义名称可能会导致工作簿内的公式失效。

## **在加载工作簿时过滤定义名称**

以下示例加载了【示例Excel文件】(61767860.xlsx)，该文件在单元格**C1**中含有定义名称的公式（=SUM(MyName1, MyName2)）。由于使用~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/)在加载工作簿时移除定义名称，输出Excel文件中的C1单元格公式将会中断，显示*#NAME?*。请查看截图了解示例代码对样例Excel文件的影响。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
