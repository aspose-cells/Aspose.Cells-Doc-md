---
title: 在加载Excel工作簿时过滤VBA项目
type: docs
weight: 140
url: /zh/python-net/filter-vba-project-while-loading-a-workbook/
---

## **在Python中加载Excel工作簿时过滤VBA项目**

一些.xlam/.xlsb文件具有极大量的宏（或非常长的宏）。Aspose.Cells for Python via .NET在打开此类工作簿时将无条件加载这些（元）数据。您可能需要通过[**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions)控制此行为，当您实际上只需提取大量工作簿的工作表名称，从而跳过此类不需要的内容。这通过引入一个新选项[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)提供了过滤功能。

## **示例代码**

以下示例代码加载工作簿，仅过滤 VBA。可以从以下链接下载用于测试此功能的示例文件：

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
